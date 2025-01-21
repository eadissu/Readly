from database import db, populate_database
from app import app

# Create the database and populate it
with app.app_context():
    db.create_all()  # Creates the database and tables
    populate_database()  # Populates the database with initial data

print("Database setup complete!")