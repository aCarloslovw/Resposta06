# Função para verificar a letra 'a' e contar suas ocorrências
def verificar_letra_a(s):
    # Converte a string para minúsculas para facilitar a verificação
    s_lower = s.lower()
    contagem = s_lower.count('a')  # Conta a quantidade de 'a' (minúscula)
    
    if contagem > 0:
        print(f"A letra 'a' (maiúscula ou minúscula) aparece {contagem} vez(es) na string.")
    else:
        print("A letra 'a' não está presente na string.")

# Entrada de dados pelo usuário
entrada_usuario = input("Digite uma string para verificar a letra 'a': ")

# Verificar a letra 'a' na string informada pelo usuário
verificar_letra_a(entrada_usuario)

# Exemplo com string previamente definida
#string_pre_definida = "Amanhã será um ótimo dia!"
#verificar_letra_a(string_pre_definida)
