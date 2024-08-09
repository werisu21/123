import time
import random
from vk_api.longpoll import VkLongPoll, VkEventType
from datetime import datetime
from vk_api import VkApi
from config import TOKEN

session = VkApi(token=TOKEN)
session_api = session.get_api()
longpool = VkLongPoll(session)

hello_list = ("Привет!", "Хай", "Салам", "Доброго времени суток", "Ку")
bye_list = ("Пока", "И тебе пока!", "До встречи!", "До свидания", "Всего доброго")
mem_list = ("-220489451_457250621", "-220489451_457250610", "-220489451_457250464", "-220489451_457250592")

while True:
    for event in longpool.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print(f'Сообщение пришло в: {str(datetime.now())}')
            print(f'Текст сообщения: {str(event.text)}')
            responce = event.text.lower()
            if event.from_user and not event.from_me:
                if responce.find("привет") >= 0 or responce.find("здравствуй") >= 0:
                    time.sleep(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {
                            "user_id": event.user_id,
                            "message": random.choise(hello_list),
                            "random_id": 0,
                        },
                    )
                elif responce.find("пока") >= 0 or responce.find("до свидания") >= 0:
                    time.sleep(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {
                            "user_id": event.user_id,
                            "message": random.choice(bye_list),
                            "random_id": 0,
                        },
                    )

                elif responce.find("как дела") >= 0 or responce.find("как жизнь?") >= 0:
                    time.sleep(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {
                            "user_id": event.user_id,
                            "message": "Хорошо, спасибо!",
                            "random_id": 0,
                        },
                    )
                elif responce.find("грустно") >= 0 or responce.find("плохо") >= 0:
                    time.sleep(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {
                            "user_id": event.user_id,
                            "sticker_id": 73070,
                            "random_id": 0,
                        },
                    )
                elif responce == "кот":
                    session.method('messages.send',{'user_id': event.user_id, 'random_id':0, 'attachment': 'photo-28905875_459432012'})
                
                elif responce.find("мем") >= 0:
                    time.sleep(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {
                            "user_id": event.user_id,
                            "attachment": f"photo{random.choice(mem_list)}",
                            "random_id": 0,
                        }
                    )
                elif responce.find("фильм") >= 0:
                    time.sleep(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {
                            "user_id": event.user_id,
                            "message": "Выбери жанр фильма: \n1) Комедия \n2) Ужастик \n Вводить нужно цифру",
                            "random_id": 0,
                        }
                    )
                elif responce.find("1") >= 0:
                    time.sleep(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {
                            "user_id": event.user_id,
                            "message": "Тупой и еще тупее",
                            "random_id": 0,
                        }
                    )
                elif responce.find("2") >= 0:
                    time.sleep(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {
                            "user_id": event.user_id,
                            "message": "Ужасающий",
                            "random_id": 0,
                        }
                    )

