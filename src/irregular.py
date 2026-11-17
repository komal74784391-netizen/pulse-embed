"""Utilities for irregular sampling grids."""


def resample_grid(times, horizon):
    return [times[0] + i * (times[-1] - times[0]) / horizon for i in range(horizon)]
