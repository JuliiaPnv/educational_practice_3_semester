# Выводит информацию о том, находится ли в отношениях (и в каких) пользователь с id_1 с пользователем с id_2
# Принимает на вход параметр vk для доступа к методам vk_api и параметры типа int - id двух пользователей

def get_relationship_status(vk, id_1, id_2):
    # получаем информацию в виде списка о родственниках и об отношениях у id_2
    relation_inf_id_2 = vk.users.get(user_ids=id_2, fields='relatives, relation')
    relation = 0  # счётчик, остаётся равным нулю, если пользователя с id_1 не окажется в личной информации у id_2
    if 'relation_partner' in relation_inf_id_2[0]:  # проверяем наличие ключа в списке
        # присваиваем параметру id, указанный в личных отношениях у id_2
        relation_partner_id = relation_inf_id_2[0]['relation_partner']['id']
        if relation_partner_id == id_1:  # сравниваем с id_1
            relation += 1
            print('Пользователь с id_2 состоит в отношениях с id_1, relation =', relation_inf_id_2[0]['relation'])
    if 'relatives' in relation_inf_id_2[0]:  # проверяем наличие ключа
        for i in range(len(relation_inf_id_2[0]['relatives'])):  # запускаем цикл по списку родственников
            relatives_id = relation_inf_id_2[0]['relatives'][i]['id']  # присваиваем id указанного родственника
            if relatives_id == id_1:  # сравниваем с id_1
                relation += 1
                print('Пользователь с id_1 является родственником пользователю с id_2, type =',
                      relation_inf_id_2[0]['relatives'][i]['type'])
    if relation == 0:
        print('Пользователь с id_1 не указан в разделе основной информации со страницы пользователя с id_2')
