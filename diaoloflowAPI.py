import apiai
import json
import config


def get_response(message, chat_id):
    request = apiai.ApiAI(config.Config.BOT_TOKEN).text_request()
    request.lang = 'ru'
    request.session_id = str(chat_id)
    request.query = message
    response = json.loads(request.getresponse().read().decode('utf-8'))
    if response['result']['fulfillment']['speech'] != '':
        return response['result']['fulfillment']['speech']
    else:
        return '?'


