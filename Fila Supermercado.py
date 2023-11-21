fila = ["Tiago","Julia","Pedro"]
print ("Fila: ", fila)

preferencial = ["Antonio","Maria"]
print("Fila Preferencial: ", preferencial) 

while True:
    if (preferencial == []):
        if (fila == []):
            break
        else:
            print()
            resposta = input("Atender ou incluir uma pessoa na fila normal ?[A/I]")
            if (resposta == "A"):
                fila.pop(0)
                print("Primeiro da fila atendido")
                if (fila != []):
                    print ("Fila Normal: ", fila)
                else:
                    print("Fila Normal Vazia")
            elif (resposta == "I"):
                novo = input("Proximo integrante da fila")
                fila.append(novo)
                print ("Fila Normal ", fila)
            else:
                print("Comando invalido")

    else:
        print()
        resposta = input("Atender ou incluir uma pessoa da fila preferencial? [A/I]")
        if (resposta == "A"):
            preferencial.pop(0)
            print("Primeiro integrante atendido")
            if (preferencial != []):
                print ("Fila preferencial: ", preferencial)
            else:
                print("Fila preferencial vazia")
        elif (resposta == "I"):
            novo = input("Insira o próximo integrante da fila preferencial: ")
            preferencial.append(novo)
            print("Fila preferencial: ", preferencial)
        else:
            print("comando invalido")
