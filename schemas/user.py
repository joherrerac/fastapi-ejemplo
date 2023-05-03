def userEntity(item) -> dict:
    return {
        "id": item["item"],
        "nombre": item["nombre"],
        "apellido1": item["apellido1"],
        "apellido2": item["apellido2"],
        "rut": item["rut"],
    }

def usersEntity(entity) -> list:
    [userEntity(item) for item in entity]