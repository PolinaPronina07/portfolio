'''import re
file = open("gcode.txt", "r+")
file2 = open("gcode2.txt", "a+")
flag = 0
stroka = "gcode.txt"
pattern1 = r'\sZ\d+'
res1 = re.findall(pattern1, stroka)
pattern2 = r'.Z:\d+'
res2 = re.findall(pattern2, stroka)
a = float(input())
while True:
 stroka = file.readline()
 if not stroka:
     break
 if "G280" in stroka:
     print(stroka)
     file2.write(stroka)
     while True:
         stroka = file.readline()
         file2.write(stroka)
         if "F9000" in stroka and flag == 0:
            flag = 1
            break
 if "F9000" in stroka and flag == 1:
     flag = 2
     continue
 res1 = re.findall(pattern1, stroka)
 res2 = re.findall(pattern2, stroka)
 if len(res1) > 0:
     c = float((stroka[stroka.find(" Z") + 2: stroka.find("\n")]))
     print(c)
     print(stroka)
     print(float((stroka[stroka.find(" Z") + 2: stroka.find("\n")])) + a)
     print(stroka[0:stroka.find(" Z") + 2] + str(c+a) + "\n")
     file2.write(stroka[0:stroka.find(" Z") + 2]+ str(c+a) + "\n")
 if len(res2) > 0 and flag != 2:
     d = float((stroka[stroka.find(".Z") + 3: stroka.find("\n")]))
     #d=float((stroka[stroka.find(pattern2) + 3: stroka.find("\n")]))
     print(d)
     print(stroka)
     print(d + a)
     #задать строку для нового файла из старой строки
     print(stroka[0:stroka.find(".Z:") + 2] + str(d + a) + "\n")
     file2.write(stroka[0:stroka.find(".Z:") + 3]  + str(d + a) + "\n")
 if len(res1) <= 0 and len(res2) <= 0:
     file2.write(stroka)'''








