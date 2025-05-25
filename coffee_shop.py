class Customer():
    def __init__(self,name):
        #calls the  name setter and runs validation
        self.name=name

    def __repr__(self):
        return f"{self.name}"
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
    #returns orders for a customer
    def orders(self):
        return [order for order in Order.all if order.customer==self]
    
    def coffees(self):
        # I am using a set to remove duplicates
        return list({order.coffee for order in Order.all if order.customer==self})
    #Enables a customer to create an order
    def create_order(self,coffee,price):
        Order(self,coffee,price)

    @classmethod
    def most_aficionado(self):
        pass


class Coffee():
    def __init__(self,name):
        #run validations during the first time initialization
        if(isinstance(name,str) and len(name)>=3):
                self._name=name
        else:
            raise Exception("Coffee should be atleast a 3 word string")
        
    def __repr__(self):
        return f"{self.name}"
        
    #getter for name
    @property
    def name (self):
        return self._name 
    #setter for name -coffee name is immutable once it has been initialized
    @name.setter
    def name (self,coffee_name):
        raise Exception("You cant change coffee name")
    #returns all orders for a speciific coffee
    def orders(self):
        return [order for order in Order.all if order.coffee==self]
    
    def customers(self):
        return list({order.customer for order in Order.all if order.coffee==self})
    #total count of order for a particular coffee
    def num_orders(self):
        #Get orders for that particular coffee and return count
        return len(self.orders()) 
    
    #Mean of all order prices for this coffee
    def average_price(self):
        orders_prices=[order.price for order in Order.all if order.coffee==self]
        return sum(orders_prices) / self.num_orders()
    

        


        
        

class Order():
    #Single source of truth-maintains data integrity
    all=[]
    def __init__(self, customer, coffee, price):
        #runs the customer setter
        self.customer = customer
        #runs the coffee setter
        self.coffee = coffee
        #checks for price validation -price is immutable after initilation
        if not (isinstance(price, float) and 1.0 <= price <= 10.0):
            raise ValueError("price must be a float between 1.0 and 10.0")
        self._price = price
        #keeps track of all orders
        Order.all.append(self)

    def __repr__(self):
        return f"{self.customer} {self.coffee} {self.price}"

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        if not isinstance(value, Customer):
            raise TypeError("customer must be an instance of Customer")
        self._customer = value

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        if not isinstance(value, Coffee):
            raise TypeError("coffee must be an instance of Coffee")
        self._coffee = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, _):
        raise AttributeError("Price is immutable once set.")
   
    
        


stella_margy=Customer(name="Stella Margy")
moffat_oloo=Customer(name="Moffat Oloo" )
laban_oloo=Customer(name="Laban Oloo")
adie_atieno=Customer(name="Adie Atieno")
# print(stella_margy.name)

lattee=Coffee(name="latte")
americano=Coffee(name="Americano")
order_001=Order(customer=stella_margy,coffee=lattee,price=2.0)
order_002=Order(customer=stella_margy,coffee=lattee,price=2.0)
order_003=Order(customer=laban_oloo,coffee=lattee,price=2.0)
order_003=Order(customer=adie_atieno,coffee=lattee,price=2.0)
print(stella_margy.coffees())
print(americano.num_orders())
print(lattee.average_price())



