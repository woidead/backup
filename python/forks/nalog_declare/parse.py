import requests

# Ваше имя пользователя и пароль на сайте
username = 'zxclilaziz@gmail.com'
password = '290505aU.'

# URL-адрес страницы для авторизации
login_url = 'https://accounts.spotify.com/ru/login'

# URL-адрес страницы, которую вы хотите спарсить
target_url = 'https://open.spotify.com'

# Создаем сессию для отправки запросов
session = requests.Session()

# Отправляем POST-запрос для авторизации на сайте
login_data = {'username': username, 'password': password}
r = session.post(login_url, data=login_data)

# Проверяем, успешно ли прошла авторизация
if r.status_code == 200:
    # Если авторизация прошла успешно, получаем данные со страницы
    r = session.get(target_url)
    # Извлекаем данные из ответа сервера
    data = r.text
    print(data)
else:
    print('Ошибка авторизации', r.status_code)
