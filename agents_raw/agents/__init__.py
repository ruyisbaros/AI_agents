from .refiner_agent import RefinerAgent
from .write_article_tool import WriteArticleTool
from .write_article_validator import WriteArticleValidator
from .sanitaze_tool import SanitazeTool
from .sanitaze_tool_validator import SanitazeToolValidator
from .summarize_tool import SummarizeTool
from .summarize_tool_validator import SummarizeToolValidator


class AgentManager:
    def __init__(self, max_retries, verbose=True):
        self.agents = {"summarize": SummarizeTool(max_retries=max_retries, verbose=verbose),
                       "summarize_validator": SummarizeToolValidator(max_retries=max_retries, verbose=verbose),
                       "write_article": WriteArticleTool(max_retries=max_retries, verbose=verbose),
                       "write_article_validator": WriteArticleValidator(max_retries=max_retries, verbose=verbose),
                       "sanitize_data": SanitazeTool(max_retries=max_retries, verbose=verbose),
                       "sanitize_data_validator": SanitazeToolValidator(max_retries=max_retries, verbose=verbose),
                       "refiner": RefinerAgent(max_retries=max_retries, verbose=verbose)}

    def get_agent(self, agent_name):
        agent = self.agents.get(agent_name)
        if agent is None:
            raise ValueError(f"Agent {agent_name} not found")
        return agent
