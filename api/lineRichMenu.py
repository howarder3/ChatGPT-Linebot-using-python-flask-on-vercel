import requests
import json
import os
from linebot import LineBotApi, WebhookHandler


class LineRichMenu:
    def createRichMenu(lineAccessToken):
    # 設定 headers，輸入你的 Access Token，記得前方要加上「Bearer 」( 有一個空白 )
        headers = {'Authorization':'Bearer ' + lineAccessToken,'Content-Type':'application/json'}

        body = {
            'size': {'width': 2500, 'height': 1686},   # 設定尺寸
            'selected': 'true',                        # 預設是否顯示
            'name': 'Richmenu demo',                   # 選單名稱
            'chatBarText': 'Richmenu demo',            # 選單在 LINE 顯示的標題
            'areas':[                                  # 選單內容
                {
                'bounds': {'x': 341, 'y': 75, 'width': 560, 'height': 340}, # 選單位置與大小
                'action': {'type': 'message', 'text': '電器'}                # 點擊後傳送文字
                },
                {
                'bounds': {'x': 1434, 'y': 229, 'width': 930, 'height': 340},
                'action': {'type': 'message', 'text': '運動用品'}
                },
                {
                'bounds': {'x': 122, 'y': 641, 'width':560, 'height': 340},
                'action': {'type': 'message', 'text': '客服'}
                },
                {
                'bounds': {'x': 1012, 'y': 645, 'width': 560, 'height': 340},
                'action': {'type': 'message', 'text': '餐廳'}
                },
                {
                'bounds': {'x': 1813, 'y': 677, 'width': 560, 'height': 340},
                'action': {'type': 'message', 'text': '鞋子'}
                },
                {
                'bounds': {'x': 423, 'y': 1203, 'width': 560, 'height': 340},
                'action': {'type': 'message', 'text': '美食'}
                },
                {
                'bounds': {'x': 1581, 'y': 1133, 'width': 560, 'height': 340},
                'action': {'type': 'message', 'text': '衣服'}
                }
            ]
        }
        # 向指定網址發送 request
        req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu',
                            headers=headers,data=json.dumps(body).encode('utf-8'))
        # 印出得到的結果
        #print(req.text)
        return req.text

    def UploadMenuImage(lineAccessToken):
        line_bot_api = LineBotApi(lineAccessToken)
        with open('/resources/TestMenu_for_RichMenu.png', 'rb') as f:
            line_bot_api.set_rich_menu_image('你的圖文選單 ID', 'image/png', f)
                #print(req.text)
        return f.name

    def showRichMenu(lineAccessToken):
        headers = {'Authorization':'Bearer ' + lineAccessToken}
        req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/你的圖文選單 ID', headers=headers)
        #print(req.text)
        return req.text

    def listRichMenu(lineAccessToken):
        line_bot_api = LineBotApi(lineAccessToken)
        rich_menu_list = line_bot_api.get_rich_menu_list()
        rich_menu_list_text = ''
        for rich_menu in rich_menu_list:
            #print(rich_menu.rich_menu_id)
            rich_menu_list_text += rich_menu.rich_menu_id +'\n'
        return rich_menu_list_text

    def deleteAllRichMenus(lineAccessToken):
        line_bot_api = LineBotApi(lineAccessToken)
        rich_menu_list = line_bot_api.get_rich_menu_list()
        rich_menu_list_text = ''
        for rich_menu in rich_menu_list:
            line_bot_api.delete_rich_menu(rich_menu.rich_menu_id)
            rich_menu_list_text += rich_menu.rich_menu_id +'\n'
        return rich_menu_list_text
    
    def deleteRichMenu(lineAccessToken, rich_menu_id):
        line_bot_api = LineBotApi(lineAccessToken)
        line_bot_api.delete_rich_menu(rich_menu_id)
        return rich_menu_id