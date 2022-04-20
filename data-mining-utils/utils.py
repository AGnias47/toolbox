#!/usr/bin/env python3

"""
Generic utilities used in this project
"""

import os
import random

import numpy as np
import torch
import torch.backends.cudnn


def seed_everything(seed=42):
    """
    Seed everything. Taken from:
    https://datascience.stackexchange.com/questions/66345/why-ml-model-produces-different-results-despite-random-state-defined-and-how-to

    Parameters
    ----------
    seed: int (default is 42)

    Returns
    -------
    None
    """
    random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    return None
