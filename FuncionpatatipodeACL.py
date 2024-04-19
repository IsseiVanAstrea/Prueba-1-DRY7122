def identificar_tipo_acl(numero_acl):
    if numero_acl < 100:
        return "ACL Layer 2 Estándar"
    elif numero_acl < 200:
        return "ACL Layer 3 Estándar"
    elif numero_acl < 300:
        return "ACL Layer 2 Extendida"
    elif numero_acl < 400:
        return "ACL Layer 3 Extendida"
    else:
        return "Número de ACL no corresponde a una lista de control de acceso"

numero_acl = int(input("Ingrese el número de ACL IPv4: "))
print(identificar_tipo_acl(numero_acl))