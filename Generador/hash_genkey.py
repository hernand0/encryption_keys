#!/usr/bin/env python3 
#/// Diego Hernando 2023 - KeyGenerator con hashing
from rich import print
from genclave.generador_jas import precio, clave, valid

print('\n[italic yellow]genKey v2.0 ~ dH_2023[/italic yellow]')
print('[italic yellow]Gracias por usar nuestro Generador y Validador de Claves seguro -[/ italic yellow]\n')
p = True
while p:
    print('\nIntroduce 0 para adquirir una clave o 1 para validar si ya tienes una:')
    a = input()
    if a == '0':
        print('\n- Has elegido Adquirir Clave -\n')
        print(f"El precio es de: {precio()} €")
        print('\n\n- Pulsa [italic green]ENTER[/italic green] para Aceptar -\n- Pulsa [italic red]C + ENTER[/italic red] para salir -\n')
        b = input()
        if b == '':
            clave()
            p = False
        elif b.lower() == 'c':
            print('\nHasta la vista, baby!\n')
            p = False            
        else:
            print('\nComando no válido: [italic green]Enter[/italic green] (Seguir) o [red italic]C + ENTER[red italic] (Cancelar)\nReseteando...\n')
    elif a == '1':
        print('\n- Has elegido Validar Clave- \n')
        valid()
        p = False
    else: print('\n- 0 para generar o 1 para validar -\n')