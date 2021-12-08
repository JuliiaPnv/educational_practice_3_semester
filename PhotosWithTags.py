# Выводит количество фотографий id_1, на которых отмечен id_2, и ссылки на них
# Принимает на вход параметр vk для доступа к методам vk_api и параметры типа int - id двух пользователей

def get_photos_with_tags(vk, id_1, id_2):
    photos_id_1 = vk.photos.getAll(owner_id=id_1)  # получаем фотографии id_1, максимальная длина 20
    count = photos_id_1['count'] // 20  # делим нацело на 20 количество фотографий
    photos_id_1 = photos_id_1['items']  # присваиваем первые 20 фотографий
    for i in range(1, count + 1):
        # помещаем всё в один список
        photos_id_1 = photos_id_1 + vk.photos.getAll(owner_id=id_1, offset=i * 20)['items']
    photos = 0  # счётчик фотографий, где отмечен id_2
    for i in range(len(photos_id_1)):
        # получаем отметки с фотографии
        photos_with_tags = vk.photos.getTags(owner_id=id_1, photo_id=photos_id_1[i]['id'])
        for j in range(len(photos_with_tags)):  # запускаем цикл по массиву отметок и сраниваем с id_2
            if photos_with_tags[j]['placer_id'] == id_2:
                photos += 1
                print('ссылка: https://vk.com/photo' + str(id_1) +
                      '_' + str(photos_id_1[i]['id']))
    if photos != 0:
        print('Количество фотографий у id_1, на которых отмечен id_2 =', photos)
    else:
        print('Фотографий у id_1, на которых отмечен id_2, нет')
