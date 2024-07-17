#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect, url_for, make_response
from markupsafe import escape
import pymongo
import datetime
from bson.objectid import ObjectId
import os
import subprocess

# instantiate the app
app = Flask(__name__)

# load credentials and configuration options from .env file
# if you do not yet have a file named .env, make one based on the template in env.example
import credentials
config = credentials.get()

# turn on debugging if in development mode
if config['FLASK_ENV'] == 'development':
    # turn on debugging, if in development
    app.debug = True # debug mnode

# make one persistent connection to the database
uri = "mongodb+srv://smi6065:ssundeecrainerbobby1@practicedb.fqgpyy1.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(uri)
db = client.football


# set up the routes

@app.route('/')
def home():
    """
    Route for the home page
    """
    return render_template('index.html')

@app.route('/team', methods=['GET', 'POST'])
def team():
    """
    Route for GET requests to the team page.
    Displays a form users can fill out to select a team and show the players for the team.
    """
    docs = db.statbomb.find({}, {"team_name": 1})
    players = db.statbomb.find({}, {"team_name": 1, "lineup.player_name": 1, "lineup.jersey_number": 1, "lineup.country.name": 1})
    selected_team = None
    if request.method == 'POST':
        selected_team = request.form.get('selected_team')
    return render_template('team.html', docs=docs, players=players, selected_team=selected_team)

@app.route('/getTeam', methods=['GET', 'POST'])
def getTeam():
    """
    Route for GET requests to the team page.
    Displays a form users can fill out to select a team and show the players for the team.
    """
    docs = db.statbomb.find({}, {"team_name": 1})
    players = db.statbomb.find({}, {"team_name": 1, "lineup.player_name": 1, "lineup.jersey_number": 1, "lineup.country.name": 1})
    selected_team = None
    if request.method == 'POST':
        selected_team = request.form.get('selected_team')
        selected_team = db.statbomb.find_one({'team_name': selected_team})
        return render_template('managedb.html', docs=docs, players=players, selected_team=selected_team)
    return render_template('managedb.html', docs=docs, players=players, selected_team=selected_team)

@app.route('/getPlayer', methods=['GET', 'POST'])
def getPlayer():
    """
    Route for GET requests to the team page.
    Displays a form users can fill out to select a team and show the players for the team.
    """
    docs = db.statbomb.find({}, {"team_name": 1})
    players = db.statbomb.find({}, {"team_name": 1, "lineup.player_name": 1, "lineup.jersey_number": 1, "lineup.country.name": 1})
    selected_team = None
    if request.method == 'POST':
        selected_team = request.form.get('selected_team')
        selected_player = request.form.get('myHiddenField')
        selected_team = db.statbomb.find_one({'team_name': selected_team})
        return render_template('managedb.html', docs=docs, players=players, selected_team=selected_team, selected_player=selected_player)
    return render_template('managedb.html', docs=docs, players=players, selected_team=selected_team,selected_player=selected_player)

# route to add a new team to the database
@app.route('/add_team', methods=['POST'])
def add_team():
    team_name = request.form['team_name']
    db.statbomb.insert_one({'team_name': team_name})
    return redirect('/managedb')

# route to render the managedb page
@app.route('/managedb')
def managedb():
    docs = db.statbomb.find({}, {"team_name": 1})
    players = db.statbomb.find({}, {"team_name": 1, "lineup.player_name": 1, "lineup.jersey_number": 1, "lineup.country.name": 1})
    return render_template('managedb.html', docs=docs, teams=docs, players=players)

@app.route('/update_team', methods=['GET', 'POST'])
def update_team():
    team_name = request.form['selected_team']
    """
    Route for GET and POST requests to the update team page.
    Displays a form users can fill out to update a team's information.
    """
    # Get the team from the database
    team = db.statbomb.find_one({'team_name': team_name})
    #if request.method == 'POST':
        # Get the form data
    #    name = request.form['name']
        # Update the team in the database
    #    db.statbomb.update_one({'team_name': team_name}, {'$set': {
    #                                                                'team_name': name}})
    #    flash(f'Team {team_name} updated successfully!', 'success')
    #    return redirect(url_for('managedb'))
    return render_template('managedb.html', team=team)

@app.route('/get_team/<team_name>')
def get_team(team_name):
    team_data = db.statbomb.find_one({"team_name": team_name})
    return jsonify(team_data)

@app.route('/edit_team/<name>', methods=['GET', 'POST'])
def edit_team(name):
    team_data = db.statbomb.find_one({"team_name": name})

    if request.method == 'POST':
        new_name= request.form['new_team_name']
        db.statbomb.update_one({'team_name': name}, {'$set': {'team_name': new_name}})
        return redirect(f'/managedb')

    return render_template('edit.html', docs=docs, teams=docs, players=players)

@app.route('/delete_team/<name>', methods=['GET', 'POST'])
def delete_team(name):
    team_data = db.statbomb.find_one({"team_name": name})

    if request.method == 'POST':
        db.statbomb.delete_one({"team_name": name})
        return redirect(f'/managedb')

    return render_template('delete.html', docs=docs, teams=docs, players=players)

@app.route('/edit_player/<name>', methods=['GET', 'POST'])
def edit_player(name):
    team_data = db.statbomb.find_one({"team_name": team_name, "player_name":name})

    if request.method == 'POST':
        new_name= request.form['new_player_name']
        team_name=request.form['team_name']
        db.statbomb.update_one({'team_name': team_name, "player_name":name}, {'$set': {'player_name': new_name}})
        return redirect(f'/managedb')

    return render_template('edit.html', docs=docs, teams=docs, players=players)

@app.route('/delete_player/<name>', methods=['GET', 'POST'])
def delete_player(name):
    team_data = db.statbomb.find_one({"team_name": name})

    if request.method == 'POST':
        team_name=request.form['team_name']
        db.statbomb.delete_one({"team_name": team_name ,"player_name":name})
        return redirect(f'/managedb')

    return render_template('delete.html', docs=docs, teams=docs, players=players)

if __name__ == '__main__':
    app.run(debug=True)





@app.route('/read')
def read():
    """
    Route for GET requests to the read page.
    Displays some information for the user with links to other pages.
    """
    
    docs = db.exampleapp.find({}).sort("created_at", -1) # sort in descending order of created_at timestamp
    return render_template('read.html', docs=docs) # render the read template


@app.route('/create', methods=['POST'])
def create_post():
    """
    Route for POST requests to the create page.
    Accepts the form submission data for a new document and saves the document to the database.
    """
    name = request.form['fname']
    message = request.form['fmessage']


    # create a new document with the data the user entered
    doc = {
        "name": name,
        "message": message, 
        "created_at": datetime.datetime.utcnow()
    }
    db.exampleapp.insert_one(doc) # insert a new document

    return redirect(url_for('read')) # tell the browser to make a request for the /read route


@app.route('/edit/<mongoid>')
def edit(mongoid):
    """
    Route for GET requests to the edit page.
    Displays a form users can fill out to edit an existing record.
    """
    doc = db.exampleapp.find_one({"_id": ObjectId(mongoid)})
    return render_template('edit.html', mongoid=mongoid, doc=doc) # render the edit template


@app.route('/edit/<mongoid>', methods=['POST'])
def edit_post(mongoid):
    """
    Route for POST requests to the edit page.
    Accepts the form submission data for the specified document and updates the document in the database.
    """
    name = request.form['fname']
    message = request.form['fmessage']

    doc = {
        # "_id": ObjectId(mongoid), 
        "name": name, 
        "message": message, 
        "created_at": datetime.datetime.utcnow()
    }

    db.exampleapp.update_one(
        {"_id": ObjectId(mongoid)}, # match criteria
        { "$set": doc }
    )

    return redirect(url_for('read')) # tell the browser to make a request for the /read route


@app.route('/delete/<mongoid>')
def delete(mongoid):
    """
    Route for GET requests to the delete page.
    Deletes the specified record from the database, and then redirects the browser to the read page.
    """
    db.exampleapp.delete_one({"_id": ObjectId(mongoid)})
    return redirect(url_for('read')) # tell the web browser to make a request for the /read route.

@app.route('/webhook', methods=['POST'])
def webhook():
    """
    GitHub can be configured such that each time a push is made to a repository, GitHub will make a request to a particular web URL... this is called a webhook.
    This function is set up such that if the /webhook route is requested, Python will execute a git pull command from the command line to update this app's codebase.
    You will need to configure your own repository to have a webhook that requests this route in GitHub's settings.
    Note that this webhook does do any verification that the request is coming from GitHub... this should be added in a production environment.
    """
    # run a git pull command
    process = subprocess.Popen(["git", "pull"], stdout=subprocess.PIPE)
    pull_output = process.communicate()[0]
    # pull_output = str(pull_output).strip() # remove whitespace
    process = subprocess.Popen(["chmod", "a+x", "flask.cgi"], stdout=subprocess.PIPE)
    chmod_output = process.communicate()[0]
    # send a success response
    response = make_response('output: {}'.format(pull_output), 200)
    response.mimetype = "text/plain"
    return response

@app.errorhandler(Exception)
def handle_error(e):
    """
    Output any errors - good for debugging.
    """
    return render_template('error.html', error=e) # render the edit template


if __name__ == "__main__":
    #import logging
    #logging.basicConfig(filename='/home/ak8257/error.log',level=logging.DEBUG)
    app.run(debug = True)