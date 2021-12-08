# Проверяет, являются ли профили пользователей закрытыми, если да, то запрашивается id другого пользователя
# Принимает на вход параметр vk для доступа к методам vk_api, параметры типа int - id двух пользователей
# и списки, содержащие информацию о приватности аккаунтов пользователей

def privacy_check(vk, id_1, id_2, users_id_1, users_id_2):
    while True:
        if users_id_1[0]['is_closed'] is True and users_id_2[0]['is_closed'] is True:
            print('Профили обоих пользователей закрыты')
            id_1 = int(input("Введите id 1 пользователя = "))
            id_2 = int(input("Введите id 2 пользователя = "))
            users_id_1 = vk.users.get(user_ids=id_1)
            users_id_2 = vk.users.get(user_ids=id_2)
        elif users_id_1[0]['is_closed'] is True:
            print('Профиль первого пользователя закрыт')
            id_1 = int(input("Введите id 1 пользователя = "))
            users_id_1 = vk.users.get(user_ids=id_1)
        elif users_id_2[0]['is_closed'] is True:
            print('Профиль второго пользователя закрыт')
            id_2 = int(input("Введите id 2 пользователя = "))
            users_id_2 = vk.users.get(user_ids=id_2)
        elif id_1 == id_2:
            print('Введён один и тот же пользователь')
            id_2 = int(input("Введите id 2 пользователя = "))
            users_id_2 = vk.users.get(user_ids=id_2)
        else:
            break
