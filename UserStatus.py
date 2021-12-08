# Выводит статусы пользователей
# Принимает на вход параметр vk для доступа к методам vk_api и параметры типа int - id двух пользователей

def get_status(vk, id_1, id_2):
    status_id_1 = vk.status.get(user_id=id_1)  # присваиваем статус пользователя
    status_id_2 = vk.status.get(user_id=id_2)
    if len(status_id_1['text']) != 0:
        print('статус пользователя с id_1:', status_id_1['text'])
    else:
        print('у пользователя с id_1 нет статуса')
    if len(status_id_2['text']) != 0:
        print('статус пользователя с id_2:', status_id_2['text'])
    else:
        print('у пользователя с id_2 нет статуса')
