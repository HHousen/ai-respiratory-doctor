from threading import Thread
from flask_mail import Message
from flask import current_app
from app.extensions import mail
from app import app
from environs import Env

env = Env()
env.read_env()

def send(recipient, subject, body):
    '''
    Send a mail to a recipient. The body is usually a rendered HTML template.
    The sender's credentials has been configured in the config.py file.
    '''
    if (env.bool('USE_MAIL', default=True)):
        sender = current_app.config['ADMINS'][0]
        message = Message(subject, sender=sender, recipients=[recipient])
        message.html = body
        # Create a new thread
        thr = Thread(target=send_async, args=[app, message])
        thr.start()


def send_async(app, message):
    ''' Send the mail asynchronously. '''
    with app.app_context():
        mail.send(message)