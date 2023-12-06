"""Curso Métodos Númericos, Bisección
programado por Henry B.R"""
import math

def bisection(x1, x2,iterations,decimales):
    x = round((x1+x2)/2,decimales)
    intervalos = [x1,x,x2]
    print(intervalos)
    resultado = []
    for i in range(iterations):
        for i in intervalos:
            y = math.e**(-i)+math.sin(i)
            resultado.append(y)
            
        if resultado[0]*resultado[1] > 0:
            x1 = round(x,decimales)
            x = round((x1+x2)/2,decimales)
            intervalos = [x1,x,x2]
            
        elif resultado[0]*resultado[1] < 0:
            x2 = round(x,decimales)
            x = round((x1+x2)/2,decimales)
            intervalos = [x1,x,x2]
        resultado = []
        print(intervalos)
    
def get_interval():
    x1 = float(input("Ingresa el extremo izquierdo del intervalo: "))
    x2 = float(input("Ingresa el extremo derecho del intervalo: "))
    return x1, x2

if __name__ == "__main__":
    x1, x2 = get_interval()
    #user_function = input("Ingresa la función a evaluar (en términos de 'x'): ")
    bisection_result = bisection(x1, x2, 16,10 )

    


    






