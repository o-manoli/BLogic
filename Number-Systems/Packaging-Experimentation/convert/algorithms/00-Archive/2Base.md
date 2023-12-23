# Converting from Decimals

## Py-Code

### Tried:

#### V-0

```python
def to_base(
      x: int, base: int,
      symbols: str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
   ) -> str:

   ans = ""

   while x:
      x, m = divmod(x, base)
      ans += symbols[m]

   return ans[::-1]
```

### Scripted:

#### [Example-0](./Py-Code/Example-0.py)

[HEX-SPeak](https://en.wikipedia.org/wiki/Hexspeak)

```python
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
```

#### [Recursive-Callback](./Py-Code/Recursive_Example-0.py)

```python
def to_base(
      x: int, base: int,
      symbols: str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
   ) -> str:
   if x == 0: return ""    # will fail if x is 0 and not the last recursive call!!!
   x, r = divmod(x, base)
   return to_base(x, base) + symbols[r]

print(to_base(3735890861, 16))
```