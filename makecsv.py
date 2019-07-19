#csvファイルの作成と前処理いらない情報の削除
import csv

o = "0"
file = "userReview"
txt = ".txt"

#リストの長さによってレビューが分割されていた場合、レビューをくっつける############
def reviewupdate(line1):

    line1 = line1.split()


    if line1[-1] == "感想・情報" or line1[-1] == "苦情":
        line1.pop()
        line1.pop()


    else:

        while line1[-1] != '感想・情報' and line1[-1] != '苦情':
            line1.pop()
            #print(str(line1) + "[" + str(len(line1)) + "]")

            if len(line1) == 2:
                break

        line1.pop()
        line1.pop()





    if len(line1) > 4:
        review = line1.pop(3)
        for i in range(len(line1) - 3):

            review = review + line1.pop(3)

        line1.append(review)



    return line1
#########################################################################


#for i in range(12):
#    if i > 9:
#        filename = file + str(i) + txt #filename更新
#        print(filename)
#    else:
#        filename = file + o + str(i) + txt
#        print(filename)
filename = "userReview00.txt"

with open('00.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["code", "data", "time", "REVIEW", ])


    with open(filename, "r") as f:
        line = f.readline()

        while line:
            line_len = line.split()
            if len(line_len) > 5 and ('感想・情報' in line or '苦情' in line):
                line = reviewupdate(line)

            writer.writerow(line)

            line = f.readline()






#
