import nltk


class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""

        # use dict for speed
        self.positives = {}
        self.negatives = {}

        test_dict = {"positive": self.positives, "negative": self.negatives}

        for k, v in test_dict.items():
            with open(k + "-words.txt", "r") as lines:
                for line in lines:
                    # remove lines with comments
                    if not line.startswith(";"):
                        # store words in positive, without leading/trailing space
                        #  v.append(line.strip())
                        # add new word in dict
                        v[line.strip()] = 1
            lines.close()

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""

        score = 0
        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = tokenizer.tokenize(text)
        for token in tokens:
            token = token.lower()
            if token in self.positives:
                score += 1
            elif token in self.negatives:
                score -= 1

        return score
