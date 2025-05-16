class Restaurant:
    def __init__(self, restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type

    def describe_restaurant(self):
        print(f'Name of restaurant:{self.restaurant_name}')
        print(f'Type of cuisine:{self.cuisine_type}')
    def open_restaurant(self):
        print(f'{self.restaurant_name} Know is open!')
newRestaurant=Restaurant("La vida loca","Spanish")
print(newRestaurant.restaurant_name)
print(newRestaurant.cuisine_type)

newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()