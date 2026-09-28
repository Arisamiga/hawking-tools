#!/usr/bin/env python3

import requests
import hawking_auth

def main():
	username = input("Username: ").strip()
	password = hawking_auth.get_password(username)
	authenticated_session = hawking_auth.get_authenticated_session(username, password)
	print("Session authenticated (debug)")

if __name__ == "__main__":
	main()
