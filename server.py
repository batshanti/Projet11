import json
import os
from datetime import datetime
from flask import Flask, render_template, request, redirect, flash, url_for


def loadClubs(data):
    with open(data) as c:
        listOfClubs = json.load(c)['clubs']
        return listOfClubs


def loadCompetitions(data):
    with open(data) as comps:
        listOfCompetitions = json.load(comps)['competitions']
        return listOfCompetitions


app = Flask(__name__)
app.secret_key = 'something_special'

try:
    if os.environ["ENV"] == "TEST":
        competitions = loadCompetitions("tests/test_competitions.json")
        clubs = loadClubs("tests/test_clubs.json")

except KeyError:
    competitions = loadCompetitions('competitions.json')
    clubs = loadClubs('clubs.json')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/showSummary', methods=['POST'])
def showSummary():
    try:
        club = [club for club in clubs if club['email']
                == request.form['email']][0]
        return render_template(
            'welcome.html',
            club=club,
            competitions=competitions,
            date=str(datetime.now())
        )
    except IndexError:
        return render_template(
            'index.html',
            message="Sorry, that email wasn't found"
        )


@app.route('/book/<competition>/<club>')
def book(competition, club):
    try:
        foundClub = [c for c in clubs if c['name'] == club][0]
        foundCompetition = [c for c in competitions if c['name'] == competition][0]
        return render_template(
            'booking.html',
            club=foundClub,
            competition=foundCompetition
        )
    except IndexError:
        flash("Competition or club not found")
        return render_template(
            'welcome.html',
            club=club,
            competition=competitions
        )


@app.route('/purchasePlaces', methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name']
                   == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])
    if int(club['points']) < placesRequired:
        flash("You don't have enough points.")

    elif placesRequired > 12:
        flash("You can't book more than 12 places in a competition.")

    elif placesRequired > int(competition['numberOfPlaces']):
        flash('Not enough places available.')

    else:
        competition['numberOfPlaces'] = int(
            competition['numberOfPlaces']) - placesRequired
        club['points'] = int(club['points']) - placesRequired
        flash('Great-booking complete!')

    return render_template(
        'welcome.html',
        club=club,
        competitions=competitions,
        date=str(datetime.now())
    )


@app.route('/clubs_points')
def point():
    return render_template('clubs_points.html', clubs=clubs)


@app.route('/logout')
def logout():
    return redirect(url_for('index'))




