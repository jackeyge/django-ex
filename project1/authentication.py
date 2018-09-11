#!/usr/bin/env pyhton
'''
This is test
'''

def login(username, password):
	try:
		user_file = open('users.txt')
		user_buf = user_file.read()
		user = [line.split("|") for line in user_buf.split("\n")]
		if [username, password] in user:
			return True
		else:
			return False
	except Exception, exc:
		print "I can't authenticate you."
		return False
	
def logout():
	print 'test'
	print 'test2'
	
	
