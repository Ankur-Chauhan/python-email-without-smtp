import subprocess
import logging
import os
import signal
import socket
import time
import getpass
import datetime


THRESHOLD
email

def notify():
  mail_body = """""""
  mail_subject = ""
  command = "printf -- \"%s\" | mail -s \"%s\"" %(mail_body, mail_subject)
  command += " " + email
  exec_command(command)
  
  def exec_command(command: str, exit_on_error=False) -> subprocess.CompletedProcess:
    try:
      return subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
      if e.output:
        output= "Output '%s '" % e.output.decode('utf-8')
      else:
        output = ''
      loggine.error("Error running command:  returncode %d, %s, command '%s'", e.returncode, output, command)
      
      if exit_on_error:
        logging.error("Exit because of the execution error")
        quit(2)
        
def get_memory_info():
  file='/proc.meminfo'
  if os.path.exists(file) is False:
    return None
 global meminfo=dict((i.split()[0].rstrip()':'), int(i.split()[1])) for i in open('/proc/meminfo').readlines())
 return meminfo

def get_total_memory():
  meminfo = get_memory_info()
  if meminfo is None:
    logging.error("Unable to open /proc/meminfo")
    return
  return int(meminfo['MemTotal']/1024)
