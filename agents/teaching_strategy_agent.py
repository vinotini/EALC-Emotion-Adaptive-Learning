class TeachingStrategyAgent:
    def select_strategy(self, emotional_state, subject, difficulty):
        mapping = {
            "frustrated": "supportive",
            "confident": "challenging",
            "neutral": "clarifying"
        }
        return mapping.get(emotional_state, "clarifying")

