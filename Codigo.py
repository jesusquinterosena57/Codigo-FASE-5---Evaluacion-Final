Sesion_clientes = [
    ["Cliente 101", 180, 15],
    ["Cliente 102", 8, 2],
    ["Cliente 103", 10, 5],
    ["Cliente 104", 5, 1],
    ["Cliente 105", 90, 7],
]


def calcular_compromiso (duracion, clicks):

    if duracion >=180 and clicks >= 8 :
        return "Alto"
    elif duracion <=60 and clicks <= 3:
        return "bajo"
    else :
        return "Medio"
    

def Generar_Informe (matriz_clientes):

    print("-" * 50)
    print("Informe de Compromiso de Clientes") 
    print("-" * 50)

    for cliente in matriz_clientes:
        nombre, duracion, clicks = cliente
        compromiso = calcular_compromiso(duracion, clicks)
        print(f"{nombre}: Duración {duracion} seg, Clicks {clicks}, Compromiso: {compromiso}")



print("-" * 50)


if __name__ == "__main__":
    Generar_Informe(Sesion_clientes)