from __future__ import unicode_literals

from imapclient import IMAPClient
from email.utils import parseaddr

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

#this is where the main part starts
def readTheEmails():
	import mainEmail
	from mainEmail import masterPassword

	HOST = 'imap.gmail.com'
	USERNAME = 'fce.pill.alert@gmail.com'
	PASSWORD = mainEmail.masterPassword
	ssl = 993
	server = IMAPClient(HOST, use_uid=True, ssl=ssl)
	server.login(USERNAME, PASSWORD)

	select_info = server.select_folder('INBOX')

	messages = server.search(['NOT DELETED'])


	seenS="\\\\Seen"

	response = server.fetch(messages, ['FLAGS', 'RFC822.SIZE', 'BODY[TEXT]', 'BODY[HEADER.FIELDS (FROM)]'])
	for msgid, data in response.iteritems():

		senderAdrs=parseaddr(data['BODY[HEADER.FIELDS (FROM)]'])
		#print "from is: ",az
		#print('ID',msgid,"d:", data['RFC822.SIZE'], ' bytes, flags=', data['FLAGS'], " from= ", senderAdrs)
		flagsStuff =str(data['FLAGS'])
		boyStuff= str(data['BODY[TEXT]'])
		firstP = "tr\">"
		lastP = "</div>"
		bodyTrue= find_between(boyStuff, firstP, lastP)
		#print "body is ", bodyTrue

		#print flagsStuff
		if(seenS in flagsStuff):
			print "message  seen"
			print('ID',msgid,"d:", bodyTrue, ' body, flags=', data['FLAGS'], " from= ", senderAdrs)
			mainEmail.gotEmails(senderAdrs, bodyTrue)

		else: 
			print "NOT SEEN"
			print('ID',msgid,"d:", bodyTrue, ' body,  flags=', data['FLAGS'], " from= ", senderAdrs)
			mainEmail.gotEmails(senderAdrs, bodyTrue)

