from carat_lexer import Lexer
from carat_parser import Parser
from virtual_machine.vm import vm
from pathlib import Path

def openFile():
    testPath = Path("testFiles/")
    print('Ingrese el nombre de la prueba: ')
    prueba = input()
    testName = open(str(testPath/prueba), "r")
    openTest = testName.read()
    return openTest


def compExec():
    runTest = openFile()
    lexer = Lexer().get_lexer()
    tokens = lexer.lex(runTest)
    pg = Parser()
    pg.parse()
    parser = pg.get_parser()
    try:
        parser.parse(tokens)
        return True
    except Exception as ex:
        print("COMPILING ERROR", ex)
        return False

def main():
    if compExec():
        vMach = vm()
        vMach.execute()

main()