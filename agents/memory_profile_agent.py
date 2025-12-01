# Memory/Profile Agent skeleton
import os, json

class MemoryProfileAgent:
    DATA_FILE = "data/learner_profiles.json"

    def __init__(self):
        os.makedirs("data", exist_ok=True)
        if not os.path.exists(self.DATA_FILE):
            with open(self.DATA_FILE, "w") as f:
                json.dump({}, f)

    def get_profile(self, learner_id):
        with open(self.DATA_FILE) as f:
            profiles = json.load(f)
        return profiles.get(learner_id, {})

    def update_profile(self, learner_id, emotional_state, progress):
        with open(self.DATA_FILE) as f:
            profiles = json.load(f)
        profiles[learner_id] = {"emotional_state": emotional_state, "progress": progress}
        with open(self.DATA_FILE, "w") as f:
            json.dump(profiles, f, indent=2)
