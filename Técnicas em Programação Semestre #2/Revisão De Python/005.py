#Crie um algoritmo que receba pelo teclado o
#nome de um aluno e três notas, ao final
#deverá ser exibido o nome do aluno, sua
#media e resultado (se for acima de 6, o aluno
#estará “aprovado” do contrario “reprovado”).

def situacao(media):
    if media > 6:
        return 'Aprovado'
    elif media == 6:
        return 'TA NA MÉDIA!!!'
    else:
        return 'Estuda mais!!! \033[32mREPROVADO\033[m'

notas = list()
nome = input('Digite o nome do aluno: ')

for c in range(0, 3):
    notas.append(float(input(f'Digite a {c + 1}° nota: ')))

media_total = sum(notas) / len(notas)

print(f'O aluno(a) {nome} obteve a média de: {media_total}, portanto ele(a) está {situacao(media_total)}')