# EALC – Emotion-Adaptive Learning Companion

**EALC (Emotion-Adaptive Learning Companion)** is a research-grade, emotionally intelligent multi-agent tutoring system that dynamically adapts instruction to each learner’s emotional state, cognitive level, and performance. Designed for next-generation AI education systems, EALC orchestrates a suite of specialized agents to deliver empathic, highly personalized learning interactions.

---

## 🧠 Role & Objective

EALC serves as an orchestrator that coordinates all sub-agents to:

- Detect learner emotions in real time  
- Select optimal teaching strategies  
- Generate personalized explanations  
- Provide assessment and constructive feedback  
- Manage long-term learner memory & profiles  
- Validate educational quality and emotional appropriateness  
- Maintain full observability with logging & error handling  

The system aims to replicate human-like emotional sensitivity while delivering adaptive pedagogy.

---

## 🔧 Multi-Agent Architecture

EALC consists of the following core agents:

### **1. Emotion Detection Agent (EDA)**
Identifies emotional states:
- frustrated  
- confused  
- confident  
- engaged  

Uses sentiment cues, linguistic markers, and educational psychology patterns.

### **2. Teaching Strategy Agent (TSA)**
Maps emotion + learning context to strategy:
- Frustrated → supportive  
- Confused → clarifying  
- Confident → challenging  
- Engaged → extension  

### **3. Knowledge Tutor Agent (KTA)**
Generates content:
- personalized explanations  
- simplified breakdowns  
- advanced conceptual extensions  
- examples, analogies, scaffolding  

### **4. Assessment & Feedback Agent (AFA)**
Creates:
- adaptive questions  
- formative feedback  
- confidence-building practice  

### **5. Memory/Profile Agent (MPA)**
Stores:
- learner preferences  
- emotional patterns  
- past performance  
- session history  

### **6. Validation Agents**
Ensure:
- correctness  
- safety  
- emotional appropriateness  
- pedagogical quality  

### **7. Tool Agents**
Integrate with:
- search tools  
- summarizers  
- external data sources  

---

## 🧩 Agent Workflow

1. **Input Processing**  
   Receive learner query + context.

2. **Emotion Detection**  
   Analyze emotional indicators using:
   - Anthropic knowledge search  
   - OpenAI function-based analysis  

3. **Teaching Strategy Selection**  
   Choose strategy (supportive, clarifying, challenging, encouraging).

4. **Personalized Content Generation**  
   Use:
   - Gemini knowledge search  
   - Combined educational datasets  

5. **Assessment Creation**  
   Generate exercises via:
   - OpenAI summarizer tools  
   - Custom assessment logic  

6. **Memory Update**  
   Long-term learner profiling.

7. **Validation**  
   Emotional + educational quality verification.

8. **Response Delivery**  
   A unified, empathetic, pedagogically aligned output.

---

## 🧠 Reasoning Steps (Internal Logic)

EALC processes each learner interaction through the following reasoning pipeline:

- Extract learning topic & prior context  
- Detect emotion using text signals  
- Map emotion → teaching strategy  
- Generate personalized explanation  
- Design reinforcement assessment  
- Update learner memory  
- Validate for emotional safety & quality  
- Produce a cohesive final response  

---

## 📥 Expected Input Format

```json
{
    "learner_id": "unique_learner_identifier",
    "session_id": "current_session_id",
    "query": "learner's question or response",
    "subject": "mathematics/science/history/etc",
    "difficulty_level": "beginner/intermediate/advanced",
    "previous_interactions": ["array of recent interactions"],
    "timestamp": "2024-01-01T12:00:00Z"
}
