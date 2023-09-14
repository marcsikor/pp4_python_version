from main import product, storage, app

def test_app_gives_catalog():
    
    # arrange
    catalog = storage.Storage()
    item1 = product.Product('apple')
    item2 = product.Product('example')
    item3 = product.Product('item')
    application = app.App()
    
    # act
    catalog.save_product(item1)
    catalog.save_product(item2)
    catalog.save_product(item3)
    application.add_catalog(catalog)
    
    with application.run_test_server() as t:
        response = t.get('/catalog')

    # assert
    assert response.status_code == 200
    assert b'apple'in response.data
    assert b'example'in response.data
    assert b'item'in response.data
    assert str(item1.ID).encode('utf-8') in response.data
