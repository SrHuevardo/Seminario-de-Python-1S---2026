
def filter_spoilers(texto_original, texto_spoilers):

    lista_spoilers = [spoiler.strip().lower() for spoiler in texto_spoilers.split(',')]
    
    texto_filtrado = texto_original
    
    for spoiler in lista_spoilers:
        longitud_spoiler = len(spoiler)
        asteriscos = "*" * longitud_spoiler
        
        while True:
            indice = texto_filtrado.lower().find(spoiler)
            
            if indice == -1:
                break
            texto_filtrado = texto_filtrado[:indice] + asteriscos + texto_filtrado[indice + longitud_spoiler:]
            
    return texto_filtrado