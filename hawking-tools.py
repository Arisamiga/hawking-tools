#!/usr/bin/env python3

import requests
import keyring
from getpass import getpass

def get_password(username):
	password = keyring.get_password("hawking-tools", username)

	if password is None:
		password = getpass("Password: ")
		keyring.set_password("hawking-tools", username, password)

	return password

def main():
	username = input("Username: ").strip()
	password = get_password(username)

	session = requests.Session()
	session.auth = (username, password)

	auth_check = session.get("https://hawking.computing.dcu.ie/api/auth")
	auth_check.raise_for_status()

	print(auth_check)

if __name__ == "__main__":
	main()
