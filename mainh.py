from flask import Flask, render_template, request
from databaseh import db
from modelsh import Booking

app = Flask(__name__)

# Database config (SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotel.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


# Home page
@app.route("/")
def home():
    return render_template("indexh.html")


# Booking route
@app.route("/book", methods=["POST"])
def book():
    name = request.form["name"]
    days = int(request.form["days"])

    price = days * 1000

    new_booking = Booking(name=name, days=days, price=price)
    db.session.add(new_booking)
    db.session.commit()

    return f"Booking confirmed for {name}, Total: {price}"


# Run server
if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)

    import os
from dotenv import load_dotenv
from flask import Flask
from databaseh import db

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    "connect_args": {"sslmode": "require"}
}

db.init_app(app)