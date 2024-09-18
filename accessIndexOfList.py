l1 = ["addidas", "nike", "balenciaga", "puma"]
print(l1)

ind = input("Which item index you want to know? : ")

for i in range(0,len(l1)):
    if ind == l1[i]:
        print(i)