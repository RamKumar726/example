# app.py
from apps import create_app, db

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Ensure your database tables are created
    app.run(debug=True)