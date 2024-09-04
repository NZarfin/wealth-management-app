import unittest
from flask_testing import TestCase
from app import create_app
from app.utils.db import db
from app.models.user import User

class BasicTests(TestCase):
    def create_app(self):
        # Set up the test configuration for the Flask app
        app = create_app()
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use in-memory SQLite for tests
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        return app

    def setUp(self):
        # Create the database schema
        with self.app.app_context():
            db.create_all()

            # Add a test user
            test_user = User(username='testuser', email='test@example.com')
            test_user.set_password('testpass')
            db.session.add(test_user)
            db.session.commit()

    def tearDown(self):
        # Tear down the database
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_home_page(self):
        # Test that the home page returns 404 since no '/' route is defined
        response = self.client.get('/')
        self.assertEqual(response.status_code, 404)

    def test_register_user(self):
        # Test user registration
        response = self.client.post('/register', json={
            'username': 'newuser',
            'password': 'newpass',
            'email': 'new@example.com'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('User registered successfully', response.json['message'])

    def test_register_existing_user(self):
        # Test registering a user with an existing username
        response = self.client.post('/register', json={
            'username': 'testuser',  # This user already exists
            'password': 'testpass',
            'email': 'test2@example.com'
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn('Username already exists', response.json['error'])

    def test_login_success(self):
        # Test successful login
        response = self.client.post('/login', json={
            'username': 'testuser',
            'password': 'testpass'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Login successful', response.json['message'])

    def test_login_invalid_user(self):
        # Test login with invalid credentials
        response = self.client.post('/login', json={
            'username': 'nonexistent',
            'password': 'wrongpass'
        })
        self.assertEqual(response.status_code, 401)
        self.assertIn('Invalid username or password', response.json['error'])

if __name__ == '__main__':
    unittest.main()
