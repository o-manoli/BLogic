"""
	Implementation of Quine-McCluskey algorithm to minimize boolean functions.
"""

from functools import partial
from typing import Iterable, Any, Callable

def reduce(X:str, Y:str) -> str | None:
	"""
		Reduced loops will be constructed by omitting redundant terms is the loop
			e.g.
			"AbC" and "ABC" builds the loop "AC"
				because both 'b' and 'B' are present
					which means that these loops are independent from $B$
		Assumes that the terms are sorted. *somewhat
	"""

	if X.lower() == Y.lower():
		# anything else isn't worth further investigation
		for i, (x, y) in enumerate(zip(X, Y), 1):
			if x != y:
				if X[i:] == Y[i:]: # anything before already matches
					return X.replace(x, '')
				break
	return None


def loops_constructor(*terms:str) -> list[str]:
	"""
		Boolean variable are represented as letters
		Capita letter indicates `True` value for the variable
		Lower letter is the `False` value of that variable

		Reduced loops will be constructed by omitting redundant terms is the loop
			e.g.
			"AbC" and "ABC" builds the loop "AC"
				because both 'b' and 'B' are present
					which means that these loops are independent from $B$

	"""

	return list(
		set(
		T
		for i, x in enumerate(terms, 1)
		for T in map(partial(reduce, x), terms[i:])
		if T is not None
		)
	)


# - - - - - - - - - - - - - - - - - - - -

#########################################
############## Logic Table ##############
#########################################


def cycle(
		n:int,
		F:tuple[bool] = (False,), # Base Vectors
		T:tuple[bool] = (True,)
	) -> list[Iterable[bool]]:
	return [2**i * (2**(n-i-1) * F + 2**(n-i-1) * T) for i in range(n)]


# - - - - - - - - - - - - - - - - - - - -

##################################
######### Representation #########
##################################

def encoder(
	encoding:Iterable[str],
	negate:Callable[[str],str],
	term:Iterable[bool]
	) -> str:
	return ''.join((r if t else negate(r)) for r, t in zip(encoding, term))


def encode(
	*terms:Iterable[bool],
	encoding:Iterable[str],
	negate:Callable[[str],str] = str.lower
	) -> list[str]:
	"""
		Assuming that position in terms correspond to representation.
		If term value is True the encoding will be taken as is
			Otherwise negated
	"""
	return list(
		term for term in map(partial(encoder, encoding, negate), terms)
	)


def represented(
	*X:Iterable[bool],
	Y:Iterable[bool],
	encoding:Iterable[str],
	negate:Callable[[str], str]
	) -> list[str]:
	"""
		Returns the Disjunctive normal form encoded in letters
		DNF
	"""

	return encode(
		*(term for *term, y in zip(*X, Y) if y),
		encoding=encoding,
		negate=negate
	)


def default_encoding(N:int = 26) -> list[str]:
	"""
		A max input of 26 [A-Z]
		Python will have a stroke at 12
	"""
	return [chr(65+i) for i in range(N-1, -1, -1)]


def latex_negation(x:str) -> str:
	return fr"\bar {x}"


def decode(
		*S:str,
		I:dict[str, str] = {x:f"x_{{{i}}}" for i, x in enumerate(default_encoding()[::-1])},
		negation:Callable[[str], str] = latex_negation,
		AND:str = r' \cdot ',
		OR:str = ' + '
	) -> str:

	return OR.join(
		AND.join(
			(I[r] if l else negation(I[r])) for r, l in zip(map(str.upper, X), map(str.isupper, X))
		) for X in S
	)

# - - - - - - - - - - - - - - - - - - - -

######################################
########### QMC Algorithms ###########
######################################


def implicit_loops(
	*X:Iterable[bool],
	Y:Iterable[bool],
	) -> list[list[str]]:
	"""
		Returns ALL possible loops that can be constructed
	"""

	R:list[list[str]] = [represented(
			*X, Y=Y,
			encoding=default_encoding(len(X)),
			negate=str.lower
		)
	]

	while len(T := loops_constructor(*R[-1])):
		R.append(T)

	return R[::-1]

def traverse_loops(loops:list[list[str]]) -> list[str]:

	if not len(loops[0]):
		return list()

	return \
	loops[0] \
	+ traverse_loops(
	[
		list(
			term
			for terms in loops[1:]
			for term in terms
			if not any(not all(x in term for x in X) for X in loops[0])
		)
	]
	)

# - - - - - - - - - - - - - - - - - - - -

## Show

def table(*V:Iterable[Any], Translator:dict[Any, str] = {True:'1', False:'0'}):
	print(*default_encoding(len(V)-1), 'Y', sep='\t')
	for line in zip(*V):
		print(*map(Translator.get, line), sep='\t')
	print("\n")
