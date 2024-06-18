
username = input("Введіть ім'я користувача: ")
password = input("Введіть пароль: ")

numbers = set("0123456789")

if len(password) < 8:
    print("Пароль надто короткий")
elif username.lower() in password.lower():
    print("Пароль містить ім'я користувача")
elif len(numbers.intersection(password)) < 3:
    print("У паролі мають бути хоча б три цифри")
else:
    print(f"Пароль для користувача {username} встановлено")
