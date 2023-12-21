from ..clipboard import clip
from ..to_base import callback, main
from typing import Callable

def wraps(
      f: Callable[[int, int], str]
   ) ->Callable[[int, int], str]:
   def wrapper(x:int, b:int) -> str:
      return clip(f(x, b))
   return wrapper

if __name__ == '__main__':
   main(wraps(callback))

