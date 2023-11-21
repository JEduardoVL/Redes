from os import system
import ipaddress


print(''' 
      Proyecto Calculadora de redes. 
      Ingresa la IP que desea conocer.
      
      CLase     SubRedes       Host
      ''')

ingreso = input()

def ip_calculator(ip_cidr):
    network = ipaddress.ip_network(ip_cidr, strict=False)

    # Determinar la clase de la IP
    first_octet = int(ip_cidr.split('.')[0])
    if 1 <= first_octet <= 126:
        ip_class = 'A'
    elif 128 <= first_octet <= 191:
        ip_class = 'B'
    elif 192 <= first_octet <= 223:
        ip_class = 'C'
    else:
        ip_class = 'Otra'

    # Calcular el número de subredes (para Clase A, B, C)
    if ip_class in ['A', 'B', 'C']:
        mask = network.prefixlen
        base_masks = {'A': 8, 'B': 16, 'C': 24}
        subnet_count = 2 ** (mask - base_masks[ip_class])
    else:
        subnet_count = 'No aplicable'

    host_count = 2 ** (32 - network.prefixlen) - 2

    return f"Clase = {ip_class}, SubRedes = {subnet_count}, Hosts = {host_count}"

print(ip_calculator(ingreso))
