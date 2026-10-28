# Organizador de arquivos em Python

Um programa simples de linha de comando que organiza arquivos de uma pasta em subpastas conforme a extensão. Por exemplo, arquivos `.txt` vão para `Documentos`, `.jpg` para `Imagens`, `.mp4` para `Vídeos` e `.mp3` para `Áudio`.

## Como funciona

1. O programa percorre os arquivos que estão diretamente dentro da pasta `arquivos_teste`.
2. Lê a extensão de cada arquivo e procura a categoria correspondente.
3. Cria a pasta da categoria, caso ainda não exista.
4. Move o arquivo para essa pasta. Extensões não cadastradas vão para `Outros`.

## Estrutura esperada

Coloque `main.py` e a pasta de entrada lado a lado:

```text
meu_projeto/
├── main.py
└── arquivos_teste/
    ├── exemplo.txt
    ├── foto.jpg
    └── musica.mp3
```

Depois da execução, a pasta ficará parecida com:

```text
arquivos_teste/
├── Documentos/
│   └── exemplo.txt
├── Imagens/
│   └── foto.jpg
└── Áudio/
    └── musica.mp3
```

## Requisitos

- Python 3
- Não precisa instalar bibliotecas externas: `pathlib` e `shutil` fazem parte da biblioteca padrão do Python.

## Como executar

Abra o terminal na pasta do projeto e execute:

```bash
python main.py
```

No Windows, se o comando acima não funcionar, tente:

```bash
py main.py
```

## Extensões reconhecidas

| Categoria | Extensões |
|---|---|
| Documentos | `.txt`, `.pdf`, `.docx` |
| Imagens | `.jpg`, `.jpeg`, `.png`, `.gif` |
| Vídeos | `.mp4`, `.mov` |
| Áudio | `.mp3`, `.wav` |
| Outros | Qualquer extensão não cadastrada |

As extensões são comparadas sem diferenciar maiúsculas de minúsculas, então `.JPG` também é reconhecida.

## Cuidados

O programa **move** os arquivos da pasta de entrada para as subpastas; não cria cópias. Para experimentar, use uma pasta de teste com cópias dos arquivos. Confira se `arquivos_teste` é o caminho correto antes de executar.

## Personalizar categorias

Edite o dicionário `categorias` em `main.py`. Por exemplo, para classificar arquivos `.zip` como compactados, adicione:

```python
".zip": "Compactados",
```

## Observação

Este README descreve a versão construída durante o projeto: ela organiza os arquivos automaticamente. Se seu código tiver diferenças, ajuste as extensões e os nomes para corresponder ao `main.py` atual.
