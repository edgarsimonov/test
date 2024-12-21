from flask import Flask, request, jsonify

app = Flask(__name__)

# Пример функции для спряжения глаголов
def get_conjugations(verb):
    return {
        "я": f"{verb}ю",
        "ты": f"{verb}ешь",
        "он/она/оно": f"{verb}ет",
        "мы": f"{verb}ем",
        "вы": f"{verb}ете",
        "они": f"{verb}ют",
    }

# Маршрут для обработки запросов
@app.route('/conjugate', methods=['GET'])
def conjugate():
    verb = request.args.get('verb')
    if not verb:
        return jsonify({"error": "No verb provided"}), 400

    conjugations = get_conjugations(verb)
    return jsonify(conjugations)

if __name__ == '__main__':
    app.run(port=5000)
