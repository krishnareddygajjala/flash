
import smtplib

fromaddr = "krrishna9848@gmail.com"
toaddr = "pskr540@gmail.com"
msg = "Hi there I am sending this mail using pyhton script"
password = "##############"

#server = smtplib.SMTP("smtp.gmail.com",587)
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.ehlo()
server.login(fromaddr, password)
server.sendmail(fromaddr,toaddr , msg)
print "sucess"
server.quit()