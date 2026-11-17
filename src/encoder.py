"""Pulse encoder for irregularly sampled series."""

import numpy as np


class PulseEncoder:
    def __init__(self, hidden: int = 64):
        self.hidden = hidden

    def encode(self, times: np.ndarray, values: np.ndarray) -> np.ndarray:
        gaps = np.diff(times, prepend=times[0])
        return np.tanh(values * np.exp(-gaps))
