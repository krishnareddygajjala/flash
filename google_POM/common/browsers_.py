

browsers = [
    {"name": "ie",     "browserName": "internet explorer", "version": "", "platform": "ANY", "path":"F:\Drivers\IEDriverServer.exe"},
    {"name": "chrome", "browserName": "chrome",            "version": "", "platform": "ANY", "path":"F:\Drivers\chromedriver.exe"},
    {"name": "opera",  "browserName": "opera",             "version": "", "platform": "ANY", "path":"F:\Drivers\operadriver.exe"},
    {"name": "edge",   "browserName": "MicrosoftEdge",     "version": "", "platform": "ANY", "path":"F:\Drivers\MicrosoftWebDriver.exe"},
]


def get_browser(name):
    try:
        return (browser for browser in browsers if browser["name"] == name).next()
    except:
        print " %s browser is not defined, enter a valid browser.\n" %name

def get_path(name):
    for i in browsers:
        if i['name'] == name:
            ind = browsers.index(i)
            return browsers[ind]['path']

        
print get_browser("chrome")["browserName"]
print get_path("chrome")