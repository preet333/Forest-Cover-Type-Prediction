from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd

scaler = joblib.load("artifacts/data_preprocessing/scaler.pkl")
model = joblib.load("artifacts/training/model.pkl")


app = Flask(__name__)

@app.route('/')
def home(): 
    return render_template("home.html")

@app.route('/predict', methods=["POST"])
def predict():

    gender = request.form['gender']
    married = request.form['Married']
    dependents = request.form['Dependents']
    education = request.form['Education']
    selfemployed = request.form['Self_Employed']
    applicantincome = int(request.form['ApplicantIncome'])
    coapplicantincome = int(request.form['CoapplicantIncome'])
    loanamount = int(request.form['LoanAmount'])
    loanamountterm = int(request.form['LoanAmountTerm'])
    credithistory = request.form['Credit_History']
    propertyarea = request.form['Property_Area']

    if gender == "Female":
        g_f = 1
        g_m = 0
    else:
        g_f = 0
        g_m = 1
   

    if married == "No":
        m_y = 0
        m_n = 1
    else:
        m_y = 1
        m_n = 0

    dep = dependents
    dp = np.zeros(4)
    if dep == '1':
        dp[1] = 1
    elif dep == '2':
        dp[2] = 1
    elif dep == '3+':
        dp[3] = 1
    else:
        dp[0] = 1

    if education == 'Graduate':
        e_g = 1
        e_n = 0
    else:
        e_g = 0
        e_n = 1

    if selfemployed == 'Yes':
        se_n = 0
        se_y = 1
    else:
        se_n = 1
        se_y = 0
        

    if credithistory == "Yes":
        credithistory = 1.0
    else:
        credithistory = 0.0

    prop_area = propertyarea
    pa = np.zeros(3)
    if prop_area == 'Rural':
        pa[0] = 1
    elif prop_area == 'Urban':
        pa[2] = 1
    else:
        pa[1] = 1


    # creating Dataframe for furthuer use
    df_temp = pd.DataFrame(index=[1])
    df_temp['ApplicantIncome'] = applicantincome
    df_temp['CoapplicantIncome'] = coapplicantincome
    df_temp['LoanAmount'] = loanamount
    df_temp['Loan_Amount_Term'] = loanamountterm
    df_temp['Credit_History'] = credithistory
    df_temp['Gender_Female'] = g_f
    df_temp['Gender_Male'] = g_m
    df_temp['Married_No'] = m_n
    df_temp['Married_Yes'] = m_y
    df_temp['Dependents_0'] = int(dp[0])
    df_temp['Dependents_1'] = int(dp[1])
    df_temp['Dependents_2'] = int(dp[2])
    df_temp['Dependents_3+'] = int(dp[3])
    df_temp['Education_Graduate'] = e_g
    df_temp['Education_Not Graduate'] = e_n
    df_temp['Self_Employed_No'] = se_n
    df_temp['Self_Employed_Yes'] = se_y
    df_temp['Property_Area_Rural'] = int(pa[0])
    df_temp['Property_Area_Semiurban'] = int(pa[1])
    df_temp['Property_Area_Urban'] = int(pa[2])

    aa = scaler.transform(df_temp)
    print(aa)
    # scaling test data
    predict = model.predict(aa)

    return render_template('index.html', prediction=predict)
 
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("5000"), debug=True)    

   