print("Digite o nome do aluno, :")
aluno = input()

print("Digite a nota do aluno. :")
nota = int(input())

def aprovacao (nota):

    if nota <= 7:
        return "Reprovado"
    else:
        return "Aprovado"

resultado = aprovacao (nota)

print("O aluno,",aluno,"esta",resultado,"nesta diciplina")