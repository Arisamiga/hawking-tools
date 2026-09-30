#!/usr/bin/env python3

import requests
import hawking_auth
import hawking_upload

def main():
	username = input("Username: ").strip()
	password = hawking_auth.get_password(username)
	hawking_auth.authentication_flow(username, password)
	authenticated_session = hawking_auth.get_authenticated_session(username, password)

	hawking_upload.upload_file(authenticated_session, "rev.py")

if __name__ == "__main__":
	main()
