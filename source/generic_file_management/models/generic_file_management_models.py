'''from generic_user_management import db


class User(db.Model):
    __tablename__ = 'generic_user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    email = db.Column(db.String(150))
    mobile = db.Column(db.String(20))
    password = db.Column(db.String(150))
    tenant_key = db.Column(db.String(100))

    def as_json(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'mobile': self.mobile,
            'password': self.password,
            'tenant_key': self.tenant_key
        }'''
