import os

input_directory = './'


word_counts = {}


word_occurrences = {}


files = [f for f in os.listdir(input_directory) if os.path.isfile(os.path.join(input_directory, f))]


for file_name in files:
    
    file_path = os.path.join(input_directory, file_name)

    # Leer el archivo y procesar cada línea
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Verificar que la línea tenga el formato esperado
            if '\t' in line:
                # Dividir la línea en palabra y recuento
                word, count = line.strip().split('\t')

                # Convertir el recuento a entero
                count = int(count)

                # Actualizar el recuento total de la palabra en el diccionario
                if word in word_counts:
                    word_counts[word] += count
                else:
                    word_counts[word] = count

                # Actualizar el diccionario de ocurrencias
                if word in word_occurrences:
                    word_occurrences[word].append((file_name, count))
                else:
                    word_occurrences[word] = [(file_name, count)]

# Guardar el recuento total en conteo_total.txt
output_file_path = 'conteo_total.txt'
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for word, count in word_counts.items():
        output_file.write(f'{word}: {count} veces\n')

# Guardar el registro de ocurrencias en ocurrencias.txt
occurrences_file_path = 'ocurrencias.txt'
with open(occurrences_file_path, 'w', encoding='utf-8') as occurrences_file:
    for word, occurrences in word_occurrences.items():
        occurrences_file.write(f'{word} | {occurrences}\n')

print(f'El conteo total se ha guardado en {output_file_path}')
print(f'El registro de ocurrencias se ha guardado en {occurrences_file_path}')