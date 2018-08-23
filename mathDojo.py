class MathDojo:
    def __init__(self,number=0):
        self.number=number

    def add(self,*numbers):
        for i in numbers:
            self.number = self.number + i
        return self

    def subtract(self,*numbers):
        for i in numbers:
            self.number = self.number - i
        return self

    def result(self):
        print(self.number)

md=MathDojo()

md.add(2).add(2,5,1).subtract(3,2).result()