try:
    with (
        open('ips.txt', 'r') as file_entrada, 
        open('ips_validas.txt', 'w') as file_validas, 
        open('ips_invalidas.txt', 'w') as file_invalidas 
    ):
         lineas = file_entrada.readlines()
         for linea in lineas:
             linea_limpia = linea.strip() 
             if linea_limpia:
                partes = linea_limpia.split('.')
                if len(partes) == 4: 
                   file_validas.write(linea_limpia + '\n')
                else:
                    file_invalidas.write(linea_limpia + '\n')
except FileNotFoundError:
    print("Error: El archivo 'ips.txt' no se encontró")