import vk_api


# Выводит количество общих групп пользователей и ссылки на них
# Принимает на вход параметр vk для доступа к методам vk_api и параметры типа int - id двух пользователей

def get_general_groups(vk, id_1, id_2):
    try:
        groups_id_1 = vk.groups.get(user_id=id_1)  # получаем количество групп и массив их id
        groups_id_2 = vk.groups.get(user_id=id_2)
    except vk_api.exceptions.ApiError:
        print('Нет доступа к группам')
        return
    groups = 0  # счётчик общих групп
    for i in range(len(groups_id_1['items'])):  # запускаем цикл по массиву id групп
        for j in range(len(groups_id_2['items'])):
            if groups_id_1['items'][i] == groups_id_2['items'][j]:  # сравниваем группы
                groups += 1
                print('ссылка: https://vk.com/club' + str(groups_id_1['items'][i]))
    print('Количество общих групп =', groups)
