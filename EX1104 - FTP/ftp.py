# -*- coding: utf-8 -*-
"""
from ftplib import FTP

# Create an FTP instance

ftpObject = FTP("");

ftpObject.connect("10.185.75.111");

ftpObject.login(user="bda", passwd="5iTaiwan");

x=ftpObject.voidcmd("NOOP")
print(x)

ftpObject.quit()
"""

import ftplib

with ftplib.FTP("10.185.75.111") as ftp1:
    try:
        ftp1.login("bda", "5iTaiwan")
        #ftp1.cwd("/PPM801")
        #ftp1.delete("/DEV001/DP0460476.11H_Reel1/DP0460476.11H_Reel1__PostPlace.zip")
        #ftp1.rmd("/DEV001/test")
        print(ftp1.pwd())
    except ftplib.all_errors as e:
        print("FTP error:", e)

"""
from ftplib import FTP
from time import sleep

my_dirs = []  # global
my_files = [] # global
curdir = ''   # global

def get_dirs(ln):
  global my_dirs
  global my_files
  #print(f"ln:'{ln}'")
  cols = ln.split(' ')
  print(cols)
  print(curdir)
  objname = cols[len(cols)-1] # file or directory name
  if ln.startswith('d'):
    my_dirs.append(objname)
  else:
    my_files.append(objname) # full path

def check_dir(adir):
  global my_dirs
  global my_files # let it accrue, then fetch them all later
  global curdir
  my_dirs = []
  gotdirs = [] # local
  curdir = ftp.pwd()
  print("going to change to directory " + adir + " from " + curdir)
  ftp.cwd(adir)
  curdir = ftp.pwd()
  print("now in directory: " + curdir)
  ftp.retrlines('LIST', get_dirs)
  gotdirs = my_dirs
  print("found in " + adir + " directories:")
  print(gotdirs)
  print("Total files found so far: " + str(len(my_files)) + ".")
  sleep(1)
  for subdir in gotdirs:
    my_dirs = []
    check_dir(subdir) # recurse  
    
  ftp.cwd('..') # back up a directory when done here
  
try:
  ftp = FTP('10.185.75.111')
  ftp.login('bda', '5iTaiwan')
  check_dir('/DEV001') # directory to start in
  ftp.cwd('/.') # change to root directory for downloading
  for f in my_files:
    print('getting ' + f)
    #file_name = f.replace('/', '_') # use path as filename prefix, with underscores
    #ftp.retrbinary('RETR ' + f, open(file_name, 'wb').write)
    sleep(1)
except:
  print('oh dear.')
  #ftp.quit()

ftp.quit()
print('all done!')
"""