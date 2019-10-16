import hibpwned
import pandas
import os
import time

api = 'API KEY'

file = input('Please input the text file path: (The file should be in same directory.)  ')

if not os.path.isfile(file):
    print ('Invalid file path.')
    quit()

elif not file.endswith('.txt'):
    print ('Only support for .txt files')
    quit()

elif file == '':
    print ('No File')
    quit()

else:
    data_list = []
    f = open(file, "r")
    emails = []
    for z in f:
        z = z.strip()
        emails.append(z)
        myApp = hibpwned.Pwned(z, 'HIBP_Email_Check', api)
        myBreaches = myApp.searchAllBreaches(truncate=False, unverified=True)
        if not '404' in str(myBreaches):
            print (z + '  is PaWnEd')
            for x in myBreaches:
                for y in x['DataClasses']:
                    pawned = [z,x['Name'],x['BreachDate'],y]
                    data_list.append(pawned)    
            else:
                not_pawned = [z,'','','']
                data_list.append(not_pawned)  
            time.sleep(1.5)   

        data = pandas.DataFrame(data_list ,columns=['Email','Incident','Breached Date','Compromised Data'])
        with pandas.ExcelWriter('Results.xlsx') as writer:
            data.to_excel(writer, sheet_name='Status', index=False)

print ('Voila Done! Check the Results.xslx file.')