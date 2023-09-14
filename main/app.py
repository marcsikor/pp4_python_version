from flask import Flask
# from main import storage

class App():

    def __init__(self):
        self.app = Flask(__name__)
        @self.app.route('/')
        def hello_world():
            return "<p>Hello, World!</p>"

    def run_test_server(self):
        return self.app.test_client()

    def add_catalog(self, catalog):
        @self.app.route('/catalog')
        def display_catalog():
            return "<p>Catalog available below<p><br>" + '[' + ''.join(('{' + str(i.ID) + ', ' + str(i) + '},' for i in catalog.get_all_products().values()))[:-1] + ']'

    def run_app(self):
        self.app.run()