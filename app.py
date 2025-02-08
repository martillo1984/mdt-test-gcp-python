# [START hello-app]
from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=["GET"])
def hello():
  who = request.args.get("who", "World")
  return f"Hola {who}!\n"

if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 8080)
# [END hello-app]
