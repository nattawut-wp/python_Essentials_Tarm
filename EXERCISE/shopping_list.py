shopping_list = []

# for i in range(50):
#     item = input("Enter item: ")
    
#     if item == "done":
#         break
        
#     shopping_list.append(item)

# print("\nShopping List:")

# for index, item in enumerate(shopping_list, start=1):
#     print(f"{index}. {item}")

# 1. สร้าง List ว่าง
shopping_list = []

# วนลูปเพื่อรับค่าเรื่อยๆ
while True:
    # 2. รับชื่อสินค้าจากผู้ใช้
    item = input("Enter item: ")
    
    # 4. หยุดรับข้อมูลเมื่อผู้ใช้พิมพ์ done
    if item.lower() == "done":
        break
        
    # 3. เพิ่มข้อมูลลงใน List
    shopping_list.append(item)

# 5. แสดงรายการสินค้าทั้งหมด
print("\nShopping List:")

for i, item in enumerate(shopping_list, start=1):
    print(f"{i}. {item}")


    
# shopping_list = []
# while True:
#     item = input("Enter item : ")
#     if item == "done":
#         break
#     shopping_list.append(item)


# print("\nShopping List:")


# for i in range(len(shopping_list)):
#     print(f"{i+1}. {shopping_list[i]}")
