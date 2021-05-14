#!/usr/bin/python

import ftplib

def annonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('annonymus', 'annonymus')
        print("[+] " + hostname + " FTP Annonymus LOGIN Succeeded.")
        ftp.quit()
        return True
    except Exception as e:
        print("[-] " + hostname + "FTP Anonymus LOGIN Failed.")    

host = input("Enter The IP Address: ")
annonLogin(host)