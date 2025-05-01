import logging
import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, ConversationHandler, CallbackQueryHandler, MessageHandler, filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

NAME, FAN_QUESTION, OPTIONS = range(3)

facts = [
    "Fato Cúrioso A Super Furia foi fundada em agosto de 2017 no Brasil",
    "Fato Cúrioso Nossa Furiosa é conhecida pelo seu estilo agressivo no CS:GO",
    "Fato CúriosoNossa seleção tem times em diversos jogos incluindo CS:GO, VALORANT, "
    "Fato Cúrioso O logotipo da Fúria é uma pantera, simbolizando agilidade e força."
    "Fato Cúrioso Nossa Furia participou de vários torneios internacionais e tem uma grande base de fãs."
]

def get_recent_matches():
    return [
        "2025-04-20: Fúiria vs Team Liquid - Vitória 2-0",
        "2025-04-15: Fúria vs G2 Esports - Derrota 1-2",
        "2025-04-10: Fúria vs MIBR - Vitória 2-1",
    ]

players = ["FalleN", "Chelo", "Yuutih", "KSCERATO", "Skullz"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Oi! Sou um grande fã da Fúria no CS:GO. Qual é o seu nome?")
    return NAME

async def name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['name'] = update.message.text
    logger.info("Nome: %s", update.message.text)
    logger.info("Nome: %s", update.message.text)
    keyboard = [
        [InlineKeyboardButton("Sim", callback_data='fan_yes')],
        [InlineKeyboardButton("Não", callback_data='fan_no')]
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
    if choice == 'fan_yes':
        await query.edit_message_text(f"Que Bom, {name}! A Super Fúria é incrível né? -_- Nosso time tem os melhores jogadores como o lendário FalleN e KSCERATO.")
    else:
        await query.edit_message_text(f"Tudo bem, {name}. Talvez você vire fã depois de assistir aos jogos deles. Eles são muito bons!")
    fact = random.choice(facts)
    await query.message.reply_text(f"A propósito, você sabia que {fact}")
    await query.message.reply_text("Quer saber mais sobre a Fúria? Confira o site oficial!: https://www.furia.gg/ ou siga no X: @FURIA")
    Keyboard = [
        [InlineKeyboardButton("Últimos resultados", callback_data='results')]
        [InlineKeyboardButton("Jogadores", callback_data='players')],
        [InlineKeyboardButton("Notícias", callback_data='news')],
        [InlineKeyboardButton("Nada, obrigado", callback_data='end')]
    ]
    reply_markup = InlineKeyboardMarkup(Keyboard)
    await query.message.reply_text("O que você gostaria de saber sobre Fúria?", reply_markup=reply_markup)
    return OPTIONS

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text('Conversa Cancelada.')
    return ConversationHandler.END

def main() -> None:
    application = Application.builder().token('8119855628:AAF-gvahskdXg9TlFVmSovLPsya7uVHLSPA').build()
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, name)],
            FAN_QUESTION: [MessageHandler(filters.TEXT & ~filters.COMMAND, fan_response)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    application.add_handler(conv_handler)
    application.run_polling()

if __name__ == '__main__':
    main()