
class Locators(object):
    
#home page locators
    login  =  "//a/u[text() = 'login']"
    createAccount = "//a/u[text() = 'create an account']"
    
#create account page
    male_radio = "//input[@value ='m']"
    female_radio = "//input[@value ='f']"
    first_name = "//input[@name='firstname']"
    last_name = "//input[@name='lastname']"
    dob = "//input[@id='dob']"
    email = "//input[@name = 'email_address']"
    company_name = "//input[@name = 'company']"
    street = "//input[@name = 'street_address']"
    suburb = "//input[@name = 'suburb']"
    post_code = "//input[@name = 'postcode']"
    city = "//input[@name = 'city']"
    state = "//input[@name = 'state']"
    country= "//select[@name='country']"
    telephone = "//input[@name='telephone']"
    fax = "//input[@name='fax']"
    newsletter = "//input[@name='newsletter']"
    password = "//input[@name='password']"
    password_confirmation = "//input[@name='confirmation']"
    continue1 = "//button[@id='tdb4']"
    errmsg = "//td[@class = 'messageStackError']"