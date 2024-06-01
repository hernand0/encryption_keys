# Diego Hernando 2023
import random, string, secrets, time, hashlib, os

__absolute_path = os.path.dirname(os.path.abspath(__file__))
__filepass = __absolute_path + '/files/pass_python.sec'
__jaspass = __absolute_path + '/files/jas_pass.sec'
__jastemp = __absolute_path + '/files/jas_temp.sec'

def precio():
    __precio = random.randint(99,999)
    __precio += .95
    return str(__precio)

def clave():
    from rich import print
    global passw_str
    passw_str = ''
    passw = []
    print('\n\nGenerando clave...\n')
    progbar(16)
    print("  [italic green]Clave generada![/italic green]\n")
    t = 0
    while t < 4:
        f = open(__filepass, "a")
        for i in range(4):
            a = secrets.choice(string.ascii_letters)
            passw.append(a)
            f.write(a)
        if t == 3: break
        else: 
            f.write('-')
            passw.append('-')
        t += 1
    f.write('\n')
    f.close()
    passw_str = ''.join(passw)
    #print(str(a), end='')
    encrp()

def encrp():
    from rich import print
    f = open(__filepass, "r")
    r = open(__jaspass, "a")
    a = f.readlines()
    hash_object = hashlib.sha256()
    for line in a:
        pass
    hash_object.update(line.encode('utf-8'))
    hash_hex = hash_object.hexdigest()
    r.write(hash_hex)
    r.write('\n')
    r.close()
    print('\n\nEncriptando clave...\n')
    os.remove(__filepass)
    progbar(16)
    print('[italic green]Clave encriptada con éxito[/italic green]\n')
    print(f'\n[yellow]Tu clave es:[/yellow] {passw_str}')
    print("\nGuarda tu clave en un lugar seguro.\nIMPORTANTE: Esta clave está encriptada y sólo tú conoces esta clave.\nEn caso de pérdida no podemos recuperarla.\n")
    print('\n\ngenKey v2.0 ~ dH_2023\n')
    
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
        print()
        if clave == 'salir': 
            print('\nHas cancelado la validación. Hasta la vista!\n')
            break
        clave = clave + '\n'
        hash_object = hashlib.sha256()
        hash_object.update(clave.encode('utf-8'))
        hash_hex = hash_object.hexdigest()
        u = open(__jastemp, "a")
        u.write(hash_hex)
        u.write('\n')
        u.close()
        f = open(__jaspass, "r")
        u = open(__jastemp, "r")
        a = f.readlines()
        b = u.readlines()
        DF = [ x for x in a if x in b ]
        #print(DF)
        if len(DF) == 1:
            f.close()
            u.close()
            os.remove(__jastemp)
            progbar(16)
            print(' [italic green] Clave Correcta!\n\n Gracias por validar tu producto![/italic green]\n\n')
            print('\ngenKey v2.0 ~ dH_2023\n')
            break
        else: 
            progbar(16)
            print('[italic red]  Clave Error\n\nRevisa tu clave y vuelve a intentarlo.\n\n[/italic red]')
            f.close()
            u.close()

if __name__ == "__main__":
    print("GenKey v2.0 ~ dH_ '23")