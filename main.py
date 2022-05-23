from carat_lexer import Lexer
from carat_parser import Parser

text_input = """
program Carat;

var int miVar1, miVar2, miVar3, miMatriz[2][3];
var float resultado;

int func fact(int miVar2) {
	var int miVar1;
    miVar1 = miVar2 + (miVar3 - miVar2 * 2 + miVar2);
    if(miVar2 == 1){
        print(miVar1);
    }else{
        print(miVar2);
    }
    return(miVar * fact(miVar2-1););
}

void func pinta(int y) {
	var int x;
	x = 1;
    penDown();
	while(x < 11) do {
		circle(y + x*5);
		penColor(x + 10, x + 15, 244);
		penSize(10 - x);
		x = x + 1;
    }
    penUp();
}

main () {
	input(miVar3);
    miVar2 = miVar3 * 2;
    miMatriz = {{1,2,3},{4,5,6}};
    point(0,0);
    miVar1 = fact(miVar3);
    for miVar1 = 0 to 5 do {
        pinta(miVar1 * miVar2);
        print(miVar1);
    }
    circle(2);
    clear();
    print("Fin de mi programa");
}
"""

text_input2 = """
program Carat;

var int miVar1, miVar2, miVar3;
var float miVar4;

main () {
    miVar2 = 2;
    miVar3 = miVar4;
}
"""

text_input3 = """
program Carat;

var int miVar1, miVar2, miVar3;

main () {
    miVar1 = 1 + 2 * (3 - 2 / 1) * 4;
    miVar2 = 2 - 1;
    while(miVar2 * 2 - 1 == 2 * 1 / (2+3)) do {
        miVar2 = 1 * 2 +1;
        if(3 < 3){
            miVar3 = 2 + 2;
            while(miVar3 > 1 + 2) do {
                print(1 + 2 * 4, 5-1);
                miVar3 = 3 - 1;
            }
        }else{
            while(4 > 2) do {
                miVar1 = 2 + 2;
                print(2 - 3);
            }
        }
    }
    miVar3 = 1 + 1;
}
"""

text_input4 = """
program Carat;

var int miVar1, miVar2, miVar3;

void func pinta(int y) {
    var int x;
    x = 1.5 + 1 * (2 - 1);
    y = 1 + 2;
    for miVar1 = 1 to 5 do {
        print("holis");
    }
}

main () {
    print("Adios");
}
"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input4)

pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens)
print("EXITO")

#miVar1 = 1 + 2 * 3 * 4 + 5 / 6 * 7;