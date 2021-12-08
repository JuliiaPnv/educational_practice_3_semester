# Выводит указанную пользователями личную информацию и совпадения в информации двух пользователей
# Принимает на вход параметр vk для доступа к методам vk_api и параметры типа int - id двух пользователей

def get_general_inf(vk, id_1, id_2):
    inf_about_id_1 = vk.users.get(user_ids=id_1, fields='country, home_town, city, education, career, military, '
                                                        'personal')  # получаем личную иннформацию о пользователе
    inf_about_id_2 = vk.users.get(user_ids=id_2, fields='country, home_town, city, education, career, military, '
                                                        'personal')
    print(inf_about_id_1)
    print(inf_about_id_2)
    if 'country' in inf_about_id_1[0] and 'country' in inf_about_id_2[0]:  # проверяем наличие ключей в списках
        if inf_about_id_1[0]['country'] == inf_about_id_2[0]['country']:  # сравниваем
            print('Оба пользователя живут в стране', inf_about_id_1[0]['country']['title'])
    if 'city' in inf_about_id_1[0] and 'city' in inf_about_id_2[0]:
        if inf_about_id_1[0]['city'] == inf_about_id_2[0]['city']:
            print('Оба пользователя живут в городе', inf_about_id_1[0]['city']['title'])
    if 'home_town' in inf_about_id_1[0] and 'home_town' in inf_about_id_2[0]:
        if inf_about_id_1[0]['home_town'] != '' and inf_about_id_2[0]['home_town'] != '':
            if inf_about_id_1[0]['home_town'] == inf_about_id_2[0]['home_town']:
                print('Родной город обоих пользователей', inf_about_id_1[0]['home_town'])
    if 'university_name' in inf_about_id_1[0] and 'university_name' in inf_about_id_2[0]:
        if inf_about_id_1[0]['university_name'] != '' and inf_about_id_2[0]['university_name'] != '':
            if inf_about_id_1[0]['university_name'] == inf_about_id_2[0]['university_name']:
                print('Оба пользователя учатся/учились в', inf_about_id_1[0]['university_name'])
