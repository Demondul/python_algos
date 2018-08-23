class Bike:
    def __init__(self, price, max_speed, miles=0):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles

    def displayInfo(self):
        print("Price : " + str(self.price))
        print("Max Speed : " + str(self.max_speed))
        print("Miles : " + str(self.miles))

    def ride(self):
        print("Riding")
        self.miles=self.miles+10

    def reverse(self):
        print("Reversing")
        self.miles=self.miles-5        


baiyk1 = Bike(200,"25mph")
baiyk1.ride()
baiyk1.ride()
baiyk1.ride()
baiyk1.reverse()
baiyk1.displayInfo()

baiyk2 = Bike(200,"25mph")
baiyk2.ride()
baiyk2.ride()
baiyk2.reverse()
baiyk2.reverse()
baiyk2.displayInfo()

baiyk3 = Bike(200,"25mph")
baiyk3.reverse()
baiyk3.reverse()
baiyk3.reverse()
baiyk3.displayInfo()