import telebot
import psycopg2

TOKEN = '6259163045:AAEVw4GVbvsG3ZlQhJwA8IohkRfiltskKC4'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'Strattonbot'
DB_USER = 'Olzhas'
DB_PASSWORD = 'OlezkaYouBk_2003'

conn = psycopg2.connect(host=DB_HOST, port=DB_PORT, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD)
cursor = conn.cursor()

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, f"Strattonbot {message.text}")
    cursor.execute("INSERT INTO messages (message_text, send_date) VALUES (%s, to_timestamp(%s))",
                   (message.text, message.date))
    conn.commit()


bot.polling(none_stop=True)
