from agents_base import AgentBase


class WriteArticleValidator(AgentBase):
    def __init__(self, max_retries, verbose=True):
        super().__init__(name="WriteArticleValidator",
                         verbose=verbose, max_retries=max_retries)

    def execute(self, topic, article):
        messages = [
            {"role": "system",
                "content": "You are an expert academic researcher who validates the research articles."
             },
            {"role": "user", "content": f"Please assess the following article whether it comprehensively covers the topic, follows logical 
               structure and maintains academic standarts.\n Provide a brief analysis and rate the article on a scale of 1 to 5 accordingly. 5 indicates exxellent 
                   and 1 indicates worst quality. \n\nArticle:\n {article}\n\n Topic: {topic}
                \n\n Validation:"}
        ]

        validation = self.call_openai(
            messages, max_tokens=500)
        return validation
