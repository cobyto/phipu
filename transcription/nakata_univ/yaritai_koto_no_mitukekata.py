import json
from copy import deepcopy as dc

import util

class Source:
    title = "やりたいことの見つけ方"
    url = [
        "https://www.youtube.com/watch?v=sk23TqDytzI",
        "https://www.youtube.com/watch?v=4KTC2TF2WsY"
    ]
    book_title = "世界一やさしい「やりたいこと」の見つけ方"

class やりたいこと:
    def 自己理解をする():
        print("--- start ---")
        print("紙とペンを用意して、自分の回答をメモしてください")
        大事なこと = 価値観()
        大事なこと.確認する()

        得意なこと = 才能()
        得意なこと.確認する()

        好きなこと = 情熱()
        好きなこと.確認する()

        print(util.dumps_json({"情熱": 好きなこと.answers, "才能": 得意なこと.自分の長所まとめ}))
        print("情熱　×　才能　でやりたいことをいくつか上げましょう")
        やりたいこと = util.複数の具体的回答を集める("やりたいことは？")
        print("")

        print("仕事の目的で、やりたいことを絞りましょう")
        絞ったやりたいこと = []
        for one in やりたいこと:
            if util.yn("「{}」は、あなたの仕事の目的にあっていますか？".format(one)):
                絞ったやりたいこと.append(one)
        print("")

        print("絞ったやりたいこと : {}".format(絞ったやりたいこと))
        print("手段を調べて、実行しましょう。")
        print("---  end  ---")

class 価値観(QA):
    定義 = [
        "行動ではなく状態",
        "こうあるべき　より　こうありたい"
    ]
    answers = {}
    def 確認する(self):
        def 質問に答えていく():
            qa = QA()

            q1_1 = "尊敬する人は誰ですか？"
            qa.質問して回答収集(q1_1)
            for a in dc(qa.answers)[q1_1]:
                q1_2 = "なぜ、{}を尊敬しているのですか".format(a)
                qa.質問して回答収集(q1_2)

            q2 = "思春期に大きな影響を受けた経験はなんですか？"
            qa.質問して回答収集(q2)

            q3 = "今の社会に足りないと思うものは？"
            qa.質問して回答収集(q3)
            # こういう社会であってほしい、というビジョン
            # 何を大事にするかの、価値観

            q4 = "周囲に「自分は何を大切にしてそう？」と聞いたときの回答は？"
            qa.質問して回答収集(q4)

            q5_1 = "他人に助言するとしたら、伝えたい行動は？（どんなふうに行動したほうがいいよ　と伝えたいか）"
            qa.質問して回答収集(q5_1)
            q5_2 = "他人に助言するとしたら、伝えたくない行動は？"
            qa.質問して回答収集(q5_2)

            self.answers = qa.answers

        print("まずはいくつかの質問に答えましょう。")
        質問に答えていく()
        print("あなたの回答 : {}".format(util.dumps_json(self.answers)))
        print("")

        print("あなたの回答のワードから、似たものをまとめましょう")
        self.keywords = util.複数の具体的回答を集める("キーワードは？")
        print("")

        print("keywords : {}".format(util.dumps_json(self.keywords)))
        print("keywordsにランキングを付けましょう。")
        self.ranking = {}
        for rank in range(len(self.keywords)):
            ans = input("{}位は？：".format(rank + 1))
            self.ranking[rank + 1] = ans
        print("")

        print("ランキング付けキーワード：{}".format(util.dumps_json(self.ranking)))
        print("ランキング付けしたキーワードをもとに、仕事の目的として翻訳してください。")
        self.shigoto_mokuteki = util.複数の具体的回答を集める(
            "社会にどういった目的で貢献しますか？どのような形でありがとうをもらいますか？")
        print("")

class 才能():
    定義 = [
        "スキルではない",
        "自分では当たり前に、楽にできてしまうこと"
    ]
    answers = {}
    def 確認する(self):
        def 質問に答えていく():
            qa = QA()

            q1 = "一番充実していた体験は？"
            qa.質問して回答収集(q1)
            # 成功ではない。充実。

            q2 = "最近イラッとしたのはいつ？"
            qa.質問して回答収集(q2)
            # 俺だったらしないのに、と思ったときにイラッとする。
            # 自分の強みを当たり前と思っているがために、他人がそれをできないことにイラッとする、というのが本質。

            q3 = "周囲に「自分の長所は？」と聞いたときの回答は？"
            qa.質問して回答収集(q3)
            # 意外と答えてくれるし、思ったのと違う評価が来ることがあるはず。

            q4 = "仕事をやめたとして、その仕事でもっとやりたかった部分は？"
            qa.質問して回答収集(q4)

            q5 = "これまでで成果が出たことは？"
            qa.質問して回答収集(q5)

            self.answers = qa.answers

        print("まずはいくつかの質問に答えましょう。")
        質問に答えていく()
        print("あなたの回答 : {}".format(util.dumps_json(self.answers)))
        print("")

        print("長所をまとめてください")
        self.自分の長所まとめ = util.複数の具体的回答を集める("キーワードは？")
        print("それが、自分の取扱説明書です。")
        print("")

    短所リスト = []
    才能リスト = []
    def 短所だからこそで探す(self):
        # 才能は往々にして短所の裏返し

        # 短所をまず挙げる
        self.短所リスト = util.複数の具体的回答を集める(短所をあげる)

        # だからこそ　をつける
        for 短所 in self.短所リスト:
            self.才能リスト.append(input("「{}」-> だからこそ、、"))
        print(self.才能リスト)

class 情熱():
    定義 = [
        "役に立つから好きなこと　ではない",
        "興味があるから好きなこと"
    ]
    大事なこと = "価値観を考えて得意なものを見極めてから、好きなことを探ること"
    answers = {}
    def 好きなものか(self, it: str = "それ"):
        if util.yn("{}は、生産的だからすきなのか？".format(it)):
            return False
        if util.yn("{}は、合理的だからすきなのか？".format(it)):
            return False
        if util.yn("{}は、役に立つからすきなのか？".format(it)):
            return False
        print(
            "{}は、説明できないし、理解してもらえないし、なんかわからないけど、すき　ということだと思います。"
            .format(it)
        )
        return True

    def 確認する(self):
        def 質問に答えていく():
            qa = QA()
            q1 = "今、お金を払ってでも勉強したいことはなんですか？"
            qa.質問して回答収集(q1)

            q2 = "本棚にはどんなジャンルの本がある？"
            qa.質問して回答収集(q2)

            q3 = "救われたと思えるもの、ジャンルは？"
            qa.質問して回答収集(q3)

            q4 = "お礼を言いたい人、仕事は？"
            qa.質問して回答収集(q4)

            q5 = "世の中に対して怒りを感じたことは？"
            qa.質問して回答収集(q5)

            self.answers = qa.answers

        print("まずはいくつかの質問に答えましょう。")
        質問に答えていく()
        print("あなたの回答 : {}".format(util.dumps_json(self.answers)))
        print("")

class QA:
    answers = {}
    def 質問して回答収集(self, q: str):
        ans = util.複数の具体的回答を集める(q)
        self.answers[q] = ans

class なにかやりたいけど症候群:
    定義 = "なにかやりたいけど、やりたいことがないんですよね、って言っている人の状態。"
    原因 = "選択肢が多すぎる状態にあること"
    必要なもの = "基準"
    基準を持つために必要なこと = "明確な自己理解"
    不要なもの = "より多くの情報"

    def 診断(self) -> bool:
        result = False
        if util.yn("目の前に選択肢がたくさんある状態ですか？"):
            if util.yn("やりたいことに対して時間や体力やお金などの余裕は足りているか"):
                print("やりたいことが多すぎて、諦めている状態です。")
                result = True
            if util.yn("選択する基準はありますか？"):
                print("選択肢が多すぎて、選べなくなっている状態です。")
                result = True
        return result
