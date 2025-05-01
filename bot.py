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
    reply_keyboard = [['Sim', 'Não']]

    await update.message.reply_text(
        f"Prazer em conhecê-lo, {update.message.text}! Você também é um SUPER FURIOSO ?",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )
    return FAN_QUESTION

async def fan_response(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    response = update.message.text.lower()
    name = context.user_data['name']
    if 'sim' in response or 'yes' in response:
        await update.message.reply_text(f"Que ótimo, {name}! A Furia é incrível, né? -_- a gente têm os jogadores mais habilidosos no nosso elenco como o lendário FALLEN ! e o KSCERATO ")
    else:
        await update.message.reply_text(f"Tudo bem, {name}.Talvez você vire fã depois de assistir aos jogos do nosso super time. Eles são muito bons!")
    fact = random.choice(facts)
    await update.message.reply_text(f"A propósito, você sabia que {fact}")
    await update.message.reply_text("Quer saber mais sobre a Fúria? Confira o site oficial: https://www.furia.gg/ ou siga no X: @FURIA")
    return ConversationHandler.END

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