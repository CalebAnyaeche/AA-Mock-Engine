from flask import Flask
app = Flask(__name__)


@app.route('/putinfo', methods=['POST'])
def putinfo():
	data = request.get_json()
	with open('data.json', 'w', ensure_ascii=False) as outfile:
		json.dump(data, outfile)


@app.route('/pullinfo', methods=['GET'])
def pullinfo():
	with open('data.json') as json_data:
		d = json.load(json_data)
	return d
if __name__=='__main__':
    app.run()