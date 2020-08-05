class Fridge:
    isOpened = False
    foods = []

    def opend(self):
        self.isOpened = True
        print("Fridge is opened")

    def put(self, thing):
        if self.isOpened:
            self.foods.append(thing)
            print('input food in fridge')
        else:
            print("I cat'n input food in fridge")

    def close(self):
        self.isOpened = False
        print("Fridge is closed")

class Food:
    pass