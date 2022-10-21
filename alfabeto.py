# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário, 
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO ord(): Retorna o valor  ASCII de cada letra ou símbolo do teclado;
letra = input()
letra = letra.upper()
print(letra)
# TODO: De acordo com a entrada, imprima a posição dessa letra no Alfabeto;
#Dicionario com chave e valor
alfabeto ={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,
           'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,
           'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
#Pesquisa pela chave e encontra o valor
print(alfabeto[letra])
