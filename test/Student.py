from Person import Person

class Student(Person):
    def study(self):
        print('열공열공...')

lee = Person()
print(lee.mouth)
print(lee.talk(), "\n")

kim = Student()
print(kim.mouth)
print(kim.talk())
print(kim.study())

