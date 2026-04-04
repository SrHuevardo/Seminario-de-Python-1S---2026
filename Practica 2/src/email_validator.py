def email_validator(correo):

    if correo.count('@') != 1:
        return False
        
    if correo.startswith(('@', '.')) or correo.endswith(('@', '.')):
        return False
        
    partes_correo = correo.split('@')
    nombre_usr = partes_correo[0]
    resto_dominio = partes_correo[1]
    
    if len(nombre_usr) < 1:
        return False
        
    if '.' not in resto_dominio:
        return False
        
    partes_dominio = resto_dominio.split('.')
    extension = partes_dominio[-1]
    
    if len(extension) < 2:
        return False
        
    return True