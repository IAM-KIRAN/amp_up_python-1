import random
import string
def generate_username(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

generated_usernames = set()
def generate_unique_usernames(n=1, length=8):
    for _ in range(n):
        while True:
            username = generate_username(length)
            if username not in generated_usernames:
                generated_usernames.add(username)
                yield username
                break

for username in generate_unique_usernames(n=10, length=8):
    print(username)
