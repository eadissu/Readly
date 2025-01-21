from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)  # e.g., "noun", "verb", etc.

    def __repr__(self):
        return f"<Word {self.word} ({self.category})>"