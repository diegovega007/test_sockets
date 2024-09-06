from flask import render_template
from app import app, socketio, db
from models import Chat
from flask_socketio import emit
from os import environ
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

DOMAIN = environ.get('DOMAIN')

@app.route('/<int:channel>/<name>/')
def open_chat(channel, name):
    my_chat = Chat.query.filter_by(channel=channel).all()
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
    # Save message
    my_new_chat = Chat(
        username=message['username'],
        text=message['text'],
        channel=message['channel']
    )
    db.session.add(my_new_chat)
    try:
        db.session.commit()
    except:
        db.session.rollback()