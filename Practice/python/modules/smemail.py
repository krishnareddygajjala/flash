
import smtplib
import yaml

with open("F:\Python WorkSpace\Parker\safecredentials.yaml") as openyaml:
    # use safe_load instead load
    safeqacredentials = yaml.safe_load(openyaml)
    safeqa = safeqacredentials['safeqa']
    safeqausername = safeqa['username']
    safeqapassword = safeqa['password1']
    openyaml.close()
    
fromaddr = "krrishna9848@gmail.com"
toaddr = "gvkreddy71@gmail.com"
msg = "Hi there I am sending this mail using pyhton script"
password = safeqapassword
server = smtplib.SMTP("smtp.gmail.com:587")
server.starttls()
server.ehlo()
server.login(fromaddr, password)
server.sendmail(fromaddr,toaddr , msg)
print "sucess"
server.quit()