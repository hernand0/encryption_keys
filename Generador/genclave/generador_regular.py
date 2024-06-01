# Diego Hernando 2023

import random, string, secrets, time, os

__absolute_path = os.path.dirname(os.path.abspath(__file__))
__filepass = __absolute_path + '/files/pass_python.sec'
precio = random.randint(99,999)
precio += .95

def clave():
    from rich import print
    print('\n\nGenerando clave...\n')
    progbar(16)
    print("  [italic green]Clave generada![/italic green]\n")
    print("\n\n[yellow]Tu clave es:[/yellow]", end=' ')
    t = 0
    while t < 4:
        f = open(__filepass, "a")
        for i in range(4):
            a = secrets.choice(string.ascii_letters)
            print(a, end='')
            f.write(a)
        if t == 3: break
        else: 
            f.write('-')
            print('-', end='')
        t += 1
    f.write('\n')
    f.close()
    print('\n\nGracias! Hasta la vista!\n')
    
def progbar(x):
    characters = ['-', '\\', '|', '/']
    for i in range(x + 1):
        frame = i % len(characters)
        print(f'\r[{characters[frame]*i:=<{x}}]', end='  ')
        time.sleep(0.15)

def valid():
    from rich import print
    while True:
        clave = input('Introduce clave o escribe "salir": ')
        if clave == 'salir': 
            print('\nHas cancelado la validación. Hasta la vista!\n')
            break
        clave = clave + '\n'
        f = open(__filepass, "r")
        a = f.readlines()
        if clave in a:
            f.close()
            print()
            progbar(16)
            print(' [italic green] Clave Correcta!\n\n Gracias por validar tu producto![/italic green]\n\n')
            break
        else: 
            progbar(16)
            print('[italic red]  Clave Error\n\nRevisa tu clave y vuelve a intentarlo.\n\n[/italic red]')
            f.close()