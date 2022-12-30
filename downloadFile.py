# coding:utf-8
 
import paramiko
 
HOST = '192.168.56.102'
USER = 'username'
PSWD = 'password'
 
LOCAL_PATH  = "/Users/*****/Desktop/sample_merged.pdf"
REMOTE_PATH = "/home/user/sample_merged.pdf"
 
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(HOST, username=USER, password=PSWD)
 
sftp = ssh.open_sftp()
sftp.get(REMOTE_PATH, LOCAL_PATH)
sftp.close()
 
ssh.close()