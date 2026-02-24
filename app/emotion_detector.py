from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class EmotionDetector:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def detect_emotion(self, text):
        scores = self.analyzer.polarity_scores(text)
        compound = scores["compound"]

        # Granular Emotion Classification
        if compound >= 0.6:
            emotion = "excited"
        elif compound >= 0.3:
            emotion = "happy"
        elif compound <= -0.6:
            emotion = "angry"
        elif compound <= -0.3:
            emotion = "concerned"
        else:
            emotion = "neutral"

        return emotion, compound