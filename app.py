from flask import Flask, render_template
from config import Config
from models import db
from flask_login import LoginManager
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Ensure upload folder exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    # Initialize database
    db.init_app(app)

    # -------------------------
    # Register Blueprints
    # -------------------------
    from routes.auth_routes import auth_bp
    from routes.forum_routes import forum_bp
    from routes.blog_routes import blog_bp
    from routes.shop_routes import shop_bp
    from routes.admin_routes import admin_bp
    from routes.user_routes import user_bp          # added
    from routes.expert_routes import expert_bp      # added

    app.register_blueprint(auth_bp)
    app.register_blueprint(forum_bp)
    app.register_blueprint(blog_bp)
    app.register_blueprint(shop_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(user_bp)                # added
    app.register_blueprint(expert_bp)              # added

    # -------------------------
    # Login Manager
    # -------------------------
    login_manager = LoginManager(app)
    login_manager.login_view = "auth.login"

    from models.user_model import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # -------------------------
    # Homepage route
    # -------------------------
    @app.route("/")
    def index():
        from models.post_model import Post, Category  # Avoid circular imports
        latest_posts = Post.query.order_by(Post.created_at.desc()).limit(5).all()
        return render_template("index.html", latest_posts=latest_posts)

    # -------------------------
    # Initialize DB & default categories
    # -------------------------
    with app.app_context():
        db.create_all()
        from models.post_model import Category
        if not Category.query.first():
            for name in ["Wheat", "Rice", "Vegetables", "Fruits", "General"]:
                db.session.add(Category(name=name))
            db.session.commit()

    return app

# -------------------------
# Run the app
# -------------------------
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
