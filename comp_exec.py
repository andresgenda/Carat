from carat_lexer import Lexer
from carat_parser import Parser
from virtual_machine.vm import vm
from pathlib import Path

text_input4 = """
program Carat; 

var int miVar1, miVar2, miVar3;
var float miFloat;

void func Pinta(int y, int z) {
    var int x;
    x = 1.5 + 1 * (2 - 1);
    y = 1 + 8;
    for miVar1 = 1 to 5 do {
        print("holis");
    }
}

main () {
    input(miVar3);
    print("Main");
    miVar2 = 1 + 1;
    Pinta(2 + 2, 4);
}
"""

text_input3 = """
program Carat; 

var int miVar1, miVar2, miVar3;
var float miFloat;

main () {
    input(miFloat);
    if(miFloat > 5){
        print("Var1 mayor que 1");
    }else{
        print("Var1 menor que 1");
    }
    miVar1 = 1;
    while(miVar1 < 5) do {
        print(miVar1);
        miVar1 = miVar1 + 1;
    }
}
"""

def compExec():
    lexer = Lexer().get_lexer()
    tokens = lexer.lex(text_input3)
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