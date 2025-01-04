import yaml

class AgentConfig:
    def __init__(self, config_file):
        with open(config_file, "r") as f:
            self.config = yaml.safe_load(f)

    def get_name(self):
        return self.config.get("name", "DefaultAgent")

    def get_personality(self):
        return self.config.get("personality", "neutral")

    def get_specialization(self):
        return self.config.get("specialization", "general")

    def display_config(self):
        print("Agent Configuration:")
        for key, value in self.config.items():
            print(f"{key}: {value}")