class Car(object):
    def __init__(self,model,color,company,speed_limit):
        self.color= color
        self.model= model
        self.company= company
        self.speed_limit= speed_limit
    
    def start(self):
        print("started")
    
    def stop(self):
        print("stopped")

    def accelarate (self):
        print("accelarating")
    
    def change_gear (self,gear_type):
        print("gear change")


audi= Car ("a6", "red", "audi", "100")
print (audi.stop())
print (audi.color)
print (audi.model)


