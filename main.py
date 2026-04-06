import telebot
import google.generativeai as genai
import os

# --- ቁልፎችህን እዚህ አስገባ ---
BOT_TOKEN = "8649208087:AAEdjKBJD9JH48O3KnWkKfx_qTqtE5Cupjo
AI_KEY = AIzaSyACzxU3JtxH_Sw3hNg5eT6wPcGlYQvrne4

# AI ማዋቀር
genai.configure(api_key=AI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
bot = telebot.TeleBot(BOT_TOKEN)

# ቦቱ ሲነሳ ሰላምታ እንዲሰጥ
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "እንኳን ደህና መጡ! እኔ በ AI የታገዝኩ የወንጌል ስርጭት ረዳት ነኝ። እንዴት ልረዳዎ እችላለሁ?")

# ለሚላኩ መልእክቶች መልስ እንዲሰጥ
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "ይቅርታ፣ ትንሽ ችግር አጋጥሞኛል። እባክዎ ደግመው ይሞክሩ።")

bot.infinity_polling()
