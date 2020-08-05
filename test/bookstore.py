class Book:

    def setData(self, title, price, author):
        self.title = title
        self.price = price
        self.author = author

    def printData(self):
        print('제목 :', self.title)
        print('가격 :', self.price)
        print('저자 :', self.author)

    def __init__(self, title, price, author):
        self.setData(title, price, author)
        print('책 개체를 새로 만들었어요')

    def __repr__(self):
        return self.title

