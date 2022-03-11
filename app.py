from flask import Flask,Response,jsonify, render_template ,logging,request
app = Flask(__name__)

@app.route('/')
def home():
    return "<p>Hello, World!</p>"

#run server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)