class parent():
    def __init__(self):
        print("This Is Parent Class")
        
    def menu(dish):
        if dish == "Burger":
            print("You Can Add Following Toppings")
            print("More Cheese | Add Jalapeno")
            
        elif dish == "Iced Americano":
            print("You Can Add The Following Toppings")
            print("Add Chocolate Flavour | Add Caramel Flavour")
            
        else:
            print("Please Enter A Valid Dish")
            
    def final_amount(dish, add_ons):
        if dish == "Burger" and add_ons == "Cheese":
            print("You Need To Pay 250 USD")
            
        elif dish == "Burger" and add_ons == "Jalapeno":
            print("You Need To Pay 350 USD")
            
        elif dish == "Iced Americano" and add_ons == "Chocolate":
            print("You Need To Pay 250 USD")
            
        elif dish == "Iced Americano" and add_ons == "Caramel":
            print("You Need To Pay 450 USD")
            
class child1(parent):
     def __init__(self, dish):
         self.new_dish = dish
         
     def get_menu(self):
        parent.menu(self.new_dish)
        
class child2(parent):
    
    def __init__(self, dish, addons):
        self.new_dish = dish
        self.addons = addons
        
    def get_final_amount(self):
        parent.final_amount(self.new_dish, self.addons)
        
child1_object = child1("Burger")
child1_object.get_menu()     
        
child2_object = child2("Burger", "Jalapeno")
child2_object.get_final_amount()      
        