from AutoHomeProject.celery import app

from .service import send

@app.task
def send_spam_email(first_name, user_email):
    send(first_name, user_email)