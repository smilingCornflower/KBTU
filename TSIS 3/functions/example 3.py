def get_longest_emails(data):
    result = max(data.items(), key=lambda x: x[1])
    return result

data = {'Nikita': 'niki_net_yt@mail.ru', 
        'Nauryzbek': 'smiling.cornflower@gmail.com', 
        'Dastan': 'ghostraijin@yahoo.com',
        'Karim': 'karim.malaev88@mail.ru'}


print(get_longest_emails(data))