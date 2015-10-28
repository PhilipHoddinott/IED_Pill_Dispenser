import readEmail
import getpass
import sendEmail
import responses

masterPassword="holder password"
def sendAnEmail(adress, resposne1,body):
	sendEmail.sendTheEmail(adress, resposne1, body)

	

def getResponse(body):
	#resposne
	return  responses.emailResopnses(body)



def gotEmails(adress, body):
	response=getResponse(body)
	sendAnEmail(adress, response, body)


def getEmails():

	readEmail.readTheEmails()




def main():

	masterPassword = getpass.getpass("enter the password for first choice engineering")
	getEmails()


main()
