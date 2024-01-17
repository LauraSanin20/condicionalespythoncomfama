# Toda lista se debe escribir en PLURAL
# Solo se pueden almacenar del mismo tipo de dato
arboles=['ceiba','yarumo','manzano','guayacan']
municipios=["Medellin","Titiribi","Carolina del principe"]
hectareasSembradas=[2500,500,1200]
lluviasMayoresA500=[False, True, True]

# Recorriendo un arreglo...
# Acceder de forma dinamica al contenido de un arreglo
# Para recorrerlo debo utilizar un ciclo o bucle o loop

# Ciclo while (mientras)
'''
contador=0
while contador < 10 :
    contador=contador+1
    print("estoy triunfando...")
'''

# Ciclo For (Para)
'''
for variableiteradora in range(1,301,2):
    print(variableiteradora)
'''

# Recorrer dinamicamente un arreglo usando un FOR EACH (PARA CADA UNO)

for arbol in arboles:
    print(arbol)

for municipio in municipios:
    print(municipio)
