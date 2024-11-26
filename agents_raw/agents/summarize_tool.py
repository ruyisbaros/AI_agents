from agents_base import AgentBase


class SummarizeTool(AgentBase):
    def __init__(self, max_retries, verbose=True):
        super().__init__(name="SummarizeTool", verbose=verbose, max_retries=max_retries)

    def execute(self, text):
        messages = [
            {"role": "system",
                "content": "you are an AI assistant that summarizes the medical texts"},
            {"role": "user", "content": f"Please provide a concise summary of the following text: \n\n {text}
                \n\n Summary:"}
        ]

        summary = self.call_openai(messages)
        return summary
