class Customer():
    def __init__(self,name):
        #calls the  name setter and runs validation
        self.name=name
    #Getter for name
    @property
    def name (self):
        return self._name
    #setter for name
    @name.setter
    def name (self,customer_name):
        #check if it is a 1-15 character string.
        if(isinstance(customer_name,str) and 1 <= len(customer_name) <= 15):
            self._name=customer_name
        #raises type error exception
        else:
            raise TypeError("Name should be a 1-15 character string")


class Coffee():
    def __init__(self,name):
        #run validations during the first time initialization
        if(isinstance(name,str) and len(name)>=3):
                self._name=name
        else:
            raise Exception("Coffee should be atleast a 3 word string")
        
    #getter for name
    @property
    def name (self):
        return self._name 
    #setter for name -coffee name is immutable once it has been initialized
    @name.setter
    def name (self,coffee_name):
        raise Exception("You cant change coffee name")

        
        

class Order():
        def __init__(self, customer, coffee, price):
            if not isinstance(customer, Customer):
                raise Exception("customer must be an instance of Customer")
            
            if not isinstance(coffee, Coffee):
                raise Exception("coffee must be an instance of Coffee")
            
            if not (isinstance(price, float) and 1.0 <= price <= 10.0):
                raise Exception("price must be a float between 1.0 and 10.0")
            # an order instance will not be created until all the validation fails 
            self.customer = customer
            self.coffee = coffee
            self._price = price
    

        
        @property
        def price (self):
            return self._price
        #prevents changing price after initialization
        @price.setter
        def price (self,value):
            raise Exception("Price is unchangeable once created.")

        
        
        


stella_margy=Customer(name="Stella Margy")
# print(stella_margy.name)

latte=Coffee(name="latte")

order_001=Order(customer=stella_margy,coffee=latte,price=1.1)
print(order_001.price)
order_001.price=5
print(order_001.price)

