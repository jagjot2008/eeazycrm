from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from eeazycrm.config import DevelopmentConfig, TestConfig, ProductionConfig
import os

# Initialize the Flask application
app = Flask(__name__, instance_relative_config=True)

# Determine the configuration class based on the environment variable
config_class = ProductionConfig()  # Default to ProductionConfig
if os.getenv('FLASK_ENV') == 'development':
    config_class = DevelopmentConfig()
elif os.getenv('FLASK_ENV') == 'testing':
    config_class = TestConfig()

# Load the configuration into the app
app.config.from_object(config_class)

# Initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Set up the command manager
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# Define a sample model
class TestUser (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

# Run the application
if __name__ == '__main__':
    manager.run()
