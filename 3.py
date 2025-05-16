class Restaurant:
    def __init__(self, restaurant_name,cuisine_type,rating):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.rating=rating

    def describe_restaurant(self):
        print(f'Name of restaurant:{self.restaurant_name}')
        print(f'Type of cuisine:{self.cuisine_type}')
        print(f'Rating:{self.rating:.1f}')
    def update_rating(self,new_rating):
        if isinstance(new_rating,float) or isinstance(new_rating,int):
            self.rating=new_rating
        else:
            print("wrong format new raiting")

newRestaurant=Restaurant("La vida loca","Spanish",4.8)
newRestaurant.describe_restaurant()
newRestaurant.update_rating(4.3)
newRestaurant.describe_restaurant()
