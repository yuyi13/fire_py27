# coding=utf-8
import csv
import os

path = 'E:/Userdata/yuy/downloads/insitu_comparison/rainfall_testData/rainfall_csv/'
output ='E:/Userdata/yuy/downloads/insitu_comparison/rainfall_testData/combine.csv'
for input in os.listdir(path):
    if input.endswith('.csv'):
        print(input)

        # 先将output文件里的每一行读出来，存到output_data这个list中
        with open(output, 'r') as file:
            reader = csv.reader(file)

            output_data = []
            for row in reader:
                output_data.append(row)

        with open((path + input), 'r') as csvinput:
            with open(output, 'w') as csvouput:
                writer = csv.writer(csvouput, lineterminator='\n')
                reader = csv.reader(csvinput)

                list = []
                for row in reader:
                    list.append(row[4])

                year = input.split('_')[2]
                month = input.split('_')[3]
                day = input.split('_')[4]
                date = day.split('.')[0]

                list[0] = year + month + date

                for t in range(len(output_data)):
                    # 这个if是为了防止，当input里ALB的长度小于output_data的长度
                    # 而导致的index out of range的error
                    # 意思是，假如output的行数大于input的行数，那么拼上空字符串，
                    # 否则就拼上ALB那一行的数据
                    if t >= len(list):
                        output_data[t].append('')
                    else:
                        output_data[t].append(list[t])

                    # 将拼好的这一行，直接写入output csv
                    writer.writerow(output_data[t])