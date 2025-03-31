# 💡 Maki: The Idea Generator Chatbot
![](https://img.shields.io/badge/Ollama-000000.svg?style=for-the-badge&logo=Ollama&logoColor=white) ![](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white)

## Maki is a creative chatbot that generates ideas on demand! Built using `ollama.py`, Maki leverages a customized model to provide more personalized and context-aware ideas for various fields, from content creators to developers.

### 🌟 Key Features
- 🎯 On-Demand Idea Generation: Instantly provides ideas based on user prompts.
- 🔄 Dynamic Conversations: Creates interactive chat sessions to refine or expand ideas.
- 🧠 AI-Powered: Utilizes the power of ollama.py for intelligent and context-aware idea generation.
```mermaid
flowchart TD
    subgraph "User Interaction"
        A("User"):::user
        B("CLI (chatcli.py)"):::internal
    end

    subgraph "Backend Processing"
        C("Chatbot Engine (main.py)"):::internal
    end

    D("Ollama External AI Service"):::external

    A -->|"input"| B
    B -->|"prompt_to_engine"| C
    C -->|"send_request"| D
    D -->|"idea_response"| C
    C -->|"result_output"| B

    click B "https://github.com/tensho-otaku/maki_chatbot/blob/main/./chatcli.py"
    click C "https://github.com/tensho-otaku/maki_chatbot/blob/main/./main.py"

    classDef internal fill:#bbf,stroke:#333,stroke-width:2px;
    classDef external fill:#f96,stroke:#333,stroke-width:2px;
    classDef user fill:#afa,stroke:#333,stroke-width:2px;
```
### 📌 How to Run Maki
> [!IMPORTANT]
>Install `ollama` on your system
Ensure you have `ollama` installed to run Maki. For installation instructions, refer to [Ollama Documentation](https://ollama.com/).

1. Clone the repository
    ```shell
    git clone https://github.com/yourusername/maki-idea-generator
    ```
2. Install dependencies
    ```shell
    pip install ollama
    ```
3. Run Maki
    ```shell
    python main.py
    ```
    
