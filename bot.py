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

