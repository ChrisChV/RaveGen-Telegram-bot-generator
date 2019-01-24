import requests 
from bottle import run, post, request as bottle_request


BOT_URL = 'https://api.telegram.org/bot717635382:AAE9Qy-9Vd0wAsUAVnII9y9CLE-8E-s9EAA/'

def get_chat_id(data):  
    chat_id = data['message']['chat']['id']
    return chat_id

def get_message(data):  
    message_text = data['message']['text']
    return message_text

def change_text_message(text):  
    return text[::-1]

def prepare_data_for_answer(data):  
    answer = change_text_message(get_message(data))

    json_data = {
        "chat_id": get_chat_id(data),
        "text": answer,
    }

    return json_data

def send_message(prepared_data):  
    message_url = BOT_URL + 'sendMessage'
    requests.post(message_url, json=prepared_data)

@post('/')  # our python function based endpoint
def main():  
    data = bottle_request.json  # <--- extract all request data
    print(data)
    send_message(prepare_data_for_answer(data))
    

    return 


if __name__ == '__main__':  
    run(host='localhost', port=8081, debug=True)