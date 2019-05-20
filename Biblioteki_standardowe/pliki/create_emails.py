import random

NUMBER_OF_USERS = 10

if __name__ == '__main__':
    emails = []
    for user_number in range(NUMBER_OF_USERS):
        emails.extend([
            f'user-{user_number}@email.com',
            f'user-{user_number}@email.com',  # duplicate
            f' user-{user_number}@email.com ',  # white chars
            f'user-{user_number}@email.com'.upper(),  # caps
            f'user-{user_number}email.com',  # missing @
            f'user@{user_number}@email.com',  # too many @
        ])

    with open('emails.txt', 'w') as f:
        random.shuffle(emails)
        for email in emails:
            f.write(email + '\n')
