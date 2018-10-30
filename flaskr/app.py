from flask import Flask
from blue_prints import bp_list


app = Flask(__name__)

for bp in bp_list:
    app.register_blueprint(bp)

@app.route('/', methods=["GET"])
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':                        
    app.run(host="0.0.0.0", port=5000, debug=True)
