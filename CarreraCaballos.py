import threading
import time
import random

#///
delay = 0.25
cant_caballos = 10
metros = 100
#///

flag = True

def caballo(num_cab):
    global flag
    pos = 0
    while (pos <= 100 and flag):
        print(f"caballo n°{num_cab} --> pos {pos}/{metros} \n")
        pos += random.randint(1,4)
        if(pos >= 100):
            print (f"\n El caballo n°{num_cab} ha ganado la carrera")
            flag = False
        time.sleep(delay)

def crearCaballos():
    listTemp = []
    for i in range(cant_caballos):
        listTemp.append(threading.Thread(target=caballo, args=(i,)))
    return listTemp

def empezarCarrera(caballos):
    for caballo in caballos:
        caballo.start()
        
caballos = crearCaballos()
empezarCarrera(caballos)