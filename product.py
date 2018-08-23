class Product:
    def __init__(self,price,item_name,weight,brand,status="sale"):
        self.price=price
        self.item_name=item_name
        self.weight=weight
        self.brand=brand
        self.status=status

        self.price=self.AddTax(0.12)

    def sell(self,status="sold"):
        self.status=status

        return self
        

    def AddTax(self,tax):
        return self.price + (self.price * tax)

    def Return(self,reason_for_return):
        if "defective" in reason_for_return:
            self.price=0
            self.sell("defective")
        elif "return" in reason_for_return or "returned" in reason_for_return:
            self.sell("for sale")
        elif "opened" in reason_for_return:
            self.sell("used")
            self.price=self.price - (self.price * 0.20)

        return self
        

    def DisplayInfo(self):
        print("Price : " + str(self.price))
        print("Item Name : " + str(self.item_name))
        print("Item Weight : " + str(self.weight))
        print("Item Brand : " + str(self.brand))
        print("Item Status: " + str(self.status))

        return self

prod = Product(25,"Mouse",1,"LoChiteg")
prod.Return("It's opened")
prod.DisplayInfo()