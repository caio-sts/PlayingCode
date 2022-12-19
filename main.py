# def criaNumero():
#     d1 = str(random.randrange(1, 9))
#     d2 = str(random.randrange(0, 9))
#     d3 = str(random.randrange(0, 9))
#     d4 = str(random.randrange(0, 9))
#     d5 = str(random.randrange(0, 9))
#     d6 = str(random.randrange(0, 9))
#     return d1+d2+d3+d4+d5+d6

def checaNumero(numero):
    numeroEstaRepetido = False
    with open("ALUNOS.DAT", "r") as f:
        for linha in f:
            numCadastro = linha.split(",")[0]
            print(linha)
            if numero == numCadastro:
                numeroEstaRepetido = True

    return numeroEstaRepetido

def printDados():
    with open("ALUNOS.DAT", "r") as f:
        if len(f.read()) == 0:
            print("Vazia.")
        else:
            print("Número, Nome, Curso, Nota 1, Nota 2, Média") ## USAR TABULATE COM SALTO DE LINHA INTERNO
            for linha in f:
                dados = linha.split(",")
                dados[-1] = dados[-1].replace(" ","").replace("\n","")
                media = (float(dados[-1])+float(dados[-2])) / 2

                list2print = ", ".join(dados)
                list2print += ", {}".format(media)
                print(list2print)
        
def changeGrade(numero, index_nota, nova_nota):
    with open("ALUNOS.DAT", "r") as f:
        data = f.readlines()

    for i in range(len(data)):
        if data[i].split(",")[0] == str(numero):
            list_data = data[i].split(',')
            if index_nota == "1":
                list_data[int(index_nota)+2] = nova_nota
            elif index_nota == "2":
                list_data[int(index_nota)+2] = nova_nota+"\n"
            data[i] = str(",".join(list_data))
        with open("ALUNOS.DAT", "w") as f:
            f.writelines(data)

def changeCourse(numero, novo_curso):
    with open("ALUNOS.DAT", "r") as f:
        data = f.readlines()

    for i in range(len(data)):
        if data[i].split(",")[0] == str(numero):
            list_data = data[i].split(',')
            list_data[2] = novo_curso
            data[i] = str(",".join(list_data))
        with open("ALUNOS.DAT", "w") as f:
            f.writelines(data)

def deleteStudent(numero):
    with open("ALUNOS.DAT", "r") as f:
        data = f.readlines()

    indx = 0
    while(indx != len(data)):        
        if data[indx].split(",")[0] == numero:
            break
        indx += 1
    while(indx < len(data)-1):
        temp_line = data[indx+1]
        
        data[indx] = temp_line
        indx += 1
    del data[-1]

    with open("ALUNOS.DAT", "w") as f:
        f.writelines(data)

def printApproveds():
    print("Número, Nome, Curso, Nota 1, Nota 2, Média") ## USAR TABULATE COM SALTO DE LINHA INTERNO
    with open("ALUNOS.DAT", "r") as f:
        for linha in f:
            dados = linha.split(",")
            dados[-1] = dados[-1].replace(" ","").replace("\n","")
            
            media = (float(dados[-1])+float(dados[-2])) / 2
            list2print = []

            if media >= 7:
                list2print = ", ".join(dados)
                list2print += ", {}".format(media)
                print(list2print)

def print2FinalExamSituation():
    print("Número, Nome, Curso, Nota 1, Nota 2, Média") ## USAR TABULATE COM SALTO DE LINHA INTERNO
    with open("ALUNOS.DAT", "r") as f:
        for linha in f:
            dados = linha.split(",")
            dados[-1] = dados[-1].replace(" ","").replace("\n","")
            
            media = (float(dados[-1])+float(dados[-2])) / 2
            list2print = []

            if media <= 7 and media >= 4:
                list2print = ", ".join(dados)
                list2print += ", {}".format(media)
                print(list2print)

def printDisapproveds():
    print("Número, Nome, Curso, Nota 1, Nota 2, Média") ## USAR TABULATE COM SALTO DE LINHA INTERNO
    with open("ALUNOS.DAT", "r") as f:
        for linha in f:
            dados = linha.split(",")
            dados[-1] = dados[-1].replace(" ","").replace("\n","")
            
            media = (float(dados[-1])+float(dados[-2])) / 2
            list2print = []

            if media < 4:
                list2print = ", ".join(dados)
                list2print += ", {}".format(media)
                print(list2print)

def inSystem():
    entrada = 1e20

    while(entrada != "0"):
        
        print("\n1 - Incluir alunos")
        print("2 - Alterar notas")
        print("3 - Alterar curso")
        print("4 - Excluir alunos")
        print("5 - Excluir todos os alunos")
        print("6 - Consultar nomes e médias")
        print("7 - Consultar alunos aprovados")
        print("8 - Consultar alunos reprovados")
        print("9 - Consultar alunos de AF")
        print("0 - Sair da execução do programa")
        print("\n")
        entrada = input("Digite o número correspondente ao que você pretende fazer:\n")

        if entrada == "1":
            numero = input("Digite o número do aluno:\n")
            if checaNumero(numero) == True:
                print("\nImpossível continuar o cadastro. Por favor, confira o número do aluno.\n")
                continue
            nome = input("Digite o nome completo:\n")
            curso = input("Digite o nome do curso:\n")
            nota1 = input("Digite a primeira nota:\n")
            nota2 = input("Digite a segunda nota:\n")

            with open("ALUNOS.DAT", "a+") as f:
                f.write("%s,%s,%s,%s,%s\n"%(numero, nome, curso, nota1, nota2))
                print("#"*10+" Aluno cadastrado com sucesso. "+"#"*10+"\n")
        
        elif entrada == "2":
            printDados()
            numStudent = input("\nQual o número do aluno que você quer que a nota seja alterada?\n")
            gradeIndx = input("\nQual a nota que deve ser alterada? 1 ou 2.\n")
            newGrade = input("\nQual o novo valor da nota?\n")
            changeGrade(numStudent, gradeIndx, newGrade)
            print("\nNota alterada com sucesso!\n")

        elif entrada == "3":
            printDados()
            numStudent = input("\nQual o número do aluno que você quer que o curso seja alterado?\n")
            course = input("\nQual o novo curso?\n")

            changeCourse(numStudent, course)
            print("\nCurso alterado com sucesso!\n")
        
        elif entrada == "4":
            numStudent = input("\nQual o número do aluno que você quer que seja excluído?\n")

            deleteStudent(numStudent)
            print("\nAluno excluído com sucesso!\n")

        elif entrada == "5":
            data = ""
            try:
                with open("ALUNOS.DAT", "w") as f:
                    f.write(data)        
                print("Todos os alunos foram excluídos com sucesso.")    
            except:
                print("Não foi possível excluir os dados.")

        elif entrada == "6":
            print("Lista dos Alunos\n")
            printDados()
        
        elif entrada == "7":
            print("Lista dos Aprovados\n")
            printApproveds()

        elif entrada == "8":
            print("Lista dos Reprovados\n")
            printDisapproveds()

        elif entrada == "9":
            print("Lista dos que vão para a Avaliação Final\n")
            print2FinalExamSituation()

        elif entrada == "0":
            print("\nEncerrando o sistema.\n")
            break
        else:
            print("Entrada inválida. Tente novamente!")

if __name__ == "__main__":
    print("Iniciando Sistema...")
    inSystem()
