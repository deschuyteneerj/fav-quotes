from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:root@localhost/quotes'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://gzbxhmegnmjpql:420246b6464555cab2c2f11bffd29c74671daa6ab71326eb73ac6cecb9a03705@ec2-34-251-245-108.eu-west-1.compute.amazonaws.com:5432/d14ookjqn3t925'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class FavQuotes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(30))
    quote = db.Column(db.String(2000))


@app.route('/')
def index():
    result = FavQuotes.query.all()
    return render_template('index.html', result=result)


@app.route('/quotes')
def quotes():
    return render_template('quotes.html')


@app.route('/process', methods=['POST'])
def process():
    author = request.form['author']
    quote = request.form['quote']
    quotedata = FavQuotes(author=author, quote=quote)
    db.session.add(quotedata)
    db.session.commit()
    return redirect(url_for('index'))
