#!/usr/bin/env python 
# -*- coding: latin-1 -*-
# -*- coding: iso-8859-15 -*-
# -*- coding: ascii -*-
# -*- coding: latin-1 -*-
# -*- coding: utf-42 -*-
# -*- coding: utf-8 -*-

import imaplib
import ConfigParser
import os
import email
import br_proxies
import re 


def verification_string(mesginfo):
    match = re.findall(r"http://blog.com/wp-login.php?.*",mesginfo)
    if match:
        br = br_proxies.main()
        for link in match:
            try:
                br.open(link)
                print br.geturl()+ " :verified"
            except:
                print link +": not find"


 
def show_header(msg_data):
    for response_part in msg_data:
        if isinstance(response_part, tuple):
            msg = email.message_from_string(response_part[1])
            for header in [ 'subject', 'to', 'from' ]:
                print '%-8s: %s' % (header.upper(), msg[header])



def selecting_unseen(conn):
    #f1 = open("f1.html","a+")
    (retcode, messages) = conn.search(None, '(UNSEEN)')
    if retcode == 'OK':
        messages = messages[0].split(' ')
        messages = messages[-3:]
        for message in messages:
            #print 'Processing :', message
            typ, msg_data = conn.fetch(message, '(RFC822)')
            if typ =="OK":
                show_header(msg_data)
                pass

            ret, mesginfo = conn.fetch(message, '(BODY.PEEK[TEXT])')  
            if ret =="OK":
                #print >>f1,'Message %s\n%s\n' % (ret, mesginfo[0][1])    
                #print >>f1, mesginfo,'\n',30*'-'
                mesginfo = 'Message %s\n%s\n' % (ret, mesginfo[0][1])
                #print >>f1, mesginfo,'\n',30*'-'
                verification_string(mesginfo)




def selecting_inbox(connection):
    conn=connection
    conn.select(readonly=1) # 
    selecting_unseen(conn)
        
    

def open_connection(username, password):
    connection = imaplib.IMAP4_SSL("imap-mail.outlook.com")
    connection.login(username, password)
    selecting_inbox(connection)

if __name__ == '__main__':
    #username = "mariltne@hotmail.com"
    #username = "jatnspochoitovi@hotmail.com"
    username = "leriones@hotmail.com"
    password="india123"
    open_connection(username, password)


