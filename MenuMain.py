from os import system
from time import sleep
from Fila_Encadeada import FilaEncadeada

fila = FilaEncadeada()
    
while True:
    print("\n\t\t\t\t\t  { FILA ENCADEADA }")
    print("\t\t\t\t ____________________________________ ")
    print("\t\t\t\t|                                    |")
    print("\t\t\t\t|   1. Enfileirar elemento           |")
    print("\t\t\t\t|   2. Verificar elemento na fila    |")
    print("\t\t\t\t|   3. Listar elementos da fila      |")
    print("\t\t\t\t|   4. Ver início da Fila            |")
    print("\t\t\t\t|   5. Ver fim da Fila               |")
    print("\t\t\t\t|   6. Desenfileirar elemento        |")
    print("\t\t\t\t|   7. Sair                          |")
    print("\t\t\t\t|____________________________________|")

    opcao = input("\nESCOLHA UMA DAS OPÇÕES: ")

    if opcao == "1":
        elemento = input("Insira o elemento que você quer enfileirar: ")
        fila.inserir_elemento(elemento)
        print(f"O elemento {elemento} foi enfileirado na fila.")
        sleep(2)
        system('cls')

    elif opcao == "2":
        elemento = input("Digite qual elemento você irá verificar na fila: ")
        if fila.pesquisar_elemento(elemento):
            print(f"O elemento {elemento} está na fila.")
            sleep(5)
            system('cls')
        else:
            print(f"Não existe {elemento} na fila.")
            sleep(5)
            system('cls')

    elif opcao == "3":
        elementos = fila.imprimir_fila()
        if elementos:
            print("Os elementos enfileirados são: ", elementos)
            sleep(5)
            system('cls')
        else:
            print("A fila está vazia.")
            sleep(5)
            system('cls')

    elif opcao == "4":
        elementos = fila.ver_inicio_fila()
        if elementos:
            print("O elemento no início da fila é: ", elementos)
            sleep(5)
            system('cls')
        else:
            print("A fila está vazia.")
            sleep(5)
            system('cls')
    
    elif opcao == "5":
        elementos = fila.ver_fim_fila()
        if elementos:
            print("O elemento no fim da fila é: ", elementos)
            sleep(5)
            system('cls')
        else:
            print("A fila está vazia.")
            sleep(5)
            system('cls')

    elif opcao == "6":
        elemento = fila.remover_elemento()
        if elemento is not None:
            print(f"O elemento {elemento} foi desenfileirado da fila.")
            sleep(5)
            system('cls')
        else:
            print("A fila está vazia.")
            sleep(5)
            system('cls')

    elif opcao == "7":
        print("Encerrado sistema, OBRIGADO!!!")
        sleep(3)
        break
    else:
        print("Opção inválida. Tente novamente.")
        sleep(1)
        system('cls')