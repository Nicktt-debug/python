from xml.dom import minidom


hour = int(input('hores: '))
min = int(input('min: '))
sec = int(input('sec: '))

sec = sec + 1
sec_min = sec // 60
sec = sec % 60

min = min + sec_min
min_hour = min // 60 
min = min % 60

hour = hour + min_hour

print(hour ,  min ,  sec )

