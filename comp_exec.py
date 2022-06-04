from carat_lexer import Lexer
from carat_parser import Parser
from virtual_machine.vm import vm
from pathlib import Path

text_input4 = """
program Carat; 

var int miVar1, miVar2, miVar3;
var float miFloat;

void func Pinta(int y, int x) {
    if(y > 4){
        (Pinta(y - x, x + 1);)
        print(y);
    }
}

main () {
    (Pinta(2 + 5, 2);)
}
"""

text_input8 = """
program Carat; 

var int miVar1, miVar2, miVar3;
var float miFloat;

int func fib(int x) {
    if(x < 2){
        return(x);
    }
    return((fib(x-1);) + (fib(x-2);));
}

main () {
    print((fib(9);));
}
"""

text_input3 = """
program Carat; 

var int miVar1, miVar2, miVar3;
var float miFloat;

main () {
    print("Ingrese un numero: ");
    input(miFloat);
    if(miFloat > 5){
        print("Var1 mayor que 5");
    }else{
        print("Var1 menor que 5");
    }
    miVar1 = 1;
    while(miVar1 < 5) do {
        print(miVar1);
        miVar1 = miVar1 + 1;
    }
}
"""

text_input5 = """
program Carat; 

var int miVar1;

main () {
    for miVar1 = 1 to 5 do {
        print("holis");
    }
}
"""

text_input9 = """
program Carat; 

var int miVar1;

int func fib(int x) {
    if(x < 2){
        return(x);
    }
    return((fib(x-1);) + (fib(x-2);));
}

main () {
    miVar1 = 3 + 4 * 2;

    lineUp(300);
    clear();
    lineDown(200);
    penUp();
    lineRt(45, 100);
    penDown();
    lineLf(75, 50);
    penSize(20 - 5);
    lineDown(400);
    penSize(20- 10);
    circle(miVar1);

    miVar1 = (fib(6););

    penSize(miVar1);
    arc(30, 120);

    penColor(255, 192, 203);

    point(5, 10);
}
"""

def compExec():
    lexer = Lexer().get_lexer()
    tokens = lexer.lex(text_input9)
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