from typing import Iterable, Any, Callable, Iterator

from collections import defaultdict

# Python Alignment Options
PAling: tuple[str, str, str] = "<", ">", "^"       # left, right and center

# Markdown Alignment Options
MAling: tuple[str, str, str] = ":-", "-:", ":-:"   # left, right and center

def mapping(keys: Iterable[str], values: Iterable[str]) -> dict[str, str]:
	return { key: value for key, value in zip(keys, values)}

P2P:dict[str, str] = mapping(PAling, PAling)
M2P:dict[str, str] = mapping(MAling, PAling)
M2M:dict[str, str] = mapping(MAling, MAling)
P2M:dict[str, str] = mapping(PAling, MAling)

# Markdown or Python to Python Alignment
MOP2P: dict[str, str] = P2P | M2P | defaultdict(lambda: "^")   # InterpreterStone
MOP2M: dict[str, str] = P2M | M2M | defaultdict(lambda: "-")   # InterpreterStone

# left, right and center
formatted_separator: dict[str, Callable[[int], str]] = {
	":-"  : lambda size : f":-{(size-2)*'-'}",
	"-:"  : lambda size : f"{(size-2)*'-'}-:",
	":-:" : lambda size : f":-{(size-3)*'-'}:",
	"-"   : lambda size : f"-{(size-1)*'-'}"
}


def table(
	data: dict[str, Iterable[Any]],
	Interpreter: dict[bool, str] = {True: '1', False: '0'},
	alignment:str = ":-:"
	) -> str:

	def T(E: Iterable[Any]) -> tuple[str, ...]:
		return tuple(Interpreter[e] for e in E)

	def unify(
			label:str, column:Iterable[str], cell:str = " {} "
		)-> Iterator[str]:

		SIZE = max(len(label), len(MOP2M[alignment]) ,*map(len, column))

		def f(C:str) -> str:
			return cell.format(f"{C:{MOP2P[alignment]}{SIZE}}")

		yield f(label)
		yield cell.format(formatted_separator[MOP2M[alignment]](SIZE))
		yield from map(f, column)

	def form_line(
		data: dict[str, Iterable[Any]] = {
				label: T(column) for label, column in data.items()
			}
		) -> Iterator[str]:

		Data = zip(*(unify(key, data[key]) for key in data))

		yield from (f"|{'|'.join(line)}|" for line in Data)

	return '\n'.join(form_line())

