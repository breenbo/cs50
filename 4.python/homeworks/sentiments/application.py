from flask import Flask, redirect, render_template, request, url_for

import helpers
import sys
import os
from analyzer import Analyzer
from helpers import get_user_timeline

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search")
def search():

    # validate screen_name
    screen_name = request.args.get("screen_name", "")
    if not screen_name:
        return redirect(url_for("index"))

    # TODO
    # retrieve the 100 post recents tweets of screen_name
    # analyze every tweets and store the score
    # count the numbers of positive, negative, neutral tweets
    # display the numbers on a piechart

    nb_tweets = 100

    # get screen_name's tweets
    try:
        tweets = get_user_timeline(screen_name, nb_tweets)
        if tweets is None:
            sys.exit(
                "Unable to retrieve " +
                screen_name +
                " tweets, private account or rate limit reached.")
    except RuntimeError:
        sys.exit("Invalid API_KEY and/or API_SECRET")

    # absolute paths to lists
    positives = os.path.join(sys.path[0], "positive-words.txt")
    negatives = os.path.join(sys.path[0], "negative-words.txt")

    # instantiate analyzer
    analyzer = Analyzer(positives, negatives)

    # analyze tweets and count type of scores
    positive, negative, neutral = 0.0, 0.0, 0.0
    for tweet in tweets:
        score = analyzer.analyze(tweet)
        if score > 0:
            positive += 1
        elif score < 0:
            negative += 1
        else:
            neutral += 1

    positive /= len(tweets)*100
    negative /= len(tweets)*100
    neutral /= len(tweets)*100

    # generate chart
    chart = helpers.chart(positive, negative, neutral)

    # render results
    return render_template("search.html", chart=chart, screen_name=screen_name)
