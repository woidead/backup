import  requests
API_link = 'https://api.telegram.org/bot5633178978:AAEdi_Yn3rd94sYcSLNPYTcJAzDGbYub8ps'
updates = requests.get(API_link + '/getUpdates?offset=-1').json() #offset = 581489150 это после какого update_id обрабатывать, а offset-1 это последний update
print(updates)
# message = updates['result'][0]['message']
# chat_id = message['from']['id']
# text = message['text']
# send_message = requests.get(API_link + f'/sendMessage?chat_id={chat_id}&text=Привет, ты прислал {text} так что хуйсоси' 
# мой 2016079139 жени 1574674905 