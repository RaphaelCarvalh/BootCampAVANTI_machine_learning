def numeros_impares(lista):
    """Retorna uma lista contendo apenas os números ímpares."""
    impares = [num for num in lista if num % 2 != 0]
    return impares


result = (numeros_impares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(result)  # Saída esperada: [1, 3, 5, 7, 9]