from main import product

def new_product_name():
    return 'Product1'

def create_product(product_name):
    return product.Product(product_name)

def test_product():
    # arrange
    product_name = new_product_name()
    # act
    product = create_product(product_name)
    # assert
    assert product.ID is not None and product.name == product_name
