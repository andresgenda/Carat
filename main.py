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
	while(x < 11) do {
		Circle(y + x*5);
		Color(x + 10);
		Size(10 - x);
		x = x + 1;
    }
}

main () {
	input(miVar3);
    miVar2 = miVar3 * 2;
    miMatriz = {{1,2,3},{4,5,6}};
    Point(0,0);
    miVar1 = fact(miVar3);
    for miVar1 = 0 to 5 do {
        pinta(miVar1 * miVar2);
        print(miVar1);
    }
    print("Fin de mi programa");
}
"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()
print("EXITO")