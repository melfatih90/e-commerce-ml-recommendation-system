from flask import Flask
from app.routes import app_routes

# تعريف التطبيق الرئيسي
app = Flask(__name__)
app = Flask(__name__, template_folder='app/templates', static_folder='app/static')
app.secret_key = "4a78d2e0cf37902d849054f4c1631ea83345f1999c3332550e5fe7075f20e318"

# تسجيل الـ Blueprint
app.register_blueprint(app_routes)

# تشغيل التطبيق
if __name__ == "__main__":
    app.run(debug=True)
