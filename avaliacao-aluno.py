# Armazena em um vetor as notas das 10 avaliações
def preenche_notas(v: list) -> None:
    for i in range(0, 10, 1):
        nota = float(input(margem + f"Avaliação {i + 1}..: "))
        while nota < 0 or nota > 10:
            print(margem + "Nota inválida. A nota deve estar entre 0 e 10.")
            nota = float(input(margem + f"Avaliação {i + 1}..: "))
        v[i] = nota

# Exibe as notas das 10 avaliações
#{i +1}, recurso pois o indice começa em zero=1
def exibe_notas(v: list) -> None:
    for i in range(0, 10, 1):
        print(margem + f"Avaliação {i + 1} = {v[i]}")

# Exibe uma nota específica
def exibe_uma_nota(v: list, av: int) -> float:
    if av > 0 and av <= 10:
        return v[av - 1] # este -1 é pq o índice e a avaliação sempre tem 1 de diferença
    else:
        return margem + f"Não há a avaliação {av}"

# Calculando a média geral
def media_geral(v: list) -> float:
    soma = 0
    for i in range(0, 10, 1):
        soma += v[i]
    return soma / 10

#------ Subalgoritmos auxiliares
def exibe_menu() -> None:
    print("""
          0- SAIR
          1 - Preencher todas as notas
          2 - Exibir todas as notas
          3 - Exibir uma nota específica
          4 - Exibir a média de todas as notas
          """)

def opcao_menu() -> int:
    exibe_menu()
    return int(input(margem + "Opção desejada: "))
    

#-----Programa Principal

# Inicialização do vetor de float com 10 posições
aluno1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# Flag que controla se o vetor está preenchido (inicia não preenchido)
preenchido = False
margem = ' ' * 8

# Rotina que executa o menu indefinidamente
while True:
    opcao = opcao_menu()

    #escolha da opção do menu digitada
    match opcao:
        case 0:
            break
        case 1:
            preenche_notas(aluno1)
            #modifica o flag para True depois que o vetor for preenchido
            preenchido = True
        case 2:
            #analisa se o vetor está preenchido para exibir as notas
            if preenchido:
                exibe_notas(aluno1)
            else:
                print(margem + "***** Notas não preenchidas *****")
        case 3:
            if preenchido:
                avaliacao = int(input(margem + "Digite o numero da avaliação: "))
                print(margem + f"Avaliação {avaliacao} => {exibe_uma_nota(aluno1, avaliacao)}")
            else:
                print(margem + "***** Notas não preenchidas *****")
        case 4:
            if preenchido:
                print(margem + f"Média = {media_geral(aluno1):.1f}")
            else:
                print(margem + "***** Notas não preenchidas *****")
        case _:
            print(margem + "***** Opção inválida! *****")                        
            