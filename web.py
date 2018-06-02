from flask import Flask,render_template,request, flash
import os,uuid
app = Flask(__name__)


@app.route('/')
def index():
    return 'hello world !'

@app.route('/loadData',methods=['GET', 'POST'])
def form_data():
    if request.method == 'GET':
        return render_template('formLoadData.html')
    else :
        file = request.files['input_file']
        file.save('data/'+str(uuid.uuid4()))
        flash('hahah')
        return 'traiter le fichier envoyé '+file.filename


if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run(debug=True, host='0.0.0.0', port=4999)
