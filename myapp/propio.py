import requests
import json

url="http://www.themealdb.com/api/json/v1/1/random.php"

r = requests.get(url)

jsonStr1 = r.text
jsonStr1 = jsonStr1[10:-2]

jsondicc = json.loads(jsonStr1)

print(jsondicc.get("idMeal")) 

#for x in dicc:
#    print("hola",x)

#string= "HOla como estas ascjaksj a3333121212"
#string= string[10:-2]



#print("la cantidad es ",cantidad)
#print(clase)