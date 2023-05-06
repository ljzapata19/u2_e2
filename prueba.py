
def operacion(argumento):
    switcher = {
        0: "zero",
        1: "one",
        2: "two",
    }
 
    return switcher.get(argumento, "la opcion es incorrecta")
 
# Driver program
def MenudeOpciones():
    print('Seleccione la opcion: ')
    print('a- Consultar Cantidad de Millas.')
    print("b- Acumular Millas")
    print("c- Canjear Millas.")
    argumento=int(input('Ingrese la opcion: '))
    
    print (operacion(argumento))

if __name__ == '__main__':
    MenudeOpciones()
    
