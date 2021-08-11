from django.core.mail import send_mail

from backend import settings

SUBJECT = """[FORUM] Регистрация аккаунта"""


class FailSendMessageToEmail(BaseException):
    pass


def send(request):
    try:
        message = f"Имя пользователя: {request.data['username']}\n" \
                  f"Почта: {request.data['email']}\n" \
                  f"Пароль: {request.data['password']}\n"

        send_mail(SUBJECT, message, settings.EMAIL_HOST_USER, [request.data['email']])
    except FailSendMessageToEmail:
        pass
