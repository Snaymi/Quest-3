import json

# Carregar dados
dados = [
    {"dia": 1, "valor": 22174.1664},
    {"dia": 2, "valor": 24537.6698},
    {"dia": 3, "valor": 26139.6134},
    {"dia": 4, "valor": 0.0},
    # Adicione os demais valores do JSON aqui...
]

valores = [d["valor"] for d in dados if d["valor"] > 0]

menor_valor = min(valores)
maior_valor = max(valores)
media_mensal = sum(valores) / len(valores)
dias_acima_da_media = len([v for v in valores if v > media_mensal])

print(f"Menor valor: {menor_valor}")
print(f"Maior valor: {maior_valor}")
print(f"Dias acima da média: {dias_acima_da_media}")
