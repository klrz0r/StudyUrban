def send_email(massage, recipient, sender='university.help@gmail.com'):
    if not ('@' in recipient) or not ('@' in sender):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif not ('.com' in recipient or '.ru' in recipient or '.net' in recipient):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif not ('.com' in sender or '.ru' in sender or '.net' in sender):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif recipient == sender:
        print(f'Нельзя отправить письмо самому себе!')
    elif sender == "university.help@gmail.com":
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru',
                   sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

