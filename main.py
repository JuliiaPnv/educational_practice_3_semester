import vk_api
from AccountAccess import privacy_check
from MutualFriendsOfUsers import get_mutual_friends
from PublicFriends import get_inf_about_public_friends
from FriendStatus import get_relationship_status
from UserGifts import get_gifts_from_user
from GeneralGroups import get_general_groups
from PhotosWithTags import get_photos_with_tags
from GeneralGeotags import get_general_geotags
from UsersInformation import get_general_inf
from UserStatus import get_status
from UserPosts import get_posts
from PostsWithLikeAndComm import get_posts_with_like_and_comm
from PostsWithTag import get_posts_with_tag


# для работы программы нужно получить токен с разрешениями: friends, photos, offline, wall, status

def main():
    token = ""  # записать токен
    vk_session = vk_api.VkApi(token=token)
    vk = vk_session.get_api()
    id_1 = int(input("Введите id 1 пользователя = "))
    id_2 = int(input("Введите id 2 пользователя = "))
    users_id_1 = vk.users.get(user_ids=id_1)
    users_id_2 = vk.users.get(user_ids=id_2)
    privacy_check(vk, id_1, id_2, users_id_1, users_id_2)
    print('Какую вызвать функцию:\n(1) Вывести информацию о количестве общих '
          'друзей.\n(2) Вывести информацию о том, указан ли пользователь с id_1 в '
          'публичном списке друзей пользователя с id_2.\n(3) Вывести информацию о '
          'том, находится ли пользователь с id_1 в разделе основной информации со '
          'страницы пользователя с id_2. Если да, то в каком статусе.\n(4) Посчитать '
          'количество подарков, которые пользователь с id_1 отправил пользователю с '
          'id_2.\n(5) Посчитать количество общих групп, сохранить ссылки в базу '
          'данных на общие группы.\n(6) Посчитать количество фотографий, на которых '
          'пользователь с id_1 отметил пользователя с id_2, сохранить ссылки на них в '
          'базу данных.\n(7) Посчитать количество общих геометок, сохранить информацию '
          'о них в базу данных.\n(8) Внести в базу данных информацию о стране, родном городе, '
          'городе проживания, образовании, карьере, военной службе, жизненной позиции '
          'двух пользователей. Вывести информацию о том, совпадает ли у пользователя '
          'с id_1 и пользователя с id_2 что-то из этого.\n(9) Вывести статусы двух '
          'пользователей\n(10) В базе данных сохранять информацию о постах (кому, '
          'от кого, дата публикации, какой текст содержит, ссылка на медиа)\n(11) '
          'Посчитать сколько постов на странице пользователя c id_1, сколько из них '
          'пролайкал/прокомментировал пользователь с id_2.\n(12) Посчитать количество '
          'упоминаний пользователя с id_1, сколько из них принадлежит пользователю с '
          'id_2. Сохранить информацию о постах в базу данных.')
    print('Введите 0 для завершения работы программы')
    while True:
        try:
            function = int(input())
        except ValueError:
            print('Неправильный ввод номера, попробуйте ещё раз')
            return
        while True:
            if 0 <= function < 13:
                if function == 0:
                    return
                break
            else:
                function = int(input('Введите другой номер:'))
        if function == 1:
            get_mutual_friends(vk, id_1, id_2)
        if function == 2:
            get_inf_about_public_friends(vk, id_1, id_2)
        if function == 3:
            get_relationship_status(vk, id_1, id_2)
        if function == 4:
            get_gifts_from_user(vk, id_1, id_2)
        if function == 5:
            get_general_groups(vk, id_1, id_2)
        if function == 6:
            get_photos_with_tags(vk, id_1, id_2)
        if function == 7:
            get_general_geotags(vk, id_1, id_2)
        if function == 8:
            get_general_inf(vk, id_1, id_2)
        if function == 9:
            get_status(vk, id_1, id_2)
        if function == 10:
            get_posts(vk, id_1, id_2)
        if function == 11:
            get_posts_with_like_and_comm(vk, id_1, id_2)
        if function == 12:
            get_posts_with_tag(vk, id_1, id_2)


if __name__ == '__main__':
    main()
