from flask import render_template
from app import app, socketio, db
#from models import Chat
from flask_socketio import emit
from os import environ
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

DOMAIN = environ.get('DOMAIN')

@app.route('/<int:channel>/<name>/')
def open_chat(channel, name):
    query = {}

    if channel:
        query['channel'] = int(channel)

    my_chat = db.chat.find(query)

    return render_template(
        'chat.html',
        domain=DOMAIN,
        chat=my_chat,
        channel=channel,
        username=name
    )


@socketio.on('new_message')
def new_message(message):
    # Send message to alls users
    emit('channel-' + str(message['channel']), {
        'username': message['username'],
        'text': message['text']
    },
        broadcast=True
    )

    #Save message
    my_new_chat = {
        "username":message['username'],
        "text":message['text'],
        "channel":message['channel'],
        "created_At": "2024-09-07 00:13:48.687741"
    }
    db.chat.insert_one(my_new_chat)