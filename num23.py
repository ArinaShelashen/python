def get_my_vk_friends():
    data = [{'name': 'Tom', 'birthday': 55},
            {'name': 'Steve', 'birthday': 5}
            ]
def get_friends_with_btd(friends, day):
    result = []
    for friend in friends:
        if friend['birthday'] == day:
            result.append(friend)
    return result
def create_congratultion(friends):
    for friend in friends:
        print(f'Поздравляю {friend["name"]}')

def run():
    friends = get_my_vk_friends()
    friends_with_btd = get_friends_with_btd(friends, 5)
    create_congratultion(friends_with_btd)