def verificar_estoque(quantidade):
    if quantidade <= 5:
        return "Estoque baixo"

    return "Estoque adequado"


print("=== VERIFICAÇÃO DE ESTOQUE ===")

print(verificar_estoque(3))
print(verificar_estoque(10))