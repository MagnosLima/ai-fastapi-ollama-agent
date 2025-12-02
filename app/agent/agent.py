from strands import Agent

from app.agent.tools.calculator import calculator_tool


def create_agent():
    """
    Inicializa o agente principal com as ferramentas registradas.
    """
    agent = Agent(
        name="FastAPIOllamaAgent",
        instructions="Você é um agente que auxilia em cálculos e interações simples.",
        tools=[calculator_tool],  # Aqui adicionamos nossas ferramentas
    )

    return agent


# Instância única do agente para ser usada no FastAPI
agent_instance = create_agent()
