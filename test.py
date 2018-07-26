import flask_testing
from unittest import TestCase
from flask import jsonify
from flask_restful import reqparse
import app


database_name = 'mydiary'
class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object('config.DevelopmentConfig"')
        return app

    def test_app_is_development(self):
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] == 'postgresql://postgres:@localhost/mydiary'
        )


class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object('config.TestingConfig"')
        return app

    def test_app_is_testing(self):
        self.assertTrue(app.config['DEBUG'])
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] == 'postgresql://postgres:@localhost/mydiary_test'
        )