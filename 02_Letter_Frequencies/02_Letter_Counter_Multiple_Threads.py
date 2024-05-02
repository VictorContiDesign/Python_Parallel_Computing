import json
from urllib.request import Request, urlopen
import time
from threading import Thread

finished_count = 0

def count_letters(url, lc_frequency):
    response = urlopen(url).read()
    txt = str(response)
    for l in txt:
        letter = l.lower()
        if letter in lc_frequency:
            lc_frequency[letter] += 1
    global finished_count
    finished_count += 1
            
def main():
    # Construcción del diccionario
    frequency = {}
    for c in "abcdefghijklmnopqrstuvwxyz":
        frequency[c] = 0
    
    # Captura de tiempo de inicio de proceso
    start = time.time()
    
    # Inicialización de variables
    i = 1000
    req = Request(
        url=f"https://www.rfc-editor.org/rfc/rfc{i}.txt", 
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    
    # Ejecución de bucle de escaneo de webs para lectura
    for i in range(1000, 1020):
        Thread(target=count_letters, args=(req, frequency)).start()
        
    while finished_count < 20:
        time.sleep(0.5)
    # Captura de tiempo de final de proceso    
    end = time.time()
    
    # Impresión del diccionario con abecedario
    result = json.dumps(frequency, indent=4)
    print(result)
    
    # Impresión del tiempo total del proceso
    print("Done, time taken : ", end - start)
    
main()