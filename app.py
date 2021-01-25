from flask import Flask, render_template, request


import pickle
import numpy as np
import sklearn

app = Flask(__name__)
loan_model = pickle.load(open('loan_model.pkl','rb'))

@app.route('/')
def home():
    return render_template('Predictor.html')

@app.route('/predict',methods=['POST'])
def predict():
    g=request.form['gender']
    if g=='m':
        gender=1.0
    else:
        gender=2.0
    m=request.form['married']
    if m=='y':
        married=1.0
    else:
        married=2.0
    d=request.form['dependents']
    if d=='z':
        dependents=0.0
    elif d=='o':
        dependents=1.0
    elif d=='t':
        dependents=2.0
    else:
        dependents=3.0
    e=request.form['education']
    if e=='g':
        education=1.0
    else:
        education=2.0
    s=request.form['self_employed']
    if s=='y':
        self_employed=1.0
    else:
        self_employed=2.0
    c=request.form['cr_history']
    if c=='y':
        credit_history=1.0
    else:
        credit_history=0.0
    p=request.form['property_area']
    if p=='su':
        property_area=2.0
    elif p=='u':
        property_area=3.0
    else:
        property_area=1.0
        
    final_features = [np.array([gender,married,dependents,education,self_employed,credit_history,property_area])]
    prediction = loan_model.predict(final_features)
    print(prediction)
    if prediction==0:
        return render_template('Predictor.html', prediction_text='Loan can not be approved.')
    else:
        return render_template('Predictor.html', prediction_text='Loan can  be approved.')

if __name__ == "__main__":
    app.run(debug=True)
