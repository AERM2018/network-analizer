import subprocess


def execute(commands,return_result):
  result = subprocess.run(commands,stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
  if(return_result):
    return result.stdout
  return