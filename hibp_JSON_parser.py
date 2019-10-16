import json
import pandas
import os

file = input('Enter File Name. (The file should be in same directory.) : ')

if not os.path.isfile(file):
    print ('Invalid file path.')
    quit()

elif not file.endswith('.json'):
    print ('Only support for .json files')
    quit()

elif file == '':
    print ('No File')
    quit()


flist = []
slist = []

with open(file) as json_file:
    data = json.load(json_file)
    for i in data['BreachSearchResults']:
        name = i['Alias']
        domain = i['DomainName']
        email = name + '@' + domain
        for n in i['Breaches']:
            breach = n['Name']
            breachd = n['BreachDate']
            data = ', '.join(n['DataClasses']) 
            damn1 = [email,breach,breachd,data]
            print (damn1)
            flist.append(damn1)
            for t in n['DataClasses']:
                damn2 = [email,breach,breachd,t]
                slist.append(damn2)


data1 = pandas.DataFrame(flist ,columns=['Email','Incident','Date','Information'])
data2 = pandas.DataFrame(slist ,columns=['Email','Incident','Date','Information'])
with pandas.ExcelWriter('HIBP_JSON_Results.xlsx') as writer:
    data1.to_excel(writer, sheet_name='Data', index=False)
    data2.to_excel(writer, sheet_name='Filter', index=False)

print ('Voila Done! Check the Results.xslx file.')

