import urllib.request
hola = input("Enter a valid ID: ")
api_key= ".json"
""" 
url = "https://world.openfoodfacts.org/api/v0/product/%s%s" % (hola, api_key)
 """



data = urllib.request.urlopen("https://world.openfoodfacts.org/api/v0/product/%s%s" % (hola, api_key))
data1 = data.read().decode('utf-8')
print(data1)
""" 
print(data["name"])
print(data["description"])
print(data["image"])
print(data["price"])
print(data["ingredients"])
print(data["tags"])
 """ 