from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/process', methods=['POST'])
@cross_origin()
def process():
    #print("hello") # ignore, test print
    data1 = request.get_data()  # data is byte encoded
    #print(data)
    data_str1 = data1.decode('utf-8')  #decode byte data into string
    #print(data_str)
    data_dict1 = json.loads(data_str1) # change string into a dictionary
    print(data_dict1[0])
    #print("hello")
    print(data_dict1[1])
    print(data_dict1[2])
    print(data_dict1[3])
    print(data_dict1[4])
    return(data_dict1)
    

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