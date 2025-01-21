import csv
from database import db, Word
from app import app

def csv_to_database(csv_file):
    with app.app_context():
        # Create tables if they don't exist
        db.create_all()
        
        # Read the CSV file and insert records
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                new_word = Word(word=row['word'], category=row['category'])
                db.session.add(new_word)

        db.session.commit()
        print("Database populated from CSV!")

# Set the file path for the CSV
csv_file = "data/words.csv" 

# Run the function
csv_to_database('words.csv')