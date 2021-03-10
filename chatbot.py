from chatterbot import ChatBot
from flask import Flask, request
from flask_cors import CORS, cross_origin
from chatterbot.trainers import ChatterBotCorpusTrainer


app = Flask('__name__')
CORS(app,resources={r"/api/*":{"origins":"*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
bot = ChatBot('chatterbot', storage_adapter='chatterbot.storage.SQLStorageAdapter')
trainer = ChatterBotCorpusTrainer(bot)
trainer.train('chatterbot.corpus.english')

#routes
@app.route('/')
@cross_origin()
def Home():
    return str('Welcome Home')

@app.route('/user',methods=['POST'])
@cross_origin()
def user():
    jsony = request.json
    data = jsony['msg']
    return str(bot.get_response(data))

app.run()


