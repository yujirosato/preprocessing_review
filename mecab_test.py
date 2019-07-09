#neologdの辞書で形態素解析
import MeCab


line = "今日も天気が悪いです。ジュースの代わりにコーヒーを飲もう。"
serch_ward = "天気"


t = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd/') # 形態素解析器の変数（オブジェクト）を作成
line3 = t.parse(line)#レビューの形態素解析
ward = [ward.replace('\t',',').split(',') for ward in line3.split('\n')[:-2]]

#wardの中に形態素解析した各単語に対する品詞情報がリストに入っている
#'今日', '名詞', '副詞可能', '*', '*', '*', '*', '今日', 'キョウ', 'キョー'
#print(str(ward))

for i in ward:
    #if i[0] == serch_ward:
    #    print("検索単語がありました。 : " + str(i))
    print(str(i))
