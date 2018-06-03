from flask import Flask,render_template,request, flash
import os,uuid
from zipfile import ZipFile
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
        uniquename='data/'+str(uuid.uuid4())
        if file.filename.endswith('.zip'):
            z=ZipFile(file)
            for f in z.namelist():
                with open(uniquename+'.'+f.split('.')[-1],'wb') as dest :
                    dest.write(z.open(f).read())
            return str(z.namelist())
        else:
            file.save(uniquename+'.'+file.filename.split('.')[-1])
        return 'fichier sauvegarde '+file.filename


if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run(debug=True, host='0.0.0.0', port=4999)
