# EALC — Emotion-Adaptive Learning Companion

EALC is an AI-powered multi-agent educational system that personalizes learning in real time by detecting learner emotions, analyzing performance, and dynamically adapting teaching strategies. The system enhances engagement, motivation, and mastery through emotionally-aware, personalized instruction.

## 🚀 Features
- Real-time emotion detection (frustration, confidence, confusion, etc.)
- Adaptive teaching strategies based on emotional & cognitive state
- Personalized explanations, practice questions, and feedback
- Learner memory profiling for long-term progression
- Full logging, validation, and decision-trace auditing

## 🧠 How It Works
EALC coordinates five core agents:
1. **Emotion Detection Agent (EDA)** — Interprets emotional cues  
2. **Teaching Strategy Agent (TSA)** — Chooses the best instructional approach  
3. **Knowledge Tutor Agent (KTA)** — Generates explanations & examples  
4. **Assessment & Feedback Agent (AFA)** — Produces questions & feedback  
5. **Memory Profile Agent (MPA)** — Updates learner history & progress  

These agents operate sequentially through the EALC orchestrator.

## 🔧 Installation

EALC requires **Python 3.11.3**.

1. Create a virtual environment (recommended):  
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
# EALC Orchestrator Workflow (Python-style pseudocode)

def process_learner_input(input_data):
    """
    Orchestrates all EALC agents to generate an adaptive, personalized response.
    """

    # 1. Emotion Detection
    emotional_state = EDA.detect_emotion(input_data["query"])
    
    # 2. Strategy Selection
    teaching_strategy = TSA.select_strategy(
        emotional_state=emotional_state,
        difficulty=input_data["difficulty_level"],
        subject=input_data["subject"]
    )
    
    # 3. Personalized Content Generation
    explanation = KTA.generate_content(
        query=input_data["query"],
        strategy=teaching_strategy,
        learner_profile=MPA.get_profile(input_data["learner_id"])
    )
    
    # 4. Assessment & Feedback
    practice_questions = AFA.create_questions(
        explanation=explanation,
        strategy=teaching_strategy
    )
    
    feedback = AFA.evaluate_response(
        learner_response=input_data.get("learner_response")
    )
    
    # 5. Memory Update
    MPA.update_profile(
        learner_id=input_data["learner_id"],
        emotional_state=emotional_state,
        progress=feedback.get("progress", None)
    )
    
    # 6. Validation
    validated_response = Validator.check(
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

