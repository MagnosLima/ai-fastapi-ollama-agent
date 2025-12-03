# FastAPI + Ollama Agent API

API de chat desenvolvida com **FastAPI** integrada a um **Agente de IA utilizando Strands Agents SDK** e **Ollama** como provedor LLM local.  
O projeto inclui uma **tool de cálculo matemático** que o agente utiliza automaticamente quando identifica operações numéricas na pergunta.

---

## ✅ Funcionalidades

- ✅ Endpoint `POST /chat`
- ✅ Integração direta com Ollama via `Strands Agents`
- ✅ Tool de cálculo matemático automática
- ✅ Respostas em JSON
- ✅ Execução local
- ✅ Configuração por `.env`
- ✅ Estrutura organizada por módulos

---

## 🧠 Arquitetura

- **FastAPI** → API HTTP
- **Strands Agents SDK** → Orquestração do agente
- **Ollama (local)** → LLM
- **Tool Calculator** → Cálculos matemáticos automáticos

Comunicação com o Ollama é feita **diretamente pelo Strands**, sem uso de `httpx`.

---

## 📁 Estrutura do Projeto

    dreamsquad-ia-chat/
    ├── app/
    │   ├── agent/
    │   │   ├── agent.py
    │   │   └── tools/
    │   │       └── calculator.py
    │   ├── core/
    │   │   └── config.py
    │   ├── schemas/
    │   │   └── chat.py
    │   └── main.py
    ├── venv/
    ├── .env
    ├── .env.example
    ├── .gitignore
    ├── requirements.txt
    └── README.md

------------------------------------------------------------------------

## ⚙️ Configuração do Ambiente

### 1️⃣ Clonar o repositório

``` bash
git clone https://github.com/MagnosLima/ai-fastapi-ollama-agent.git
cd ai-fastapi-ollama-agent
```

------------------------------------------------------------------------

### 2️⃣ Criar e ativar ambiente virtual

``` bash
python -m venv venv
```

#### Windows (PowerShell / Git Bash):

``` bash
venv\Scripts\activate
```

#### Linux / Mac:

``` bash
source venv/bin/activate
```

#### Git Bash:

``` bash
source venv/Scripts/activate
```

------------------------------------------------------------------------

### 3️⃣ Instalar dependências

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

### 4️⃣ Instalar e configurar o Ollama

✅ Baixar o Ollama: https://ollama.com

✅ Baixar o modelo utilizado no projeto:

``` bash
ollama pull qwen3:4b
```

✅ Verificar se o Ollama está rodando:

``` bash
ollama list
```

⚠️ O servidor padrão do Ollama roda em:

    http://localhost:11434

------------------------------------------------------------------------

### 5️⃣ Configurar variáveis de ambiente

Crie um arquivo `.env` baseado no `.env.example`:

``` env
LLM_MODEL=qwen3:4b
LLM_ENDPOINT=http://localhost:11434
```

------------------------------------------------------------------------

## ▶️ Executando a Aplicação

Com o ambiente virtual ativo:

``` bash
uvicorn app.main:app --reload
```

✅ A aplicação estará disponível em:

    http://127.0.0.1:8000

✅ Documentação interativa (Swagger):

    http://127.0.0.1:8000/docs

------------------------------------------------------------------------

## 🔁 Endpoint de Chat

### 📌 POST /chat

### Exemplo de Request:

``` json
{
  "message": "Qual é a capital da França?"
}
```

### Exemplo de Response:

``` json
{
  "response": "A capital da França é Paris."
}
```

------------------------------------------------------------------------

## 🧮 Teste da Tool de Cálculo

Exemplos de perguntas:

``` json
{
  "message": "1234 * 5678"
}
```

Resposta esperada:

``` json
{
  "response": "7006652"
}
```

Outro exemplo:

``` json
{
  "message": "Qual a raiz quadrada de 144?"
}
```

``` json
{
  "response": "12"
}
```

------------------------------------------------------------------------

## 🧠 Funcionamento do Agente

-   O agente utiliza o modelo local do Ollama.
-   Caso identifique uma operação matemática, ele chama automaticamente
    a **tool calculator**.
-   Caso contrário, responde utilizando o LLM normalmente.

------------------------------------------------------------------------

## 🛑 Encerrando a Aplicação

No terminal onde o Uvicorn está rodando:

    CTRL + C

------------------------------------------------------------------------

## 📦 Versionamento

O projeto já possui `.gitignore` configurado para ignorar:

-   Ambiente virtual (`venv/`)
-   Arquivo `.env`
-   Cache do Python
-   Arquivos temporários
-   Binários do Ollama

------------------------------------------------------------------------

## ✅ Status do Projeto

✔ API operacional\
✔ Integração com Ollama funcionando\
✔ Tool de cálculo validada\
✔ Swagger funcionando

------------------------------------------------------------------------

## 👨‍💻 Autor

[Magnos Lima ](https://github.com/MagnosLima)
