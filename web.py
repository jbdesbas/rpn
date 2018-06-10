from flask import Flask,render_template,request, flash,url_for
import os
import rpn
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
        token=rpn.token()
        if file.filename.endswith('.zip'):
            z=ZipFile(file)
            for f in z.namelist():
                with open('data/temp/'+token.id+'.'+f.split('.')[-1],'wb') as dest :
                    dest.write(z.open(f).read())
                flash(f,'file')
        else:
            file.save('data/temp/'+token.id+'.'+file.filename.split('.')[-1])
            flash(file.filename,'file')
        flash(token.id,'token')
        token.save_to_db()
        token.save_file()
        return render_template('formLoadData.html',token=token.id)

@app.route('/rapport/<token>')
def rapport(token):
    r=rpn.rpn(rpn.token(token))
    return render_template('rapport.html',observateurs=r.observateurs(),especes=r.especes())

if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True, host='0.0.0.0', port=4999)
