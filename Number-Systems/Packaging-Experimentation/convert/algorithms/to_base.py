
def to_base(
      x: int, base: int,
      symbols: str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
   ) -> str:

   ans = ""

   while x:
      x, r = divmod(x, base)
      ans = symbols[r] + ans

   return ans if ans else "0"

