"""
   Convert a decimal rational number into base b rational

   Usage in command line:
      - As one time function
         `py ./to_float.py [base] [rational number in decimal]`
      - In a loop
         `py ./to_float.py`
            Input a base and a number: [base] [number]
            *Separated with a space *or-many *or-even-a-tab

   Or as imported module:

      - Use `convert_rational` e. g. `convert_rational(base=2)("0.03")`

"""


from .to_rational import convert_rational

# - - - - - - - - - - - - - - - - - - - - - - - -
############################
########### MAIN ###########
############################


def main(base:str, number:str):
   n, period = convert_rational(int(base))(number)
   print(
      f"({number})_10 is ({n})_{base}",
      "" if not len(period) else f"with Period of: {period}"
   )


def loop():
   while (In := input("Input a base and a number: ")):
      base, number = In.split()
      main(base, number)

if __name__ == '__main__':

   import sys

   if len(sys.argv) == 1:
      loop()
      exit()

   if any(
      C in sys.argv for C in ["-h", "--help"]
   ):
      print(__doc__)
      exit()

   if len(sys.argv) != 3:
      print(__doc__)
      raise ValueError(f"\n\t{sys.argv} is no good\n\n")

   main(sys.argv[1], sys.argv[2])

