# stdlib
import random

# third party
import numpy as np
import torch


def enable_reproducible_results(seed: int = 0) -> None:
    """Set fixed seed for all the libraries"""
    np.random.seed(seed)
    torch.manual_seed(seed)
    random.seed(seed)
