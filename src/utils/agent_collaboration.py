import queue
import threading


class CollaborationFramework:
    """Handles collaboration and messaging between agents."""

    def __init__(self):
        self.message_queue = queue.Queue()

    def send_message(self, sender_id, recipient_id, message):
        """Send a message to another agent."""
        self.message_queue.put({
            "sender_id": sender_id,
            "recipient_id": recipient_id,
            "message": message
        })
        print(f"Message sent from Agent {sender_id} to Agent {recipient_id}: {message}")

    def receive_message(self, agent_id):
        """Receive messages for a specific agent."""
        messages = []
        while not self.message_queue.empty():
            msg = self.message_queue.get()
            if msg["recipient_id"] == agent_id:
                messages.append(msg)
            else:
                # Put back messages not meant for this agent
                self.message_queue.put(msg)
                break
        return messages

    def delegate_task(self, sender_id, recipient_id, task_description):
        """Delegate a task to another agent."""
        self.send_message(sender_id, recipient_id, f"Task delegation: {task_description}")
        print(f"Agent {sender_id} delegated task to Agent {recipient_id}: {task_description}")