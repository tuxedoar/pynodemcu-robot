#!/usr/bin/env python

from bottle import route, run, template, SimpleTemplate, post, static_file, error, request
import robot_handler

robot = robot_handler.control()

@route('/static/<path:path>')
def static(path):
	return static_file(path, root='static')

@error(404)
def not_found(error):
	return template('noexiste')

@route('/')
def index():
	return template("index")

@route('/info')
def index():
	return template("info")

@route('/<cmd>', method='POST')
def control_robot(cmd=None):
	if cmd:
		robot.command(cmd)

run(host='0.0.0.0', port=8080, reloader=True)
