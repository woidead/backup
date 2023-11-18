# #oop

# class Hello():
#     maxsp = 100
#     dead_health = 0
#     def __init__(self, race = 'ork', damage = 800, armor = 50, health = 100):
#         self.race = race
#         self.damage = damage
#         self.armor = armor
#         self.health = health
#     def hit(self, damage):
#         # meme = self.health + self.armor
#         # meme -= damage
#         # self.armor = meme / 2
#         # self.health = meme / 2


#         # self.armor -= damage
#         # if self.armor < damage:
#         #     self.health += self.armor


#         meme = damage /2
#         if meme > self.armor or meme == self.armor:
#             self.armor-=meme
#             sl = self.armor-meme
#             self.health +=sl
#         if meme < self.armor:
#             self.armor-=meme
#             self.health-=meme
            
#     def isdead(self):
#             if self.health + self.armor < Hello.dead_health or self.health + self.armor == Hello.dead_health :
#                 return 'hero dead'
#             elif self.health + self.armor > Hello.dead_health:
#                 return {self.health}
#             return self.health == Hello.dead_health
        
# hello = Hello()
# hello.hit(20)
# # print('урон:',hello.damage)
# if hello.health > 0:
#     print('здоровье', hello.health)
# elif hello.health < 0 or hello.health == 0 :
#     print('здоровье: 0')
# if hello.armor > 0:
#     print('защита', hello.armor)
# elif hello.armor < 0 or hello.armor == 0 :
#     print('защита: 0')

# # print(hello.isdead())
# # print(hello.__dict__)