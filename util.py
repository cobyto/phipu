import json

if True:    # data_handle
    def dumps_json(data: dict) -> str:
        return json.dumps(data, ensure_ascii=False, indent=4)

if True:    # comunicate
    def yn(q: str) -> bool:
        """yes/noのみの質問"""
        ans = input(q + "[yes/no]: ")
        if ans in ["yes", "y"]:
            return True
        if ans in ["no", "n"]:
            return False

        raise SystemError("Answer is not yes/no.")

    def 複数の具体的回答を集める(q_msg: str) -> list:
        reslist = []
        while True:
            if len(reslist):
                print("他には、")
            ans = input(q_msg + "[入力なしで終了]")
            if not ans:
                print("")
                return reslist
            reslist.append(ans)

if True:    # exception
    class SystemError(Exception):
        pass
