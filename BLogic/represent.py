import numpy
from typing import Any, Iterable

def P(
		*V:Iterable[Any], sep:str=3*' ',
		Interpreter: dict[bool, str] = {True: '1', False: '0'}
	):
	for v in zip(*V):
		print(*map(Interpreter.get, v), sep=sep)

def Sep(Repeat:int=12, Ch:str='-', S:str=' ', start:str='', end:str='\n'):
	"""
		Prints a Separating line
	"""
	print(start, S.join(Repeat*Ch), sep='', end=end)

def Sectors(
		Matrix:numpy.ndarray[Any, numpy.dtype[Any]],
		Interpreter: dict[bool,str] = {True: '1', False: '0'}
	):
	def tab(
		R: Iterable[bool], Sep:str = ' ',
		I: dict[bool,str] = Interpreter
	) -> str:
		return Sep.join(I[r] for r in R)

	def line(
		Rows:Iterable[Iterable[bool]], Sep:str = 3*' '
	) -> str:
		return Sep.join(map(tab, Rows))

	def echo(*LogicVectors:numpy.ndarray[Any, numpy.dtype[numpy.bool_]]):
		for Rows in zip(*(b[Matrix] for b in LogicVectors)):
			print(line(Rows))
	return echo

