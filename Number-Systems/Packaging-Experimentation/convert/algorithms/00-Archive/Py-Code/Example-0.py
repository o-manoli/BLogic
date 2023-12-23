number: int = 4276993775
base: int = 16  # target base

# extend the 0..9 "symbols" used in base 10
symbols: str = "0123456789ABCDEF"

n_b = ""  # the number represented in base b

while number != 0:
   number, r = divmod(number, base) # divide and returns the rest as well
   n_b = symbols[r] + n_b # append at start!

else :  # while is false
   if not n_b: n_b = "0"  # when number is 0

print(f"{{{n_b}}}_{base}")
