"""
   Converting function from decimal to base b
"""

from functools import wraps
from typing import Callable
from collections import defaultdict

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

########################################
######### Whole Part Conversion #########
########################################

def as_integer(f:Callable[[int], str]) -> Callable[[str], str]:
   """
      Allows a function to accept number input as string
      Ignores integer inputs, because int(<int>) is still int
      Empty input will be interpreted as 0
   """
   @wraps(f)
   def wrapper(N:str) -> str:
      return f(int(N or "0"))
   return wrapper


def positive_input(f:Callable[[int], str]) -> Callable[[int], str]:
   """
      Wraps a function to ensure that only positive integer are used as an input argument
   """
   @wraps(f)
   def wrapper(n:int) -> str:
      return f(-n if n < 0 else n)
   return wrapper


def zero_output(f:Callable[[int], str]) -> Callable[[int], str]:
   """
      Interprets empty string output as "0"
   """
   @wraps(f)
   def wrapper(n:int) -> str:
      return f(n) or "0"
   return wrapper

Symbols:dict[int, str] = {
   i:c for i, c in enumerate("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
} | defaultdict(lambda: "_Out_Of_Range_Number_")

def to_base(
      base:int, Interpreter:dict[int, str] = Symbols
   ) -> Callable[[str], str]:
   """
      Returns a function that convert to base b
   """
   @as_integer
   @positive_input
   @zero_output
   def convert(n:int, base:int = base) -> str:
      n_b = ""
      while n:
         n, r = divmod(n, base)
         n_b = f"{Interpreter[r]}{n_b}"
      return n_b
   return convert

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

############################################
######### Rational Part Conversion #########
############################################

## Parse -> Otherwise split will fail!!

def parse_coma(f:Callable[[str], tuple[str,str]]) -> Callable[[str], tuple[str,str]]:
   """
      If there is no "," nothing will be replaced
   """
   @wraps(f)
   def wrapper(n:str) -> tuple[str,str]:
      return f(n.strip().replace(",", "."))
   return wrapper

def parse_only_rational(f:Callable[[str], tuple[str,str]]) -> Callable[[str], tuple[str,str]]:
   """
      Accepts ".3" as "0.3"
   """
   @wraps(f)
   def wrapper(n:str) -> tuple[str,str]:
      return f( f"0{n}" if n.startswith(".") else n)
   return wrapper

def parse_only_integer(f:Callable[[str], tuple[str,str]]) -> Callable[[str], tuple[str,str]]:
   """
      Accepts "2" as "2.0"
   """
   @wraps(f)
   def wrapper(n:str) -> tuple[str,str]:
      return f(f"{n}.0" if "." not in n else n)
   return wrapper

def parse_as_float(f:Callable[[str], tuple[str,str]]) -> Callable[[str], tuple[str,str]]:
   """
      Accepts "2." as "2.0"
   """
   @wraps(f)
   def wrapper(n:str) -> tuple[str,str]:
      return f(f"{n}0" if n.endswith(".") else n)
   return wrapper

def convert_rational(
      base:int, Interpreter:dict[int, str] = Symbols
   ) -> Callable[[str], tuple[str, str]]:
   """
      Returns a function that converts decimal numbers into base b
   """
   @parse_as_float
   @parse_only_integer
   @parse_only_rational
   @parse_coma
   def converter(number:str) -> tuple[str, str]:
      f"""
         Converts a number written in base 10 to base {base}
         # european commas will be tolerated
      """
      cycle:dict[str, str] = dict()

      hole_bits, n = number.split(".")

      rational_bits = ""

      while n not in cycle and int(n) != 0:
         D = f"{base*int(n):0>{(d := len(n))+1}}"
         m, n_ = Interpreter[int(D[:-d])], D[-d:]
         rational_bits += m
         cycle[n] = m
         n = n_

      index = P.index(n) if len(P := tuple(cycle.keys())) and n in P else len(cycle)

      period = ''.join(tuple(cycle.values())[index:])

      rational_bits = f".{rational_bits}" if len(rational_bits) else ''

      return f"{to_base(base)(hole_bits)}{rational_bits}", period

   return converter

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

