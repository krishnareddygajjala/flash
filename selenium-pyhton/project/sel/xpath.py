#parent - []
#child - /

#  (//div[@class='formWrap padT15']/div/input)[2]      ****
#//input[@id='gosuggest_inputDest']
#//div/input[@id='gosuggest_inputDest']
#//div[@class='formWrap padT15']/div/input[@id='gosuggest_inputDest']

#by using descendant  = Approximate child
#//div[@class='formWrap padT15']/descendant::input[@id='gosuggest_inputDest']

# siblings == following-sibling / preceding-sibling
# following-sibling == younger brother
# preceding-sibling == elder brother
 
# //div[@class='formWrap padT15']/a[@id='swap']/following-sibling::div/input[@id='gosuggest_inputDest']

#//div[@class='formWrap padT15']/div[@class='fl width100']/preceding-sibling::div/input[@id='gosuggest_inputDest']
####//input[@id='gosuggest_inputDest']/ancestor::div[@id='searchWidgetCommon']