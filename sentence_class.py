class Sentence:
    def __init__(self, sentence):
        # Instance variables
        self._sentence = sentence  # List of strings
        self._index = 0           # Starts at 0

    # Getter and setter for sentence
    def get_sentence(self):
        return self._sentence

    def set_sentence(self, sentence):
        if isinstance(sentence, list) and all(isinstance(word, str) for word in sentence):
            self._sentence = sentence
        else:
            raise ValueError("Sentence must be a list of strings.")

    # Getter and setter for index
    def get_index(self):
        return self._index

    def set_index(self, index):
        if isinstance(index, int) and 0 <= index < len(self._sentence):
            self._index = index
        else:
            raise ValueError("Index must be a non-negative integer within the sentence bounds.")

    # Get the current word based on index
    def get_word(self):
        if 0 <= self._index < len(self._sentence):
            return self._sentence[self._index]
        else:
            raise IndexError("Index is out of bounds of the sentence.")
