#!/usr/bin/python3
"""This iss a matrix multiplication function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return multiplication of two matrices.
    Args:
        m_a: The first matrix.
        m_b: The second matrix.
    """

    return (np.matmul(m_a, m_b))
