prova1 = int(input('Digite uma nota: '))
prova2 = int(input('Digite uma nota: '))
prova3 = int(input('Digite uma nota: '))
media = (prova1+prova2+prova3)/3
if(media >=7):
    print('Você foi aprovado')
else:
    print('Você Não foi aprovado e terá que fazer o exame final')
    exame = int(input('Digite sua nota no exame: '))
    final = (media + exame)/2
    if(final >= 5):
        print('Aprovado')
    else:
        print('Reprovado')

