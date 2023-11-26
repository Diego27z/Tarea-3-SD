import json

# Ruta al archivo ocurrencias.txt
ocurrencias_path = 'ocurrencias.txt'

# Diccionario para almacenar los datos en el formato deseado
word_occurrences = {}

# Leer el archivo ocurrencias.txt y procesar cada línea
with open(ocurrencias_path, 'r', encoding='utf-8') as file:
    for line in file:
        # Dividir la línea en palabra y lista de (archivo, frecuencia)
        parts = line.strip().split(' | ')
        word = parts[0]
        occurrences_list = eval(parts[1])  # Convertir la cadena a una lista de tuplas

        # Actualizar el diccionario de ocurrencias
        word_occurrences[word] = [{"Documento": doc, "Frecuencia": freq} for doc, freq in occurrences_list]

# Guardar el diccionario en un archivo JSON
json_path = 'word_occurrences.json'
with open(json_path, 'w', encoding='utf-8') as json_file:
    json.dump(word_occurrences, json_file, ensure_ascii=False, indent=2)

print(f'Los datos se han guardado en el archivo JSON: {json_path}')