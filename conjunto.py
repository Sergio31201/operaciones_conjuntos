import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn3
"""
Operaciones entre dos o más conjuntos
o Unión
o Intersección
o Diferencia
o Complemento.
o Combinación entre ellos

"""
# Definimos los conjuntos
conjunto1 = {1, 2, 3, 4}
conjunto2 = {2, 9, 8, 0}
conjunto3 = {2, 9, 8, 6, 0}

# Diagrama de Venn para el conjunto 2 y conjunto 3
venn2([conjunto2, conjunto3], set_labels=('Conjunto2', 'Conjunto3'))
plt.show()

# Operación de Unión
union = set()
for elemento in conjunto1:
    union.add(elemento)
for elemento in conjunto2:
    union.add(elemento)
print("Unión:", union)

# Operación de Intersección
interseccion = set()
for elemento in conjunto1:
    if elemento in conjunto2:
        interseccion.add(elemento)
print("Intersección:", interseccion)

# Operación de Diferencia
diferencia = set()
for elemento in conjunto1:
    if elemento not in conjunto2:
        diferencia.add(elemento)
print("Diferencia (conjunto 1 - conjunto 2):", diferencia)

# Operación de Complemento
complemento = set()
for elemento in conjunto3:
    if elemento not in conjunto2:
        complemento.add(elemento)
print("Complemento (conjunto 3 - conjunto 2):", complemento)

# Operación de Combinación
combinacion = set()
for elemento in conjunto1:
    combinacion.add(elemento)
for elemento in conjunto2:
    combinacion.add(elemento)
for elemento in conjunto3:
    combinacion.add(elemento)
print("Combinación:", combinacion)

# Cardinalidad
cardinalidad_conjunto3 = sum(1 for _ in conjunto3)
print("Cardinalidad del Conjunto 3:", cardinalidad_conjunto3)

# Subconjunto
subconjunto = all(elemento in conjunto3 for elemento in conjunto2)
print("¿Conjunto 2 es subconjunto de Conjunto 3?:", subconjunto)

# Disjuntos
disjuntos = not any(elemento in conjunto2 for elemento in conjunto1)
print("¿Conjunto 1 y Conjunto 2 son disjuntos?:", disjuntos)

