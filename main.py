import sys
import random
import string

sys.stdin.reconfigure(encoding='utf-8')

word = input("含めたい単語を入力してね: ")
characters = input("含めたい文字を入力してね: ")
length = int(input("パスワードの長さを指定してね: "))

include_symbols = input("記号を含める? (はい/いいえ): ").strip().lower()
if include_symbols == 'はい':
    all_characters = characters + string.ascii_letters + string.digits + string.punctuation
else:
    all_characters = characters + string.ascii_letters + string.digits

remaining_length = length - len(word)

random_part = ''.join(random.choice(all_characters) for _ in range(remaining_length))
password_parts = list(random_part)
insert_position = random.randint(0, len(password_parts))  
password_parts.insert(insert_position, word)
password = ''.join(password_parts)
print(f"生成されたパスワード: {password}")
