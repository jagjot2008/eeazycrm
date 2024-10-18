from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

import os

# Import configuration classes using absolute imports
from eeazycrm.config import DevelopmentConfig, TestConfig, ProductionConfig

# Database handle
db = SQLAlchemy(session_options={"autoflush": False})

# Encryptor handle
bcrypt = Bcrypt()

# Manage user login
login_manager = LoginManager()
login_manager.login_view = 'users.login'  # Function name of the login route


def run_install(app_ctx):
    from eeazycrm.install.routes import install
    app_ctx.register_blueprint(install)
    return app_ctx


def create_app(config_class=ProductionConfig):
    app = Flask(__name__, instance_relative_config=True)

    # Set the configuration class based on the environment variable
    if os.getenv('FLASK_ENV') == 'development':
        config_class = DevelopmentConfig()
    elif os.getenv('FLASK_ENV') == 'production':
        config_class = ProductionConfig()
    elif os.getenv('FLASK_ENV') == 'testing':
        config_class = TestConfig()

    app.config.from_object(config_class)
    app.url_map.strict_slashes = False
    app.jinja_env.globals.update(zip=zip)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        # Check if the config table exists; otherwise, run install
        engine = db.get_engine(app)
        if not engine.dialect.has_table(engine, 'app_config'):
            return run_install(app)
        else:
            from eeazycrm.settings.models import AppConfig
            row = AppConfig.query.first()
            if not row:
                return run_install(app)

        # Application is installed, so extend the config
        from eeazycrm.settings.models import AppConfig, Currency, TimeZone
        app_cfg = AppConfig.query.first()
        app.config['def_currency'] = Currency.get_currency_by_id(app_cfg.default_currency)
        app.config['def_tz'] = TimeZone.get_tz_by_id(app_cfg.default_timezone)

        # Include the routes
        from eeazycrm.main.routes import main
        from eeazycrm.users.routes import users
        from eeazycrm.leads.routes import leads
        from eeazycrm.accounts.routes import accounts
        from eeazycrm.contacts.routes import contacts
        from eeazycrm.deals.routes import deals
        from eeazycrm.settings.routes import settings
        from eeazycrm.settings.app_routes import app_config
        from eeazycrm.reports.routes import reports

        # Register routes with blueprints
        app.register_blueprint(main)
        app.register_blueprint(users)
        app.register_blueprint(settings)
        app.register_blueprint(app_config)
        app.register_blueprint(leads)
        app.register_blueprint(accounts)
        app.register_blueprint(contacts)
        app.register_blueprint(deals)
        app.register_blueprint(reports)

        return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)  # Enable debug mode for development
