import json

#Carrega os dados do JSON
with open('dados.json', 'r') as dados:
    faturamento = json.load(dados)

#Insere somente os faturamentos positivos
faturamento_positivo = [dia["valor"] for dia in faturamento if dia["valor"] > 0]

menor_faturamento = min(faturamento_positivo)

maior_faturamento = max(faturamento_positivo)
    
media_faturamento = sum(faturamento_positivo) / len(faturamento_positivo)
    
dias_acima_da_media = sum(1 for valor in faturamento_positivo if valor > media_faturamento)
    
print(f"Menor valor de faturamento: R$ {menor_faturamento:}")
print(f"Maior valor de faturamento: R$ {maior_faturamento:}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")