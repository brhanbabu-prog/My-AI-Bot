import telebot
import google.generativeai as genai

# --- ቁልፎችህን እዚህ በጥንቃቄ አስገባ ---
BOT_TOKEN = "8649208087:AAEdjKBJD9JH48O3KnWkKfx_qTqtE5Cupjo"
AI_KEY = "AIzaSyACzxU3JtxH_Sw3hNg5eT6wPcGlYQvrne4"
# AI ማዋቀር
genai.configure(api_key=AI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "ሰላም! እኔ ያንተ የግል AI ረዳት ነኝ። ማንኛውንም ጥያቄ ልትጠይቀኝ ትችላለህ። በምን ልርዳህ?")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        # የተላከውን መልዕክት ወደ AI መላክ
        response = model.generate_content(message.text)
        # ከ AI የመጣውን መልስ ለተጠቃሚው መመለስ
        bot.reply_to(message, response.text)
    except Exception as e:
        print(e)
        bot.reply_to(message, "ይቅርታ፣ ጥያቄህን ማስተናገድ አልቻልኩም። የ API ቁልፍህን አረጋግጥ።")

bot.infinity_polling()
