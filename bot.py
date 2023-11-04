import telebot
import math
import re

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot = telebot.TeleBot('6897949043:AAFJR4a0g7wKydGh0u10v3Ct0uNCRgFNq4A')

# Messages
START_MESSAGE = """Send me a mathematical expression, and I will calculate the result for you."""
HELP_MESSAGE = """You can send me a mathematical expression using the following operators and functions:
- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)
- Exponentiation (**)
- Trigonometric functions: sin(x), cos(x), tg(x)
- Factorial: fact(x)
- Square root: sqrt(x)
- Square: sqr(x)
- Logarithms: log2(x), lg(x), ln(x), log(b, x)

For example, you can type '2 + 2' or 'sin(30)'. I will calculate the result for you."""

# Helper functions for mathematical operations
def fact(x):
    return math.factorial(x)

def cos(x):
    return math.cos(math.radians(x))

def sin(x):
    return math.sin(math.radians(x))

def tg(x):
    return math.tan(math.radians(x))

def log(base, x):
    return math.log(x, base)

def lg(x):
    return math.log10(x)

def log2(x):
    return math.log2(x)

def sqr(x):
    return x * x

# Define a function to handle text messages
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    chat_id = message.chat.id
    text = message.text

    if text.lower() == '/start':
        bot.send_message(chat_id, START_MESSAGE)
    elif text.lower() == '/help':
        bot.send_message(chat_id, HELP_MESSAGE)
    else:
        try:
            result = str(eval(text, {"__builtins__": None}, {
                "fact": fact,
                "cos": cos,
                "sin": sin,
                "tg": tg,
                "log": log,
                "lg": lg,
                "log2": log2,
                "sqr": sqr,
                "sqrt": math.sqrt
            }))
            bot.send_message(chat_id, f"Result: {result}")
        except Exception as e:
            bot.send_message(chat_id, "Invalid input. Please enter a valid mathematical expression.")

# Start the bot
bot.polling()
