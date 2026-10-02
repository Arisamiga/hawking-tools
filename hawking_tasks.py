#!/usr/bin/env python3

from pathlib import Path
from pygments import highlight
from pygments.lexers import guess_lexer
from pygments.formatters import TerminalFormatter
import json
import base64

api_base = "https://hawking.computing.dcu.ie/api"
module_for_task = api_base + "/moduleForTask"

def get_module_from_task(authenticated_session, task):
	return authenticated_session.get(f"{module_for_task}/{Path(task).name}").json()[0].get("id")

def display_task_info(response):
	data = json.loads(response)["output"]
	script = data["attempt"]["source"]
	highlighted_script = highlight(script, guess_lexer(script), TerminalFormatter(style="monokai"))
	print(f"\n{highlighted_script}\n")

	for test, result in zip(data["tests"], data["results"]):
		args = base64.b64decode(test["args"]).decode("utf-8").strip().replace("\n", " ")

		print(f"{test["name"]} | {args} | {result["correct"]}")
