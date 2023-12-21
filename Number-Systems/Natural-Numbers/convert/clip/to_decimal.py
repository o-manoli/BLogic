from ..clipboard import clip
from ..to_decimal import callback, main
from typing import Callable

def wraps(
      f: Callable[[str, int], int]
   ) ->Callable[[str, int], int]:
   def wrapper(x:str, b:int) -> int:
      clip(f"{(r := f(x, b))}")
      return r
   return wrapper

if __name__ == '__main__':
   main(wraps(callback))
