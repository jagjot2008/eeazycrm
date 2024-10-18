import logging
import os
from eeazycrm import create_app

# Configure logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Configuration class
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default_secret_key')
    DEBUG = os.environ.get('DEBUG', 'True') == 'True'

# Create the app with configuration
app = create_app()
app.config.from_object(Config)

@app.before_first_request
def before_first_request():
    logging.info("Application has started.")

@app.errorhandler(404)
def not_found(error):
    logging.warning("404 error occurred.")
    return {"error": "Resource not found."}, 404

@app.errorhandler(500)
def internal_error(error):
    logging.error(f"500 error occurred: {error}")
    return {"error": "Internal server error."}, 500

@app.route('/')
def home():
    return "Welcome to the Easy CRM application!"

@app.route('/api/health', methods=['GET'])
def health_check():
    return {"status": "healthy"}, 200

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
