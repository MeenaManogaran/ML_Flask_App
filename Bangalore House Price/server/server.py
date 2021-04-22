#import all the libaries and modules
from flask import Flask, request, jsonify,render_template
import warnings
warnings.filterwarnings('ignore')
import util

#flask constructor with the current module
app=Flask(__name__,static_folder="../client",static_url_path="/client",template_folder="../client")

@app.route('/')
def index():
    return render_template("app.html")

#creating two api end points to get the location and post the estimated price
@app.route('/get_location_names')
def get_location_names():
    response=jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/predict_home_price',methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting python server for Home Price Prediction")
    app.run(debug=True)