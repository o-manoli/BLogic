"""
	Boolean Logic Library
"""

# from . import vectorized
#
# InputSpace = vectorized.logicBaseVectorGenerator

from . import objectify
from . import mapped
from . import markdown
from . import represent

P = represent.P
Sep = represent.Sep
Sectors = represent.Sectors

InputSpace = objectify.InputSpace
karnaugh_matrix = mapped.karnaugh_matrix
table = markdown.table

