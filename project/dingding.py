from dingtalkchatbot.chatbot import DingtalkChatbot

class SendMsg:
    def __init__(self):
        self.webtoken = '20d8558d01a4170b91d5a1254fa08930573925d014366de38411ef38fdd52628'

    def send_msg(self, msg):
        # https://oapi.dingtalk.com/robot/send?access_token=20d8558d01a4170b91d5a1254fa08930573925d014366de38411ef38fdd52628
        webhook = 'https://oapi.dingtalk.com/robot/send?access_token={}'.format(self.webtoken)

        bot = DingtalkChatbot(webhook)
        print(msg)
        res = bot.send_text(msg + ' ', is_at_all=False)
        res = bot.send_text(msg='我就是小丁，小丁就是我！', is_at_all=False)
        print(res)
        if res['errcode'] == 0:
            print('send ok')
            return
        else:
            print('发送失败 -- ', res['errmsg'])
            return True
