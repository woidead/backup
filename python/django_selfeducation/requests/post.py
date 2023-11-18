import requests
website = 'https://jsonplaceholder.typicode.com/posts/1'
response = requests.post(website, data={ 
    #data или json это данные которые мы добавляем
    "userId": 12,
    'title': 'My new post',
    'body': 'body for my new post asasass',
    'photo': {'1.png', '2.png'}
})
print(response.json())
print(response.reason) #проверка что с командой