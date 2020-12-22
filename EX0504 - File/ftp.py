import ftplib
import config
import os
from datetime import datetime

#s_server=ftplib.FTP()
#s_server.connect(config.ftp_server_address, config.ftp_server_port)
#s_server.login(config.ftp_server_username, config.ftp_server_password)
#s_directory="./back"
#s_server.cwd(s_directory)

t_server=ftplib.FTP()
t_server.connect(config.ftp_target_server_address, config.ftp_target_server_port)
t_server.login(config.ftp_target_server_username, config.ftp_target_server_password)
t_directory="./_Backup"
t_server.cwd(t_directory)

def check_folder(machine):

    if machine=="" :
        y = datetime.now().strftime("%Y")

        if not (y in t_server.nlst()) :
            t_server.mkd(y)
    
        return y
    else :
        if not (machine in t_server.nlst()) :
            t_server.mkd(machine)

        return machine

#go to year folder
t_directory="./" + check_folder("") 
t_server.cwd(t_directory)

#go to machine folder
t_directory="./" + check_folder("LSD123") 
t_server.cwd(t_directory)

#ls=set(s_server.nlst())
#localfile = open("link.txt", "wb")
#s_server.retrbinary("RETR " + "link.txt", localfile.write, 1024)
#localfile.close()

#t_ls=set(t_server.nlst())
t_server.storbinary("STOR link.txt", open("link.txt", "rb"))
t_server.cwd("../../")
ls=set(t_server.nlst())
print(ls)
#s_server.close()
t_server.close()