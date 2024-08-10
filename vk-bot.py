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
how_are_you_list = ("Хорошо, спасибо!", "Отлично, твои как?", "Плохо(", "Все нормально, а твои как?")
what_are_you_doing_list = ("Сижу дома", "Лежу, а ты?", "Кушаю, а ты чем занимаешься?", "Собираюсь на тренировку, а ты?")

while True:
    for event in longpool.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print(f'Сообщение пришло в: {str(datetime.now())}')
            print(f'Текст сообщения: {str(event.text)}')
            responce = event.text.lower()
            if event.from_user and not event.from_me:
                if responce.find("привет") >= 0 or responce.find("здравствуй") >= 0 or responce.find("здарова") >= 0 or responce.find("салам") >= 0 or responce.find("хай") >= 0 or responce.find("ку") >= 0:
                    time.sleep(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {
                            "user_id": event.user_id,
                            "message": random.choice(hello_list),
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
                            "message": random.choice(how_are_you_list),
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
                elif responce.find("какой фильм посоветуешь?") >= 0:
                    time.sleep(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {
                            "user_id": event.user_id,
                            "message": "Выбери жанр фильма: \n1) Комедия \n2) Ужастик \n3) Фантастика \n4) Боевик \n Вводить нужно цифру",
                            "random_id": 0,
                        }
                    )
                elif responce.find("1") >= 0:
                    time.sleep(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {
                            "user_id": event.user_id,
                            "message": "\n1) Тупой и еще тупее \n2) О чем говорят мужчины \n3) Каха",
                            "random_id": 0,
                        }
                    )
                elif responce.find("2") >= 0:
                    time.sleep(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {
                            "user_id": event.user_id,
                            "message": "\n1) Ужасающий \n2) Оно \n3) Собиратель душ",
                            "random_id": 0,
                        }
                    )
                elif responce.find("3") >= 0:
                    time.sleep(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {
                            "user_id": event.user_id,
                            "message": "\n1) Назад в Будущее \n2) Бегущий по лезвию 2049 \n3) Обливион",
                            "random_id": 0,
                        }
                    )
                elif responce.find("4") >= 0:
                    time.sleep(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {
                            "user_id": event.user_id,
                            "message": "\n1) Джон Уик \n2) Гнев человеческий \n3) Форсаж",
                            "random_id": 0,
                        }
                    )    
                elif responce.find("спокойной ночи") >= 0 or responce.find("сладких снов") >= 0:
                    time.sleep(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {
                            "user_id": event.user_id,
                            "message": "Споки",
                            "random_id": 0,
                        },
                    )
                elif responce.find("что делаешь?") >= 0 or responce.find("чем занимаешься?") >= 0:
                    time.sleep(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {
                            "user_id": event.user_id,
                            "message": random.choice(what_are_you_doing_list),
                            "random_id": 0,
                        }
                    )
                elif responce.find("хорошо") >= 0 or responce.find("отлично") >= 0 or responce.find("нормально") >= 0:
                    time.sleep(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {
                            "user_id": event.user_id,
                            "sticker_id": 95130,
                            "random_id": 0,
                        },
                    )
                elif responce.find("гуляю") >= 0:
                    time.sleep(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {
                            "user_id": event.user_id,
                            "message": "Хорошей прогулки",
                            "random_id": 0,
                        }
                    )
                elif responce.find("Сижу") >= 0 or responce.find("Лежу") >= 0:
                    time.sleep(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {
                            "user_id": event.user_id,
                            "message": "Понятно)",
                            "random_id": 0,
                        }
                    )
                elif responce.find("ужинаю") >= 0 or responce.find("кушаю") >= 0 or responce.find("завтракаю") >= 0 or responce.find("обедаю") >= 0 or responce.find("ем") >= 0:
                    time.sleep(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {
                            "user_id": event.user_id,
                            "message": "Приятного аппетита!",
                            "random_id": 0,
                        }
                    )
                elif responce.find("Иду на тренировку") >= 0 or responce.find("Иду на репетитор") >= 0:
                    time.sleep(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {
                            "user_id": event.user_id,
                            "message": "Хорошо позаниматься:)",
                            "random_id": 0,
                        }
                    )
