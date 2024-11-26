from agents_base import AgentBase


class SanitazeToolValidator(AgentBase):
    def __init__(self, max_retries, verbose=True):
        super().__init__(name="SanitazeToolValidator",
                         verbose=verbose, max_retries=max_retries)

    def execute(self, original_data, sanitazed_data):
        messages = [
            {"role": "system",
                "content": "You are an expert academic researcher who validates the sanitazed medical data by checking removal of Protected Health Information (PHI)."
             },
            {"role": "user", "content": f"Given the original data and sanitazed data. Please verify all PHI has been removed.\n 
             Provide a brief analysis and rate the sanitization on a scale of 1 to 5 accordingly. 5 indicates exxellent 
                   and 1 indicates worst quality. \n\n Original Data: {original_data}\n\n Sanitazed data:\n {sanitazed_data}
                \n\n Validation:"}
        ]

        validation = self.call_openai(
            messages, max_tokens=500)
        return validation
