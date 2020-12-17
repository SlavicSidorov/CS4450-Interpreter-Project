import sys
import enum

class Type(enum.Enum):
    ASTERISK = 'Asterisk'
    SLASH = 'Slash'
    COLON = 'Colon'
    OPENPARENTHESIS = 'OpenParenthesis'
    CLOSEDPARENTHESIS = 'ClosedParenthesis'
    COMMA = 'Comma'
    PLUS = 'Plus'
    INDENTATION = 'Indentation'
    STRING = 'String'
    ENDOFFILE = 'EndOfFile'
    NEWLINE = 'NewLine'

