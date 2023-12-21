"""
   Linux clipboard shim

   TODO #NOT-Implemented

   Try to look into a cli tool the can read writes to system clipboard.
   Like perhaps `xsel`, `xclip` ...

   PowerShell also available on some Linux-Distro.
   I believe The `Get-Commands` relies on `xclip` so that could works too.

   On WSL you should be able to call PowerShell from the Windows host from the sub system and so gain access to `Get-Clipboard` and `Set-Clipboard` commands.
   But why would you run this on WSL when you already have windows

"""

def unclip() -> str:
   """
      NOt implemented.
      Will just be ignored
   """
   return ""

def clip(S:str):
   """
      NOt implemented.
      Will just be ignored
   """
   return ""

