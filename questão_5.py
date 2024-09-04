"""5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
"""
def inverter_string(string):
    string_invertida = ""
    for i in range(len(string)-1, -1, -1):
        string_invertida += string[i] 
    return string_invertida 

def main():
    while True:
        string = input("Informe uma string: ")
        string_invertida = inverter_string(string)
        print(f"String invertida: {string_invertida}\n")
    
        continuar = input("Deseja inserir outra string? (S/N): ")
        if continuar.upper() != "S":
            break

if __name__ == "__main__":
    main()