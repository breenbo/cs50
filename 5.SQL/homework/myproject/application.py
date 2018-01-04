from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
from tempfile import mkdtemp

from helpers import apology, login_required, lookup, usd

# configure application
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

# ensure responses aren't cached
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

# custom filter
app.jinja_env.filters["usd"] = usd

# configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.route("/")
@login_required
def index():
    portfolio_rows = db.execute("SELECT * FROM portfolio WHERE user_id=:user_id",
                           user_id=session["user_id"])
    # check the actual price of the portfolio's stock
    # list of stock_symbol, shares, actual price
    for row in portfolio_rows:
        row["price"] = lookup(row["stock_symbol"])["price"]

    return render_template("index.html",
                           username=session["user_name"].capitalize(),
                           cash=session["cash"],
                           portfolio_rows=portfolio_rows)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock."""
    # use variables stored by the login def in session[var]
    # retrieve stock price with lookup function
    quote = True
    if request.method == "POST":
        if request.form["stock"] == "":
            # Personnel enhancement
            #  quote = False
            #  return render_template("buy.html", quote=quote, savings=savings)
            return apology("Please enter a valid stock symbol")

        symbol = request.form["stock"]
        # only one request, parse result in html with {{ result.subresult }}
        result = lookup(symbol)
        # store result in session variable iot use later
        session["result"] = result
        if result is None:
            return apology("Sorry, unable to find the stock")

        return render_template("buy.html",
                               cash=session["cash"],
                               result=result,
                               quote=quote)

    if request.method == "GET":
        return render_template("buy.html", cash=session["cash"], quote=quote)


@app.route("/bought", methods=["POST"])
@login_required
def bought():
    cash = session["cash"]
    result = session["result"]
    if request.form["shares"] == "":
        return apology("Sorry, enter a number of share")
    #  elif int(request.form["shares"]) < 0:
    else:
        # check if users has entered a positive integer
        try:
            # check if it's integer
            int(request.form["shares"])
        except:
            return apology("Please enter an integer")
        else:
            # check if it's positive
            if int(request.form["shares"]) < 0:
                return apology("Please enter a positive integer")

            # work with the datas now the user input is safe
            # create some easy variables
            stock_symbol = result["symbol"]
            price = float(result["price"])
            number_share = int(request.form["shares"])
            user_id = session["user_id"]
            buy_amount = number_share * price
            cash -= buy_amount
            # update session["cash"] for later use
            session["cash"] = cash
            # return apology if total bought price > available cash
            if cash < 0:
                return apology("Sorry, you're to poor for that...")

            # valid transaction
            # create a buy_history table if not exist
            db.execute("CREATE TABLE IF NOT EXISTS buy_history (" +
                       " buy_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL," +
                       " user_id INTEGER NOT NULL," +
                       " stock_symbol TEXT NOT NULL," +
                       " price FLOAT NOT NULL," +
                       " number_share INTEGER," +
                       " date_time TEXT NOT NULL," +
                       " FOREIGN KEY(user_id) REFERENCES users(id))")
            # create a portfolio table if not exist
            db.execute("CREATE TABLE IF NOT EXISTS portfolio (" +
                       " value_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL," +
                       " user_id INTEGER NOT NULL," +
                       " stock_symbol TEXT UNIQUE NOT NULL," +
                       " number_share INTEGER," +
                       " FOREIGN KEY(user_id) REFERENCES users(id))")
            # store data of buy in database 'buy_history' to validate the buy
            db.execute("INSERT INTO buy_history (" +
                       " user_id," +
                       " stock_symbol," +
                       " price," +
                       " number_share," +
                       " date_time" +
                       ")" +
                       " VALUES (" +
                       " :user_id," +
                       " :stock_symbol," +
                       " :price," +
                       " :number_share," +
                       " datetime('now', 'localtime')" +
                       ")",
                       user_id=user_id,
                       stock_symbol=stock_symbol,
                       price=price,
                       number_share=number_share)
            # check if stock already exist in portfolio
            shares = db.execute("SELECT number_share FROM portfolio" +
                                " WHERE user_id = :user_id" +
                                " AND stock_symbol = :stock_symbol",
                                user_id=session["user_id"],
                                stock_symbol=stock_symbol)

            # check if stock already in portfolio
            # if yes -> update number of shares
            if len(shares) == 1:
                shares = int(shares[0]["number_share"])
                shares += number_share
                db.execute("UPDATE portfolio SET number_share=:number_share" +
                           " WHERE user_id=:user_id AND stock_symbol=:stock_symbol",
                           number_share=shares,
                           user_id=user_id,
                           stock_symbol=stock_symbol)
            # if no -> insert new stock in portfolio
            else:
                db.execute("INSERT INTO portfolio (" +
                       " user_id," +
                       " stock_symbol," +
                       " number_share" +
                       ")" +
                       " VALUES (" +
                       " :user_id," +
                       " :stock_symbol," +
                       " :number_share" +
                       ")",
                       user_id=user_id,
                       stock_symbol=stock_symbol,
                       number_share=number_share)

            # update amount of available cash for user
            db.execute("UPDATE users SET cash=:cash WHERE id=:user_id",
                       cash=cash,
                       user_id=user_id)

            return render_template("buy.html", cash=cash, result=result,
                                   quote=True)


@app.route("/history")
@login_required
def history():
    """Show history of transactions."""
    return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in."""

    # forget any user_id
    session.clear()

    # if user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password")

        # query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # ensure username exists and password is correct
        if len(rows) != 1 or not pwd_context.verify(request.form.get("password"),
                                                    rows[0]["hash"]):
            return apology("invalid username and/or password")

        # remember some user info from database
        session["user_id"] = rows[0]["id"]
        session["user_name"] = rows[0]["username"]
        session["cash"] = rows[0]["cash"]

        # redirect user to home page
        return redirect(url_for("index"))

    # else if user reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out."""

    # forget any user_id
    session.clear()

    # redirect user to login form
    return redirect(url_for("login"))


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    # if user get quote with GET (click on a link), display a form to demand
    # which user inputs for stock's symbol : quote.html
    quote = True
    if request.method == "POST":
        if request.form["symbol"] == "":
            # Personnel enhancement
            #  quote = False
            #  return render_template("quote.html", quote=quote)
            return apology("Please enter a valid stock symbol")
        symbol = request.form["symbol"]
        # only one request, parse result in html with {{ result.subresult }}
        result = lookup(symbol)
        return render_template("quoted.html", result=result, quote=quote)

    if request.method == "GET":
        return render_template("quote.html", quote=quote)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user into database users."""
    # check if post method -> protect from get method
    if request.method == "POST":
        # check if register correct (non empty)
        if request.form["username"] == "" or request.form["password"] == "":
            return apology("Please enter a name and a password.")
        # store name and hashed password in db users (username, hash)
        db.execute("INSERT INTO users (username, hash) VALUES (:username," +
                   " :password)",
                   username=request.form["username"],
                   password=pwd_context.hash(request.form["password"]))
        # then go to the login view to ensure a proper login
        return render_template("login.html")
    # else if user reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock."""
    return apology("TODO")
