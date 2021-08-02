from django.core.mail import send_mail


def send(first_name, user_email):
    send_mail(
        'Заявка на тест-драйв.',
        'Здравствуйте уважаемый ' + first_name + '! Ваша заявка на тест-драйв успешно оформлена. Подробную информацию Вы можете увидеть в Вашем личном кабинете на сайте. Для уточнения можете связаться с нами: autohome228@gmail.com',
        'autohome228@gmail.com',
        [user_email],
        fail_silently=False
    )