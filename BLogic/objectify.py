from BLogic.vectorized import (
	logicBaseVectorMatrix,
	logicVectorConverter,
	BASE_VECTOR
)

import numpy

from typing import Any

def InputSpace(
		Dimension: int,
		LogicBaseVector:tuple[bool, bool] = BASE_VECTOR
	) -> type:
	"""
		Comments ...
	"""
	class LogicVector(numpy.ndarray[Any, numpy.dtype[numpy.bool_]]):
		BaseVectorsMatrix = logicBaseVectorMatrix(
			Dimension, LogicBaseVector= LogicBaseVector
		)
		Converter = logicVectorConverter(Dimension)

		def __new__(cls, b: int | None = None, v: int | None = None):
			"""
				Very Helpful Comment! #TODO
			"""
			if v is None:
				if b is None:
					# raise ValueError("Must Specify Vector")
					return numpy.flip(cls.BaseVectorsMatrix.T, 0)
				return cls.BaseVectorsMatrix[:, b]
			return cls.Converter(v)
	return LogicVector


