from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import psycopg2
import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

app = FastAPI()

# Static folder
app.mount("/static", StaticFiles(directory="static"), name="static")

# Database URL
DATABASE_URL = os.getenv("DATABASE_URL")


# Database connection
def get_connection():
    return psycopg2.connect(DATABASE_URL)


# Home Page
@app.get("/", response_class=HTMLResponse)
async def home():

    return """
    <!DOCTYPE html>
    <html>

    <head>
        <title>Hotel Booking Form</title>

        <link rel="stylesheet" href="/static/style.css">
    </head>

    <body>

        <div class="container">

            <h1>Hotel Booking Form</h1>

            <form action="/book" method="post">

                <input type="text" name="full_name" placeholder="Full Name" required>

                <input type="email" name="email" placeholder="Email" required>

                <input type="text" name="phone" placeholder="Phone Number" required>

                <label>Check In Date</label>
                <input type="date" name="check_in" required>

                <label>Check Out Date</label>
                <input type="date" name="check_out" required>

                <input type="text" name="room_type" placeholder="Room Type" required>

                <input type="number" name="guests" placeholder="Number of Guests" required>

                <textarea name="special_requests" placeholder="Special Requests"></textarea>

                <button type="submit">Book Now</button>

            </form>

        </div>

    </body>

    </html>
    """


# Booking Route
@app.post("/book")
async def book(
    full_name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
    check_in: str = Form(...),
    check_out: str = Form(...),
    room_type: str = Form(...),
    guests: int = Form(...),
    special_requests: str = Form("")
):

    try:

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO bookings
            (
                full_name,
                email,
                phone,
                check_in,
                check_out,
                room_type,
                guests,
                special_requests
            )

            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            full_name,
            email,
            phone,
            check_in,
            check_out,
            room_type,
            guests,
            special_requests
        ))

        conn.commit()

        cursor.close()
        conn.close()

        return HTMLResponse("""

        <html>

        <head>
            <link rel="stylesheet" href="/static/style.css">
        </head>

        <body>

            <div class="success-box">

                <h1>Booking Saved Successfully!</h1>

                <a href="/">Go Back</a>

            </div>

        </body>

        </html>

        """)

    except Exception as e:

        print(e)

        return HTMLResponse(
            content=f"<h1>Error:</h1><p>{e}</p>",
            status_code=500
        )