"""
   Windows specific Clipping Callbacks
"""

import subprocess

# most-likely be machine specific
# could be dynamically bound *if I know how
READ_ENCODING = "CP850"       #keyboard-specific #hardwired
WRITE_ENCODING = "UTF-16LE"

#WORKED-ON-MY_MACHINE :)

def system_call(*CMDs:str) -> str:
   return subprocess.run(
      CMDs, capture_output=True, text=True, encoding=READ_ENCODING
   ).stdout

def powershell(*CMDs:str) -> str:
   return system_call("PowerShell", "-Command", *CMDs)

def unclip() -> str:
   """
      reads from clip board
   """
   return powershell("Get-Clipboard")

def clip(S:str) -> str:
   """
      writes to clipboard
   """
   subprocess.run(["CLIP"], input=S.encode(WRITE_ENCODING))
   return S # pass-throw
