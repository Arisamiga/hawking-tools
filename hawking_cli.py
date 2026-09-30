#!/usr/bin/env python3

import sys
import requests
import hawking_auth
import hawking_upload
from pathlib import Path
import time

def main():
	display_welcome()
	
	username = input("Username: ").strip()
	password = hawking_auth.get_password(username)
	hawking_auth.authentication_flow(username, password)
	authenticated_session = hawking_auth.get_authenticated_session(username, password)

	while True:
		command = input("Enter a command: ")
		if command == "exit":
			sys.exit()
		if command.split(" ")[0] == "upload":
			hawking_upload.bulk_upload(authenticated_session, Path(".").glob(command.split(" ")[1]))
			time.sleep(1)

def display_welcome():
	print(r"""
			 _   _                _    _                ____ _     ___ 
			| | | | __ ___      _| | _(_)_ __   __ _   / ___| |   |_ _|
			| |_| |/ _` \ \ /\ / / |/ / | '_ \ / _` | | |   | |    | | 
			|  _  | (_| |\ V  V /|   <| | | | | (_| | | |___| |___ | | 
			|_| |_|\__,_| \_/\_/ |_|\_\_|_| |_|\__, |  \____|_____|___|
			                                   |___/                   
	""")


if __name__ == "__main__":
	main()
