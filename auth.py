from crud.crud_medico import get_med

def create_med_pass(rut):
    return 'killcoronavirus' + rut[-4]

from crud.crud_medico import get_med

ADMIN_USERNAME = "ADMIN"
ADMIN_PASSWORD = "admincorona123"

def generar_password_medico(rut):
    return rut[-4:] + "killcoronavirus"

def login(username, password):
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        return {"rol": "admin"}
    
    medico = get_med(username)
    if medico:
        expected_password = generar_password_medico(username)
        if password == expected_password:
            return {"rol": "medico", "usuario": medico}
    
    return None
