#JavaScript Object Notation
import json

data = '{"var1":"Shrishti", "var2":20}'

parsed = json.loads(data)
print(parsed['var1'])

#json loads
import json 
	
# JSON string: 
# Multi-line string 
data = """{ 
	"Name": "Jennifer Smith", 
	"Contact Number": 7867567898, 
	"Email": "jen123@gmail.com", 
	"Hobbies":["Reading", "Sketching", "Horse Riding"] 
	}"""
	
# parse data: 
res = json.loads( data ) 
	
# the result is a Python dictionary: 
print( res )

#load()
import json 

data = { 
	"name": "Satyam kumar", 
	"place": "patna", 
	"skills": [ 
		"Raspberry pi", 
		"Machine Learning", 
		"Web Development"
	], 
	"email": "xyz@gmail.com", 
	"projects": [ 
		"Python Data Mining", 
		"Python Data Science"
	] 
} 
with open( "data_file.json" , "w" ) as write: 
	json.dump( data , write ) 

with open("data_file.json", "r") as read_content: 
	print(json.load(read_content))


#dumps
