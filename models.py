from extensions import db

class Team(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    contact = db.Column(db.String(120), unique=True, nullable=False)

    # string representation for debugging
    def __repr__(self):
        return '<Team %r>' % self.name
    

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)   
    email = db.Column(db.String(120), unique=True, nullable=False)

# new_user = User(username='johndoe', email='johndoe@example.com')
# db.session.add(new_user)
# db.session.commit()