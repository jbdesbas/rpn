from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world !'

@app.route('/loadData',methods=['GET', 'POST'])
def form_data():
    if request.method == 'GET':
        return render_template('formLoadData.html')
    else :
        return 'traiter le fichier envoyé'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4999)
