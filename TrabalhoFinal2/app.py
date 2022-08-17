from flask import Flask, redirect, render_template, request, jsonify

gpio = {'lampada_quarto': ['off', '65535'], 'ventilador_quarto': ['off', '65535'],
        'lampada_suite': ['off', '65535'], 'climatizador_suite': ['off', '65535'],
        'lampada_sala': ['off', '65535'], 'ventilador_sala': ['off', '65535'],
        'lampada_cozinha': ['off', '65535'], 'forno': ['off', '65535'], 'liquidificador': ['off', '65535']}

temperatura = 0
 
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/get-data', methods=['GET', 'POST'])
def data_request():
    global temperatura
    temperatura = request.args.get('temp')
    print(temperatura)
    return gpio

@app.route('/get-temp')
def get_temperature():
    global temperatura
    return str(temperatura)

@app.route('/quarto', methods=['GET', 'POST'])
def quarto_load():
    
    return render_template('quarto.html', gpio=gpio)

@app.route('/suite', methods=['GET', 'POST'])
def suite_load():
    
    return render_template('suite.html', gpio=gpio)


@app.route('/sala', methods=['GET', 'POST'])
def sala_load():
    
    return render_template('sala.html', gpio=gpio)

@app.route('/cozinha', methods=['GET', 'POST'])
def cozinha_load():
    
    return render_template('cozinha.html', gpio=gpio)

@app.route('/update-var', methods=['GET', 'POST'])
def update_values():
    if request.args.get('lampada_quarto'):
        gpio['lampada_quarto'][0] = request.args.get('lampada_quarto')
    if request.args.get('intensidade_lampada_quarto'):
        gpio['lampada_quarto'][1] = request.args.get('intensidade_lampada_quarto')
    if request.args.get('ventilador_quarto'):
        gpio['ventilador_quarto'][0] = request.args.get('ventilador_quarto')
    if request.args.get('velocidade_ventilador_quarto'):
        gpio['ventilador_quarto'][1] = request.args.get('velocidade_ventilador_quarto')
    
    if request.args.get('lampada_suite'):
        gpio['lampada_suite'][0] = request.args.get('lampada_suite')
    if request.args.get('intensidade_lampada_suite'):
        gpio['lampada_suite'][1] = request.args.get('intensidade_lampada_suite')
    if request.args.get('climatizador_suite'):
        gpio['climatizador_suite'][0] = request.args.get('climatizador_suite')
    if request.args.get('velocidade_climatizador_suite'):
        gpio['climatizador_suite'][1] = request.args.get('velocidade_climatizador_suite')
        
    if request.args.get('lampada_sala'):
        gpio['lampada_sala'][0] = request.args.get('lampada_sala')
    if request.args.get('intensidade_lampada_sala'):
        gpio['lampada_sala'][1] = request.args.get('intensidade_lampada_sala')
    if request.args.get('ventilador_sala'):
        gpio['ventilador_sala'][0] = request.args.get('ventilador_sala')
    if request.args.get('velocidade_ventilador_sala'):
        gpio['ventilador_sala'][1] = request.args.get('velocidade_ventilador_sala')
    
    if request.args.get('lampada_cozinha'):
        gpio['lampada_cozinha'][0] = request.args.get('lampada_cozinha')
    if request.args.get('intensidade_lampada_cozinha'):
        gpio['lampada_cozinha'][1] = request.args.get('intensidade_lampada_cozinha')
    if request.args.get('forno'):
        gpio['forno'][0] = request.args.get('forno')
    if request.args.get('intensidade_forno'):
        gpio['forno'][1] = request.args.get('intensidade_forno')
    if request.args.get('liquidificador'):
        gpio['liquidificador'][0] = request.args.get('liquidificador')
    if request.args.get('velocidade_liquidificador'):
        gpio['liquidificador'][1] = request.args.get('velocidade_liquidificador')
        
    return jsonify('OK')
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
