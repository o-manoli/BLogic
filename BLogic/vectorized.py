import numpy
from functools import partial
from typing import (
	Callable,
	Any,
)

BASE_VECTOR: tuple[bool, bool] = False, True

def logicBaseVectorGenerator(
		InputSpace:int, LogicBaseVector:tuple[bool, bool] = BASE_VECTOR
		) -> Callable[[int], numpy.ndarray[Any, numpy.dtype[numpy.bool_]]]:
	"""
		Generates Logic Vector within an input Space
	"""
	def cycler(
			Input:int, Space:int = InputSpace,
			T:tuple[bool] = (LogicBaseVector[0],),
			F:tuple[bool] = (LogicBaseVector[1],)
			) -> numpy.ndarray[Any, numpy.dtype[numpy.bool_]]:
		"""
			Generates Logic Vector within an input Space
				- Input specify which logic vector within an input space
					The 0 th input has a cycle of 1
					The 1 th input has a cycle of 2
					The 2 th input has a cycle of 4
						-> n th ==> 2^n cycle length
		"""
		return numpy.array(
			2**(Space-Input-1) * (2**Input * T + 2**Input * F)
			, dtype = numpy.bool_
		)
	return cycler

def logicBaseVectorMatrix(
		InputSpace:int, LogicBaseVector:tuple[bool, bool] = BASE_VECTOR
		) -> numpy.ndarray[Any, numpy.dtype[numpy.bool_]]:
	"""
		Generates Logic Matrix for an input Space
	"""
	S = logicBaseVectorGenerator(InputSpace, LogicBaseVector)
	return numpy.column_stack([*map(S, range(InputSpace))])


def logicVectorConverter(
		InputSpace:int | None = None, /, BITS:int | None = None,   # keyword only
		RosettaStone:dict[str, bool] = {'0': False, '1':True}
		)->Callable[[int], numpy.ndarray[Any, numpy.dtype[numpy.bool_]]]:
	"""
		Converts a number input to a logic vector
		Leading bit is at the start/top
	"""
	if BITS is None:
		if InputSpace is None:
			raise ValueError("Must Specify Number of bits")
		Bits: int = 2**InputSpace
	else:
		Bits: int = BITS
	def Converter(
			x: int, R: dict[str, bool] = RosettaStone,
			b: Callable[[int], str] = partial(numpy.binary_repr, width = Bits)
		) -> numpy.ndarray[Any, numpy.dtype[numpy.bool_]]:
		"""
			Will truncate overflow bits.
			Starts at the leading bits
		"""
		return numpy.array(tuple(map(R.get, b(x)[:Bits])), dtype=numpy.bool_)
	return Converter

def logicVectorsMatrix(
		BITS: int, /,
		Interpreter:dict[str, bool] = {'0': False, '1':True}
	) -> Callable[..., numpy.ndarray[Any, numpy.dtype[numpy.bool_]]]:
	Converter = logicVectorConverter(BITS=BITS, RosettaStone=Interpreter)
	def C(*V:int):
		return numpy.row_stack(tuple(map(Converter, V)))
	return C