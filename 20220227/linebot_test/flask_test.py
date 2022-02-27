from flask import Flask, request

app=Flask(__name__)

@app.route('/')
def hello():
	name=request.args.get("name","world")
	return f'hello,{name}!'

app.run(host='0.0.0.0',port=8080)