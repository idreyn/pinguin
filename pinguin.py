#! /usr/bin/python

import os
import sys
import argparse
import json
import urllib2
import base64

def overwrite_token(k):
	k = k.strip()
	home = os.path.expanduser('~')
	with open(home + '/.pb_token','w') as file:
		file.write(k )

def get_token():
	home = os.path.expanduser('~')
	try:
		with open(home + '/.pb_token','r') as file:
			token = file.read()
	except IOError:
		return False
	return token.strip()

def main(message,detail,t):
	if not get_token():
		print 'Pinguin looks for your Pushbullet API token at ~/.pb_token.'
		print 'You can get it from https://www.pushbullet.com/account'
		res = raw_input('Do you want to set it now? (y/n) ')
		if res[0].lower() == 'y':
			t = True
			message = raw_input('Okay, what\'s your token? ')
		else:
			print 'Okay, come back when you\'ve found it!'
			return
	if t:
		home = os.path.expanduser('~')
		if not message or len(message) == 0:
			message = raw_input('Okay, what\'s your token? ')
		try:
			overwrite_token(message)
		except:
			print 'Failed to write your token to ~/.pb_token' + ' :('
		print 'Great, your token has been stored in ~/.pb_token!'
		print 'You can run Pinguin again with your message now.'
		return
	push_message(message,detail,get_token())

def push_message(message,detail,token):
	default = 'Pinged from pinguin!'
	if not message:
		message = default
		detail = ''
	elif not detail:
		detail = ''
	url = 'https://api.pushbullet.com/v2/pushes'
	data = {
		'type': 'note',
		'title': message,
		'body': detail
	}
	req = urllib2.Request(url, json.dumps(data), {'Content-Type': 'application/json'})
	req.add_header("Authorization", "Basic %s" % base64.b64encode(token))
	try:
		urllib2.urlopen(req)
	except urllib2.HTTPError as e:
		print 'Oh no!'
		if e.code == 401:
			print 'Looks like your API token at ~/.pb_token is invalid :('
			print 'You can run Pinguin with the -t flag to set a new one.'
		else:
			print 'Pinguin couldn\'t connect to the Pushbullet API'
			print 'Are you connected to the internet?'


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='A tiny Pushbullet CLI')
	parser.add_argument('message',default=False,nargs='*',help='The message you want to push')
	parser.add_argument('-t',action='store_true',default=False,help='Use "-t [TOKEN]" to set your Pushbullet API token')
	args = parser.parse_args()
	message = args.message
	t = args.t
	if message:
		if len(message) > 1:
			message, detail = message[0], ' '.join(message[1:])
		else:
			message = message[0]
			detail = ''
		message = message.strip()
		detail = detail.strip()
	else:
		message = False
		detail = False
	if message and len(message) == 0:
		message = False
	if detail and len(detail) == 0:
		detail = False 
	main(message,detail,t)