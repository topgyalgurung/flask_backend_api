
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLAlCHEMY_DATABASE_URL'] = 'sqlite:///my_flask_app.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)   
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %> ' % self.username


# create 

with app.app_context():
    db.create_all()

new_user = User(username='johndoe', email='johndoe@example.com')
db.session.add(new_user)
db.session.commit()


# Read 
all_users = User.query,all()
for user in all_users:
    print(user.username, user.email)

# Update
user = User.query.filter_by(username="johndoe").first()
user.email = 'newemail@example.com'
db.session.commit()

# delete
user = User.query.filter_by(username="johndoe").first()
db.session.delete(user)
db.session.commit()

# filtering 
user = User.query.filter_by(user.email.endswith('@gmail.com')).all()

# ordering 
users_by_username = User.query.order_by(User.username).all()

# limiting 
first_two_users = User.query.limit(2).all()

#counting 
total_users = User.query.count()

# Error handling 

try:
    db.session.add(new_user)
    #...other database operations
    db.session.commit()
except:
    db.session.rollback()
    print(f"Error: {e}")


# filtering with complex calculations
active_customers = session.query(Customer).filter(Customer.is_active == True).all()

# complex filtering with multiple operators 
from datetime import datetime, timedelta

thirty_days_ago = datetime.now() - timedelta(days=30)

customers = session.query(Customer).filter(
    or_(
        and_(Customer.is_active == True, Customer.last_purchase_date >= thirty_days_ago),
        Customer.is_vip == True
    )
).all()

# retrieve all order by customers in a specific city 
orders = session.query(Order).join(Customer).filter(Customer.city == 'New York').all()


# sorting results 
customers = session.query(Customer).order_by(Customer.last_name).all()

# obtain latest data 
orders = session.query(Order).order_by(Order.order_date.desc()).all()

# sort multiple columns 
customers = session.query(Customer).order_by(Customer.city, Customer.last_name).all()

# aggregate data 
total_orders = session.query(func.count(Order.id)).scalar()