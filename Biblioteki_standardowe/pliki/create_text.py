import datetime
import random

PARAGRAPHS = 10
LOREM = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et " \
        "dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex " \
        "ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat " \
        "nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit " \
        "anim id est laborum."


def random_post_code():
    return f'{random.randint(10, 99)}-{random.randint(100, 999)}'


def random_email():
    return f'user-{random.randint(1, 100)}@email.{random.choice(["pl", "com", "edu.pl", "gov.uk"])}'


def random_date():
    start = datetime.date(1990, 1, 1)
    result = start + datetime.timedelta(days=random.randint(1, 365 * 20))
    return result.strftime('%d %b %Y')


if __name__ == '__main__':
    with open('input.txt', 'w') as f:
        for _ in range(PARAGRAPHS):
            words = []
            for word in LOREM.split(' '):
                if random.randint(1, 5) == 1:
                    generator = random.choice([random_post_code, random_email, random_date])
                    words.append(generator())
                words.append(word)
            f.write(' '.join(words) + '\n')
