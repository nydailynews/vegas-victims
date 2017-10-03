#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import json
from flask import Flask
from flask import Markup
from flask import g, render_template, url_for, redirect, abort, request
from datetime import date, datetime


app = Flask(__name__)
app.debug = True

page = {
    'title': 'Las Vegas Shooting Victims',
    'title_twitter': 'The victims of the shooting in Las Vegas'.decode('utf-8'),
    'url': 'http://interactive.nydailynews.com/project/vegas-victims/',
    'description': 'DESCRIPTION',
    'author': '"NAME", "Interactive Project"',
    'datestamp': '2017-10-03',
    'keywords': 'Las Vegas, mass shooting, gun, violence',
    'keywords_array': '"las vegas","mass shooting","gun","violence"',
    'shareimg': 'http://interactive.nydailynews.com/project/vegas-victims/static/img/vegas-victims.jpg',
    'shareimg_static': 'http://interactive.nydailynews.com/project/mta-funding/static/img/vegas-victims.jpg',
    'shareimgdesc': '',
}

with app.app_context():
    app.url_root = '/'
    app.page = page
    app.sitename = ''

@app.route('/')
def index():
    response = {
        'app': app,
    }
    return render_template('index.html', response=response)

@app.template_filter(name='last_update')
def last_update(blank):
    """ Returns the current date. That means every time the project is deployed,
        the datestamp will update.
        Returns a formatted date object, ala "Friday Feb. 20"
        """
    today = date.today()
    return today.strftime('%A %B %d')

@app.template_filter(name='timestamp')
def timestamp(blank):
    """ What's the current date and time?
        """
    today = datetime.today()
    return today.strftime("%A %B %d, %-I:%M %p")

@app.template_filter(name='ordinal')
def ordinal_filter(value):
    """ Take a number such as 62 and return 62nd. 63, 63rd etc.
        """
    digit = value % 10
    if 10 < value < 20:
        o = 'th'
    elif digit is 1:
        o = 'st'
    elif digit is 2:
        o = 'nd'
    elif digit is 3:
        o = 'rd'
    else:
        o = 'th'
    return '%d%s' % (value, o)
app.add_template_filter(ordinal_filter)

if __name__ == '__main__':
    app.run()
