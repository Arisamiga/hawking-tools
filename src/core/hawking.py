#!/usr/bin/env python3

import sys
import hawking_auth
from services import hawking_upload
from pathlib import Path
import time

def main():
	username = hawking_auth.get_username()
	password = hawking_auth.get_password(username)
	hawking_auth.authentication_flow(username, password)
	authenticated_session = hawking_auth.get_authenticated_session(username, password)

	''' Todo: command-based args
	while True:
		user_input = input(". ݁₊ ⊹ . ݁ Enter a command: ")
		if user_input == "exit":
			sys.exit()

		command = user_input.split(" ")[0]

		if command == "upload":
			hawking_upload.bulk_upload(authenticated_session, Path(".").glob(user_input.split(" ")[1]))
			time.sleep(1)
	'''

if __name__ == "__main__":
	main()
