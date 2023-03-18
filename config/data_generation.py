import random as random_numbers

def number_of_user():
    user = 'Bartal_test_user_'
    random_numbers.randint(0, 100)
    return (user + str(random_numbers.randint(0, 100)))

def mail():
    group_number = '_07_'
    last_name = 'Bartal'
    number = random_numbers.randint(100, 999)
    fake_mail = last_name + group_number + str(number) + '@toster.com'
    return fake_mail


def password():
    pas = ''
    for x in range(8):
        pas = pas + random_numbers.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
    return pas

