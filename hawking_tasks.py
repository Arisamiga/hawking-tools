#!/usr/bin/env python3

api_base = "https://hawking.computing.dcu.ie/api"
module_for_task = api_base + "/moduleForTask"

def get_module_from_task(authenticated_session, task):
	return authenticated_session.get(f"{module_for_task}/{task}").json()[0].get("id")
