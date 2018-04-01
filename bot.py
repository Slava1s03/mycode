import vk_api
import time




#vk=vk_api.VkApi(token='')
#vk=vk_api.VkApi(login='', password='')
vk.auth()


values = {'out': 0,'count': 100,'time_offset': 60}

def write_msg(user_id, s):
    vk.method('messages.send', {'user_id':user_id,'message':s})

while True:
    response = vk.method('messages.get', values)
    if response['items']:
        values['last_message_id'] = response['items'][0]['id']
    for item in response['items']:
        if response['items'][0]['body']=='Привет':
            write_msg(item[u'user_id'],u'Здравствуйте! Сейчас Слава не в сети, но вы можете поговорить со мной! Если хочешь поиграть нажми 1, если нет то 2.')
        elif response['items'][0]['body']=='1':
            write_msg(item[u'user_id'], u'Отгадай загадку. Что делал слон, когда пришёл Наполеон?')
        elif response['items'][0]['body']=='Травку жевал':
            write_msg(item[u'user_id'], u'Правильно!')
            write_msg(item[u'user_id'], u'На этом всё, пока!')
        elif response['items'][0]['body']=='2':
            write_msg(item[u'user_id'], u'Ну ладно, пока!')

        else:
            write_msg(item[u'user_id'], u'Я тебя не понимаю. :(')
    time.sleep(1)
