nome = input("Digite seu nome: ")
nota1 = float(input("Digite sua nota da primeira avaliação: "))
nota2 = float(input("Digite sua nota da segunda avaliação: "))
nota3 = float(input("Digite sua nota da terceira avaliação: "))

with open("arquivo.txt", "w") as arquivo:
    arquivo.write(f"Nome: {nome}\n")
    arquivo.write(f"Nota 1: {nota1}\n")
    arquivo.write(f"Nota 2: {nota2}\n")
    arquivo.write(f"Nota 3: {nota3}\n")

with open("arquivo.txt", "r") as arquivo:
    linhas = arquivo.readlines()

nome = linhas[0].strip().split(": ")[1]
nota1 = float(linhas[1].strip().split(": ")[1])
nota2 = float(linhas[2].strip().split(": ")[1])
nota3 = float(linhas[3].strip().split(": ")[1])

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    situacao = "Aprovado"
elif 5 <= media < 7:
    situacao = "Exame"
else:
    situacao = "Reprovado"

if situacao == "Aprovado":
    with open("aprovados.txt", "a") as arquivo_aprovados:
        arquivo_aprovados.write(f"Nome: {nome}, Média: {media}\n")
elif situacao == "Exame":
    situacao = "Reprovado"
else:
    nota_exame = float(input("Digite a nota do exame: "))
    media_atualizada = (media + nota_exame) / 2
    if media_atualizada >= 5:
        situacao = "Aprovado após exame"
        with open("aprovados.txt", "a") as arquivo_aprovados:
            arquivo_aprovados.write(f"Nome: {nome}, Média: {media_atualizada}, Situação: {situacao}\n")
    else:
        situacao = "Reprovado após exame"
        with open("reprovados.txt", "a") as arquivo_reprovados:
            arquivo_reprovados.write(f"Nome: {nome}, Média: {media_atualizada}, Situação: {situacao}\n")
        

def imprimir_situacao(nome_arquivo):
    with open(nome_arquivo, "r") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            print(linha.strip())

print("Alunos aprovados:")
imprimir_situacao("aprovados.txt")

print("\nAlunos reprovados:")
imprimir_situacao("reprovados.txt")