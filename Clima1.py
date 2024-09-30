import requests
api_key="bdf79b2f2d5637450827abd057f7c1d1"

def menu() : 
    while True:
        print("Seleccione una opcion")
        print("1)temperatura")
        opcion=input()
        if opcion== "1":
            opcion1()
        elif opcion!= "0":
            break            
def opcion1():
    print("Ingrese su ciudad")
    ciudad=input()
    Urlciudad=f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric"
    info=requests.get(Urlciudad)
    infojson=info.json()
    temp = infojson["main"]["temp"]
    min = infojson["main"]["temp_min"]
    max = infojson["main"]["temp_max"]


    print(f"la temperatura en {ciudad} es de {temp}")
    print(f"la temperatura minima es de {min}")
    print(f"la temperatura maxima es de {max}")

menu()   