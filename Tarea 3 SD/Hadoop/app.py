from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Cargar el JSON con la estructura deseada
with open('./examples/word_occurrences.json', 'r', encoding='utf-8') as json_file:
    word_occurrences = json.load(json_file)

@app.route('/consulta', methods=['GET'])
def consulta_palabra():
    palabra = request.args.get('palabra', '')

    # Verificar si la palabra está en el JSON
    if palabra in word_occurrences:
        return jsonify({"palabra": palabra, "ocurrencias": word_occurrences[palabra]})
    else:
        return jsonify({"error": f"La palabra '{palabra}' no fue encontrada."})

if __name__ == '__main__':
    app.run(debug=True)