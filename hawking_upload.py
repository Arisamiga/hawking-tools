#!/usr/bin/env python3

import requests
import hawking_tasks

api_base = "https://hawking.computing.dcu.ie/api"
upload_url = api_base + "/upload"
tasks_path = api_base + "/tasks"

def upload_file(authenticated_session, file):
	file_upload = {"file": open(file, "rb")}
	module = hawking_tasks.get_module_from_task(authenticated_session, file)

	print("Uploading...")
	try:
		request = authenticated_session.post(f"{upload_url}/{module}/{file}", files=file_upload, timeout=10)
	except requests.exceptions.ReadTimeout:
		print("Request timed out! Try again.")
		return

	if request.status_code == 200:
		print(f"Successfully uploaded {file}!")

if __name__ == "__main__":
	main()
