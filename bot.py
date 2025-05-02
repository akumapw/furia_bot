import logging
import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, ConversationHandler, CallbackQueryHandler, MessageHandler, filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

NAME, FAN_QUESTION, OPTIONS = range(3)

Highlights = {
    "FalleN": "FalleN é conhecido por suas habilidades de AWP e liderança. Aqui um clipe do lendário FalleN:▶️ https://www.youtube.com/watch?v=7CJ4UXefngA",
    "chelo": "Chelo é um rifler versátil com grande experiência em competições internacionais. Aqui um clipe do nosso menino Chelo:▶️ https://www.youtube.com/watch?v=brAIvXM-9_w",
    "yuurih": "Yuurih é famoso por suas jogadas clutch e mira precisa. Saca só esse clip..:▶️ https://www.youtube.com/watch?v=OviF7bKEBGQ",
    "KSCERATO": "KSCERATO é um dos melhores jogadores do Brasil, com destaque em vários torneios. Saca Só esse compilado do KSCERATO:▶️ https://www.youtube.com/shorts/6AsDMhJkYNo",
    "skullz": "Skullz é um jovem talento que já mostrou grande potencial na equipe. Se liga como nosso menino joga!▶️ https://www.youtube.com/shorts/6ccttAWzPPk"
}

facts = [
    " A Super Furia foi fundada em agosto de 2017 no Brasil",
    " Nossa Furiosa é conhecida pelo seu estilo agressivo no CS:GO",
    "Nossa seleção tem times em diversos jogos incluindo CS:GO, VALORANT, "
    " O logotipo da Fúria é uma pantera, simbolizando agilidade e força."
    " Nossa Furia participou de vários torneios internacionais e tem uma grande base de fãs."
]


def get_recent_matches():
    return [
        "2025-04-20: Fúiria vs Team Liquid - Vitória 2-0",
        "2025-04-15: Fúria vs G2 Esports - Derrota 1-2",
        "2025-04-10: Fúria vs MIBR - Vitória 2-1",
    ]

players = [
    "FalleN: https://www.hltv.org/stats/players/2023/fallen",
    "Chelo https://www.hltv.org/stats/players/10566/chelo",
    "Yuurih: https://www.hltv.org/stats/players/12553/yuurih",
    "KSCERATO: https://www.hltv.org/stats/players/15631/kscerato", 
    "Skullz https://www.hltv.org/stats/players/18676/skullz"
    ]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("🖤💛 Oi! Sou um bot FURIA. Qual é o seu nome?")
    return NAME

async def name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['name'] = update.message.text
    logger.info("Nome: %s", update.message.text)
    keyboard = [
        [InlineKeyboardButton("Sim, sou FURIOSO!", callback_data='fan_yes')],
        [InlineKeyboardButton("Ainda não", callback_data='fan_no')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        f"Prazer em conhecê-lo, {update.message.text}! Você também é um SUPER FURIOSO ?",
        reply_markup=reply_markup
    )
    return FAN_QUESTION

async def fan_response(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    choice = query.data
    name = context.user_data['name']
    logger.info(f"Resposta sobre ser fã: {choice}")
    if choice == 'fan_yes':
        await query.edit_message_text(f"Que Bom, FUR {name}! A Super Fúria é incrível né? Qual é seu jogador favorito?")
        Keyboard = [
            [InlineKeyboardButton("FalleN", callback_data='player_FalleN')],
            [InlineKeyboardButton("chelo", callback_data='player_chelo')],
            [InlineKeyboardButton("yuurih", callback_data='player_yuurih')],
            [InlineKeyboardButton("KSCERATO", callback_data='player_KSCERATO')],
            [InlineKeyboardButton("skullz", callback_data='player_skullz')],
        ]
        reply_markup = InlineKeyboardMarkup(Keyboard)
        await query.message.reply_text("Escolha um Jogador:", reply_markup=reply_markup)
        return OPTIONS
    else:
        await query.edit_message_text(f"Tudo bem, {name}. Talvez você vire fã depois de assistir aos jogos deles. Eles são muito bons!")
    fact = random.choice(facts)
    await query.message.reply_text(f"A propósito, você sabia que {fact}?")   
    await query.message.reply_text("Quer saber mais sobre a Fúria? Confira o site oficial!: https://www.furia.gg/ ou siga no X: @FURIA")
    Keyboard = [
        [InlineKeyboardButton("📅Últimos resultados", callback_data='results')],
        [InlineKeyboardButton("🎮Jogadores", callback_data='players')],
        [InlineKeyboardButton("📅Notícias", callback_data='news')],
        [InlineKeyboardButton("❌Nada, obrigado", callback_data='end')],
    ]
    reply_markup = InlineKeyboardMarkup(Keyboard)
    logger.info("Enviando menu de opções")
    await query.message.reply_text("O que você gostaria de saber sobre Fúria?", reply_markup=reply_markup)    
    return OPTIONS

async def option_selected(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    choice = query.data
    logger.info(f"Opção selecionada: {choice}")
    if choice.startswith('player_'):
        player = choice.split('_')[1]
        context.user_data['favorite_player'] = player
        hihighlight = Highlights.get(player, "Informação não disponível.")
        await query.edit_message_text(f"Você escolheu {player}! {hihighlight}" )
    if choice == 'results':
        matches = get_recent_matches()
        await query.edit_message_text(text="📅 Aqui estão os últimos resultados:\n" + "\n".join(matches))
    elif choice == 'players':
        await query.edit_message_text(text="🎮 Os jogadores atuais são: " + ", ".join(players))
    elif choice == 'news':
        await query.edit_message_text(text="📰 Confira as últimas notícias no X da Fúria: https://x.com/FURIA")
    elif choice == 'end':
        await query.edit_message_text(text="Obrigado por conversar! Até a próxima 🖤💛")
        return ConversationHandler.END
    Keybord = [
        [InlineKeyboardButton("Últimos resultados", callback_data='results')],
        [InlineKeyboardButton("Jogadores", callback_data='players')],
        [InlineKeyboardButton("Notícias", callback_data='news')],
        [InlineKeyboardButton("Nada, obrigado", callback_data='end')]
    ]
    reply_markup = InlineKeyboardMarkup(Keybord)
    logger.info("Enviando menu de opções novamente")
    await query.message.reply_text("Mais alguma coisa?", reply_markup=reply_markup)
    return OPTIONS

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text('Obrigado por conversar! Até a próxima 🖤💛')
    return ConversationHandler.END

def main() -> None:
    application = Application.builder().token('8119855628:AAF-gvahskdXg9TlFVmSovLPsya7uVHLSPA').build()
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, name)],
            FAN_QUESTION: [CallbackQueryHandler(fan_response)],
            OPTIONS: [CallbackQueryHandler(option_selected)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    application.add_handler(conv_handler)
    application.run_polling()

if __name__ == '__main__':
    main()
