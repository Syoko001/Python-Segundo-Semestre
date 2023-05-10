import os

arquivos_diretorio = os.listdir("Lista de exercícios 08/NovaPasta")

if len(arquivos_diretorio) > 0:
    for c in range(len(arquivos_diretorio)):
        os.remove(f"Lista de exercícios 08/NovaPasta/{arquivos_diretorio[c]}")

os.rmdir("Lista de exercícios 08/NovaPasta")

print("\033[1;33mDiretório deletado com sucesso!\033[m")