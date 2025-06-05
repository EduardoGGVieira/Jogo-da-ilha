from time import sleep

def linha(lin="-",n=0):
    print(f"{lin}"*n)
    

def titulo(txt, lin="-" , n=0):
    linha(lin,n)
    print(f"{txt:^{n}}")
    linha(lin,n)


def paragrafo(txt,n=0.01):
    cont=0
    for i in txt:
        sleep(n)
        print(i, end='', flush=True)
        cont+=1
        if cont == 40:
            print()
            cont = 0
