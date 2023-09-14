class Storage():

    def __init__(self):
        self.storage = {}

    def save_product(self, product):
        self.storage[product.ID] = product

    def get_product(self, product_id):
        return self.storage[product_id]

    def get_all_products(self):
        return self.storage