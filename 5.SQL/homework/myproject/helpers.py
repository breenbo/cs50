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


def stock_transaction(transaction, db, user_id, cash, potential_cash):
    portfolio_rows = db.execute("SELECT * FROM portfolio" +
                                " WHERE user_id=:user_id",
                                user_id=user_id)
    # check if the stocks to be sold for each row of database
    no_sold = False
    for row in portfolio_rows:
        # check every row and calculate global potential cash
        actual_price = row["actual_price"]
        potential_cash += actual_price * row["number_share"]
        potential_cash = round(potential_cash, 2)

        stock_symbol = row["stock_symbol"]
        if request.form[stock_symbol] == "":
            # do nothing, no stock to sold
            # but recall that there is no integer in input
            no_integer = True
        else:
            # check the user input
            try:
                int(request.form[stock_symbol])
            except:
                no_integer = True
                if transaction == "sell":
                    return render_template("sell.html",
                                        cash=session["cash"],
                                        portfolio_rows=portfolio_rows,
                                        potential_cash=potential_cash,
                                        no_sold=no_sold,
                                        no_integer=no_integer)
                elif transaction == "buy":
                    return apology("test of function except")
            else:
                no_integer = False
                #  sell the numbers of stock
                number_sold = int(request.form[stock_symbol])
                number_share = int(row["number_share"])
                if number_sold > number_share:
                    no_sold = True
                if number_share < 0:
                    no_integer = True

                # update the databases of buy/sold stocks
                if transaction == "sell":
                    # set negatives values for numbers and positive for amount
                    pass
                elif transaction == "buy":
                    # set positives values for numbers and negative for amount
                    pass

                number_share += number_sold
                price = float(row["actual_price"])
                potential_value = price * number_share
                potential_value = round(potential_value, 2)

                sold_amount = price * number_sold
                sold_amount = round(sold_amount, 2)

                # add sold_amount to user cash
                cash += sold_amount
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
                           " :number_sold," +
                           " datetime('now', 'localtime')" +
                           ")",
                           user_id=user_id,
                           stock_symbol=stock_symbol,
                           price=price,
                           number_sold=number_sold)

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

    return render_template("sell.html",
                           cash=session["cash"],
                           portfolio_rows=portfolio_rows,
                           potential_cash=potential_cash,
                           no_sold=no_sold,
                           no_integer=no_integer)
