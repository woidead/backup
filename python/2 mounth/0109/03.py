class Counter:
    def start_from(self, count = 0):
        self.count = count
    
    def increment(self):
        self.count += 1 
    
    def display(self):
        print( "текущее значние =" (self.count))
    
    def reset(self):
        self.count = 0

    count = Counter ()
    count.start_from(5)
    count.increment()    
    count.increment()    
    count.display()    # 7
    count.increment()    
    count.display()    # 8
    count.reset()    
    count.display()    # 0
