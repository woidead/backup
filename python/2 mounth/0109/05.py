
y = ['A', 'a','E', 'e', 'I', 'i', 'O', 'o', 'U' ,'u', 'Y', 'y']
class Letter:
    def __init__(self, letter):
        self.letter = letter
        
    def check(self):
            if self.letter in y:
                print("your letter is a vowel", self.letter)
            elif len(self.letter) == 1 and isinstance(self.letter, str): #and isalpha #(self.letter)
                print("your letter is a not vowel", self.letter)
            else :
                print('Латинскую!!')
                

l = Letter('b')
l.check()
        