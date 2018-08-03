from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    # name = request.form['name']
    # location = request.form['location']
    # language = request.form['language']
    # comment = request.form['comment']
    print(request.form)
    print("Hello Quang")
    return render_template('success.html')

if __name__=="__main__":
    app.run(debug=True) 
