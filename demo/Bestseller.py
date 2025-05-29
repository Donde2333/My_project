# -- coding: utf-8 -*-

# 以“读取”模式打开Bestseller - Sheet1.csv文件。
# 使用 CSV 阅读器浏览数据并通过sales in millions列找到销量最高的书籍。
# 使用 CSV 编写器创建一个名为bestseller_info.csv的新文件。
# 在新文件中，使用.writerow()添加新的 CSV 数据。

import csv
max_sales = 0   # 最大销量
bestseller = None  # 畅销书名

with open('demo/Bestseller - Sheet1.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    head = next(csv_reader)  # 跳过表头

    for row in csv_reader:
        sales = float(row[4])  # 销量在第五列（索引为4）
        if sales > max_sales:
            max_sales = sales
            bestseller = row[0]
            row_bestseller = row
print(f"列表中销量最高的书是：{bestseller}")

with open("demo/bestseller_info.csv", "w", encoding="utf-8", newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow([f"列表中销量最高的书是：{bestseller}"])
    csv_writer.writerow(head)
    csv_writer.writerow(row_bestseller)
print("写入成功")
