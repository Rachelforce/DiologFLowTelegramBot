# DiologFLowTelegramBot
apiai==1.2.3
numpy==1.18.1
public==2019.4.13
pyTelegramBotAPI==3.6.7
requests==2.7.0
six==1.14.0
values==2019.4.13

Добавить в библеотке telebot к типу User метод:
    def to_json(self):
        json_dict = {'first_name': self.first_name,
                     'id': self.id,
                     'is_bot':self.is_bot,
                     'last_name': self.last_name,
                     'username': self.username,
                     'language_code': self.language_code}
        return json_dict
