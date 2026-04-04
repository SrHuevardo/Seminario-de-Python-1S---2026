def normalize_students(lista_alumnos):

    alumnos_limpios = {}

    for alumno in lista_alumnos:
        nombre = alumno.get("name")
        nota = alumno.get("grade")
        estado = alumno.get("status")

        if nombre is None or not nombre.strip():
            continue

        if nota is None or not str(nota).strip().isdigit():
            continue

        nombre_norm = nombre.strip().title()
        estado_norm = estado.strip().title() if estado else ""
        
        nota_norm = int(str(nota).strip())

        if nombre_norm not in alumnos_limpios:
            alumnos_limpios[nombre_norm] = {"nota": nota_norm, "estado": estado_norm}
        else:
            if nota_norm > alumnos_limpios[nombre_norm]["nota"]:
                alumnos_limpios[nombre_norm] = {"nota": nota_norm, "estado": estado_norm}

    nombres_ordenados = sorted(alumnos_limpios.keys())

    resultado_final = []
    for nombre in nombres_ordenados:
        resultado_final.append({
            "nombre": nombre,
            "nota": alumnos_limpios[nombre]["nota"],
            "estado": alumnos_limpios[nombre]["estado"]
        })

    return resultado_final