import os

current_dir = os.path.dirname(__file__)

import_file = os.path.join(current_dir, "allow_list.txt")
import_file_remove = os.path.join(current_dir, "remove_list.txt")
updated_ip_addresses = []
user_deleted = []


def Extrair_Ip(ip_addresses):
    for line in ip_addresses:
        parts = line.strip().split(",")
        if len(parts) >= 2:
            ip = parts[1]
            if ip not in remove_list:
                updated_ip_addresses.append(line)
            else:
                user_deleted.append(parts[0])



# Lê lista de remoção linha por linha
with open(import_file_remove, "r") as file:
    remove_list = [line.strip() for line in file]

# Lê lista de permissão linha por linha
with open(import_file, "r") as file:
    ip_addresses = file.readlines()


# Extrair IP que não está na remove_list

Extrair_Ip(ip_addresses)

print("Lista Original:")
print("User | IP address | Time | Date")
print("".join(ip_addresses))

print("*"*60)
print("Usuários deletados: ", user_deleted)
print("*"*60)
print("\nLista Atualizada:")
print("User | IP address | Time | Date")
print("".join(updated_ip_addresses))



