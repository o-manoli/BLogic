"""
   TODO
"""

from typing import Callable

def process(number: str) -> str:
   sign = number[0]
   n = int(number[1:], 2)
   if sign == "0":
      return f"{n}"
   return f"{n - 2**(len(number)-1)}"

def one_liner(n:str) -> str:
   return f"{int(n[1:], 2) - (n[0] == '1') * 2**(len(n)-1)}"


def loop(process:Callable[[str], str] = process):
   while (In := input("Input a number in binary: ")):
      print(f"{In} formatted as two's complement binary: {process(In)}")

if __name__ == "__main__":
   loop()

