from flask import Flask,render_template

app=Flask(__name__)
posts=[
    {
        'name':'Ishan Kumar',
        'dob':'17th Jan 1989',
        'city':'Dubai,Duabi State'
    },
    {
        'name':'Vishal Kumar',
        'dob':'13th April 1990',
        'city':'Bangalore,Karnataka'
    }
]
#print(posts)
@app.route('/')
def main():
    return "Hello,how are you"

@app.route('/home')
def index():
    print(posts)
    print("hi JAisw")
    return render_template('index.html',posts=posts)

@app.route('/about')
def about():
    return render_template('about.html',title='About')

if __name__=='__main__':
    app.run(debug=True)