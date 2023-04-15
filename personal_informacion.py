import os

def clear_console():
    command = "clear"
    if os.name in ("nt", "dos"):
        command = "clear"
        os.system(command)


def student_name():
    clear_console()
    name = input("Ingrese su nombre\n")
    return name
def student_lastname():
    clear_console()
    lastname = input("Ingrese su apellido\n")
    clear_console()
    return lastname
def student_code():
    code = input("Ingrese el codigo de su sección\n")
    clear_console()
    return code
def student_site():
    site = input("Ingrese su sede\n")
    clear_console()
    return site

def student_information():
    name = student_name()
    lastname = student_lastname()
    code = student_code()
    site = student_site()
    print ("Bienvenido", name, lastname,"\n"+"Codigo sección:", code, "\n"+ "Sede:", site)

student_information()


