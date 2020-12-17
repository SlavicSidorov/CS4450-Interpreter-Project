import enum
import sys
from Token import *


class Tokenize:

# TOKENIZER CLASS INITIALIZATIONS 
    def __init__(self, inputFile):
        self.fileLength = 0
        self.inputFile = inputFile

    def getFileLength(self): # GET FILE LENGTH FOR PARSER
        self.fileLength = len(self.inputFile)
        return self.fileLength

    def initializeTokenizer(self): # SET INDEX TO BEFORE ARRAY START ( although in python apparently this is the last element, whoops, but doesn't matter.)
        self.index = -1
        self.indexValue = None

    def comment(self):
        if (self.indexValue == '#'):
            while (self.indexValue != '\n' and self.peek() != '\0'):
                self.tokenize()
    
    def emptySpace(self):
        while (self.indexValue == ' '):
           self.tokenize()

    def emptyReturnChar(self):
        while (self.indexValue == '\r'):
            self.tokenize()

    def emptyTab(self):
        while (self.indexValue == '\t'):
            self.tokenize()

    def tokenize(self):
        self.index += 1

        if (self.peek() != '\0'): # IF NOT END OF FILE
            self.indexValue = self.inputFile[self.index]
        else:
            return '\0'

    def peek(self): # PEEK NEXT CHARACTER TO CHECK FOR FILEEND AND OPERATORS
        if (self.index + 1 >= self.fileLength):
            return '\0' # IF REACHED END OF FILE RETURN END OF FILE CHARACTER
        else:
            return self.inputFile[self.index + 1]

    def token(self):
        
        self.emptyReturnChar()
        self.emptyTab()
        self.emptySpace()
        self.comment()

# SIMPLE VALUES WITH NO FOLLOWING CHARACTER
        if (self.indexValue == '\n'):
            value = Token(self.indexValue, Type.NEWLINE)
            
        if (self.indexValue == '('):
            value = Token(self.indexValue, Type.OPENPARENTHESIS)

        if (self.indexValue == ')'):
            value = Token(self.indexValue, Type.CLOSEDPARENTHESIS)

        if (self.indexValue == '*'):
            value = Token(self.indexValue, Type.ASTERISK)

        if (self.indexValue == '\0'):
            value = Token(self.indexValue, Type.ENDOFFILE)

        if (self.indexValue == '/'):
            value = Token(self.indexValue, Type.SLASH)

        if (self.indexValue == ':'):
            value = Token(self.indexValue, Type.COLON)
# Parenthesis and other in function paramater type strings

        if (self.indexValue == ','):
            token = Token(self.indexValue, Type.COMMA)


        self.tokenize()
        return value