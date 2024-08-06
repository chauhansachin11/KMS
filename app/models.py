from datetime import datetime
from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.Integer, db.ForeignKey('store.id'), nullable=False)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(120), index=True, unique=True)
    role = db.Column(db.String(64))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Store(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    address = db.Column(db.String(256))

class CommonMedicine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    manufacturer_name = db.Column(db.String(128))
    type = db.Column(db.String(128))
    pack_size_label = db.Column(db.String(128))
    short_composition = db.Column(db.String(256))

class StoreMedicineBatch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.Integer, db.ForeignKey('store.id'), nullable=False)
    common_medicine_id = db.Column(db.Integer, db.ForeignKey('common_medicine.id'), nullable=False)
    batch_number = db.Column(db.String(128))
    quantity = db.Column(db.Integer)
    manufacturer_date = db.Column(db.Date)
    expiry_date = db.Column(db.Date)
    HSN_number = db.Column(db.String(128))
    wholesale_price = db.Column(db.Float)
    sale_retail_price = db.Column(db.Float)
    maximum_retail_price = db.Column(db.Float)
    supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.id'), nullable=False)
    added_date = db.Column(db.Date, default=datetime.utcnow)
    __table_args__ = (db.UniqueConstraint('store_id', 'common_medicine_id', 'batch_number', name='uix_store_medicine_batch'),)

class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    contact_person = db.Column(db.String(128))
    phone = db.Column(db.String(128))
    email = db.Column(db.String(128))
    address = db.Column(db.String(256))

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    phone = db.Column(db.String(128))
    email = db.Column(db.String(128))
    address = db.Column(db.String(256))

class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    date = db.Column(db.Date, default=datetime.utcnow)
    total_amount = db.Column(db.Float)

class InvoiceItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    invoice_id = db.Column(db.Integer, db.ForeignKey('invoice.id'), nullable=False)
    store_medicine_batch_id = db.Column(db.Integer, db.ForeignKey('store_medicine_batch.id'), nullable=False)
    quantity = db.Column(db.Integer)
    price = db.Column(db.Float)
    expiry_date = db.Column(db.Date)
    maximum_retail_price = db.Column(db.Float)
    manufacturer_date = db.Column(db.Date)
