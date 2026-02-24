# Simple character-level tokenizer for Shakespeare text

class Tokenizer:
    def __init__(self):
        # 65 chars: a-z, A-Z, 0-9, punctuation, space, newline, and special tokens
        self.chars = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~\n\r\t\x00"""
        self.stoi = {ch: i for i, ch in enumerate(self.chars)}
        self.itos = {i: ch for i, ch in enumerate(self.chars)}
        self.vocab_size = len(self.chars)

    def encode(self, s):
        return [self.stoi[c] for c in s if c in self.stoi]

    def decode(self, ids):
        return ''.join([self.itos[i] for i in ids if i in self.itos])

# Example usage (uncomment to test):
# t = Tokenizer()
# print(t.encode("hello"))
# print(t.decode([36, 37, 38, 38, 39]))
