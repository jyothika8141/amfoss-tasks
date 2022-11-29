import os
import telebot
import requests
import json
import csv

# TODO: 1.1 Get your environment variables 
yourkey = os.getenv("API_Key")
bot_id = os.getenv("Token")

with open('movie.csv', 'w', newline='') as f:
        wtr = csv.writer(f)
        wtr.writerow(['Title', 'Year', 'Released', 'imdbRating'])

bot = telebot.TeleBot(bot_id)   

@bot.message_handler(commands=['start', 'hello'])
def greet(message):
    global botRunning
    botRunning = True
    bot.reply_to(
        message, 'Hello there! I am a bot that will show movie information for you and export it in a CSV file.\n\n')
    
@bot.message_handler(commands=['stop', 'bye'])
def goodbye(message):
    global botRunning
    botRunning = False
    bot.reply_to(message, 'Bye!\nHave a good time')
    


@bot.message_handler(func=lambda message: botRunning, commands=['help'])
def helpProvider(message):
    bot.reply_to(message, '1.0 You can use \"/movie MOVIE_NAME\" command to get the details of a particular movie. For eg: \"/movie The Shawshank Redemption\"\n\n2.0. You can use \"/export\" command to export all the movie data in CSV format.\n\n3.0. You can use \"/stop\" or the command \"/bye\" to stop the bot.')


@bot.message_handler(func=lambda message: botRunning, commands=['movie'])
def getMovie(message):
    text = str(message.text).lower()
    movie_nm = text[7:]
    url = f"http://www.omdbapi.com/?apikey={yourkey}&t={movie_nm}"
    bot.reply_to(message, 'Getting movie info...')
    # TODO: 1.2 Get movie information from the API
    response = requests.request("GET", url)
    
    # TODO: 1.3 Show the movie information in the chat window
    data = json.loads(response.text)
    
    if data['Response'] == 'True':
        title = data['Title']
        year = data['Year']
        released = data['Released']
        poster = data['Poster']
        rate = data['imdbRating']
        bot.send_photo(chat_id=message.chat.id, photo=poster, caption=f'Movie Name: {title}\nYear: {year}\nReleased: {released}\nimdbRating: {rate}' )

        # TODO: 2.1 Create a CSV file and dump the movie information in it
        with open('movie.csv', 'a') as f:
            wtr = csv.writer(f)
            wtr.writerow([title, year, released, rate])
    else: 
        bot.send_message(chat_id=message.chat.id, text="No movie found, please try agian.")
           
        

  
@bot.message_handler(func=lambda message: botRunning, commands=['export'])
def getList(message):
    bot.reply_to(message, 'Generating file...')
    #TODO: 2.2 Send downlodable CSV file to telegram chat
    bot.reply_to(message, 'File generated!')
    bot.send_document(chat_id=message.chat.id, document=open(r'movie.csv', 'rb'))

@bot.message_handler(func=lambda message: botRunning)
def default(message):
    bot.reply_to(message, 'I did not understand '+'\N{confused face}')
    
bot.infinity_polling()
