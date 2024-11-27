import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_astradb import AstraDBVectorStore
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain.tools.retriever import create_retriever_tool
from langchain import hub

from github import fetch_github_issues
from note import note_tool

load_dotenv("../.env")

owner = "techwithtim"
repo = "Flask-Web-App-Tutorial"

ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
ASTRA_DB_API_ENDPOINT = os.getenv("ASTRA_DB_API_ENDPOINT")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

#### DB CONNECTIONS #####


def connect_to_vector_store():
    embeddings = OpenAIEmbeddings()

    vstore = AstraDBVectorStore(
        collection_name="github_agents",
        embedding=embeddings,
        token=ASTRA_DB_APPLICATION_TOKEN,
        api_endpoint=ASTRA_DB_API_ENDPOINT,
    )

    return vstore


vstore = connect_to_vector_store()
add_to_vstore = input(
    "Do you want to update the issues? (y/N): ").lower() in ["yes", "y"]

if add_to_vstore:
    issues = fetch_github_issues(owner, repo)
    try:
        vstore.delete_collection()
    except Exception as e:
        # print(f"Error deleting existing collection: {e}")
        pass

    vstore = connect_to_vector_store()  # after delete reconnect may need
    vstore.add_documents(issues)

    """ results = vstore.similarity_search("flash messages", k=3)

    for result in results:
        print(f"* {result.page_content} {result.metadata}") """


#### AGENT SETUP ####

retriever = vstore.as_retriever(search_kwargs={"k": 3})
retriever_tool = create_retriever_tool(
    retriever, "github_search", "Search for information about github issues. For any questions about github issues, you must use this tool!",)


prompt = hub.pull("hwchase17/openai-functions-agent")
llm = ChatOpenAI()
tools = [retriever_tool, note_tool]

agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

while (question := input("Ask a question about github issues (q to quit): ")) != "q":
    response = agent_executor.invoke({"input": question})
    print(response["output"])
