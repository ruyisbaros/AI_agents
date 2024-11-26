from loguru import logger
import sys
import os


if not os.path.exists("../logs"):
    os.makedirs("../logs")

logger.remove()
logger.add(
    sys.stdout, format="<green> {timestamp}</green> <level>{message}</level>")
logger.add("../logs/agent_manager.log",
           format="{time} {level} {message}", level="DEBUG", rotation="1 MB", retention="10 days")
