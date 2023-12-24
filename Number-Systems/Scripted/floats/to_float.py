"""
   Usage in command line:
      - As one time function
         `py ./to_float.py [base] [rational number in decimal]`
      - In a loop
         `py ./to_float.py`
            Input a base and a number: [base] [number]
            *Separated with a space *or-many *or-even-a-tab

   Or as imported module:

      - Use `convert_rational` e. g. `convert_rational(base=2)("0.03")`
      - Or `show_convert_rational(16)("172.859375")`

"""

from typing import Callable, Iterator
from functools import wraps, partial

def as_integer(f:Callable[[int], str]) -> Callable[[str], str]:
   @wraps(f)
   def wrapper(N:str) -> str:
      return f(int(N))
   return wrapper

def positive_input(f:Callable[[int], str]) -> Callable[[int], str]:
   @wraps(f)
   def wrapper(n:int) -> str:
      return f(-n if n < 0 else n)
   return wrapper

def zero_output(f:Callable[[int], str]) -> Callable[[int], str]:
   @wraps(f)
   def wrapper(n:int):
      return f(n) or "0"
   return wrapper

def parse_comma(f:Callable[[str], str]) -> Callable[[str], str]:
   """
      Replaces nothing if the input doesn't have a `,`
   """
   @wraps(f)
   def wrapper(S:str) -> str:
      return f(S.replace(",", '.'))
   return wrapper


Symbols:dict[int, str] = {
   i:c for i, c in enumerate("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
}

def interpret_number(Interpreter:dict[int, str] = Symbols):
   def decorator(
         f:Callable[[int, str], Iterator[int]]
      ) -> Callable[[int, str], Iterator[str]]:
      @wraps(f)
      def wrapper(b:int, n:str) -> Iterator[str]:
         yield from (Interpreter[n] for n in f(b, n))
      return wrapper
   return decorator


def to_base(
      base:int, Interpreter:dict[int, str] = Symbols
   ) -> Callable[[str], str]:
   @as_integer
   @zero_output
   @positive_input
   def convert(n:int, base:int = base) -> str:
      n_b = ""
      while n:
         n, r = divmod(n, base)
         n_b = f"{Interpreter[r]}{n_b}"
      return n_b
   return convert


def left_overflow(base:int, r:str) -> tuple[int, str]:
   n = f"{base*int(r):0>{len(r)+1}}" # initlize carry over bit,
   digits = len(n) - len(r)
   return int(n[:digits]), n[digits:]


def sequenced_rational(base:int, number:str) -> Iterator[tuple[int, str]]:
   f = partial(left_overflow, base)
   cycle:dict[str, bool] = dict()
   n = number.split('.')[-1]
   while n not in cycle and int(n) != 0:
      cycle[n] = True
      m, n = f(n)
      yield m, n

@interpret_number()
def rational_sequence(base:int, number: str) -> Iterator[int]:
   yield from tuple(s for s, _ in sequenced_rational(base, number))


def convert_rational(base:int) -> Callable[[str], str]:
   @parse_comma
   def converter(number: str) -> str:
      """
         Converts a decimal rational number in base b.

         Example:
            convert_rational(2, "0.3") -> "0.01001"

         The result will truncate the periodic part of the number

         Also parses `,` into `.`
      """
      hole, decimal = number.split('.')
      return f"{to_base(base)(hole)}.{''.join(rational_sequence(base, decimal))}"
   return converter


def show_convert_rational(base:int) -> Callable[[str], str]:
   @parse_comma
   def converter(number: str) -> str:
      """
         Also parses `,` into `.`
      """

      print(f"\n\n\tInput: {number}\n\n")

      hole, decimal = number.split('.')

      CELL_WIDTH = len(number)
      n = int(hole)

      while n:
         n_, r = divmod(n, base)
         print(f"{n:>{CELL_WIDTH}} / {base} = {r}")
         n = n_

      print(f"{n:>{CELL_WIDTH}} / {base} = 0")

      print(f"\n\tHole Part Conversion: ({hole})_10 = ({to_base(base)(hole or '0')})_{base} \n")


      print("\n\tDecimal Part Conversion:\n")

      num = f"0.{decimal}"

      for m, n in sequenced_rational(base, f"0.{decimal}"):
         print(f"{num} x {base} = ", (num := f"{m}.{n}"), f" -> {m}")

      print(f"\n\n\t({number})_10 = ({(ans := convert_rational(base)(number))})_{base}\n\n")

      return ans
   return converter



# - - - - - - - - - - - - - - - - - - - - - - - -

############################
########### MAIN ###########
############################


def main(base:int, number:str):
   hole, decimal = number.replace(',', ".").split('.')
   print(
      f"({to_base(base)(hole)}.{''.join(rational_sequence(base, decimal))})_{base}"
   )

def loop():
   while (In := input("Input a base and a number: ")):
      base, number = In.split()
      main(int(base), number)

if __name__ == '__main__':

   import sys

   if len(sys.argv) == 1:
      loop()
      exit()

   if "-h" or "--help" in sys.argv:
      print(__doc__)
      exit()

   if len(sys.argv) != 3:
      print(__doc__)
      raise ValueError(f"\n\t{sys.argv} is no good\n\n")

   main(int(sys.argv[1]), sys.argv[2])

