from main import app

def test_app_starts_localhost():
    # arrange
    application = app.App()
    # act
    with application.run_test_server() as t:
        response = t.get( '/')
    # assert
    assert response.status_code == 200
    assert b'<p>Hello, World!</p>' in response.data

