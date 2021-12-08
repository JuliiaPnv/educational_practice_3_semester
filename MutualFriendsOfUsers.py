# Выводит количество общих друзей пользователей и их id
# Принимает на вход параметр vk для доступа к методам vk_api и параметры типа int - id двух пользователей
# На выходе длина массива с id общих друзей и сам массив

def get_mutual_friends(vk, id_1, id_2):
    # получаем массив общих друзей пользователей
    mutual_friends = vk.friends.getMutual(source_uid=id_1, target_uid=id_2)
    print('Количество общих друзей =', len(mutual_friends), '\nОбщие друзья:', mutual_friends)
