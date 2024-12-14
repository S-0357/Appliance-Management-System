# Appliance Management System (DBMS Project)

## Overview
The **Appliance Management System** is a database-driven web application designed to manage and maintain records of appliances efficiently. This project showcases the practical implementation of database management principles, providing a user-friendly interface for adding, updating, and deleting appliance details.

## Features
- **Separate Categories:** Includes individual pages for appliances such as Fridges, Washing Machines (WM), Air Conditioners (AC), Televisions (TV), and Iron Boxes (IB).
- **CRUD Operations:** Supports Create, Read, Update, and Delete operations for all appliance records.
- **Dynamic Web Application:** Built using Flask for backend functionality and MySQL for database management.
- **Responsive Design:** Designed to ensure a seamless user experience.

## Technologies Used
- **Frontend:** HTML, CSS (inline styles used for simplicity).
- **Backend:** Flask (Python).
- **Database:** MySQL.
- **Server:** Localhost for testing purposes.

## Database Schema
Each appliance category has the following fields:
1. **ID:** Unique identifier for the appliance.
2. **Brand:** Manufacturer's name.
3. **Model:** Model name or number.
4. **Capacity:** Capacity or size specifications.
5. **Energy Rating:** Energy efficiency rating.
6. **Quantity:** Number of units available.

## Project Setup
### Prerequisites
1. Python installed with Flask library.
2. MySQL server installed and configured.
3. A code editor or IDE (e.g., VS Code, PyCharm).

### Steps to Run the Project
1. **Clone the repository** or download the project files.
2. **Set up the database:**
   - Create a database in MySQL.
   - Import the provided SQL schema and data file to set up the tables.
3. **Install dependencies:**
   ```bash
   pip install flask mysql-connector-python
   ```
4. **Run the Flask app:**
   ```bash
   python app.py
   ```
5. Open your browser and navigate to `http://127.0.0.1:5000` to access the application.

## Usage
1. Navigate to the homepage, which displays categories of appliances.
2. Click on any category to view the respective records.
3. Use the provided buttons to add new records, update existing ones, or delete entries.

## Future Enhancements
- Integrate user authentication for secure access.
- Implement advanced search and filter options.
- Add analytics and reporting features.

## Credits
This project was developed as part of a DBMS course to demonstrate the implementation of database concepts in a real-world application. Special thanks to the guide and peers for their support.



