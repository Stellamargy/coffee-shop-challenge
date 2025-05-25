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
    pass


# stella_margy=Customer(name=1)
# print(stella_margy.name)

# coffe1=Coffee(name=1)
# print(coffe1.name)
# coffe1.name="Expresso"