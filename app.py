from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/')
def home():
     return render_template('home.html')

@app.route('/about')
def about():
    return  render_template('about.html')

@app.route('/product')
def product():
    return render_template('product.html')



@app.route('/contact')
def contact():
    return render_template('contact.html')  

@app.route('/login' , methods=['GET','POST'])
def login():
    error = None
    if request.method=='POST':
        if request.form['text']=='user' and request.form['password']=='user':
            return render_template('dashboard.html')
        else:
            error='Wrong username or password'
            return render_template('login.html',error=error) 

    else:
         return render_template('login.html')  



app.add_url_rule('/home','home',home)



if __name__ == '__main__':
    app.run(debug=True)
    