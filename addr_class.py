class Address(): # Имя класса выбирает програмист!
    name = ''    # Строковое поле класса
    line1 = ''
    line2 = ''
    city = ''
    state = ''
    zip_code = ''
    zip_code2 = ''

homeaddress = Address()
homeaddress.name = "Иван Иванов"
homeaddress.line1 = "Московский пр. 122"
homeaddress.line2 = "Тихая ул. 12"
homeaddress.city = "Москва"
homeaddress.state = "Восточный"
homeaddress.zip_code = "123678"

vocationHomeAddress = Address()
vocationHomeAddress.name = "Иван Иванов"
vocationHomeAddress.line1 = "пр.Мира 12"
vocationHomeAddress.line21 = ""
vocationHomeAddress.city = "Коломна"
vocationHomeAddress.state = "Центральный район"
vocationHomeAddress.zip_code = "12489"

print("Основной адрес проживания " + homeaddress.city)
print("Адрес загородного дома " + vocationHomeAddress.city)

def printAddress(Address):
    print(Address.name)
    if(len(Address.line1) > 0):
        print(Address.line1)
    if(len(Address.line2) > 0):
        print(Address.line2)
    print(Address.city + ", " + Address.state + " " + Address.zip_code + " " + Address.zip_code2)
# Вызов функции, передача аргументов!
printAddress(homeaddress)
printAddress(vocationHomeAddress)
