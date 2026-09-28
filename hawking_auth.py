#!/usr/bin/env python3

import requests
import keyring
import sys
from getpass import getpass

def get_password(username):
	password = keyring.get_password("hawking-tools", username)

	if password is None or not is_valid_login(username, password):
		password = getpass("Password: ")

		if is_valid_login(username, password):
			keyring.set_password("hawking-tools", username, password)
		else:
			# todo: will make a more robust system for this soon, that allows n attempts before restart
			sys.exit("Incorrect password. Please restart the CLI and try again.")

	return password

def is_valid_login(username, password):
	session = requests.Session()
	session.auth = (username, password)

	auth_check = session.get("https://hawking.computing.dcu.ie/api/auth", timeout=10)

	if auth_check.status_code == 200:
		return True

	return False

def get_authenticated_session(username, password):
	session = requests.Session()
	session.auth = (username, password)
	return session

if __name__ == "__main__":
	main()
