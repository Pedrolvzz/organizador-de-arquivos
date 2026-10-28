from pathlib import Path # representar e trabalhar com caminhos de pastas e arquivos.
import shutil # ferramentas para operações com arquivos; usamos shutil.move para mover cada arquivo.

pasta = Path("arquivos_teste") # define a pasta que o programa vai organizar.

categorias = {
    ".txt": "Documentos",
    ".pdf": "Documentos",
    ".jpg": "Imagens",
    ".png": "Imagens",
    ".gif": "Imagens",
    ".mp4": "Vídeos",
    ".mov": "Vídeos",
    ".mp3": "Áudio",
    ".wav": "Áudio",
}

for arquivo in pasta.iterdir(): # percorre os itens que estão diretamente dentro da pasta.
    if arquivo.is_file(): # continua apenas quando o item é um arquivo.
        categoria = categorias.get(arquivo.suffix.lower(), "Outros") # obtém a extensão e a converte para minúsculas, para reconhecer também extensões como .JPG.
        destino = pasta / categoria # monta o caminho da pasta de destino, como arquivos_teste/Imagens.
        destino.mkdir(exist_ok=True) # cria essa pasta se ela ainda não existir. Se já existir, continua sem erro.
        shutil.move(str(arquivo), str(destino / arquivo.name)) # move o arquivo para a pasta de destino.
        print(f"{arquivo.name} iria para a pasta {categoria}")