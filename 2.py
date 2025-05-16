class Restaurant:
    def __init__(self, restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type

    def describe_restaurant(self):
        print(f'Name of restaurant:{self.restaurant_name}')
        print(f'Type of cuisine:{self.cuisine_type}')

Restaurant1=Restaurant("La vida loca","Spanish")
Restaurant2=Restaurant("Black bull","American")
Restaurant3=Restaurant("Kimchi","Korean")

Restaurant1.describe_restaurant()
Restaurant2.describe_restaurant()
Restaurant3.describe_restaurant()
