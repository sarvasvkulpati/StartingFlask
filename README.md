# StartingFlask



## Getting Started

1. Download the project on your computer.
`
git clone https://github.com/sarvasvkulpati/StartingFlask
`
or download the ZIP file

2. Go to the directory with the file: ``` cd StartingFlask ```

3. Download the required packages: ``` pip install -r requirements.txt ```

4. Run the project: ``` export FLASK_APP=app.py && flask run ```

## What is Flask?

The internet is based on something called the HyperText Transfer Protocol, or HTTP. That's the thing you see in your url all the time.

In essence, it's a set of rules that define how computers on the internet should communicate with each other. 

![web server](https://github.com/sarvasvkulpati/StartingFlask/blob/master/images/webserver.gif)

Everytime you request for information on the internet, there's a 'web server' that serves that information. Flask makes it easy to write the code that powers these.

## Starter Flask Application
Let's begin with the absolute minimum code required to create a flask server.

First, we import flask at the top of the file 
```python
from flask import Flask 
```
Next, we define our current file as our web application 
```python
app = Flask(__name__)
```
Then, we create our root page. The forward slash means that it exists at the base url.
```python
@app.route('/', methods=['GET'])
def root():
    return "Root"
```
And finally, we create the main function
```python
if __name__ == "__main__":
    app.run(debug=True)
```
Now, time to run the file from the terminal. There's two ways of doing this. The easy way is 
```
python3 app.py
```
Though a better way to do it would be 
```
export FLASK_APP=app.py 
export FLASK_DEBUG=1
flask run
```
You should see something like this:
![flask run output](https://github.com/sarvasvkulpati/StartingFlask/blob/master/images/flaskrun.jpg)

You'll notice that it's being served on the url http://127.0.0.1:5000/ . That url is called your localhost, and it uses your computer to internally run a webserver. 
