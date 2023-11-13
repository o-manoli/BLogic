import numpy
from typing import Any
from functools import lru_cache

def karnaugh_base_vector(
		dimension: int
	) -> numpy.ndarray[Any, numpy.dtype[Any]]:
	"""
		#TODO
	"""
	if dimension < 1:
		return numpy.array([0], dtype=numpy.uint32).reshape(1, 1)

	if not dimension & 1:
		return karnaugh_base_vector(dimension-1).reshape(-1, 1)

	v0 = karnaugh_base_vector(dimension-1).reshape(1, -1)

	return numpy.column_stack([v0, 2**(dimension-1) + numpy.flip(v0)])

V = lru_cache(karnaugh_base_vector)   # Cached

def karnaugh_matrix(dimension: int) -> numpy.ndarray[Any, numpy.dtype[Any]]:
	"""
		#TODO
	"""
	return V(dimension) + 2 * V(dimension - 1)


