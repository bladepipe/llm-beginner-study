import torch
import torch.nn as nn


class Embedding(nn.Module):
    def __init__(self, vocab_size: int = 65, n_embd: int = 32):
        super().__init__()
        self.token_embedding_table = nn.Embedding(vocab_size, n_embd)

    def forward(self, idx: torch.Tensor) -> torch.Tensor:
        # idx: (B, T) where B=batch size, T=sequence length
        # return: (B, T, n_embd)
        return self.token_embedding_table(idx)


# Example usage (uncomment to run):
# if __name__ == "__main__":
#     from tokenizer import Tokenizer
#     t = Tokenizer()
#     e = Embedding(vocab_size=65, n_embd=32)
#     ids = torch.tensor(t.encode("hello world"))
#     vecs = e(ids)
#     print(vecs.shape)  # should be (11, 32)