from crud.crud_medico import get_med
from menu_admin import Menu_Admin
from menu_medico import Menu_Medico

ADMIN_USER = 'ADMIN'
ADMIN_PASSWORD = 'admincorona1234'

def create_med_pass(rut):
    return 'killcoronavirus' + rut[-4]

def login(user, password):
    if user == ADMIN_USER and password == ADMIN_PASSWORD:
        return Menu_Admin.menu()
    
    medico = get_med(user)
    if medico:
        truePassword = create_med_pass(user)
        if password == truePassword:
            return Menu_Medico.menu()
        
    return None