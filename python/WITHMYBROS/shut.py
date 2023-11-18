# import os
# os.system('shutdown/s')

list= ['aaa', 'dddd', 'adbbb']
x = (max(list, key=len))
c  = (x[0],x[1])
z = ''.join(c)
for i in range (0,len(list)):
    if True == list[i].startswith(z):
        print(True)
    else:
        print ('False')
    
# print(list[i].startswith(z))