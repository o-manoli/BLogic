"""
   TODO
"""

def process(number: str) -> str:
   sign = number[0]
   n_decimal = int(number[1:], 2)
   if sign == "0":
      return f"+{n_decimal}"
   return f"-{n_decimal}"

def loop():
   while (In := input("Input a number in binary: ")):
      print(f"{In} formatted as signed magnitude binary: {process(In)}")

if __name__ == "__main__":
   loop()

