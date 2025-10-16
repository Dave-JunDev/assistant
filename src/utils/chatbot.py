from strands import Agent
from strands.models.ollama import OllamaModel
from strands.agent.conversation_manager import SummarizingConversationManager

custom_system_prompt = """
You are summarizing a technical conversation. Create a concise bullet-point summary that:
- Focuses on code changes, architectural decisions, and technical solutions
- Preserves specific function names, file paths, and configuration details
- Omits conversational elements and focuses on actionable information
- Uses technical terminology appropriate for software development
"""

class Chatbot:
    def __init__(self):
        ollama_model = OllamaModel(
            host="http://host.docker.internal:11434",
            model_id="gemma3:4b",
            temperature=0.6,
        )
        conversation_manager = SummarizingConversationManager(
            summary_ratio=0.5,  # Summarize 30% of messages when context reduction is needed
            preserve_recent_messages=10,
            summarization_system_prompt=custom_system_prompt
        )
        self.agent = Agent(model=ollama_model, conversation_manager=conversation_manager)

    def get_response(self, prompt: str) -> str:
        response = self.agent(prompt)
        print("messages:", self.agent.messages)
        return response.message["content"][0]["text"]

    def set_conversation_history(self, messages):
        formatted_messages = [{"content":[{"text": msg.content}] , "role": msg.role } for msg in messages]
        self.agent.messages = formatted_messages