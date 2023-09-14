from main import product, storage

def storage_exists():
    return storage.Storage()

def example_product():
    return product.Product('example')

def test_add_product():
    
    # arrange    
    stor = storage_exists()
    prod = example_product()
    
    # act
    stor.save_product(prod)

    # assert
    assert stor.get_product(prod.ID).ID == prod.ID
