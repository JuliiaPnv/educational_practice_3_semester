# Выводит количество общих геометок пользователей и информацию о них
# Принимает на вход параметр vk для доступа к методам vk_api и параметры типа int - id двух пользователей

def get_general_geotags(vk, id_1, id_2):
    photos_id_1 = vk.photos.getAll(owner_id=id_1)  # получаем фотографии id_1, максимальная длина 20
    photos_id_2 = vk.photos.getAll(owner_id=id_2)
    count_id_1 = photos_id_1['count'] // 20  # делим нацело на 20 количество фотографий
    photos_id_1 = photos_id_1['items']  # присваиваем первые 20 фотографий
    for i in range(1, count_id_1 + 1):
        # помещаем всё в один список
        photos_id_1 = photos_id_1 + vk.photos.getAll(owner_id=id_1, offset=i * 20)['items']
    count_id_2 = photos_id_2['count'] // 20  # повторяем всё с id_2
    photos_id_2 = photos_id_2['items']
    for i in range(1, count_id_2 + 1):
        photos_id_2 = photos_id_2 + vk.photos.getAll(owner_id=id_2, offset=i * 20)['items']
    geotags = 0  # счётчик общих геометок
    for i in range(len(photos_id_1)):  # запускаем цикл по фотографиям пользователя с id_1
        if 'lat' in photos_id_1[i] and 'long' in photos_id_1[i]:  # проверяем налиие ключей в списке
            lat_1 = round(photos_id_1[i]['lat'])  # присваиваем указанную широту и округляем её
            long_1 = round(photos_id_1[i]['long'])  # присваиваем указанную долготу и округляем её
            for j in range(len(photos_id_2)):  # запускаем цикл по фотографиям пользователя с id_2
                if 'lat' in photos_id_2[j] and 'long' in photos_id_2[j]:
                    lat_2 = round(photos_id_2[j]['lat'])
                    long_2 = round(photos_id_2[j]['long'])
                    if lat_1 == lat_2 and long_1 == long_2:  # сравниваем широту и долготу
                        geotags += 1
                        print(photos_id_2[j]['lat'], photos_id_2[j]['long'])
    if geotags != 0:
        print('Количество общих геометок =', geotags)
    else:
        print('Общих геометок нет')
