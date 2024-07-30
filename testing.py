
import re

class Tokenizer:
    def tokenize(self, text):
        # Split text into tokens based on whitespace and punctuation
        tokens = re.findall(r'\b\w+\b|[^\w\s]', text)
        return tokens

# Example usage
tokenizer = Tokenizer()

text = "Hello! This is a sample sentence, with some punctuation."
tokens = tokenizer.tokenize(text)

print(tokens)