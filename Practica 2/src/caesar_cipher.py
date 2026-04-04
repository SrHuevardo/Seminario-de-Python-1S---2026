import string

def apply_cipher(texto_original, desplazamiento):

    abecedario_min = string.ascii_lowercase
    abecedario_may = string.ascii_uppercase
    
    texto_procesado = ""
    
    for caracter in texto_original:
        if caracter in abecedario_min:

            indice_actual = abecedario_min.index(caracter)
            nuevo_indice = (indice_actual + desplazamiento) % 26
            texto_procesado += abecedario_min[nuevo_indice]
            
        elif caracter in abecedario_may:

            indice_actual = abecedario_may.index(caracter)
            nuevo_indice = (indice_actual + desplazamiento) % 26
            texto_procesado += abecedario_may[nuevo_indice]
            
        else:
            texto_procesado += caracter
            
    return texto_procesado