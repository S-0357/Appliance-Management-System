from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Function to retrieve data from a specific table
def get_appliances(table):
    db = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="2005",
        database="gadjets"
    )
    cursor = db.cursor()
    query = f"SELECT * FROM {table}"
    cursor.execute(query)
    appliances = cursor.fetchall()
    cursor.close()
    db.close()
    return appliances

# Route for the index page to display all appliances
@app.route('/')
def index():
    db = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="2005",
        database="gadjets"
    )
    cursor = db.cursor()
    query = "SELECT * FROM all_appliances"
    cursor.execute(query)
    appliances = cursor.fetchall()  # Fetch all rows from the view
    cursor.close()
    db.close()
    
    return render_template('index.html', appliances=appliances)

# Routes for displaying specific appliances
@app.route('/fridge')
def fridge():
    appliances = get_appliances('fridge')
    return render_template('fridge.html', appliances=appliances)

@app.route('/WM')
def WM():
    appliances = get_appliances('WM')
    return render_template('WM.html', appliances=appliances)

@app.route('/AC')
def AC():
    appliances = get_appliances('AC')
    return render_template('AC.html', appliances=appliances)

@app.route('/TV')
def TV():
    appliances = get_appliances('TV')
    return render_template('TV.html', appliances=appliances)

@app.route('/IB')
def IB():
    appliances = get_appliances('IB')
    return render_template('IB.html', appliances=appliances)

# Route to delete an appliance entry
@app.route('/delete_appliance/<table>/<int:id>', methods=['POST'])
def delete_appliance(table, id):
    db = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="2005",
        database="gadjets"
    )
    cursor = db.cursor()
    query = f"DELETE FROM {table} WHERE id = %s"
    cursor.execute(query, (id,))
    db.commit()
    cursor.close()
    db.close()
    return redirect(request.referrer)

# Routes to add appliances
@app.route('/add_fridge', methods=['GET', 'POST'])
def add_fridge():
    if request.method == 'POST':
        id = request.form['id']
        brand = request.form['brand']
        rating = request.form['rating']
        quantity = request.form['quantity']
        price = request.form['price']
        model = request.form['model']

        db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="2005",
            database="gadjets"
        )
        cursor = db.cursor()
        query = "INSERT INTO fridge (id, brand, rating, quantity, price, model) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (id, brand, rating, quantity, price, model))
        db.commit()
        cursor.close()
        db.close()
        return redirect(url_for('fridge'))
    
    return render_template('add_fridge.html')

@app.route('/add_wm', methods=['GET', 'POST'])
def add_wm():
    if request.method == 'POST':
        id = request.form['id']
        brand = request.form['brand']
        rating = request.form['rating']
        quantity = request.form['quantity']
        price = request.form['price']
        model = request.form['model']

        db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="2005",
            database="gadjets"
        )
        cursor = db.cursor()
        query = "INSERT INTO WM (id, brand, rating, quantity, price, model) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (id, brand, rating, quantity, price, model))
        db.commit()
        cursor.close()
        db.close()
        return redirect(url_for('WM'))
    
    return render_template('add_wm.html')

@app.route('/add_ac', methods=['GET', 'POST'])
def add_ac():
    if request.method == 'POST':
        id = request.form['id']
        brand = request.form['brand']
        rating = request.form['rating']
        quantity = request.form['quantity']
        price = request.form['price']
        model = request.form['model']

        db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="2005",
            database="gadjets"
        )
        cursor = db.cursor()
        query = "INSERT INTO AC (id, brand, rating, quantity, price, model) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (id, brand, rating, quantity, price, model))
        db.commit()
        cursor.close()
        db.close()
        return redirect(url_for('AC'))
    
    return render_template('add_ac.html')

@app.route('/add_tv', methods=['GET', 'POST'])
def add_tv():
    if request.method == 'POST':
        id = request.form['id']
        brand = request.form['brand']
        rating = request.form['rating']
        quantity = request.form['quantity']
        price = request.form['price']
        model = request.form['model']

        db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="2005",
            database="gadjets"
        )
        cursor = db.cursor()
        query = "INSERT INTO TV (id, brand, rating, quantity, price, model) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (id, brand, rating, quantity, price, model))
        db.commit()
        cursor.close()
        db.close()
        return redirect(url_for('TV'))
    
    return render_template('add_tv.html')

@app.route('/add_ib', methods=['GET', 'POST'])
def add_ib():
    if request.method == 'POST':
        id = request.form['id']
        brand = request.form['brand']
        rating = request.form['rating']
        quantity = request.form['quantity']
        price = request.form['price']
        model = request.form['model']

        db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="2005",
            database="gadjets"
        )
        cursor = db.cursor()
        query = "INSERT INTO IB (id, brand, rating, quantity, price, model) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (id, brand, rating, quantity, price, model))
        db.commit()
        cursor.close()
        db.close()
        return redirect(url_for('IB'))
    
    return render_template('add_ib.html')

# Routes to update appliances
@app.route('/update_fridge/<int:id>', methods=['GET', 'POST'])
def update_fridge(id):
    if request.method == 'POST':
        brand = request.form['brand']
        rating = request.form['rating']
        quantity = request.form['quantity']
        price = request.form['price']
        model = request.form['model']
        
        db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="2005",
            database="gadjets"
        )
        cursor = db.cursor()
        query = """
            UPDATE fridge
            SET brand = %s, rating = %s, quantity = %s, price = %s, model = %s
            WHERE id = %s
        """
        cursor.execute(query, (brand, rating, quantity, price, model, id))
        db.commit()
        cursor.close()
        db.close()

        return redirect(url_for('fridge'))

    appliance = get_appliance_by_id('fridge', id)
    return render_template('update_fridge.html', appliance=appliance)

@app.route('/update_wm/<int:id>', methods=['GET', 'POST'])
def update_wm(id):
    if request.method == 'POST':
        brand = request.form['brand']
        rating = request.form['rating']
        quantity = request.form['quantity']
        price = request.form['price']
        model = request.form['model']
        
        db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="2005",
            database="gadjets"
        )
        cursor = db.cursor()
        query = """
            UPDATE WM
            SET brand = %s, rating = %s, quantity = %s, price = %s, model = %s
            WHERE id = %s
        """
        cursor.execute(query, (brand, rating, quantity, price, model, id))
        db.commit()
        cursor.close()
        db.close()

        return redirect(url_for('WM'))

    appliance = get_appliance_by_id('WM', id)
    return render_template('update_wm.html', appliance=appliance)

@app.route('/update_ac/<int:id>', methods=['GET', 'POST'])
def update_ac(id):
    if request.method == 'POST':
        brand = request.form['brand']
        rating = request.form['rating']
        quantity = request.form['quantity']
        price = request.form['price']
        model = request.form['model']
        
        db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="2005",
            database="gadjets"
        )
        cursor = db.cursor()
        query = """
            UPDATE AC
            SET brand = %s, rating = %s, quantity = %s, price = %s, model = %s
            WHERE id = %s
        """
        cursor.execute(query, (brand, rating, quantity, price, model, id))
        db.commit()
        cursor.close()
        db.close()

        return redirect(url_for('AC'))

    appliance = get_appliance_by_id('AC', id)
    return render_template('update_ac.html', appliance=appliance)

@app.route('/update_tv/<int:id>', methods=['GET', 'POST'])
def update_tv(id):
    if request.method == 'POST':
        brand = request.form['brand']
        rating = request.form['rating']
        quantity = request.form['quantity']
        price = request.form['price']
        model = request.form['model']
        
        db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="2005",
            database="gadjets"
        )
        cursor = db.cursor()
        query = """
            UPDATE TV
            SET brand = %s, rating = %s, quantity = %s, price = %s, model = %s
            WHERE id = %s
        """
        cursor.execute(query, (brand, rating, quantity, price, model, id))
        db.commit()
        cursor.close()
        db.close()

        return redirect(url_for('TV'))

    appliance = get_appliance_by_id('TV', id)
    return render_template('update_tv.html', appliance=appliance)

@app.route('/update_ib/<int:id>', methods=['GET', 'POST'])
def update_ib(id):
    if request.method == 'POST':
        brand = request.form['brand']
        rating = request.form['rating']
        quantity = request.form['quantity']
        price = request.form['price']
        model = request.form['model']
        
        db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="2005",
            database="gadjets"
        )
        cursor = db.cursor()
        query = """
            UPDATE IB
            SET brand = %s, rating = %s, quantity = %s, price = %s, model = %s
            WHERE id = %s
        """
        cursor.execute(query, (brand, rating, quantity, price, model, id))
        db.commit()
        cursor.close()
        db.close()

        return redirect(url_for('IB'))

    appliance = get_appliance_by_id('IB', id)
    return render_template('update_ib.html', appliance=appliance)

if __name__ == '__main__':
    app.run(debug=True)
