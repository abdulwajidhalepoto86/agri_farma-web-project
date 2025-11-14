🌾 Agri_Farma – Flask Web Application

Agri_Farma is a modular Flask-based web platform that includes user authentication, forums, blogs, shop features, admin tools, and expert support. It follows an app factory pattern, uses Flask-Login, and organizes logic through blueprints.

📁 Project Structure (Important)
Agri_Farma/
│── app.py                     # Entry point
│── config.py                  # App configuration
│── models/
│   ├── __init__.py
│   ├── db.py                  # SQLAlchemy init
│   ├── user_model.py
│   ├── post_model.py
│   └── ... more models
│
│── routes/
│   ├── auth_routes.py
│   ├── forum_routes.py
│   ├── blog_routes.py
│   ├── shop_routes.py
│   ├── admin_routes.py
│   ├── user_routes.py
│   └── expert_routes.py
│
│── templates/
│── static/
│── instance/
│── .env
│── requirements.txt
│── README.md

⚙️ Environment Variables (.env)

Create a .env file in the project root:

FLASK_ENV=development
SECRET_KEY=your_secret_key

# Database
SQLALCHEMY_DATABASE_URI=mysql+pymysql://user:password@localhost/agri_farma
SQLALCHEMY_TRACK_MODIFICATIONS=False

# Uploads
UPLOAD_FOLDER=uploads/


Ensure the folder in UPLOAD_FOLDER exists or let the app auto-create it (your code already does this).

🛠 Installation & Setup
1. Clone the repository
git clone https://github.com/your-username/agri_farma.git
cd agri_farma

2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

3. Install dependencies
pip install -r requirements.txt

4. Create the database

(MySQL example)

CREATE DATABASE agri_farma;

🗄 Database Migration Steps

Your code uses:

db.create_all()


…which creates tables automatically.
If you prefer migrations, enable Flask-Migrate.

Option A — Auto-create tables (default)

Nothing to run. The code:

with app.app_context():
    db.create_all()


creates all models and inserts default categories.

Option B — Use Flask-Migrate (recommended for production)

Install:

pip install Flask-Migrate


Initialize:

flask db init


Generate migration:

flask db migrate -m "initial tables"


Apply migration:

flask db upgrade

▶️ Running the App
1. Run with python
python app.py


or if using FLASK CLI:

flask run

Default URL:

👉 http://127.0.0.1:5000/

🧠 How the App Works (Blueprints + App Factory)

Your create_app() function:

Loads config (config.Config)

Ensures upload folder exists

Initializes SQLAlchemy

Registers these blueprints:

auth_bp – authentication

forum_bp – community forum

blog_bp – blog module

shop_bp – e-commerce

admin_bp – admin dashboard

user_bp – user profile features

expert_bp – agricultural experts system

Loads user via Flask-Login

Creates database tables

Inserts default blog categories (Wheat, Rice, Vegetables, Fruits, General)

Homepage

Loads latest 5 blog posts:

latest_posts = Post.query.order_by(Post.created_at.desc()).limit(5).all()

🧪 Testing (Optional)
pytest

🙌 Contributing

Fork the repo

Create a new branch

Commit changes

Push & open PR

📜 License

MIT License.

If you want, I can also generate:

✅ ER Diagram
✅ API Documentation (REST endpoints for all blueprints)
✅ A full requirements.txt
✅ Dockerfile + docker-compose
