import unittest
from orchestrator_agent import EALCOrchestrator

class TestWorkflows(unittest.TestCase):

    def setUp(self):
        self.ealc = EALCOrchestrator()

    def test_full_workflow(self):
        input_data = {
            "learner_id": "workflow_1",
            "query": "Explain the Pythagorean theorem",
            "subject": "mathematics",
            "difficulty_level": "intermediate",
            "learner_response": None
        }
        response = self.ealc.process_learner_input(input_data)

        # Check that all main keys exist
        expected_keys = [
            "emotional_acknowledgment",
            "explanation",
            "practice_questions",
            "encouragement",
            "progress"
        ]
        for key in expected_keys:
            self.assertIn(key, response)

        # Ensure explanation and questions are not empty
        self.assertTrue(len(response["explanation"]) > 0)
        self.assertTrue(len(response["practice_questions"]) > 0)

if __name__ == "__main__":
    unittest.main()

