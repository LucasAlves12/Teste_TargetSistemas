"""4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
• SP = R$67.836,43
• RJ – R$36.678,66
• MG – R$29.229,88
• ES – R$27.165,48
• Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.  """

def calcula_percentual(x, y):
    return (x / y) * 100

def main():
    SP = 67836.43
    RJ = 36678.66
    MG = 29229.88
    ES = 27165.48
    OUTROS = 19849.53
    TOTAL = SP + RJ + MG + ES + OUTROS

    print(f"Percentual de vendas de SP: {calcula_percentual(SP, TOTAL):.2f}%")
    print(f"Percentual de vendas de RJ: {calcula_percentual(RJ, TOTAL):.2f}%")
    print(f"Percentual de vendas de MG: {calcula_percentual(MG, TOTAL):.2f}%")
    print(f"Percentual de vendas de ES: {calcula_percentual(ES, TOTAL):.2f}%")
    print(f"Percentual de vendas de OUTROS: {calcula_percentual(OUTROS, TOTAL):.2f}%")

if __name__ == "__main__":
    main()