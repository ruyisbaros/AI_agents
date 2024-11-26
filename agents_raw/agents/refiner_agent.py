from .agents_base import AgentBase


class RefinerAgent(AgentBase):
    def __init__(self, max_retries, verbose=True):
        super().__init__(name="RefinerAgent", verbose=verbose, max_retries=max_retries)

    def execute(self, draft):
        messages = [
            {"role": "system",
                "content":
                    [
                        {
                            "type": "text",
                            "text": "You are an academic researcher and editor that refines medical articles by improving the quality and clarity."
                        }
                    ]},
            {"role": "user", "content": (f"Please refine the following article draft to improve its language, coherence and overall quality : \n\n {draft}\
                \n\n Refined Article:")}
        ]

        refined_article = self.call_openai(
            messages, temprature=0.3, max_tokens=500)
        return refined_article
