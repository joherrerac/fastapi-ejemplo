def userEntity(item) -> dict:
    return {
        "id": int(item["_id"]),
        "nombre": item["nombre"],
        "apellido1": item["apellido1"],
        "apellido2": item["apellido2"],
        "rut": item["rut"],
    }

def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]