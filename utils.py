import tensorflow as tf
import numpy as np

def scale_to(x, min_val, max_val, scale=1.0):
    '''
    example:

    low = 0, high = 30, scale = 1.5
    So: -1.5 => 0, 1.5 => 30
    if x = -1,
    Output should be: 5
    '''
    scale = float(scale)
    assert max_val > min_val
    x = x * (max_val - min_val) * 0.5 / scale + (max_val + min_val) * 0.5
    return x