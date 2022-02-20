from flask import Flask, render_template, url_for, request, jsonify, redirect, make_response
import sys
import logging

app = Flask(__name__)
app.debug = True

# logging.basicConfig(filename='record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

@app.route('/', methods=['GET', 'POST']) 
def index():
  return render_template('index.html')

@app.route('/results', methods=['GET', 'POST'])
def results():
  if request.method == 'POST':
    return redirect(url_for('results'))
  return render_template('results.html')

# @app.route('/my_function', methods=['GET', 'POST'])
# def my_function():
#   if request.method == 'POST':
#     data = request.get_json()
#     print(data)
#     app.logger.info(data)
#     return jsonify(data)
#   else:
#     print(data)
#     return render_template('index.html', data)

# @app.route('/my_function', methods=['POST'])
# def my_function():
#     jsdata = request.form['data']
#     print(jsdata)
#     return jsonify(jsdata)

if __name__ == "__main__":
  app.run(host="localhost", debug=True)

