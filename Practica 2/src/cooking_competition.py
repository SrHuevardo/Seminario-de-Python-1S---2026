def simulate_competition(lista_rondas):
    
    estadisticas = {}
    historial_rondas = []
    
    # Inicializamos las estadisticas 
    nombres_cocineros = lista_rondas[0]['scores'].keys()
    for nombre in nombres_cocineros:
        estadisticas[nombre] = {
            'puntaje_total': 0,
            'rondas_ganadas': 0,
            'mejor_ronda': 0
        }
        
    cantidad_rondas = len(lista_rondas)
    
    # Procesamos ronda por ronda
    for i in range(cantidad_rondas):
        ronda_actual = lista_rondas[i]
        tema = ronda_actual['theme']
        
        puntajes_de_esta_ronda = {}
        
        # Calculamos puntajes por cocinero

        for cocinero, notas_jueces in ronda_actual['scores'].items():

            total_ronda = sum(notas_jueces.values()) 
            puntajes_de_esta_ronda[cocinero] = total_ronda
            

            estadisticas[cocinero]['puntaje_total'] += total_ronda
            

            if total_ronda > estadisticas[cocinero]['mejor_ronda']:
                estadisticas[cocinero]['mejor_ronda'] = total_ronda
                
        # Buscamos al ganador de esta ronda
        puntaje_maximo = max(puntajes_de_esta_ronda.values())
        
        ganadores_ronda = []
        for cocinero, puntaje in puntajes_de_esta_ronda.items():
            if puntaje == puntaje_maximo:
                ganadores_ronda.append(cocinero)
                estadisticas[cocinero]['rondas_ganadas'] += 1
                
        # Armamos el texto del resumen de esta ronda
        nombres_ganadores = ", ".join(ganadores_ronda) 
        
        texto_ronda = f"Ronda {i+1} - {tema}:\nGanador: {nombres_ganadores} ({puntaje_maximo} pts)\n"
        
        posiciones = []
        for c, p in puntajes_de_esta_ronda.items():
            posiciones.append({"nombre": c, "puntos": p})
            
        def ordenar_por_puntos(item):
            return item["puntos"]
            
        posiciones.sort(key=ordenar_por_puntos, reverse=True)
        
        for pos, datos in enumerate(posiciones):
            texto_ronda += f"  {pos+1}. {datos['nombre']}: {datos['puntos']} pts\n"
            
        historial_rondas.append(texto_ronda)
        
    # build tabla final
    tabla_final = []
    for cocinero, stats in estadisticas.items():
        promedio = stats['puntaje_total'] / cantidad_rondas
        tabla_final.append({
            'cocinero': cocinero,
            'puntaje': stats['puntaje_total'],
            'rondas_ganadas': stats['rondas_ganadas'],
            'mejor_ronda': stats['mejor_ronda'],
            'promedio': promedio
        })
        
    # tabla final ordenada
    def ordenar_final(item):
        return item['puntaje']
        
    tabla_final.sort(key=ordenar_final, reverse=True)
    
    return {
        'resumen_rondas': historial_rondas,
        'tabla_final': tabla_final
    }