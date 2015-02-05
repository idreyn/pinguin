#! /usr/bin/python

from pushbullet import *
import os
import sys
import click

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

@click.command()
@click.argument('message',default=False)
@click.argument('detail',default=False)
@click.option('-t', default=False,is_flag=True,help='Set your Pushbullet API token')
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
			sys.exit(0)
	if t:
		home = os.path.expanduser('~')
		if not message or len(message) == 0:
			message = raw_input('Okay, what\'s your token? ')
		try:
			overwrite_token(message)
			print 'Great, it\'s been stored at ~/.pb_token!'
			print 'You can run Pinguin again with your message now.'
		except:
			print 'Failed to write your token to ~/.pb_token' + ' :('
		sys.exit(0)
	push_message(message,detail,get_token())

def push_message(message,detail,token):
	default = 'Pinged from pinguin!'
	try:
		pb = Pushbullet(token)
	except InvalidKeyError:
		print 'Oh no!'
		print 'Looks like your API token at ~/.pb_token is invalid :('
		print 'You can run pinguin with the -t flag to set a new one.'
		sys.exit(0)
	if not message:
		message = default
		detail = ''
	elif not detail:
		detail = ''
	pb.push_note(message,detail)



if __name__ == '__main__':
	main()