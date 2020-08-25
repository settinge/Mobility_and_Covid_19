import sqlalchemy 
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from flask import Flask,  jsonify, render_template

app = Flask(__name__,template_folder='template')

    #replace the user, password, hostname and database according to your configuration according to your information
  
user = 'fnndwadhzybkmd'
password = 'a1dc1d35a0e00e4bed93cdd9abe243c4dd462d33f649a3adaa6298b6fe38c967'

rds_connection_string = f"{user}:{password}@ec2-54-156-121-142.compute-1.amazonaws.com:5432/d2tr0g56o6acrq"
engine = create_engine(f'postgresql://{rds_connection_string}')
# def __init__(self):
#     self.connection = self.engine.connect()
#     print("DB Instance created")
    
# def fetchByQyery(self, query):
#     fetchQuery = self.connection.execute(f"SELECT * FROM mobility")
        
#     for data in fetchQuery.fetchall():
#         print(data)

Base = automap_base()

Base.prepare(engine, reflect=True)
Base.classes.keys()
# Mob=Base.classes.mobility

# Base = automap_base()
# rds_connection_string = f"{user}:{password}@localhost:5432/mobility_db"
# engine = db.create_engine(f'postgresql://{rds_connection_string}')

# Base.prepare(engine, reflect=True)            
# Meas = Base.classes.mobility

# session = Session(engine)
# max_date=session.query(Meas.date)
# print(max_date)
mob_result=engine.execute('select * from covid')
# for row in mob_result:
#     print(row)
    
@app.route("/")
def welcome():
    # qu= "select * from mobility"
    # transit = engine.execute(qu)
    
    # for row in transit:
    #     transit= {"transit_type":row[0]}
    #     transit=jsonify(transit)
    #whatever you get back from the database
    return render_template('Pract.html')

    # """List all available api routes."""
    # return (
    #     f"Available Routes:<br/>"
    #     f"/api/v1.0/mobility<br/>"

@app.route('/rate_of_change_visualization.html')
def viz(): 
    return render_template('rate_of_change_visualization.html')

@app.route('/Mobility_Scores_Over_Time.html')
def vi():
    return render_template('Mobility_Scores_Over_Time.html')
@app.route('/Landing.html')
def v():
    return render_template('Landing.html')
@app.route('/machine_learning.html')
def a():
    return render_template('machine_learning.html')
 
@app.route("/fetch")   
def fetch():
    query="select * from covid"
    data=engine.execute(query)
    mob_list=[]
    for row in data:
        toAppend={"geo_type":row[0],"region":row[1],"transportation_type":row[2],"score":row[3],"date":row[4]}
        mob_list.append(toAppend)
    data = mob_list
    return jsonify(data)   

# @app.route("/fetch")   
# def fetch():
#     data = #get something from the database
#     return jsonify(data)
    
# @app.route("/api/v1.0/mobility")

# def all_students():
#     qu= "select distinct(geo_type) from mobility"
#     transit = engine.execute(qu)
    
#     for row in transit:
#         transit= {"transit_type":row[0]}
#         # transit_data.append(transit)

#     # transit_data["transit"] = transit_data
#     return jsonify(transit)
# @app.route("/api/v1.0/mob")

# def all_s():
#     que="select * from mobility"




if __name__ == '__main__':
    app.run(debug=True)