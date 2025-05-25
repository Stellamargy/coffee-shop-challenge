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
    pass

class Order():
    pass


# stella_margy=Customer(name=1)
# print(stella_margy.name)