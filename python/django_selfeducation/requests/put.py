import requests
website = 'https://jsonplaceholder.typicode.com/posts/1'
print(requests.get(website).json()) # до пута
response = requests.put(website, data={
    "userId": 12,
    'title': 'My new post',
    'body': 'body for my new post asasass',
    
})
 
print(response.json())