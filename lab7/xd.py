from random import randrange


def merge_into_pairs(my_list, pairs):
    while my_list:
        idx1 = randrange(0, len(my_list))
        name1 = my_list[idx1]
        my_list.pop(idx1)
        idx2 = randrange(0, len(my_list))
        name2 = my_list[idx2]
        my_list.pop(idx2)
        pairs.append((name1, name2))


for x in range(5):
    my_list = ['Wiktor', 'Marek', 'Maciek', 'Dominik', 'Hubert', 'Franciszek']
    pairs = []

    merge_into_pairs(my_list,pairs)

for x in pairs:
    print(x)

