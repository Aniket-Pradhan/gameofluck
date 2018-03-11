import random
from flask import Flask, redirect, render_template, request

app = Flask(__name__)
var=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
lis=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
i=0
n=0
c=0
p=0
s1=0
s2=0


@app.route('/')
def first():
	return render_template('first2.html', url1 = '/p1', url2 = '/p2' )

@app.route('/first')
def firsty():
	global arr
	global var
	for i in range(25):
		var[i]=random.randint(1, 2)
	return render_template('first.html', url1 = '/p1', url2 = '/p2')

@app.route('/second')
def secondy():
	global arr
	global var
	for i in range(25):
		var[i]=random.randint(1, 3)
	return render_template('first.html', url1 = '/p1', url2 = '/p2')

@app.route('/third')
def thirdy():
	global arr
	global var
	for i in range(25):
		var[i]=random.randint(1, 4)
	return render_template('first.html', url1 = '/p1', url2 = '/p2')

@app.route('/p1', methods = ["POST","GET"])
def startgame1():
	global n
	global s1
	global p
	global c
	method = request.method
	if method == "POST":
		x1 = request.form["xmove"]
		lis[int(x1)-1]+=1
		print (x1)
		n = int(var[int(x1)-1])
		p+=1
	if p>0 and n==c:
		s1+=1
	return render_template('p1.html', num = n, var=var, lis=lis, score=s1)	

@app.route('/p2', methods = ["POST","GET"])
def startgame2():
	global c
	global n
	global p
	global s2
	method = request.method
	if method == "POST":
		x1 = request.form.get("xmove")
		lis[int(x1)-1]+=1
		print(x1)
		c = int(var[int(x1)-1])
		p+=1
	if p>0 and 	c==n:
		s2+=1
	return render_template('p2.html', num =c, var=var, lis=lis, score=s2)

@app.route('/ins.txt')
def inst():
	return render_template('ins.txt')
	
@app.route('/check')
def checker():
	global p
	if p%2==0:
		return '1'
	else:
		return '0'


if __name__ == '__main__':
      app.run(debug=True,host='0.0.0.0')
