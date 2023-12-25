from flask import Flask, render_template, request, jsonify, url_for

app = 	Flask('__name__')

@app.route('/', methods=['GET'])
def home():
	return render_template('index.html')

@app.route('/mycv', methods=['GET'])
def cv():
	return 'cv'

@app.route('/myproject', methods=['GET'])
def project():
	return 'project'

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)