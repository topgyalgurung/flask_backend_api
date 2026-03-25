#This code needs to be run in a separate cell
# --- Setting up the '/create' Route ---
 
# Import the necessary library for handling web requests
from flask import request
from flask import jsonify

@app.route('/employees')
def get_employees():
    """
	This function handles GET requests to the '/employees' route.
	It retrieves all employees from the database and returns them
	as a JSON response.
	"""

	# --- Retrieving All Employees ---
 
	# Query the database to get all employee records

    employees = Employee.query.all()
    # --- Formatting the Response ---

    # Convert the results to a list of dictionaries for easier display
# This makes it easier to display the data in a structured format
    employee_list = [{'id': emp.id, 'name': emp.name, 'email': emp.email, 'department': emp.department} for emp in employees]
# Return the employee data as a JSON response
    return jsonify(employee_list)

# --- Setting up the '/employees/<int:employee_id>' Route ---

@app.route('/employees/<int:employee_id>')
def get_employee(employee_id):
    """
	This function handles GET requests to the '/employees/<int:employee_id>' route.
	It retrieves a specific employee from the database based on their ID.
	"""
 
	# --- Retrieving a Specific Employee ---
 
	# Query the database to get the employee with the given ID
	# If no employee is found with that ID, return a 404 Not Found error

    employee = Employee.query.get_or_404(employee_id)
# --- Formatting the Response ---
 
	# Return the employee data as a JSON response

    return jsonify({'id': employee.id, 'name': employee.name, 'email': employee.email, 'department': employee.department})
# --- Simulating Requests in Jupyter ---
 
# Simulate a GET request to '/employees' to retrieve all employees

with app.test_request_context(path='/employees', method='GET'):
    print(get_employees())
# Simulate a GET request to '/employees/1' to retrieve employee with ID 1

with app.test_request_context(path='/employees/1', method='GET'):
    print(get_employee(1))

#  CREATE Route

@app.route('/create', methods=['POST'])
def create_employee():
    """
	This function handles POST requests to the '/create' route.
	It simulates adding a new employee to the database.
 
	In a real-world application, the employee data would be
	collected from an HTML form submitted by the user.
	"""
 
	# --- Simulating Form Data ---

    #Normally this data would come from a form submitted by the user
# Here, we simulate the form data within the Jupyter Notebook.
    name = request.form.get('name')
    email = request.form.get('email')
    department = request.form.get('department')
    # --- Creating and Adding the Employee ---
 
	# Create a new Employee object with the provided data 
  
    new_employee = Employee(name=name, email=email, department=department)
    # Add the new employee to the database session

    db.session.add(new_employee)
# Commit the changes to the database to persist the data
    db.session.commit()
    return "Employee added successfully!"

#Jupyter does not run a persistent web server by default. We'll use app.test_request_context() to simulate a request:
#Since we are in a Jupyter Notebook, let's simulate a form submission
#This code needs to be run in a separate cell
with app.test_request_context(path='/create', method='POST', 
                           data={'name': 'John Doe', 'email': 'john.doe@example.com', 'department': 'IT'}):
    # Call the 'create_employee' function to process the simulated request

    print(create_employee())