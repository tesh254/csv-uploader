from flask import Flask
from celery import Celery
from flask import render_template, request, url_for

app = Flask(__name__)

app.config["CELERY_BROKER_URL"] = "redis://localhost:6379/0"
app.config["CELERY_RESULT_BACKEND"] = "redis://localhost:6379/0"

celery = Celery(app.name, broker=app.config["CELERY_BROKER_URL"])

celery.conf.update(app.config)

ALLOWED_EXTENSIONS = {"csv"}


@app.route("/")
def index():
    return render_template("home.html", title="CSV Uploader", desription="Upload any CSV file")

@app.route("/", methods=["POST"])
def upload_csv():
    pass

if __name__ == "__main__":
    app.run()
