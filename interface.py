from flask import Flask,jsonify,request,render_template
from project_app.utils import MedicalInsurance

import config

app = Flask(__name__)
#############################################################################################
################################ Home API ###################################################
#############################################################################################

@app.route("/")   # Home API
def hello_flask():
    print("Welcome to flask")
    #return "Hello Python"
    return "Hello Python"
    

#############################################################################################
################################ Test API ###################################################
#############################################################################################
@app.route("/predict_charges")
def get_insurance_charges():

    
    age  = 19
    sex  = 'male'
    bmi  = 25 
    children = 2
    smoker = 'yes'
    region = 'southwest'

    med_ins = MedicalInsurance(age,sex,bmi,children,smoker,region)
    charges = med_ins.get_predict_charges()

    return jsonify({"Return" : f"Predicted medical isurance charges are :{charges}"})



if __name__ == "__main__":
    app.run( )  # server start