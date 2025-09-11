def segundo_maior(lista):
    """Encontra o segundo maior valor em uma lista de números inteiros."""
    if len(lista) < 2:
        return "A lista deve ter pelo menos dois elementos."
    
    lista_sem_duplicatas = sorted(list(set(lista)), reverse=False)
    
    if len(lista_sem_duplicatas) < 2:
        return "Não há um segundo maior valor (apenas um valor único na lista)."
        
    return lista_sem_duplicatas[1]

result = segundo_maior([10, 20, 4, 45, 99, 99, 45])
print(result)  # Saída esperada: 10