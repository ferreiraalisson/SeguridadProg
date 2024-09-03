import sys
import os

def cifragem_menu():
    print("\nMétodos de cifragem disponível para o arquivo: \n1. Cifra de transposição reversa \n2. Cifra de César \n3. Cifra de substituição aleatória \n4. Sair \n")
    escolha = int(input("Escolha uma das opções do menu de 1 a 4: "))
    return escolha

def inversaoMensagem(msg):
    msg = list(msg)
    newMsg = ""
    for _ in range(len(msg)):
        newMsg += msg[-1]
        del msg[-1]
    return newMsg

def cifra_cesar(conteudo, deslocamento):
    resultado = []
    for letra in conteudo:
        if letra.isalpha():
            deslocamento_real = deslocamento % 26
            codigo_inicial = ord('A') if letra.isupper() else ord('a')
            nova_letra = chr(codigo_inicial + (ord(letra) - codigo_inicial + deslocamento_real) % 26)
            resultado.append(nova_letra)
        else:
            resultado.append(letra)
    return ''.join(resultado)

def cifra_aleatoria(conteudo, alfCifrado):
    valores = alfCifrado.replace(" ", "").replace("-", "")
    alfabeto = {chr(65 + i): valores[i] for i in range(26)}
    texto = conteudo.upper()
    resultado = []
    
    for letra in texto:
        if letra in alfabeto:
            resultado.append(str(alfabeto[letra]))
        else:
            resultado.append(letra)

    return ''.join(resultado)

def ler_arquivo(arquivo):
    try:
        with open(arquivo, 'r') as arq:
            conteudo = arq.read().strip()
        return conteudo.lower()
    except FileNotFoundError:
        print(f"O arquivo {arquivo} não foi encontrado")
        return None  

def operacao(nomeArquivo, conteudo):
    while True:
        opcao = cifragem_menu()
        
        if opcao == 1:
            print("\nCifragem de transposição reversa")
            arquivo = open(os.path.splitext(nomeArquivo)[0] + "Inverso.txt", "w")
            arquivo.write(inversaoMensagem(conteudo))
            arquivo.close()
            arquivo = open(os.path.splitext(nomeArquivo)[0] + "Inverso.txt", "r")
            conteudoCriptografado = arquivo.read()
            arquivo.close()
            print(f"Mensagem invertida: {conteudoCriptografado} \n")
        elif opcao == 2: 
            print("Cifragem de César")
            deslocamento = int(input("Informe o deslocamento para a cifra de César: "))
            arquivo = open(os.path.splitext(nomeArquivo)[0] + "Cesar.txt", "w")
            arquivo.write(cifra_cesar(conteudo, deslocamento))
            arquivo.close()
            arquivo = open(os.path.splitext(nomeArquivo)[0] + "Cesar.txt", "r")
            conteudoCriptografado = arquivo.read()
            arquivo.close()
            print(f"Mensagem cifrada com César: {conteudoCriptografado} \n")
        elif opcao == 3:
            print("Você escolheu a cifra de substituição aleatória!")
            tipoAlfabeto = int(input("Qual o alfabeto que deseja, 1 ou 2? "))
            if tipoAlfabeto == 1:
                alfCifrado = ler_arquivo("alfabeto_1.txt")
            else:
                alfCifrado = ler_arquivo("alfabeto_2.txt")

            arquivo = open(os.path.splitext(nomeArquivo)[0] + "SubstituicaoAleatoria.txt", "w")
            arquivo.write(cifra_aleatoria(conteudo, alfCifrado).capitalize())
            arquivo.close()
            arquivo = open(os.path.splitext(nomeArquivo)[0] + "SubstituicaoAleatoria.txt", "r")
            conteudoCriptografado = arquivo.read()
            arquivo.close()
            print(f"Mensagem com método de substituição: {conteudoCriptografado}")
        elif opcao == 4:
            print("Programa encerrado")
            break
        else:
            print("Opção inválida, tente novamente de 1 a 4 \n")
    
def main():
    
    nomeArquivo = sys.argv[1]
    conteudo = ler_arquivo(nomeArquivo)
    
    if conteudo:
        operacao(nomeArquivo, conteudo)
        
if __name__ == "__main__":
    main()
    input("Pressione Enter para confirmar o encerramento")
    
