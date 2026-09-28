#!/usr/bin/env python3

import requests
import keyring
import sys
from getpass import getpass

def get_password(username):
	return keyring.get_password("hawking-tools", username)

def set_password(username, password):
	keyring.set_password("hawking-tools", username, password)

def authentication_flow(username, password):
	while not is_valid_login(username, password):
		password = getpass("Password: ")

	keyring.set_password("hawking-tools", username, password)

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
