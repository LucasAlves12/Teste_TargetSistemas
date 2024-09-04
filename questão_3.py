"""3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;"""

import json

def read_faturamento(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def calcular_estatisticas(faturamento):
    # Filtrar dias com faturamento
    faturamento_filtrado = [dia['valor'] for dia in faturamento if dia['valor'] > 0]
    
    # Calcular menor e maior valor de faturamento
    menor_valor = min(faturamento_filtrado)
    maior_valor = max(faturamento_filtrado)
    
    # Calcular média mensal de faturamento
    media_mensal = sum(faturamento_filtrado) / len(faturamento_filtrado)
    
    # Contar dias com faturamento superior à média mensal
    dias_acima_da_media = sum(1 for valor in faturamento_filtrado if valor > media_mensal)
    
    return menor_valor, maior_valor, dias_acima_da_media

def main():
    file_path = 'dados.json'  # Caminho para o arquivo JSON
    faturamento = read_faturamento(file_path)
    
    menor_valor, maior_valor, dias_acima_da_media = calcular_estatisticas(faturamento)
    
    print(f"Menor valor de faturamento: {menor_valor}")
    print(f"Maior valor de faturamento: {maior_valor}")
    print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")

if __name__ == "__main__":
    main()