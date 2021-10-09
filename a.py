
import csv
#replace csv 
with open('./a.csv',encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    l = [row for row in reader]

n=15 #the index of last row
for i in range(2,n):
  for element in l[i]:
      parts = element.split(';')
      print(" ")
      print("Tiền trọ")
      print(" ")
      print("TÊN PHÒNG:               " + parts[0])  
      print("Tiền phòng:              " + parts[1]+"đồng")
      print("Số điện trước:           " + parts[2])
      print("Số điện sau:             " + parts[3])
      print("Tiền điện:               " + parts[4]+"đồng")
      print("Số nước trước:           " + parts[5])
      print("Số nước sau:             " + parts[6])
      print("Tiền nước:               " + parts[7]+"đồng")
      print("Tiền rác:                " + parts[8]+"đồng")
      print("Tiền trọ tháng này:      " + parts[9]+"đồng")
      print("Nợ cũ:                   " + parts[10]+"đồng")
      print(" ")
      print("Tổng cộng:               " + parts[11]+"đồng")
      print("----------------------------")
      