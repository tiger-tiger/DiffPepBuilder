# ---------------------------------------------------------------------------
# FILENAME: test.py
# CREATED: 2025-01-16 10:59:00+08:00
# UPDATED:
# AUTHOR: Newton <newton@earth.com>
# DESCRIPTION:
# Copyright (c) Newton Inc. All Rights Reserved.
# ---------------------------------------------------------------------------

import torch
import numpy as np
import torch.nn as nn
import torch.nn.functional as F


class DQN:
    def __init__(self, state_dim, hidden_dim, action_dim):
        self.fc1 = nn.Linear(state_dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, actional_dim)

    def forward(self, x):
        x = nn.ReLU(self.fc1(x))
        return self.fc2(x)


# test.py ENDS HERE
