from dataclasses import dataclass
import torch
import torch.nn as nn
from torch.nn import functional as F

batch_size: int = 64
block_size: int = 256
max_iters: int = 5000
eval_interval: int = 500
learning_rate = 3e-4
device = 'cuda' if torch.cuda.is_available() else 'cpu'
eval_iters: int = 200
n_embd: int = 384
n_head: int = 6
n_layer: int = 6
dropout: float = 0.2

@dataclass
class GPTConfig(object):
    block_size: int = 256
    vocab_size: int = 65
    n_layer: int = 6
    n_head: int = 6
    n_embd: int = 384


class Block(nn.Module):

    def __init__(self, config):
        super().__init__()
        self.ln_1 = nn.LayerNorm(config.n_embd)
        self.attr = CasualSelfAttention(config.n_embd)
        self.ln_2 = nn.LayerNorm(config.n_embd)
        self.mlp = MLP(config)
    
    def forward(self, x):
        x = x + self.attr(self.ln_1(x))
        x = x + self.attr(self.ln_2(x))
        return x


class GPT(nn.Module):

    def __init__(self, config):
        super().__init__()
        self.cofing = config

        self.transformer = nn.ModuleDict(dict(
            wte = nn.Embedding(config.vocab_size, config.n_embd), # weights for token embedings
            wpe = nn.Embedding(config.block_size, config.n_embd), # weights for position embeding
            h = nn.ModuleList([Block(config) for _ in range(config.n_layer)]),
            ln_f = nn.LayerNorm(config.n_embd),
        ))
        self.lm_head = nn.Linear(config.n_embd, config.vocab_size, bias=False)