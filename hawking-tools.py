#!/usr/bin/env python3

import requests
import hawking_auth

def main():
	username = input("Username: ").strip()
	password = hawking_auth.get_password(username)

	session = requests.Session()
	session.auth = (username, password)

	auth_check = session.get("https://hawking.computing.dcu.ie/api/auth")
	auth_check.raise_for_status()

	print(auth_check)

if __name__ == "__main__":
	main()
