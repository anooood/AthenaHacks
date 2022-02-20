from flask import Flask, render_template, url_for, request, jsonify
import sys

app = Flask(__name__)

@app.route('/my_function', methods=['GET', 'POST']) 
def my_function():
  if request.method == 'POST':
    data = request.json()
    print(data, file=sys.stderr)
  return jsonify(data)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#   return render_template('index.html')

# if __name__ == "__main__":
#   app.run(debug=True)

x=4
