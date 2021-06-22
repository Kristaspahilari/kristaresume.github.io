from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
 
@app.route("/fizzbuzz/<int:count_to>")
def count(count_to):
    i = 1
    if (i % 3 == 0) and (i % 5 == 0):
        print("FizzBuzz")
    elif (i % 3 == 0):
        print("Fizz")
    elif (i % 5 == 0):
        print("Buzz")
    else :
        print(i)
    l = list(range(1, count_to + 1))
    
    return render_template('fizzbuzz.html', numbers=l )
    
