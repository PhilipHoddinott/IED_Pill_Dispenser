
import smtplib



def sendTheEmail(toaddrs, function, body):
	import mainEmail
	from mainEmail import masterPassword
	fromaddr = 'fce.pill.alert@gmail.com'
	#msg = 'A command was send to the server'
	stringMEssage = "Hello  You sent this command to the server:", body,".  As a result we will execute this function: ", function
	msg = str(stringMEssage)
	username = 'fce.pill.alert@gmail.com'
	password = mainEmail.masterPassword
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.ehlo()
	server.starttls()
	server.login(username,password)
	server.sendmail(fromaddr, toaddrs, msg)
	server.quit()

