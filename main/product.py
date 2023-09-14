import uuid

class Product():

    def __init__(self, product_name):
        self.ID = uuid.uuid4()
        self.name = product_name
    
    def __str__(self):
        return self.name