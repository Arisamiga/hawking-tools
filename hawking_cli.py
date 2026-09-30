#!/usr/bin/env python3

import sys
import requests
import hawking_auth
import hawking_upload
from pathlib import Path
import time

def main():
	print_file("greeting.txt")

	username = input("Username: ").strip()
	password = hawking_auth.get_password(username)
	hawking_auth.authentication_flow(username, password)
	authenticated_session = hawking_auth.get_authenticated_session(username, password)

	print("To view available commands, type 'help'.")

	while True:
		command = input("Enter a command: ")
		if command == "exit":
			sys.exit()

		if command == "upload":
			hawking_upload.bulk_upload(authenticated_session, Path(".").glob(command.split(" ")[1]))
			time.sleep(1)
		elif command == "help":
			print_file("manual.txt")

def print_file(file):
	with open(file, "r") as f:
		print(f"\n{ f.read() }\n")

if __name__ == "__main__":
	main()
