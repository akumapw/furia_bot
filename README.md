Chat Bot FURIA para Telegram

Este projeto implementa um bot de chat no Telegram voltado para os fãs do time brasileiro de CS:GO, FURIA. O bot conversa com o usuário, coleta o nome, verifica se é fã, compartilha destaques de jogadores, fatos curiosos, resultados recentes e links para notícias.

📋 Funcionalidades

Saudação personalizada: solicita o nome do usuário e utiliza-o nas mensagens.

Verificação de fã: pergunta se o usuário é um “SUPER FURIOSO”.

Destaques de jogadores: ao escolher um jogador, exibe uma mensagem com clipes em vídeo.

Fatos sobre FURIA: quando o usuário não é fã, apresenta curiosidades aleatórias sobre a equipe.

Menu de opções:

🗓️ Últimos resultados de partidas.

🎮 Lista de jogadores com links para estatísticas no HLTV.

📰 Link para as notícias oficiais no X (antigo Twitter).

❌ Encerrar conversa.

🛠️ Tecnologias e Bibliotecas

Python 3.7 ou superior

python-telegram-bot

logging (módulo padrão do Python)

🚀 Pré-requisitos

Token do bot: crie um bot junto ao BotFather e obtenha o TELEGRAM_TOKEN.

Python 3.7+ instalado na máquina.

(Opcional) Ambiente virtual com venv ou virtualenv.

⚙️ Instalação

Clone este repositório:

git clone https://github.com/seu-usuario/chat-bot-furia.git
cd chat-bot-furia

(Opcional) Crie e ative um ambiente virtual:

python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\\Scripts\\activate  # Windows

Instale as dependências:

pip install -r requirements.txt

🔧 Configuração

Renomeie o arquivo config_example.py (se disponível) para config.py ou defina a variável de ambiente:

export TELEGRAM_TOKEN="SEU_TOKEN_AQUI"

Ou substitua diretamente na chamada de Application.builder().token("SEU_TOKEN") no código.

▶️ Como executar

No diretório do projeto, execute:

python bot.py

ou, se a função principal estiver em outro arquivo:

python main.py

O bot ficará ativo em modo polling, aguardando mensagens em seu chat do Telegram.

🗂️ Estrutura de Diretórios

chat-bot-furia/
├── bot.py              # Código principal do bot
├── requirements.txt    # Dependências do Python
├── README.md           # Este arquivo
└── .gitignore          # Arquivos e pastas a ignorar no Git

🤝 Contribuição

Contribuições são bem-vindas! Sinta-se livre para abrir issues e pull requests.
