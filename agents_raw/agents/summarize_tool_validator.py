from .agents_base import AgentBase


class SummarizeToolValidator(AgentBase):
    def __init__(self, max_retries, verbose=True):
        super().__init__(name="SummarizeToolValidator",
                         verbose=verbose, max_retries=max_retries)

    def execute(self, summarized_text, original_text):
        messages = [
            {"role": "system",
                "content": "You are an expert academic researcher who validates the summarized medical texts."
             },
            {"role": "user", "content": f"Given the original text and summarized text. Please verify wheter the summary accurately capture the key \
                points of original text.\n \
             Provide a brief analysis and rate the summarization on a scale of 1 to 5 accordingly. 5 indicates exxellent  \
                   and 1 indicates worst quality. \n\n Original text: {original_text}\n\n Summarized text:\n {summarized_text} \
                \n\n Validation:"}
        ]

        validation = self.call_openai(
            messages, max_tokens=500)
        return validation
