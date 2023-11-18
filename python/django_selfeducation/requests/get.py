import requests

# page = requests.get('http://google.com/', params={
#     'q':'коты',
# }) #params можно писать методы для get запроса, не ломая голову как. слева метод, справа значение

# request - запрос на сервер от пользователя
# response - ответ от сервера на request

# content - не раскодированные данные
# text - данные в нужной кодировке
# if page.status_code == 200:
#     print('все нормально')
# else:
#     print('error', page.status_code)
#200 - ok
#404 - not found ошибка со стороны пользователя
#500 - inrernal server error ошибка на сервере

# print(page.content) # выводит структуру сайта(html и style)

# print(page.content.decode('utf-8')) #декодировка 
# print(page.content.decode(page.encoding)) 

# print(page.text) # расскодированные данные

# print(page.url) #url показывает ссылку из запроса
# print(page.headers)


response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

data = response.json()
print(data['title'] )



