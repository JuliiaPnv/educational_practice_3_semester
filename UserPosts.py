# Выводит информацию о постах пользователей
# Принимает на вход параметр vk для доступа к методам vk_api и параметры типа int - id двух пользователей

def get_posts(vk, id_1, id_2):
    wall_id_1 = vk.wall.get(owner_id=id_1)  # получаем список постов пользователя, максимальная длина 20
    count_id_1 = wall_id_1['count'] // 20  # делим количество постов нацело на 20
    wall_id_1 = wall_id_1['items']  # присваиваем первые 20 постов
    for i in range(1, count_id_1 + 1):
        # помещаем всё в один список
        wall_id_1 = wall_id_1 + vk.wall.get(owner_id=id_1, offset=i * 20)['items']
    print('Посты пользователя с id_1:')
    for i in range(len(wall_id_1)):  # запускаем цикл по списку постов и выводим информацию о них
        print('кому:', wall_id_1[i]['owner_id'], 'от кого:', wall_id_1[i]['from_id'], 'дата публикации:',
              wall_id_1[i]['date'], 'текст:', wall_id_1[i]['text'],
              'ссылка: https://vk.com/wall' + str(wall_id_1[i]['owner_id']) + '_' + str(wall_id_1[i]['id']))

    wall_id_2 = vk.wall.get(owner_id=id_2)
    count_id_2 = wall_id_2['count'] // 20
    wall_id_2 = wall_id_2['items']
    for i in range(1, count_id_2 + 1):
        wall_id_2 = wall_id_2 + vk.wall.get(owner_id=id_2, offset=i * 20)['items']
    print('\nПосты пользователя с id_2:')
    for i in range(len(wall_id_2)):
        print('кому:', wall_id_2[i]['owner_id'], 'от кого:', wall_id_2[i]['from_id'], 'дата публикации:',
              wall_id_2[i]['date'], 'текст:', wall_id_2[i]['text'],
              'ссылка: https://vk.com/wall' + str(wall_id_2[i]['owner_id']) + '_' + str(wall_id_2[i]['id']))
