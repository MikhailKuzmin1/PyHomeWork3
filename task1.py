# ✔ Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.

friends = {'Игорь':('мяч','вода','палатка'), 'Олег':('компас','вода','палатка'), 'Стас':('нож','вода','консервы')}
# union_fr = set(friends['Игорь']) & set(friends['Олег']) & set(friends['Стас'])
for item, value in friends.items():
    inter_friend = set(friends[item])
    break
for item, value in friends.items():
    inter_friend = inter_friend & set(friends[item])
print(f'у всех друзей с собой есть {inter_friend}')
diff_friend = set()
for item, value in friends.items():
    diff_friend = diff_friend ^ set(friends[item])
diff_friend = diff_friend - inter_friend
print(f'Уникальные вещи {diff_friend}')
uniq_friend = set()
for item, value in friends.items():
    uniq_friend = uniq_friend | set(friends[item])
uniq_friend = uniq_friend.difference(diff_friend, inter_friend)
res_items = []
for i in uniq_friend:
    for item, value in friends.items():
        if i not in value:
            res_items.append(item)
print(f'Вещи {uniq_friend} есть у всех кроме {res_items}')
