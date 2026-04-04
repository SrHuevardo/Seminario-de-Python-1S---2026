def analyze_playlist(playlist):

    total_segundos_absolutos = 0
    

    cancion_mas_larga = None
    max_segundos = -1
    
    cancion_mas_corta = None
    min_segundos = float('inf') 
    
    for cancion in playlist:

        tiempo_texto = cancion["duration"]
        partes = tiempo_texto.split(":") 
        
        minutos = int(partes[0])
        segundos = int(partes[1])
        
        segundos_actual = (minutos * 60) + segundos
        total_segundos_absolutos += segundos_actual
        
        if segundos_actual > max_segundos:
            max_segundos = segundos_actual
            cancion_mas_larga = cancion
            
        if segundos_actual < min_segundos:
            min_segundos = segundos_actual
            cancion_mas_corta = cancion


    minutos_finales = total_segundos_absolutos // 60
    segundos_finales = total_segundos_absolutos % 60
    
    return {
        "tiempo_total": f"{minutos_finales}m {segundos_finales}s",
        "larga": cancion_mas_larga,
        "corta": cancion_mas_corta
    }