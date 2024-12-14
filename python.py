import mysql.connector

# Function to connect to MySQL and retrieve products
def get_appliances():
    db = mysql.connector.connect(
        host="127.0.0.1",  # Change if your MySQL is hosted elsewhere
        user="root",  # Your MySQL username
        password="2005",  # Your MySQL password
        database="gadjets"  # Your database name
    )
    
    cursor = db.cursor()
    cursor.execute("SELECT * FROM appliances")  # Query to get all products
    appliances = cursor.fetchall()  # Fetch all products from the result
    for appliance in appliances:
        print(appliance)

    cursor.close()
    db.close()

# Call the function to retrieve and display products
get_appliances()
