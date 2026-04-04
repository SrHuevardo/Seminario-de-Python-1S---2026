import random

def draw_secret_friend(lista_participantes):

    total_personas = len(lista_participantes)

    if total_personas < 2:
        return "Error: Se necesitan al menos 2 personas para jugar."
        
    mezclados = lista_participantes.copy()
    
    random.shuffle(mezclados)
    
    asignaciones = []

    for i in range(total_personas):
        donante = mezclados[i]
        
        receptor = mezclados[(i + 1) % total_personas]
        
        asignaciones.append((donante, receptor))
        
    return asignaciones