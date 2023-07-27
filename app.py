import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle


app = Flask(__name__)
classifier_major_dt = pickle.load(open('classifier_major_dt.pkl','rb'))
classifier_major_knn = pickle.load(open('classifier_major_knn.pkl','rb'))
classifier_major_svm = pickle.load(open('classifier_major_svm.pkl','rb'))
classifier_major_rf = pickle.load(open('classifier_major_rf.pkl','rb'))
classifier_major_NB = pickle.load(open('classifier_major_NB.pkl','rb'))


@app.route('/')


@app.route('/index')
def home():
    return render_template("index.html")
  
@app.route('/predict',methods=['GET'])
def predict():
    
    Gender = int(request.args.get('Gender') or 1)
      
      
    Age = int(request.args.get('Age'))
    
    
    hypertension = (request.args.get('hypertension') or 1)
    if hypertension=="High":
      hypertension = 1
    else:
      hypertension = 0
    
    heart_disease = (request.args.get('heart_disease') or 1)
    if heart_disease=="Yes":
      heart_disease = 1
    else:
      heart_disease = 0
      
      
    married = (request.args.get('married') or 1)
    if married=="Yes":
      married = 1
    else:
      married = 0
      
    work_type = (request.args.get('work_type') or 1)
    if work_type=="children":
      work_type = 1
    elif work_type=="Private":
      work_type = 2
    elif work_type=="Self emplyed":
      work_type = 3
    else:
      work_type==0
      
      
    residence_type = (request.args.get('residence_type') or 1)
    if residence_type=="Urban":
      residence_type = 1
    else:
      residence_type==0
    
    Avg_glucose_level = int(request.args.get('Avg_glucose_level') )
    bmi = int(request.args.get('bmi'))
    
    
    Smoking_status = int(request.args.get('Smoking_status') or 1)
    if Smoking_status=="Formerly":
      Smoking_status = 1
    elif Smoking_status=="never":
      Smoking_status = 2
    else:
      Smoking_status==0
    
    
    

# CreditScore	Geography	Gender	Age	Tenure	Balance	NumOfProducts	HasCrCard	IsActiveMember	EstimatedSalary	
    Model = (request.args.get('Model'))

    if Model=="Decision_Tree":
      prediction = classifier_major_NB.predict([[Gender, Age, hypertension, heart_disease, married, work_type, residence_type, Avg_glucose_level, bmi, Smoking_status]])

    elif Model=="KNN":
      prediction = classifier_major_NB.predict([[Gender, Age, hypertension, heart_disease, married, work_type, residence_type, Avg_glucose_level, bmi, Smoking_status]])

    elif Model=="SVM":
      prediction = classifier_major_NB.predict([[Gender, Age, hypertension, heart_disease, married, work_type, residence_type, Avg_glucose_level, bmi, Smoking_status]])
    
    elif Model=="Random_Forest":
      prediction = classifier_major_NB.predict([[Gender, Age, hypertension, heart_disease, married, work_type, residence_type, Avg_glucose_level, bmi, Smoking_status]])

    elif Model=="Naive_Bayes":
      prediction = classifier_major_NB.predict([[Gender, Age, hypertension, heart_disease, married, work_type, residence_type, Avg_glucose_level, bmi, Smoking_status]])

    
    if prediction == [1]:
      return render_template('index.html', prediction_text='stroke chances', extra_text =" as per Prediction by model " + Model)
    
    else:
      return render_template('index.html', prediction_text='No stroke chances', extra_text ="as per Prediction by model " + Model)


if __name__ == "__main__":
    app.run(debug=True)
