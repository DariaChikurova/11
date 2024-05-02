def zadanie1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Название ресторана: {self.restaurant_name}")
            print(f"Тип кухни: {self.cuisine_type}")

        def open_restaurant(self):
            print(f"Ресторан {self.restaurant_name} открыт!")

    newRestaurant = Restaurant("Darchi", "Азиатская")
    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()

def zadanie2():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Название ресторана: {self.restaurant_name}")
            print(f"Тип кухни: {self.cuisine_type}")

        def open_restaurant(self):
            print(f"Ресторан {self.restaurant_name} открыт!")

    restaurant1 = Restaurant("Darchi1", "Итальянская")
    restaurant2 = Restaurant("Darchi2", "Мексиканская")
    restaurant3 = Restaurant("Darchi3", "Японская")

    restaurant1.describe_restaurant()
    restaurant1.open_restaurant()
    restaurant2.describe_restaurant()
    restaurant2.open_restaurant()
    restaurant3.describe_restaurant()
    restaurant3.open_restaurant()

def zadanie3():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, restaurant_rating=0 ):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.restaurant_rating = restaurant_rating

        def describe_restaurant(self):
            print(f"Название ресторана: {self.restaurant_name}")
            print(f"Тип кухни: {self.cuisine_type}")
            print(f"Рейтинг: {self.restaurant_rating}")

        def open_restaurant(self):
            print(f"Ресторан {self.restaurant_name} открыт!")

        def update_rating(self, newrestaurant_rating):
            self.restaurant_rating = newrestaurant_rating
            print(f"Рейтинг ресторана {self.restaurant_name} обновлен до {self.restaurant_rating}")

    restaurant1 = Restaurant("Darchi1", "Итальянская", 1)
    restaurant1.describe_restaurant()
    restaurant1.update_rating(3)
    restaurant1.describe_restaurant()

while True:
    print('1. ресторан')
    print('2. 3 ресторана ')
    print('3. рейтинг')
    print('4. Выход')
    a = int(input('Выберите действие: '))
    if a == 1:
        zadanie1()
    elif a == 2:
        zadanie2()
    elif a == 3:
        print(zadanie3())
    elif a == 4:
        break
    else:
        print('Неверное действие')