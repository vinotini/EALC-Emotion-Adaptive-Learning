from agents.emotion_detection import EmotionDetectionAgent
from agents.teaching_strategy import TeachingStrategyAgent
from agents.knowledge_tutor import KnowledgeTutorAgent
from agents.assessment_feedback import AssessmentFeedbackAgent
from agents.memory_profile import MemoryProfileAgent
from agents.validators import Validator
from tools.utils import format_response, generate_encouragement

class EALCOrchestrator:
    def __init__(self):
        self.EDA = EmotionDetectionAgent()
        self.TSA = TeachingStrategyAgent()
        self.KTA = KnowledgeTutorAgent()
        self.AFA = AssessmentFeedbackAgent()
        self.MPA = MemoryProfileAgent()
        self.Validator = Validator()

    def process_learner_input(self, input_data):
        # 1. Emotion Detection
        emotional_state = self.EDA.detect_emotion(input_data["query"])

        # 2. Strategy Selection
        teaching_strategy = self.TSA.select_strategy(
            emotional_state=emotional_state,
            difficulty=input_data["difficulty_level"],
            subject=input_data["subject"]
        )

        # 3. Personalized Content Generation
        explanation = self.KTA.generate_content(
            query=input_data["query"],
            strategy=teaching_strategy,
            learner_profile=self.MPA.get_profile(input_data["learner_id"])
        )

        # 4. Assessment & Feedback
        practice_questions = self.AFA.create_questions(
            explanation=explanation,
            strategy=teaching_strategy
        )
        feedback = self.AFA.evaluate_response(
            learner_response=input_data.get("learner_response")
        )

        # 5. Memory Update
        self.MPA.update_profile(
            learner_id=input_data["learner_id"],
            emotional_state=emotional_state,
            progress=feedback.get("progress", None)
        )

        # 6. Validation
        validated_response = self.Validator.check(
            explanation=explanation,
            practice_questions=practice_questions
        )

        # 7. Response Delivery
        response = format_response(
            emotional_ack=emotional_state,
            explanation=validated_response["explanation"],
            questions=validated_response["practice_questions"],
            encouragement=generate_encouragement(emotional_state),
            progress=feedback.get("progress", None)
        )

        return response

# Example usage
if __name__ == "__main__":
    orchestrator = EALCOrchestrator()
    input_data = {
        "learner_id": "student_123",
        "query": "I don't understand this algebra problem at all!",
        "subject": "mathematics",
        "difficulty_level": "intermediate"
    }
    response = orchestrator.process_learner_input(input_data)
    print(response)
# Orchestrator Agent skeleton
