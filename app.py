from flask import Flask , render_template , request
app = Flask(__name__) # interface between my server and my application 
import pickle
model = pickle.load(open('/Users/sanjaytulabandula/Desktop/DataScienceProject/model.pkl' , 'rb'))

@app.route('/')# binds to an url
def helloworld():
    return render_template("index.html")

@app.route('/login' , methods = ['POST'])# binds to an url
def login():
    p = request.form["ag"]
    s = request.form["s"]
    
    b = request.form["bm"]
    c = request.form["ch"]
    sm = request.form["sm"]
        
    rg = request.form["rg"]

        
    t=[[int(p),int(s),float(b),int(c),int(sm),int(rg)]]
    output= model.predict(t)
    print(output)
    
    return render_template("index.html" , Y = "The predicted Insurance Cost is " + str(output[0]))
if __name__ == '__main__' :
    app.run(debug= True)
    
        
    