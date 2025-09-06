import random
import string

def generate_email():
    #Генерирует случайный email вида loginXXXX@domain.com
    login_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    domains = ['ya.ru', 'mail.ru', 'gmail.com']
    domain = random.choice(domains)
    return f"{login_part}@{domain}"

def generate_password(length=8):
    #Генерирует случайный пароль из букв и цифр
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))