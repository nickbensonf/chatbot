import telebot
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('API_KEY')
bot = telebot.TeleBot(token=os.getenv('TOKEN'))

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.send_message(message.chat.id,
                     "Привет! Я Чат-Бот Гимназист, являющийся твоим ассистентом во всех вопросах. Для того, чтобы задать вопрос, необходимо отправить его в виде сообщения. А также, поскольку пользователей много, а серверов достаточно мало, я могу отвечать с небольшой задержкой. Но, несмотря на это, в скором времени я смогу генерировать изображения согласно твоим запросам. Приятного использования :)")
@bot.message_handler(func=lambda _: True)
def handle_message(message):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": message.text}
        ]
    )
    bot.send_message(chat_id=message.from_user.id, text = response.choices[0].message.content)

bot.infinity_polling()
