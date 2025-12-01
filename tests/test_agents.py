import unittest
from orchestrator_agent import EALCOrchestrator

class TestAgents(unittest.TestCase):

    def setUp(self):
        self.ealc = EALCOrchestrator()

    def test_emotion_detection(self):
        input_data = {
            "learner_id": "test_1",
            "query": "I am really frustrated with this problem!",
            "subject": "mathematics",
            "difficulty_level": "beginner",
            "learner_response": None
        }
        response = self.ealc.process_learner_input(input_data)
        self.assertIn("frustration", response["emotional_acknowledgment"].lower())

    def test_strategy_selection(self):
        input_data = {
            "learner_id": "test_2",
            "query": "I solved it easily, what next?",
            "subject": "science",
            "difficulty_level": "advanced",
            "learner_response": None
        }
        response = self.ealc.process_learner_input(input_data)
        self.assertIn("challenging", response["encouragement"].lower())

if __name__ == "__main__":
    unittest.main()
