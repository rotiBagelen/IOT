from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize the Database
db = SQLAlchemy()

def create_app():

    # Initialize the Flask app
    app = Flask(__name__)

    # app's configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URL')
    app.debug = os.getenv('FLASK_DEBUG', default=False)

    db.init_app(app)

    from .models import Taplog, Temperature, cardID
    from .views import views

    # Register the views blueprint
    app.register_blueprint(views, url_prefix='/')

    with app.app_context():
        db.create_all()

    with app.app_context():
        if not cardID.query.filter_by(userName='isa').first():
            new_card = cardID(card_id='B592C501', userName='isa')
            new_card2 = cardID(card_id='B7921705', userName='rezqi')
            db.session.add(new_card)
            db.session.add(new_card2)
            db.session.commit()
            
    return app