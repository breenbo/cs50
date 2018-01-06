from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
from tempfile import mkdtemp

from helpers import apology, login_required, lookup, usd, stock_transaction

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


@app.route("/", methods=["POST", "GET"])
@login_required
# add portfolio_buy here for post method ? and index() for get method ?
def index():
    if request.method == "GET":
        # default view.
        # contains a portfolio view
        # update prices each time and store them in portfolio database
        user_id = session["user_id"]
        portfolio_rows = db.execute("SELECT * FROM portfolio" +
                                    " WHERE user_id=:user_id",
                                    user_id=user_id)
        # check the actual price of the portfolio's stock
        # list of stock_symbol, shares, actual price
        potential_cash = 0
        for row in portfolio_rows:
            stock_symbol = row["stock_symbol"]
            actual_price = lookup(stock_symbol)["price"]
            # calculate the potential value of each stock
            row["actual_price"] = actual_price
            potential_cash += actual_price * row["number_share"]
            potential_cash = round(potential_cash, 2)
            potential_value = actual_price * row["number_share"]
            # update stocks actual price in portfolio db
            db.execute("UPDATE portfolio" +
                       " SET" +
                       " actual_price=:actual_price," +
                       " potential_value=:potential_value," +
                       " last_updated=datetime('now', 'localtime')" +
                       " WHERE" +
                       " user_id=:user_id" +
                       " AND" +
                       " stock_symbol=:stock_symbol",
                       actual_price=actual_price,
                       user_id=user_id,
                       potential_value=potential_value,
                       stock_symbol=stock_symbol)

        # store the new database in portfolio_rows var
        portfolio_rows = db.execute("SELECT * FROM portfolio" +
                                    " WHERE user_id=:user_id",
                                    user_id=user_id)

        # set portfolio_rows as session to immediate use in sell page

        return render_template("index.html",
                               username=session["user_name"].capitalize(),
                               cash=session["cash"],
                               portfolio_rows=portfolio_rows,
                               potential_cash=potential_cash)

    elif request.method == "POST":
        user_id = session["user_id"]
        cash = session["cash"]
        potential_cash = 0
        return stock_transaction("buy", db, user_id, cash, potential_cash)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock."""
    # use variables stored by the login def in session[var]
    # retrieve stock price with lookup function
    cash = session["cash"]
    quote = True
    # set default number to display proper results headings
    number = True
    if request.method == "POST":
        if request.form["stock"] == "":
            # Personnel enhancement
            quote = False
            return render_template("buy.html", quote=quote, cash=cash)
            #  return apology("Please enter a valid stock symbol")

        symbol = request.form["stock"]
        # only one request, parse result in html with {{ result.subresult }}
        result = lookup(symbol)
        if result is None:
            quote = False
            return render_template("buy.html", quote=quote, cash=cash)
            #  return apology("Sorry, unable to find the stock")
        # store result in session variable iot use later
        session["result"] = result

        return render_template("buy.html",
                               cash=cash,
                               result=result,
                               quote=quote,
                               number=number)

    if request.method == "GET":
        return render_template("buy.html", cash=cash, quote=quote)


@app.route("/bought", methods=["POST"])
@login_required
# finalize the purchase
# check if inputs are correct
# store data in buy_history and portfolio
def bought():
    number = True
    success = False
    cash = session["cash"]
    result = session["result"]
    if request.form["shares"] == "":
        number = False
    else:
        # check if users has entered a positive integer
        try:
            # check if it's integer
            int(request.form["shares"])
        except:
            number = False
            return render_template("buy.html",
                                   cash=cash,
                                   result=result,
                                   quote=quote,
                                   number=number)
        else:
            # check if it's positive
            if int(request.form["shares"]) < 0:
                number = False
                return render_template("buy.html",
                                       cash=cash,
                                       result=result,
                                       quote=quote,
                                       number=number)
                #  return apology("Please enter a positive integer")

            number = True
            # work with the datas now the user input is safe
            # create some easy variables
            stock_symbol = result["symbol"]
            price = float(result["price"])
            number_share = int(request.form["shares"])
            user_id = session["user_id"]
            buy_amount = number_share * price
            buy_amount = round(buy_amount, 2)
            cash -= buy_amount
            cash = round(cash, 2)
            # update session["cash"] for later use
            session["cash"] = cash
            # return apology if total bought price > available cash
            if cash < 0:
                return apology("Sorry, you're to poor for that...")

            # valid transaction
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
                                user_id=user_id,
                                stock_symbol=stock_symbol)

            # check if stock already in portfolio
            # if yes -> update number of shares
            if len(shares) == 1:
                shares = int(shares[0]["number_share"])
                shares += number_share
                db.execute("UPDATE portfolio" +
                           " SET" +
                           " number_share=:number_share," +
                           " last_updated=datetime('now', 'localtime')" +
                           " WHERE" +
                           " user_id=:user_id" +
                           " AND" +
                           " stock_symbol=:stock_symbol",
                           number_share=shares,
                           user_id=user_id,
                           stock_symbol=stock_symbol)
            # if no -> insert new stock in portfolio
            else:
                db.execute("INSERT INTO portfolio (" +
                           " user_id," +
                           " stock_symbol," +
                           " number_share," +
                           " actual_price," +
                           " potential_value," +
                           " last_updated" +
                           ")" +
                           " VALUES (" +
                           " :user_id," +
                           " :stock_symbol," +
                           " :number_share," +
                           " :actual_price," +
                           " :potential_value," +
                           " datetime('now', 'localtime')" +
                           ")",
                           user_id=user_id,
                           stock_symbol=stock_symbol,
                           number_share=number_share,
                           actual_price=price,
                           potential_value=buy_amount)

            # update amount of available cash for user
            db.execute("UPDATE users SET cash=:cash WHERE id=:user_id",
                       cash=cash,
                       user_id=user_id)

            # success var to display success message in buy.html
            success = True

            return render_template("buy.html",
                                   cash=cash,
                                   result=result,
                                   quote=True,
                                   number=number,
                                   success=success,
                                   number_share=number_share,
                                   buy_amount=buy_amount)


@app.route("/history")
@login_required
def history():
    """Show history of transactions."""
    user_id = session["user_id"]
    # read buy and sell history, then display them in history.html
    buy_history = db.execute("SELECT * FROM buy_history" +
                             " WHERE user_id=:user_id",
                             user_id=user_id)
    sell_history = db.execute("SELECT * FROM sell_history" +
                              " WHERE user_id=:user_id",
                              user_id=user_id)
    return render_template("history.html",
                           buy_history=buy_history,
                           sell_history=sell_history)


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
        session["cash"] = round(rows[0]["cash"], 2)

        # create a buy_history table if not exist
        db.execute("CREATE TABLE IF NOT EXISTS buy_history (" +
                    " buy_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL," +
                    " user_id INTEGER NOT NULL," +
                    " stock_symbol TEXT NOT NULL," +
                    " price FLOAT NOT NULL," +
                    " number_share INTEGER," +
                    " date_time TEXT NOT NULL," +
                    " FOREIGN KEY(user_id) REFERENCES users(id))")
        # create a sell_history table if not exist
        db.execute("CREATE TABLE IF NOT EXISTS sell_history (" +
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
                    " stock_symbol TEXT NOT NULL," +
                    " number_share INTEGER," +
                    " actual_price FLOAT," +
                    " potential_value FLOAT," +
                    " last_updated TEXT NOT NULL," +
                    " FOREIGN KEY(user_id) REFERENCES users(id))")

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
            quote = False
            return render_template("quote.html", quote=quote)
            #  return apology("Please enter a valid stock symbol")
        symbol = request.form["symbol"]
        # only one request, parse result in html with {{ result.subresult }}
        result = lookup(symbol)
        if result == None:
            quote = False
            return render_template("quote.html", quote=quote)
        return render_template("quoted.html", result=result, quote=quote)

    if request.method == "GET":
        return render_template("quote.html", quote=quote)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user into database users."""
    # check if post method -> protect from get method
    login = True
    if request.method == "POST":
        # check if register correct (non empty)
        if request.form["username"] == "" or request.form["password"] == "":
            login = False
            return render_template("register.html",
                                   login=login)
            #  return apology("Please enter a name and a password.")
        # store name and hashed password in db users (username, hash)
        db.execute("INSERT INTO users (username, hash) VALUES (:username," +
                   " :password)",
                   username=request.form["username"],
                   password=pwd_context.hash(request.form["password"]))
        # then go to the login view to ensure a proper login
        return render_template("login.html")
    # else if user reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html",
                               login=login)


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock."""
    # query the database to have the last stored datas
    user_id = session["user_id"]
    cash = session["cash"]
    portfolio_rows = db.execute("SELECT * FROM portfolio" +
                                " WHERE user_id=:user_id",
                                user_id=user_id)

    # display the portfolio
    potential_cash = 0

    if request.method == "POST":
        # check if the stocks to be sold for each row of database
        return stock_transaction("sell", db, user_id, cash, potential_cash)

    elif request.method == "GET":
        # check every row in portfolio_rows and calculate global potential cash
        for row in portfolio_rows:
            actual_price = row["actual_price"]
            potential_cash += actual_price * row["number_share"]
            potential_cash = round(potential_cash, 2)

        return render_template("sell.html",
                               cash=session["cash"],
                               portfolio_rows=portfolio_rows,
                               potential_cash=potential_cash,
                               no_sold=False,
                               no_integer=False)
