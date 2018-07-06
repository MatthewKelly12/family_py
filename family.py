my_family = {
    'sister': {
        'name': 'Emily',
        'age': 40
    },
    'mother': {
        'name': 'Beverley',
        'age': 67
    }
}

family = {
    # print(my_family[x])
    # print(x, y)
    # print(y['name'])
    # print(y['age'])
    str(y['name']) + " "
    + 'is my' + " " + str(x) + " "
    + 'and is' + " "+ str(y['age'])
    for (x,y) in my_family.items()
}

print(family)




