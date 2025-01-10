from flask import Flask, request, jsonify, render_template


app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/wow', methods=['POST'])
def wow():
    return jsonify({'result': "wadup hello world wouw test"})


@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    try:
        num1 = float(data.get('num1'))
        num2 = float(data.get('num2'))
        operation = data.get('operation')

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                return jsonify({'error': 'Division by zero is not allowed'}), 400
            result = num1 / num2
        else:
            return jsonify({'error': 'Invalid operation'}), 400

        return jsonify({'result': result})

    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid input'}), 400

if __name__ == '__main__':
    app.run(debug=True)
