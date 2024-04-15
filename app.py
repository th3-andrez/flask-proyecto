from flask import Flask, render_template, request,redirect,url_for,flash
from flask_mysqldb import MySQL

app=Flask(__name__)
app.config['MySQL_HOST']='localhost'
app.config['MySQL_USER']='root'
app.config['MySQL_PASSWORD']=''
app.config['MYSQL_DB']='flask2'
mysql=MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/comentarios', methods=['POST'])
def add_contact():
    if request.method=='POST':
        fullname=request.form['fullname']
        comentario=request.form['comentario']
        cur=mysql.connection.cursor()
        cur.execute('INSERT INTO contacts (fullname, comentario) VALUES (%s, %s)',
        (fullname, comentario))
        mysql.connection.commit()
        flash('cometario enviado')

        return redirect(url_for('index.html'))

@app.route('/edit')
def edit_contact():
    return 'edit_comentario'

@app.route('/delete')
def delete_contact():
    return 'delete_contact'

if __name__ =='__main__':
    app.run(port=3000, debug=True)