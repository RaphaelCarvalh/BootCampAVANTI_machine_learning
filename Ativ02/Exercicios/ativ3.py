def elementos_unicos(lista1, lista2):
    """
    Retorna uma lista com os elementos que estão presentes
    em apenas uma das listas.
    """
    set1 = set(lista1)
    set2 = set(lista2)
    
    elementos_exclusivos = list(set1.symmetric_difference(set2))
    return elementos_exclusivos

result = elementos_unicos([1, 2, 3, 4], [3, 4, 5, 6])
print(result)  # Saída esperada: [1, 2, 5, 6]