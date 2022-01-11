from flask import Flask, request, render_template, session, redirect, url_for
import pymongo
from pymongo.errors import ConnectionFailure

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html', username=session["username"])
    else:
        return redirect(url_for('login'))

# ==================================================
# INSERT
# ==================================================
@app.route('/insert')        
def insert():
    return render_template('insert.html', username=session["username"])

@app.route('/insertDriver', methods=['POST'])        
def insertDriver():
    return 0

@app.route('/insertUser', methods=['POST'])        
def insertUser():
    return 0
    
@app.route('/insertMerchant', methods=['POST'])        
def insertMerchant():
    return 0

@app.route('/insertPromo', methods=['POST'])        
def insertPromo():
    return 0



# ==================================================
# AUTHENTIFICATION
# ==================================================
@app.route('/login')
def login():
    try:
        error = request.args['error']
    except:
        error = 0
    else:
        error = request.args['error']
    return render_template('auth.html', cauth = error)

@app.route('/auth', methods=['POST'])
def auth():
    print("Connecting..")
    username = request.form['username']
    password = request.form['password']
    url = "mongodb://{}:{}@mycluster-shard-00-00.3onxd.mongodb.net:27017,mycluster-shard-00-01.3onxd.mongodb.net:27017,mycluster-shard-00-02.3onxd.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-123ipc-shard-0&authSource=admin&retryWrites=true&w=majority".format(username, password)

    es = 0
    while(True):
        try:
            client = pymongo.MongoClient(url)
            client.admin.command('ismaster')        
        except ConnectionFailure:
            print("Server not available")
            print("Reconnecting..")
        except pymongo.errors.OperationFailure:
            print("Username or Password not correct")
            es = 1
            break
        else:
            print("connected")
            session['username'] = username
            es = 2
            break

    if(es == 1):
        return redirect(url_for('login', error = 2))
    elif(es == 2):
        return redirect(url_for('index'))

        
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)