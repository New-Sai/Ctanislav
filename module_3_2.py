def send_email (message, recipient, sender = 'university.help@gmail.com'):
    correct_domen = ('.com', '.ru', '.net')
    correct_ending = recipient.endswith(correct_domen) == sender.endswith(correct_domen)

    if recipient.count('@') and sender.count('@'):
        if correct_ending is not True:
         print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        elif recipient == sender:
            print('Нельзя отправить письмо самому себе!')
        elif sender == 'university.help@gmail.com':
            print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
        else:
            print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
