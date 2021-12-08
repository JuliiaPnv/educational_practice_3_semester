import vk_api


# Выводит количество подарков от id_1 для id_2
# Принимает на вход параметр vk для доступа к методам vk_api и параметры типа int - id двух пользователей

def get_gifts_from_user(vk, id_1, id_2):
    try:
        gift_id_2 = vk.gifts.get(user_id=id_2)  # получаем список подарков id_2 (не всех)
    except vk_api.exceptions.ApiError:
        print('Подарки пользователя с id_2 закрыты')
        return
    count = gift_id_2['count']  # присваиваем всё количество подарков
    gift_id_2 = vk.gifts.get(user_id=id_2, count=count)  # получаем доступ ко всем подаркам
    gifts = 0  # счётчик подарков от id_1
    for i in range(len(gift_id_2['items'])):  # запускаем цикл по списку подарков
        if gift_id_2["items"][i]["from_id"] == id_1:  # сравниваем id отправителя с id_1
            gifts += 1
    print('Количество подарков от id_1 для id_2 =', gifts)
