class Module:
    """Base class for all modules."""
    def execute(self, data):
        raise NotImplementedError("Modules must implement the execute method.")

class ModularAgent:
    """A modular agent that can dynamically load and execute modules."""
    def __init__(self, id):
        self.id = id
        self.modules = {}

    def add_module(self, name, module):
        """Add a module to the agent."""
        self.modules[name] = module

    def remove_module(self, name):
        """Remove a module from the agent."""
        if name in self.modules:
            del self.modules[name]

    def process(self, data):
        """Process data through all loaded modules."""
        for name, module in self.modules.items():
            print(f"Executing module: {name}")
            data = module.execute(data)
        return data

# Example usage
if __name__ == "__main__":
    class MultiplyModule(Module):
        def execute(self, data):
            return data * 2

    agent = ModularAgent(1)
    agent.add_module("multiplier", MultiplyModule())
    print(agent.process(10))  # Output: 20