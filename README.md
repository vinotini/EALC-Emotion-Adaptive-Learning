# EALC — Emotion-Adaptive Learning Companion

**EALC** is an AI-powered multi-agent educational system that personalizes learning in real time by detecting learner emotions, analyzing performance, and dynamically adapting teaching strategies. It enhances engagement, motivation, and mastery through emotionally-aware, personalized instruction.

---

## 🚀 Features

- Real-time emotion detection (frustration, confidence, confusion, etc.)  
- Adaptive teaching strategies based on emotional & cognitive state  
- Personalized explanations, practice questions, and feedback  
- Learner memory profiling for long-term progression  
- Full logging, validation, and decision-trace auditing  

---

## 🧠 How It Works

EALC coordinates **five core agents**:

1. **Emotion Detection Agent (EDA)** — Interprets emotional cues  
2. **Teaching Strategy Agent (TSA)** — Chooses the best instructional approach  
3. **Knowledge Tutor Agent (KTA)** — Generates explanations & examples  
4. **Assessment & Feedback Agent (AFA)** — Produces questions & feedback  
5. **Memory Profile Agent (MPA)** — Updates learner history & progress  

These agents operate sequentially through the **EALC orchestrator** to deliver adaptive, personalized learning experiences.

---

## 🔄 Orchestrator Workflow

The EALC orchestrator manages all agents to deliver a cohesive learning experience:

1. **Emotion Detection**  
   Learner input is analyzed to detect emotional states like frustration, confidence, or confusion.

2. **Strategy Selection**  
   The system selects an optimal teaching strategy based on emotion, subject, and difficulty (supportive, clarifying, challenging, etc.).

3. **Personalized Content Generation**  
   Explanations, examples, and learning content are tailored to the learner’s profile and the chosen strategy.

4. **Assessment & Feedback**  
   Practice questions and exercises are generated, and learner responses are evaluated to provide constructive feedback and track progress.

5. **Memory Update**  
   Learner profiles are updated with emotional patterns, learning history, and progress.

6. **Validation**  
   All outputs are validated to ensure educational quality, accuracy, and emotional sensitivity.

7. **Response Delivery**  
   Learners receive an integrated response including empathetic acknowledgment, personalized content, interactive questions, motivational prompts, and progress tracking.

---


## 🔧 Installation & Setup

EALC requires **Python 3.11.3**.

1. **Create a virtual environment**:  
```bash
python -m venv venv
# Activate the environment
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
