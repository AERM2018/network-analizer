import paramiko
def get_SSH_client(target_ip,credentials):
  ssh = paramiko.SSHClient()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  ssh.connect(target_ip, username=credentials[0],password=credentials[1])
  return ssh 