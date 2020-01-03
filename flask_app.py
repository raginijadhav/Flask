from flask import Flask, render_template,request
import numpy
import pickle
app=Flask(__name__)
@app.route('/')
def hello_World():
        return render_template('flaskhtml.html')
@app.route('/predict',methods=['POST'])
def get_result():
        poly=pickle.load(open('poly.pkl','rb'))
        model=pickle.load(open('model.pkl','rb'))
        query=[[float(request.form['text2'])]]
        X_query=poly.transform(query)
        sal=model.predict(X_query)
        return 'Dear'+request.form["text1"]+ 'your predicted salary after'+request.form["text2"]+'Experience is:'+str(sal)

if __name__=='__main__':
    app.run(debug=True)
    