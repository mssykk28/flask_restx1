from flask import Flask

from src.api import bl

app = Flask(__name__)
app.config["RESTX_MASK_SWAGGER"] = False
app.register_blueprint(blueprint=bl, url_prefix="/")

if __name__ == "__main__":
    app.run(debug=True)
