
class Shopping_cart:
    def __init__(self):
        self.item= {}


    def add_cart(self):
        self.item_name = input('Please add your item?')
        self.price = input(f"What is the price of your {self.item_name}?")
        self.item[self.item_name] = self.price
    
    def show_cart(self):
        print('Thank you for shopping.')
        print(f'Your cart contains:')
        for item_name,price in self.item.items():
                print(f"{item_name}: {price}")

    def delete_cart(self):
        remov = input('What would you like to remove from your cart? (capitalization matters)')
        try:
            del self.item[remov]
            print(f'{remov} was successfully removed from your cart.')
        except:
            print(f'{remov} was not in your cart.')
        
my_cart=Shopping_cart()        

def shopping_list(cart): 

    shopping=True
    while shopping==True:
        begin=input("What do you want to do? Add/ Show/ Delete/ Quit?")
        
        if begin.title()=="Add":
            cart.add_cart()
                  
        elif begin.title()=='Show':
            cart.show_cart()

        elif begin.title()=='Delete':
            cart.delete_cart()
              
        elif begin.title()=='Quit':
            for item_name,price in cart.item.items():
                print(f"{item_name}: {price}")
            break

        else:
            print('Invalid input, please try again.')      

shopping_list(my_cart)