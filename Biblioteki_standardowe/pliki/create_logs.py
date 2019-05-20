import random
from collections import defaultdict

NUMBER_OF_USERS = 10
NUMBER_OF_ENTRIES = 100

if __name__ == '__main__':
    user_is_logged = defaultdict(lambda: False)
    time = 0

    with open('logs.txt', 'w') as f:
        for _ in range(NUMBER_OF_ENTRIES):
            user_number = random.randint(1, NUMBER_OF_USERS)
            action = 'LOGOUT' if user_is_logged[user_number] else 'LOGIN'
            user_is_logged[user_number] = not user_is_logged[user_number]
            time += random.randint(1, 120)
            f.write(f'user-{user_number};{action};{time}\n')
        for user_number in filter(lambda user: user_is_logged[user], user_is_logged):
            time += random.randint(1, 120)
            f.write(f'user-{user_number};LOGOUT;{time}\n')
