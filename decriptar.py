substituicoes = {
    'A1': 'A', 'A2': 'B', 'A3': 'C', 'A4': 'D', 'A5': 'E', 'A6': 'F', 'A7': 'G', 'A8': 'H', 'A9': 'I',
    'B1': 'J', 'B2': 'K', 'B3': 'L', 'B4': 'M', 'B5': 'N', 'B6': 'O', 'B7': 'P', 'B8': 'Q', 'B9': 'R',
    'C1': 'S', 'C2': 'T', 'C3': 'U', 'C4': 'V', 'C5': 'W', 'C6': 'X', 'C7': 'Y', 'C8': 'Z'
}

def decriptar_texto(texto):
    texto_substituido = texto
    for chave, valor in substituicoes.items():
        texto_substituido = texto_substituido.replace(chave, valor)
    return texto, texto_substituido
