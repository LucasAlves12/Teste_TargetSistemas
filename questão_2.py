"""2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;"""

def fibonacci_sequence(max_num):
    sequence = [0, 1] 
    while sequence[-1] < max_num:
        next_value = sequence[-1] + sequence[-2] 
        if next_value > max_num:
            break
        sequence.append(next_value)
    return sequence

def is_in_fibonacci(num):
    if num < 0:
        return False
    sequence = fibonacci_sequence(num)
    return num in sequence

def main():
    while True:
        try:
            num = int(input("Informe um número: "))
            if is_in_fibonacci(num):
                print(f"O número {num} pertence à sequência de Fibonacci.\n")
            else:
                print(f"O número {num} não pertence à sequência de Fibonacci.\n")
        except ValueError:
            print("Por favor, informe um número inteiro válido.")    
        
        continuar = input("Deseja continuar? (S/N): ")
        if continuar.upper() != "S":
            break

if __name__ == "__main__": 
    main()