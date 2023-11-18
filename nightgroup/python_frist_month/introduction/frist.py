import os, random, string

os.makedirs('newdir', exist_ok=True)
for i in range(5):
    name = ''
    for _ in range(8):
        name += (random.choice(string.ascii_letters+string.digits))
    with open('newdir/'+name+'.txt', 'w') as data:
        data.write(name)
        