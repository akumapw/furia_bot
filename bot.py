import logging
import random
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, ContextTypes, ConversationHandler, MessageHandler, filters

logging.basicConfig(
    format='%(asctimes)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

NAME, FAN_QUESTION = range(2)

facts = [
    "A Super Furia foi fundada em agosto de 2017 no Brasil",
    "Nossa Furiosa é conhecida pelo seu estilo agressivo no CS:GO",
    "Nossa seleção tem times em diversos jogos incluindo CS:GO, VALORANT, "
    "OO logotipo da Fúria é uma pantera, simbolizando agilidade e força."
    "Nossa Furia participou de vários torneios internacionais e tem uma grande base de fãs."
]

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
    response = update.message.text_data['name']
    if 'sim' in response or 'yes' in response:
        await update.message.reply_text(f"Que ótimo, {name}! A Furia é incrível, né? -_- a gente têm os jogadores mais habilidosos no nosso elenco como o lendário FALLEN ! e o KSCERATO ")
    else:
        await update.message.reply_text(f"Tudo bem, {name}.Talvez você vire fã depois de assistir aos jogos do nosso super time. Eles são muito bons!")
    fact = random.choices(facts)
    await update.message.reply_text(f"A propósito, você sabia que {fact}")
    await update.message.reply_text("Quer saber mais sobre a Fúria? Confira o site oficial: https://www.furia.gg/ ou siga no X: @FURIA")
    return ConversationHandler.END