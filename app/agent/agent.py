from strands import Agent

from app.agent.tools.calculator import calculator_tool


def create_agent():
    """
    Inicializa o agente principal com as ferramentas registradas.
    """
    agent = Agent(
        name="FastAPIOllamaAgent",
        tools=[calculator_tool],
    )

    return agent


# Instância única do agente para ser usada no FastAPI
agent_instance = create_agent()
