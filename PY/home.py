from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class  Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(40), nullable=False)
    apellido = db.Column(db.String(40), nullable=False)
    razonSocial = db.Column(db.String(40), nullable=False)
    direccion = db.Column(db.String(40), nullable=False)
    pais = db.Column(db.String(40), nullable=False)
    codigoPostal = db.Column(db.Integer(40), nullable=False)
    //faltan deff


class  Factura(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idCliente = db.Column(db.Integer, nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)
    idConcepto = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Integer, nullable=False)
    iva = db.Column(db.Integer, nullable=False)
    baseImponible = db.Column(db.Integer, nullable=False)
    //faltan deff


class  Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    concepto = db.Column(db.String(40), nullable=False)
    precioUnidad = db.Column(db.Integer, nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Integer, nullable=False)
    //faltan deff