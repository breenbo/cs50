import csv
import urllib.request

from flask import redirect, render_template, request, session
from functools import wraps


def apology(message, code=400):
    """Renders message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/0.12/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


def lookup(symbol):
    """Look up quote for symbol."""

    # reject symbol if it starts with caret
    if symbol.startswith("^"):
        return None

    # reject symbol if it contains comma
    if "," in symbol:
        return None

    # query Yahoo for quote
    # http://stackoverflow.com/a/21351911
    try:

        # GET CSV
        url = f"http://download.finance.yahoo.com/d/quotes.csv?f=snl1&s={symbol}"
        webpage = urllib.request.urlopen(url)

        # read CSV
        datareader = csv.reader(webpage.read().decode("utf-8").splitlines())

        # parse first row
        row = next(datareader)

        # ensure stock exists
        try:
            price = float(row[2])
        except:
            return None

        # return stock's name (as a str), price (as a float), and (uppercased) symbol (as a str)
        return {
            "name": row[1],
            "price": price,
            "symbol": row[0].upper()
        }

    except:
        pass

    # query Alpha Vantage for quote instead
    # https://www.alphavantage.co/documentation/
    try:

        # GET CSV
        url = f"https://www.alphavantage.co/query?apikey=NAJXWIA8D6VN6A3K&datatype=csv&function=TIME_SERIES_INTRADAY&interval=1min&symbol={symbol}"
        webpage = urllib.request.urlopen(url)

        # parse CSV
        datareader = csv.reader(webpage.read().decode("utf-8").splitlines())

        # ignore first row
        next(datareader)

        # parse second row
        row = next(datareader)

        # ensure stock exists
        try:
            price = float(row[4])
        except:
            return None

        # return stock's name (as a str), price (as a float), and (uppercased) symbol (as a str)
        return {
            "name": symbol.upper(), # for backward compatibility with Yahoo
            "price": price,
            "symbol": symbol.upper()
        }

    except:
        return None


def usd(value):
    """Formats value as USD."""
    return f"${value:,.2f}"


def pot_cash(portfolio_rows):
    """ calcul potential cash of users stocks """
    potential_cash = 0
    for row in portfolio_rows:
        # check every row and calculate global potential cash
        actual_price = row["actual_price"]
        potential_cash += actual_price * row["number_share"]
        potential_cash = round(potential_cash, 2)

    return potential_cash


def stock_transaction(transaction, db, user_id, cash, potential_cash):
    portfolio_rows = db.execute("SELECT * FROM portfolio" +
                                " WHERE user_id=:user_id",
                                user_id=user_id)
    # check if the stocks to be sold for each row of database
    no_sold = False
    potential_cash = pot_cash(portfolio_rows)

    for row in portfolio_rows:
        stock_symbol = row["stock_symbol"]
        if request.form[stock_symbol] == "":
            # do nothing, no stock to sold
            # but recall that there is no integer in input
            pass
        else:
            # check the user input
            try:
                int(request.form[stock_symbol])
            except:
                # bad input number
                no_integer = True
                if transaction == "sell":
                    return render_template("sell.html",
                                           cash=cash,
                                           portfolio_rows=portfolio_rows,
                                           potential_cash=potential_cash,
                                           no_sold=no_sold,
                                           no_integer=no_integer)
                elif transaction == "buy":
                    return render_template("index.html",
                                           username=session["user_name"].capitalize(),
                                           cash=cash,
                                           portfolio_rows=portfolio_rows,
                                           potential_cash=potential_cash,
                                           no_integer=no_integer)
            else:
                no_integer = False
                number_share = int(row["number_share"])
                # update the databases of buy/sold stocks
                if transaction == "sell":
                    # set negatives values for numbers
                    number_move = - int(request.form[stock_symbol])
                    # bad input number
                    if number_move > 0:
                        no_integer = True
                        return render_template("sell.html",
                                               cash=cash,
                                               portfolio_rows=portfolio_rows,
                                               potential_cash=potential_cash,
                                               no_sold=no_sold,
                                               no_integer=no_integer)
                    # can't sell more than user have
                    if abs(number_move) > number_share:
                        no_sold = True
                        return render_template("sell.html",
                                               cash=cash,
                                               portfolio_rows=portfolio_rows,
                                               potential_cash=potential_cash,
                                               no_sold=no_sold,
                                               no_integer=no_integer)

                elif transaction == "buy":
                    # set positives values for numbers
                    number_move = int(request.form[stock_symbol])
                    if number_move < 0 and abs(number_move) > number_share:
                        # can't sell more than we have
                        no_sold = True
                        return render_template("index.html",
                                               username=session["user_name"].capitalize(),
                                               cash=cash,
                                               portfolio_rows=portfolio_rows,
                                               potential_cash=potential_cash,
                                               no_integer=no_integer,
                                               no_sold=no_sold)

                    # bad input number
                    #  if number_move < 0:
                        #  no_integer = True
                        #  return render_template("index.html",
                                               #  username=session["user_name"].capitalize(),
                                               #  cash=cash,
                                               #  portfolio_rows=portfolio_rows,
                                               #  potential_cash=potential_cash,
                                               #  no_integer=no_integer)

                number_share += number_move
                price = float(row["actual_price"])
                potential_value = price * number_share
                potential_value = round(potential_value, 2)

                # amount is oposite sign of number_move
                move_amount = - (price * number_move)
                move_amount = round(move_amount, 2)

                # add move_amount to user cash
                cash += move_amount
                cash = round(cash, 2)
                session["cash"] = cash

                # update portfolio
                db.execute("UPDATE portfolio" +
                           " SET" +
                           " number_share=:number_share," +
                           " potential_value=:potential_value," +
                           " last_updated=datetime('now', 'localtime')" +
                           " WHERE" +
                           " user_id=:user_id" +
                           " AND" +
                           " stock_symbol=:stock_symbol",
                           number_share=number_share,
                           potential_value=potential_value,
                           user_id=user_id,
                           stock_symbol=stock_symbol)

                if transaction == "sell":
                # update sell_history
                    db.execute("INSERT INTO sell_history (" +
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
                               " :number_move," +
                               " datetime('now', 'localtime')" +
                               ")",
                               user_id=user_id,
                               stock_symbol=stock_symbol,
                               price=price,
                               number_move=abs(number_move))

                elif transaction == "buy":
                    # update buy history
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
                               " :number_move," +
                               " datetime('now', 'localtime')" +
                               ")",
                               user_id=user_id,
                               stock_symbol=stock_symbol,
                               price=price,
                               number_move=abs(number_move))

    # delete all rows with no shares
    db.execute("DELETE FROM portfolio" +
               " WHERE number_share = 0")
    # update cash
    db.execute("UPDATE users SET cash=:cash WHERE id=:user_id",
               cash=cash,
               user_id=user_id)
    # reload updated portfolio_rows before display
    portfolio_rows = db.execute("SELECT * FROM portfolio" +
                                " WHERE user_id=:user_id",
                                user_id=user_id)

    # update potential_cash with new values of stocks
    potential_cash = pot_cash(portfolio_rows)

    # display the results
    if transaction == "sell":
        return render_template("sell.html",
                               cash=cash,
                               portfolio_rows=portfolio_rows,
                               potential_cash=potential_cash,
                               no_sold=no_sold,
                               no_integer=no_integer)
    elif transaction == "buy":
        return render_template("index.html",
                               username=session["user_name"].capitalize(),
                               cash=cash,
                               portfolio_rows=portfolio_rows,
                               potential_cash=potential_cash)
