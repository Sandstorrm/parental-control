import requests
import subprocess
import sys, os

def update_file_from_url(url, filename):

  try:
    response = requests.get(url, stream=True)
    response.raise_for_status()

    with open(filename, "wb") as f:
      for chunk in response.iter_content(1024):
        f.write(chunk)

    print(f"File downloaded successfully: {filename}")
  except requests.exceptions.RequestException as e:
    print(f"Error downloading file: {e}")

def run_pyw_script(script_path):
    pythonw_executable = os.path.join(sys.prefix, "pythonw3.12.exe")
    subprocess.Popen([pythonw_executable, script_path])
  
autopilot_url = "https://raw.githubusercontent.com/Sandstorrm/parental-control/main/autopilot.pyw"
settings_url = "https://raw.githubusercontent.com/Sandstorrm/parental-control/main/settings.json"
hosts_url = "https://raw.githubusercontent.com/Sandstorrm/parental-control/main/hosts.py"
autopilot_file = "autopilot.pyw"
settings_file = "settings.json"
hosts_file = "hosts.py"

subprocess.run(["taskkill", "/F", "/IM", "pythonw.exe"])

update_file_from_url(autopilot_url, autopilot_file)
update_file_from_url(settings_url, settings_file)
update_file_from_url(hosts_url, hosts_file)

run_pyw_script(os.path.abspath(autopilot_file))


import subprocess
import sys, os

def run_pyw_script(script_path):
    pythonw_executable = os.path.join(sys.prefix, "pythonw.exe")
    subprocess.Popen([pythonw_executable, script_path])

run_pyw_script(os.path.abspath("autopilot.pyw"))