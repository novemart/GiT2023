from flask import Flask, request

app = Flask(__name__)

# endpoint - part of URL + req specification + function to run
@app.route('/home', methods=['GET'])
def welcome():
    return "Hello World!"

#<> - defines a parameter
@app.route('/home/<name>')
def welcomePerson(name):
    return "Hello "+ name

@app.route('/home', methods=['POST, DELETE'])
def welcome_post():
    data = request.get_json()
    print(data)
    return data['name'] + data['surname']


if __name__=='__main__':
    app.run(debug=True)