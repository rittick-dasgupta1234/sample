from flask import Flask, request, render_template

app=Flask("__name__")
 
@app.route('/')
def home():
    return render_template("index.html")
@app.route('/form' , methods=['POST'])
def index():
    if request.method=='POST':
        name=request.form.get("name")
        return "success"
    else:
        return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)
    
