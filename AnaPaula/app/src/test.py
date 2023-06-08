import pytest
from flask_testing import TestCase
from app import app

class HomeTestCase(TestCase):
    def create_app(self):
        return app

    def test_home(self):
        response = self.client.get('/')
        assert response.status_code == 200
        assert response.data.decode() == 'Hello, World!'

if __name__ == '__main__':
    pytest.main()
