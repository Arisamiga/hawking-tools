#!/usr/bin/env python3

import requests
import hawking_tasks
from pathlib import Path

api_base = "https://hawking.computing.dcu.ie/api"
upload_url = api_base + "/upload"
tasks_path = api_base + "/tasks"

def upload_file(authenticated_session, file):
	file_upload = {"file": open(file, "rb")}
	module = hawking_tasks.get_module_from_task(authenticated_session, file)

	file = Path(file).name

	print(f"Uploading {file}...")
	try:
		request = authenticated_session.post(f"{upload_url}/{module}/{file}", files=file_upload, timeout=10)
		#print(request.text)
		hawking_tasks.display_task_info(request.text)
	except requests.exceptions.ReadTimeout:
		print("Request timed out while uploading {file}. Try again.")
		return

	if request.status_code == 200:
		print(f"Successfully uploaded {file}!")

def bulk_upload(authenticated_session, files):
	for file in files:
		upload_file(authenticated_session, file)

if __name__ == "__main__":
	main()
