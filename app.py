from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/odoo12_T1"
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class SaleOrder(db.Model):
    __tablename__ = 'sale_order'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    state = db.Column(db.String())

    def __init__(self, name, state):
        self.name = name
        self.state = state

    def __repr__(self):
        return f"<Order {self.name}>"

if __name__ == '__main__':
    app.run(debug=True)