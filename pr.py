from flask import Flask,render_template,request,send_file,redirect
from flask import url_for
import json
import copy
from collections import namedtuple
from flask_sqlalchemy import SQLAlchemy
import os
app=Flask(__name__,static_url_path='/static')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db = SQLAlchemy(app)
phon=0

totals=0
new_dict = {'counts': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'prices': [8401.6, 382, 2987.76, 2466.2, 0, 3790.75, 0, 0, 0, 0, 0], 'titles': ['Problem-Solving Strategies', 'Problem Solving 101', 'Group Problem Solving', 'All Life is Problem Solving', 'Problem Solving and Decision Making', 'Quality Problem Solving', 'Schemas in Problem Solving', 'Made-to-measure Problem-solving', 'Environmental Problem Solving', 'Organization and Management Problem Solving']}
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(80),nullable=True)
    pho = db.Column(db.String(120),nullable=True)
    book_1=db.Column(db.Integer,nullable=True)
    book_2=db.Column(db.Integer,nullable=True)
    book_3=db.Column(db.Integer,nullable=True)
    book_4=db.Column(db.Integer,nullable=True)
    book_5=db.Column(db.Integer,nullable=True)
    book_6=db.Column(db.Integer,nullable=True)
    book_7=db.Column(db.Integer,nullable=True)
    book_8=db.Column(db.Integer,nullable=True)
    book_9=db.Column(db.Integer,nullable=True)
    book_10=db.Column(db.Integer,nullable=True)
    total=db.Column(db.Integer,nullable=True)

    def __init__(self, user,pho,book_1,book_2,book_3,book_4,book_5,book_6,book_7,book_8,book_9,book_10,total):
        self.user = user
        self.pho = pho
        self.book_1=book_1
        self.book_2=book_2
        self.book_3=book_3
        self.book_4=book_4
        self.book_5=book_5
        self.book_6=book_6
        self.book_7=book_7
        self.book_8=book_8
        self.book_9=book_9
        self.book_10=book_10
        self.total=total
           
                


@app.route('/show_books/')
def showbooks():
    return  render_template('app.html')
  

@app.route('/return-files/')
def send_js():
    return send_file('C:/Users/Vikram/Desktop/Project/problem.json',attachment_filename='problem.json')
@app.route('/your/flask/endpoint', methods=['POST','GET'])
def get_names():
    if request.method == 'POST':
        names = request.get_json()
        print(names)
        global totals
        for i in range(0,9):
            new_dict['counts'][i]=names['counts'][i]
            new_dict['prices'][i]=names['prices'][i]
            totals+=new_dict['counts'][i]*new_dict['prices'][i]
            new_dict['titles'][i]=names['titles'][i] 
        print(totals)    
        return '', 200
    else:
        print(new_dict['counts'][0])
        return render_template('index.html',i=new_dict['counts'][0])             
@app.route('/ha/')
def ha():
    print(new_dict)  
    return '', 200
@app.route('/checkout/',methods=['POST','GET'])
def success():
        
        if request.method=='POST':
               global phon
               global totals
               text = request.form['text']
               phon =request.form['phoneno']
               x = User(text,phon,new_dict['counts'][0],new_dict['counts'][1],new_dict['counts'][2],new_dict['counts'][3],new_dict['counts'][4],new_dict['counts'][5],new_dict['counts'][6],new_dict['counts'][7],new_dict['counts'][8],new_dict['counts'][9],totals)
               db.create_all()
               db.session.add(x)
               db.session.commit()
               err="success"  
               output=""
               output+='<h1>'+err+'</h1>'
               return output
        else:         
            
            z=totals*10
            totals=totals+z/100
            return render_template('index.html',title=new_dict['titles'],count=new_dict['counts'],price=new_dict['prices'],total=totals)  
@app.route('/show_orders/',methods=['POST','GET'])
def showorders():
         if request.method=='POST':
               text = request.form['text']
               phon =request.form['phoneno']
               spinach = db.session.query(User).filter_by(user = text).filter_by(pho = phon).all()
               if len(spinach)==0:
                       err="No data found"
                       output=""
                       output+='<h1>'+err+'</h1>'
                       return output
               else:    
                   return render_template('ha.html',sp=spinach,title=new_dict['titles'],price=new_dict['prices'])
         else:      
               return render_template('pos.html')
                  

if __name__=='__main__':
        
        app.debug=True
        app.run(host="0.0.0.0",port=5000)