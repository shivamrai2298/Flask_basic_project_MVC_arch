from flask import Flask
from controllers.home_controller import home_bp
from controllers.student_controller import student_bp

app = Flask(__name__)
app.secret_key = "123"

# Register Blueprints
app.register_blueprint(home_bp)
app.register_blueprint(student_bp)

if __name__ == "__main__":
    app.run(debug=True)
