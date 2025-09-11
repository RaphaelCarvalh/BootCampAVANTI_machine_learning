def eh_primo(n):
    """Verifica se um número é primo."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def numeros_primos(lista):
    """Retorna uma lista com os números primos presentes."""
    primos = [num for num in lista if eh_primo(num)]
    return primos


result = numeros_primos([10, 15, 3, 7, 8, 23, 42, 17])
print(result)  # Saída esperada: [3, 7, 23, 17]

