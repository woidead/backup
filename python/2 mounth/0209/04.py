class Factory:
    def engine(self):
        print('двигатель создан')
    def bridge(self):
        print(' ходовая чсть создана')
class Toyota(Factory):
    def wheels(self):
        print( "Колёса крутятся")
    def window(self):
        print("Стёкла опущены")

toyota = Toyota()
toyota.bridge()
toyota.engine()
toyota.wheels()
toyota.window()