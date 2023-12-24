"""
   Library Code to convert to binary
"""

from functools import wraps

from typing import Callable

def loop(process:Callable[[str], str], Result:str):
   while (In := input("Input a number: ")):
      # either there is:
      #     Nothing to process
      #     The user pressed Crt + C
      #     Something went terribly wrong and the python interpreters crashed
      # this loop will be broken!
      print(Result.format(In, process(In)))


def to_binary(n:int) -> str:
   n_b = ""
   n = -n if n < 0 else n # denies the existents of negative numbers!
   # otherwise infinite loop
   #     cause `-1 // 2` is always `-1` and never `False`
   while n:
      n, r = divmod(n, 2)
      n_b = f"{r}" + n_b
   return n_b if n_b else "0" # was already 0


def fixed(WIDTH:int) -> Callable[[Callable[[int], str]], Callable[[int], str]]:
   def decorator(callback:Callable[[int], str]) -> Callable[[int], str]:
      @wraps(callback)
      def wrapper(n:int) -> str:
         return f"{callback(n):0>{WIDTH}}"[:WIDTH]
      return wrapper
   return decorator


def as_int(f: Callable[[int], str]) -> Callable[[str], str]:
   @wraps(f)
   def wrapper(n: str) -> str:
      return f(int(n))
   return wrapper

def integer_feeder(
      f:Callable[[int], Callable[[int], str]]
   ) -> Callable[[int], Callable[[str], str]]:
   @wraps(f)
   def wrapper(n: int) -> Callable[[str], str]:
      return as_int(f(n))
   return wrapper

def main(n: int) -> str:
   print(r := to_binary(n))
   return r

if __name__ == "__main__":
   import sys
   if len(sys.argv) < 2:
      print(__doc__)
      exit()
   main(int(sys.argv[-1]))

