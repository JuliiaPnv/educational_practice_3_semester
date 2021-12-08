# Выводит количество упоминаний пользователя с id_1
# и количество упоминаний, принадлежащих пользователю с id_2
# Принимает на вход параметр vk для доступа к методам vk_api и параметры типа int - id двух пользователей

def get_posts_with_tag(vk, id_1, id_2):
    wall_id_1 = vk.wall.get(owner_id=id_1)  # получаем список постов пользователя, максимальная длина 20
    count_id_1 = wall_id_1['count'] // 20  # делим количество постов нацело на 20
    wall_id_1 = wall_id_1['items']  # присваиваем первые 20 постов
    for i in range(1, count_id_1 + 1):
        # помещаем всё в один список
        wall_id_1 = wall_id_1 + vk.wall.get(owner_id=id_1, offset=i * 20)['items']
    posts_tag_id_2 = 0  # количество постов с упоминанием пользователя с id_2
    posts_tag = 0  # количество постов с упоминаниями
    for i in range(len(wall_id_1)):  # запускаем цикл по списку постов
        text = wall_id_1[i]['text']  # присваиваем текст поста
        if (len(text)) != 0:  # проверяем наличие текста
            if text.find('[id') != -1:  # проверяем наличие упоминания
                print('ссылка: https://vk.com/wall' + str(wall_id_1[i]['owner_id'])
                      + '_' + str(wall_id_1[i]['id']))
                j = 0
                while text.find('[id', j) != -1:  # собираем все упоминания с поста
                    j = text.find('[id', j) + 3
                    posts_tag += 1
            if text.find(str(id_2)) != -1:  # проверяем наличие упоминания пользователя с id_2
                posts_tag_id_2 += 1
                print('ссылка: https://vk.com/wall' + str(wall_id_1[i]['owner_id'])
                      + '_' + str(wall_id_1[i]['id']))
    print('Количество отметок всего =', posts_tag,
          '\nКоличество отметок, принадлежащих id_2 =', posts_tag_id_2)
