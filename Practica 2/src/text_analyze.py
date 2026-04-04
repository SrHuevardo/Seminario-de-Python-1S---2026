def analyze_zen(texto):
    
    lineas = texto.strip().split('\n')
    total_lineas = len(lineas)

    palabras_por_linea = [len(linea.split()) for linea in lineas]
    total_palabras = sum(palabras_por_linea)
    promedio = total_palabras / total_lineas

    indices_lineas_largas = [i for i, cantidad in enumerate(palabras_por_linea) if cantidad > promedio]
    
    resultados_lineas_largas = []
    for i in indices_lineas_largas:
        resultados_lineas_largas.append({
            "texto_linea": lineas[i],
            "cantidad_palabras": palabras_por_linea[i]
        })

    return {
        "total_lineas": total_lineas,
        "total_palabras": total_palabras,
        "promedio": promedio,
        "detalle_lineas_largas": resultados_lineas_largas
    }