from flask import Flask, render_template, jsonify
from src.agents.ai_agent import AIAgent
import threading
import random

app = Flask(__name__)

# Simulated agents for demonstration
agents = [
    AIAgent(agent_id=1, role="worker", provider="openai", base_url="https://api.openai.com"),
    AIAgent(agent_id=2, role="worker", provider="openai", base_url="https://api.openai.com"),
    AIAgent(agent_id=3, role="coordinator", provider="openai", base_url="https://api.openai.com"),
]

# Background task to simulate agent activity
def simulate_agent_activity():
    while True:
        for agent in agents:
            task = f"Task-{random.randint(1, 100)}"
            agent.add_task(priority=random.randint(1, 5), task_description=task)
            agent.process_next_task()

# Start background thread for simulation
threading.Thread(target=simulate_agent_activity, daemon=True).start()

@app.route("/")
def index():
    return render_template("dashboard.html")

@app.route("/api/metrics")
def get_metrics():
    metrics = []
    for agent in agents:
        metrics.append({
            "id": agent.agent_id,
            "role": agent.role,
            "knowledge_base_size": len(agent.knowledge_base),
            "task_queue_size": agent.task_queue.qsize(),
        })
    return jsonify(metrics)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)