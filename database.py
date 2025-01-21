from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)  # e.g., "noun", "verb", etc.
    pronunciation = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Word {self.word} ({self.category})>"

def populate_database():
    words = [
{"word": "cat", "category": "noun"},
{"word": "dog", "category": "noun"},
{"word": "bird", "category": "noun"},
{"word": "tree", "category": "noun"},
{"word": "car", "category": "noun"},
{"word": "house", "category": "noun"},
{"word": "book", "category": "noun"},
{"word": "friend", "category": "noun"},
{"word": "ball", "category": "noun"},
{"word": "garden", "category": "noun"},
{"word": "river", "category": "noun"},
{"word": "star", "category": "noun"},
{"word": "school", "category": "noun"},
{"word": "teacher", "category": "noun"},
{"word": "child", "category": "noun"},
{"word": "city", "category": "noun"},
{"word": "mountain", "category": "noun"},
{"word": "ocean", "category": "noun"},
{"word": "planet", "category": "noun"},
{"word": "computer", "category": "noun"},

        {"word": "run", "category": "verb"},
        {"word": "happy", "category": "adjective"},
        {"word": "blue", "category": "adjective"},
        
        
    ]

    for word in words:
        new_word = Word(word=word['word'], category=word['category'], pronunciation=word['pronunciation'])
        db.session.add(new_word)

    db.session.commit()
    print("Database populated with sample words!")