import sys
from Tokenize import *


def interpreter():

    print("PYTHON INTERPRETER VYACHESLAV SIDOROV...")

    if len(sys.argv) != 2:
        print("python3 interpreter.py <file to interpret>")
        sys.exit("USE CORRECT INPUTS")
        return

    print("Opening File...")
    fileName = sys.argv[1]
    with open (fileName, 'r') as file:
        inputFile = file.read()


    tokens = Tokenize(inputFile)
    print(str(tokens.getFileLength()) + " Characters in file...")
    print("Begin Tokenization...")
    tokens.initializeTokenizer()
    tokens.tokenize()
    token = tokens.token()

interpreter()