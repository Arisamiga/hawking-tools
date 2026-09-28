#!/usr/bin/env python3

import keyring
from getpass import getpass

def get_password(username):
	password = keyring.get_password("hawking-tools", username)

	if password is None:
		password = getpass("Password: ")
		keyring.set_password("hawking-tools", username, password)

	return password

if __name__ == "__main__":
	main()
