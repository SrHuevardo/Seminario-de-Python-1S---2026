
def calculate_shipping(peso, zona):

    zona_limpia = zona.strip().lower()
    
    zonas_validas = {"local", "regional", "nacional"}
    if zona_limpia not in zonas_validas:
        return "Zona no válida. Las zonas disponibles son: local, regional, nacional."

    if peso <= 1:
        tarifas = {"local": 500, "regional": 1000, "nacional": 2000}
    elif peso <= 5:

        tarifas = {"local": 1000, "regional": 2500, "nacional": 4500}
    else:

        tarifas = {"local": 2000, "regional": 5000, "nacional": 8000}

    return tarifas[zona_limpia]