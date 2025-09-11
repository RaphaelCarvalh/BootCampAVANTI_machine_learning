def ordenar_por_nome(pessoas):
    """
    Recebe uma lista de tuplas (nome, idade) e retorna a lista
    ordenada pelo nome em ordem alfabética.
    """
    pessoas_ordenadas = sorted(pessoas, key=lambda pessoa: pessoa[0])
    return pessoas_ordenadas

result = ordenar_por_nome([("Carlos", 25), ("Ana", 30), ("Bruno", 20)])
print(result)  # Saída esperada: [('Ana', 30), ('Bruno', 20), ('Carlos', 25)]