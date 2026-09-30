#!/usr/bin/env python3

api_base = "https://hawking.computing.dcu.ie/api"
upload_url = api_base + "/upload"
tasks_path = api_base + "/tasks"
module_from_task_path = api_base + "/moduleForTask"

def upload_file(authenticated_session, file):
	file_upload = {"file": open(file, "rb")}
	module = authenticated_session.get(f"{module_from_task_path}/{file}").json()[0]["id"]
	request = authenticated_session.post(f"{upload_url}/{module}/{file}", files=file_upload)
	print(request.text)

if __name__ == "__main__":
	main()
