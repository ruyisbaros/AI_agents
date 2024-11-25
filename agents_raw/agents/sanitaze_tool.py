from agents_base import AgentBase


class SanitazeTool(AgentBase):
    def __init__(self, max_retries, verbose=True):
        super().__init__(name="SanitazeTool", verbose=verbose, max_retries=max_retries)

    def execute(self, medical_data):
        messages = [
            {"role": "system",
                "content": "you are an AI assistant that sanitazes medical data by removing Protected Health Information (PHI)"},
            {"role": "user", "content": f"Please remove all PHI from following data: \n\n {medical_data}\
                \n\n Sanitazed Data:"}
        ]

        sanitazed_data = self.call_openai(messages)
        return sanitazed_data
