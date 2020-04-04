from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'



if __name__ == "__main__": # pragma: no cover
    app.debug = True
    app.run(host='0.0.0.0', port=5001)
