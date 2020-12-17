import sys
import enum
from Type import *

class Token:   
    def __init__(self, value, tokenType):
        self.value = value
        self.type = tokenType