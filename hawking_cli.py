#!/usr/bin/env python3

import requests
import hawking_auth
import hawking_upload
from pathlib import Path

def main():
	username = input("Username: ").strip()
	password = hawking_auth.get_password(username)
	hawking_auth.authentication_flow(username, password)
	authenticated_session = hawking_auth.get_authenticated_session(username, password)

	current_path = Path(".")
	hawking_upload.bulk_upload(authenticated_session, current_path.glob("assignments/*.py"))

if __name__ == "__main__":
	main()
