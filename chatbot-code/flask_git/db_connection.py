#import MySQLdb
import re
data2={"conversation":[]}
#data2["conversation"]=[];
new_arr=[]
 

#To remove html characters from answer
def cleanhtml_answer(raw_html):
    cleanr = re.compile('<[A-Za-z\/][^>]*>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext
 
db = MySQLdb.connect("127.0.0.1","root","","node_db" )
cursor = db.cursor()
sql="select Name,paswword from node_table"
 
cursor.execute(sql)
results = cursor.fetchall()
for row in results:
    res1=row[0]
    res2=cleanhtml_answer(row[1])
    res1 = str(res1).replace('"','')
    res2 = str(res2).replace('"','')
                            
    new_arr.append(res1)
    new_arr.append(res2)
    
data2["conversation"].append(new_arr)
test = str(data2)
test = test.replace("'",'"')
test = test.replace('\\', '/')
file = open("D:/bots/flask_git/chatterbot/corpus/data/oam/oam.corpus2.json","w")
file.write(test) 
file.close()
#print (test)
#test = str(data).replace("'", '"')
#print test
 
db.close()