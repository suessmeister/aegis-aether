from flask import Flask, jsonify, request
from src.core.modular_agent import ModularAgent

app = Flask(__name__)
agent = ModularAgent(1)

@app.route("/add_module", methods=["POST"])
def add_module():
    data = request.json
    module_name = data["name"]
    # Dynamically add a module (for simplicity, a placeholder here)
    agent.add_module(module_name, lambda x: x + " processed")
    return jsonify({"message": f"Module {module_name} added."})

@app.route("/process", methods=["POST"])
def process():
    data = request.json
    input_data = data["input"]
    result = agent.process(input_data)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True, port=5001)