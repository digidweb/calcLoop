# Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. No início, o programa mostrará a seguinte lista de operações:

# 1: Soma
# 2: Subtração
# 3: Multiplicação
# 4: Divisão
# 0: Sair

# Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.

# Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. Depois precisa executar a operação e mostrar o resultado na tela. Quando o usuário escolher a opção “Sair”, o sistema irá parar.

# É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado. 

# Trabalhe esse código em seu IDE, suba ele para sua conta no GitHub e compartilhe o link desse projeto no campo ao lado para que outros desenvolvedores possam analisá-lo.

def calculadora(n1, n2, n3):
    if n3 == 1:
        return n1 + n2
    elif n3 == 2:
        return n1 - n2
    elif n3 == 3:
        return n1 * n2
    elif n3 == 4:
        return n1 / n2
    else:
        return 0

executar = True

while (executar == True):  
    n3 = int(input("Escolha a operação: 1-Soma, 2-Subtração, 3-Multiplicação, 4-Divisão e 0-Sair: "))

    if (n3 < 0) or (n3 > 4):
        print("Essa opção não existe")
    elif n3 == 0:
        executar = False
    else:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))

        resultado = calculadora(n1, n2, n3)
        print("Resultado:", resultado)


