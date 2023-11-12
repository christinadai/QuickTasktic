# how to run flask: make sure you have python3 and flask downloaded,
# do this command: python3 -m flask --app test run
# test is the name of the backend file, change it if file name differs
# while flask is running, copy path the .html file into browser
# input userinput onto website
# click submit
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/process', methods=['POST'])
@cross_origin()
def process():
    #print("hello") # ignore, test print
    data = request.get_data()  # data is byte encoded
    print(data)
    data_str = data.decode('utf-8')  #decode byte data into string
    print(data_str)
    data_dict = json.loads(data_str) # change string into a dictionary
    print(data_dict)
    name = data_dict["name"] #calling parts of the dictionary
    email = data_dict["email"]
    print("Name:", name)
    print("Email:", email)
    return(data_dict)
    

    # Process the data or perform any backend tasks
    # ...

    # Return a response back to the frontend
    # response = {
    #     "status": "success",
    #     "message": "Data received successfully!"
    # }
    # print(response.message)

    # response.headers.add('Access-Control-Allow-Origin', '*')

    # return jsonify(response)

if __name__ == '__main__':
    app.run()