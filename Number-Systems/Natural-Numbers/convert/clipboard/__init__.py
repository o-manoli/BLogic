import platform
import importlib

from typing import Callable

source = f".{platform.system()}_SHIM" # too bad if your on BSD

lib = importlib.import_module(source, __package__)

clip: Callable[[str], str] = lib.clip
unclip: Callable[[], str] = lib.unclip
