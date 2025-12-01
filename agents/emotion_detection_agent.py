class EmotionDetectionAgent:
    def detect_emotion(self, text):
        # Placeholder: replace with NLP model or API
        if "don't understand" in text or "frustrated" in text:
            return "frustrated"
        elif "solved" in text or "easy" in text:
            return "confident"
        else:
            return "neutral"
