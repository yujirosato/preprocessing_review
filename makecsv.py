#csvファイルの作成と前処理いらない情報の削除
import csv

#o = "0"
#file = "userReview"
#txt = ".txt"

#リストの長さによってレビューが分割されていた場合、レビューをくっつける############
##感想・情報, 苦情のカテゴリー分類がある場合
def reviewupdate(line1):


    line1 = line1.split()
    line_post = line1


    if line1[-1] == "感想・情報" or line1[-1] == "苦情":
        line1.pop()
        line1.pop()


    else:

        while line1[-1] != '感想・情報' and line1[-1] != '苦情':
            line1.pop()
            #print(str(line1) + "[" + str(len(line1)) + "]")

            if len(line1) == 2:
                #print(str(line1))
                return review_join(line_post)

                break

        line1.pop()
        line1.pop()





    if len(line1) > 4:
        return review_join(line1)



    return line1



#感想,情報,苦情のタグ付けなし####ホテル側の返信削除###############################
def reviewupdate_nontag(line2):
    if line2[-1].isdecimal() == True:
        line2.pop()
    else:
        while line2[-1].isdecimal() == False:
            line2.pop()

    line2.pop()

    if len(line2) > 4:

        return review_join(line2)

    return line2
#########################################################################
#変に区切られた文章を結合####################################################
def review_join(line_div):

    line3 = []
    count = 0
    join_review = ""
    #line3.append(line_div[0])
    for elem in line_div:
        if count < 3:
            line3.append(elem)
        else:
            join_review = join_review + elem

        count = count + 1

    line3.append(join_review)


    return line3
#for i in range(12):
#    if i > 9:
#        filename = file + str(i) + txt #filename更新
#        print(filename)
#    else:
#        filename = file + o + str(i) + txt
#        print(filename)
filename = "userReview00.txt"
count = 0
count_num = 0

with open('00.csv', 'w') as f:
    writer = csv.writer(f)
    #writer.writerow(["code", "data", "time", "REVIEW", ])


    with open(filename, "r") as f:
        line = f.readline()

        while line:
            #レビュー情報を１行づつ処理
            line_div = line.split()

            #ホテル側の返信があれば、返信番号がline_divに２箇所入っているため、そこを処理
            for line_num in line_div:
                if line_num.isdecimal() == True:
                    count = count + 1

            ################################

            if len(line_div) > 5 and ('感想・情報' in line or '苦情' in line) and count == 2:
                line = reviewupdate(line)
                writer.writerow(line)

            elif len(line_div) > 5 and count == 2:
                line = reviewupdate_nontag(line_div)
                writer.writerow(line)

            elif len(line_div) == 4:
                writer.writerow(line_div)

            elif len(line_div) > 4:

                if line_div[-1].isdecimal() == True:
                    line_div.pop()

                writer.writerow(review_join(line_div))

            else:
                print(str(line_div))
            count = 0


            count_num = count_num + 1



            line = f.readline()
print(str(count_num))





#
