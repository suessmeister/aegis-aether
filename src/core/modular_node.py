class Module:
    def execute(self, data):
        raise NotImplementedError("Each module must implement the execute method.")

class ModularNode:
    def __init__(self, id):
        self.id = id
        self.modules = []

    def add_module(self, module):
        self.modules.append(module)

    def process(self, data):
        for module in self.modules:
            data = module.execute(data)
        return data

# Example usage
if __name__ == "__main__":
    class PrintModule(Module):
        def execute(self, data):
            print(f"Node received: {data}")
            return data

    node = ModularNode(1)
    node.add_module(PrintModule())
    node.process("Hello, World!")