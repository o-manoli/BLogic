

def to_base(
      x: int, base: int,
      symbols: str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
   ) -> str:
   if x == 0: return ""    # will fail if x is 0 and not the last recursive call!!!
   x, r = divmod(x, base)
   return to_base(x, base) + symbols[r]

print(to_base(3735890861, 16))
