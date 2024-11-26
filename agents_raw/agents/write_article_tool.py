from .agents_base import AgentBase


class WriteArticleTool(AgentBase):
    def __init__(self, max_retries, verbose=True):
        super().__init__(name="WriteArticleTool", verbose=verbose, max_retries=max_retries)

    def execute(self, topic, outline=None):
        messages = [
            {"role": "system",
                "content": "You are an expert academy researcher and a writer."},
            {"role": "user", "content": f"Please write an article on following: \n\n {topic} \
                \n\n Article:"}
        ]

        article = self.call_openai(messages, max_tokens=500)
        return article
