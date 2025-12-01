EALC — Emotion-Adaptive Learning Companion

EALC is an AI-powered multi-agent educational system that personalizes learning in real time by detecting learner emotions, analyzing performance, and dynamically adapting teaching strategies. The system enhances engagement, motivation, and mastery through emotionally-aware, personalized instruction.

🚀 Features

Real-time emotion detection (frustration, confidence, confusion, etc.)

Adaptive teaching strategies based on emotional & cognitive state

Personalized explanations, practice questions, and feedback

Learner memory profiling for long-term progression

Full logging, validation, and decision-trace auditing

🧠 How It Works

EALC coordinates five core agents:

Emotion Detection Agent (EDA) — Interprets emotional cues

Teaching Strategy Agent (TSA) — Chooses the best instructional approach

Knowledge Tutor Agent (KTA) — Generates explanations & examples

Assessment & Feedback Agent (AFA) — Produces questions & feedback

Memory Profile Agent (MPA) — Updates learner history & progress

These agents operate sequentially through the EALC orchestrator to provide adaptive, personalized learning.

🔄 Orchestrator Workflow

The EALC orchestrator manages all agents to deliver a cohesive learning experience:

Emotion Detection
Learner input is analyzed to detect emotional states like frustration, confidence, or confusion.

Strategy Selection
The system selects an optimal teaching strategy based on emotion, subject, and difficulty (e.g., supportive, clarifying, challenging).

Personalized Content Generation
Explanations, examples, and learning content are tailored to the learner’s profile and the chosen strategy.

Assessment & Feedback
Practice questions and exercises are generated, and learner responses are evaluated to provide constructive feedback and track progress.

Memory Update
Learner profiles are updated with emotional patterns, learning history, and progress for long-term personalization.

Validation
All outputs are validated to ensure educational quality, accuracy, and emotional sensitivity.

Response Delivery
Learners receive an integrated response including empathetic acknowledgment, personalized content, interactive questions, motivational prompts, and progress tracking.

🧠 Example Interactions

Frustrated Learner

Input:

{
  "learner_id": "student_123",
  "query": "I don't understand this algebra problem at all! I've been trying for an hour and nothing makes sense!",
  "subject": "mathematics",
  "difficulty_level": "intermediate"
}


Agent Process:

EDA: High frustration detected

TSA: Supportive, step-by-step strategy

KTA: Simplified explanation

AFA: Easy→medium practice questions

MPA: Stores frustration pattern

Output:
"I can hear that you're feeling frustrated — and that's completely normal. Let’s take this step by step. Here’s the first piece…"

Confident Learner

Input:

{
  "learner_id": "student_456",
  "query": "I solved that calculus problem easily! What's next?",
  "subject": "mathematics",
  "difficulty_level": "advanced"
}


Agent Process:

EDA: High confidence

TSA: Challenging extension strategy

KTA: Advanced applications

AFA: Complex problem set

MPA: Records mastery progression

Output:
"Excellent work! Since you're ready for more advanced challenges, let's explore real-world optimization problems..."

🔒 Error Handling & Observability

EALC supports:

Full agent-interaction logging

Decision trace auditing

Retry mechanisms for failed agent calls

Validation before response delivery

Monitoring emotional-detection accuracy

Engagement and learning metrics tracking

💡 Output Format

EALC responses always include:

Empathetic acknowledgment

Personalized explanations

Interactive practice questions

Encouragement and motivation

Learning progress tracking

📚 Knowledge Sources

knowledge.expanded_learner_interaction_dataset

knowledge.www_wiley_com_en_in_grow_teach_learn

knowledge.knewton_alta

knowledge.studentlife_cs_dartmouth_edu

🔧 Installation

Requires Python 3.11.3.

Create a virtual environment:

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows


Install dependencies:

pip install -r requirements.txt


Run the agent in ADK Web mode:

adk web


Run integration tests:

python -m tests.test_agent

📦 Folder Structure
EALC/
│── ealc_orchestrator.py
│── agents/
│    ├── emotion_detection.py
│    ├── teaching_strategy.py
│    ├── knowledge_tutor.py
│    ├── assessment_feedback.py
│    ├── memory_profile.py
│    └── validators.py
│── tools/
│── data/
│── README.md

