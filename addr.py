name = 'Иван Иванов'
line1 = 'Московский пр. 122'
line2 = ''
city = 'Москва'
state = 'Восточный'
zip_code = '12345678'
zip_code2 = '5678900'

def printAddress(name, line1, line2, city, state, zip_code, zip_code2):
    print(name)
    if(len(line1) > 0):
        print(line1)
    if(len(line2) > 0):
        print(line2)
    print(city + ", " + state + " " + zip_code + " " + zip_code2)
# Вызов функции, передача аргументов!
printAddress(name, line1, line2, city, state, zip_code, zip_code2)
