from flask import Flask, request, render_template, session, redirect, url_for, flash
import pymongo
from pymongo.errors import ConnectionFailure
from files.CRUD import CRUD
from bson.objectid import ObjectId

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    if 'username' in session:
        crud = CRUD("db_tubes")
        data = {
            "driver" : crud.getCollectionData("driver"),
            "user" : crud.getCollectionData("user"),
            "merchant" : crud.getCollectionData("merchant"),
            "promo" : crud.getCollectionData("promo"),
            "order" : crud.getCollectionData("order"),
        }
        return render_template('index.html', username=session["username"], coll = data)
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
    data = {
        "name" : request.form['name'],
        "phone" : request.form['phone'],
        "email" : request.form['email'],
        "password" : request.form['password'],
        "balance" : request.form['balance'],
        "nik" : request.form['nik'],
        "vehicleType" : request.form['vehicleType'],
        "vehicleYear" : request.form['vehicleYear'],
        "licenseNumber" : request.form['licenseNumber'],
    }
    print(data)
    crud = CRUD("db_tubes")
    if (crud.insert("driver", data)):
        flash('success')
        return redirect(url_for('insert'))
    else:
        flash('failed')
        return redirect(url_for('insert'))

@app.route('/insertUser', methods=['POST'])        
def insertUser():
    data = {
        "name" : request.form['name'],
        "phone" : request.form['phone'],
        "email" : request.form['email'],
        "password" : request.form['password'],
        "balance" : request.form['balance'],
    }
    print(data)
    crud = CRUD("db_tubes")
    if (crud.insert("user", data)):
        flash("success")
        return redirect(url_for('insert'))
    else:
        flash("failed")
        return redirect(url_for('insert'))
    
@app.route('/insertMerchant', methods=['POST'])        
def insertMerchant():
    data = {
        "name" : request.form['name'],
        "phone" : request.form['phone'],
        "email" : request.form['email'],
        "password" : request.form['password'],
        "balance" : request.form['balance'],
        "address" : request.form['address'],
    }
    print(data)
    crud = CRUD("db_tubes")
    if (crud.insert("merchant", data)):
        flash('success')
        return redirect(url_for('insert'))
    else:
        flash('failed')
        return redirect(url_for('insert'))

@app.route('/insertPromo', methods=['POST'])        
def insertPromo():
    data = {
        "name" : request.form['name'],
        "multiplier" : request.form['multiplier'],
        "minTransaction" : request.form['minTransaction'],
        "expire" : request.form['expire'],
    }
    print(data)
    crud = CRUD("db_tubes")
    if (crud.insert("promo", data)):
        flash('success')
        return redirect(url_for('insert'))
    else:
        flash('failed')
        return redirect(url_for('insert'))
        



# ==================================================
# DELETE
# ==================================================
@app.route('/delete')
def delete():
    id = request.args['id']
    coll = request.args['coll']
    query = {
        "_id" : ObjectId(id)
    }
    crud = CRUD("db_tubes")
    crud.delete(coll, query)
    return redirect(url_for('index'))

# ==================================================
# UPDATE
# ==================================================
@app.route('/edit')
def edit():
    id = request.args['id']
    coll = request.args['coll']
    query = {
        "_id" : ObjectId(id)
    }
    crud = CRUD("db_tubes")
    result = crud.find(coll, query)
    return render_template('edit.html', username=session["username"], doc = result)

@app.route('/updateDriver', methods=['POST'])
def updateDriver():
    data = {
        '$set':{
            "name" : request.form['name'],
            "phone" : request.form['phone'],
            "email" : request.form['email'],
            "password" : request.form['password'],
            "balance" : request.form['balance'],
            "nik" : request.form['nik'],
            "vehicleType" : request.form['vehicleType'],
            "vehicleYear" : request.form['vehicleYear'],
            "licenseNumber" : request.form['licenseNumber'],
        }
    }
    id = request.form['id']
    coll = request.form['coll']

    query = {
        "_id" : ObjectId(id)
    }
    crud = CRUD("db_tubes")
    result = crud.find(coll, query)
    print("Res")
    print(result)
    crud.update(coll, result, data)
    return redirect(url_for('index'))
    
@app.route('/updateUser', methods=['POST'])
def updateUser():
    data = {
        '$set':{
            "name" : request.form['name'],
            "phone" : request.form['phone'],
            "email" : request.form['email'],
            "password" : request.form['password'],
            "balance" : request.form['balance'],
        }
    }
    id = request.form['id']
    coll = request.form['coll']

    query = {
        "_id" : ObjectId(id)
    }
    crud = CRUD("db_tubes")
    result = crud.find(coll, query)
    crud.update(coll, result, data)
    return redirect(url_for('index'))

@app.route('/updateMerchant', methods=['POST'])
def updateMerchant():
    data = {
        '$set':{
            "name" : request.form['name'],
            "phone" : request.form['phone'],
            "email" : request.form['email'],
            "password" : request.form['password'],
            "balance" : request.form['balance'],
            "address" : request.form['address'],
        }
    }
    id = request.form['id']
    coll = request.form['coll']

    query = {
        "_id" : ObjectId(id)
    }
    crud = CRUD("db_tubes")
    result = crud.find(coll, query)
    crud.update(coll, result, data)
    return redirect(url_for('index'))

@app.route('/updatePromo', methods=['POST'])
def updatePromo():
    data = {
        '$set':{
            "name" : request.form['name'],
            "multiplier" : request.form['multiplier'],
            "minTransaction" : request.form['minTransaction'],
            "expire" : request.form['expire'],
        }
    }
    id = request.form['id']
    coll = request.form['coll']

    query = {
        "_id" : ObjectId(id)
    }
    crud = CRUD("db_tubes")
    result = crud.find(coll, query)
    crud.update(coll, result, data)
    return redirect(url_for('index'))
    

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
    # url = "mongodb://{}:{}@mycluster-shard-00-00.3onxd.mongodb.net:27017,mycluster-shard-00-01.3onxd.mongodb.net:27017,mycluster-shard-00-02.3onxd.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-123ipc-shard-0&authSource=admin&retryWrites=true&w=majority".format(username, password)
    url = "mongodb://localhost:27017/"

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
            client = pymongo.MongoClient(url)
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