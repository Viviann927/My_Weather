import tkinter as tk
import urllib.request
import urllib.parse
import json


loc = ['基隆市', '臺北市', '新北市', '桃園市', '新竹市', '新竹縣', '苗栗縣', '臺中市', '彰化縣', '南投縣', '雲林縣', 
     '嘉義市', '嘉義縣', '臺南市', '高雄市', '屏東縣', '宜蘭縣', '花蓮縣', '臺東縣', '澎湖縣', '金門縣', '連江縣']

def set_tw():
    lb.config(text='已選擇：' + tw.get())


def fd_wt():    
    url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-091?Authorization=CWB-29654F18-4C41-4CE1-BF28-A6889EACDBCD'
    re = urllib.request.Request(url)
    req = urllib.request.urlopen(re)
    jsontext = json.loads(req.read())
    for tt in loc:
        if tw.get() == tt:
            print(tt)
            for i in jsontext['records']['locations'][0]["location"]:
                if i['locationName'] == tt:
                    wea_01 = i['weatherElement'][10]['time'][0]['startTime'],'～',i['weatherElement'][10]['time'][0]['endTime']
                    wea_03 = i['weatherElement'][10]['time'][0]['elementValue'][0]['value'].split('。')
                    wea_11 = i['weatherElement'][10]['time'][1]['startTime'],'～',i['weatherElement'][10]['time'][1]['endTime']
                    wea_13 = i['weatherElement'][10]['time'][1]['elementValue'][0]['value'].split('。')
                    wea_21 = i['weatherElement'][10]['time'][2]['startTime'],'～',i['weatherElement'][10]['time'][2]['endTime']
                    wea_23 = i['weatherElement'][10]['time'][2]['elementValue'][0]['value'].split('。')
                    wea_31 = i['weatherElement'][10]['time'][3]['startTime'],'～',i['weatherElement'][10]['time'][3]['endTime']
                    wea_33 = i['weatherElement'][10]['time'][3]['elementValue'][0]['value'].split('。')
                    wea_41 = i['weatherElement'][10]['time'][4]['startTime'],'～',i['weatherElement'][10]['time'][4]['endTime']
                    wea_43 = i['weatherElement'][10]['time'][4]['elementValue'][0]['value'].split('。')               
                    wea_51 = i['weatherElement'][10]['time'][5]['startTime'],'～',i['weatherElement'][10]['time'][5]['endTime']
                    wea_53 = i['weatherElement'][10]['time'][5]['elementValue'][0]['value'].split('。')
                    wea_61 = i['weatherElement'][10]['time'][6]['startTime'],'～',i['weatherElement'][10]['time'][6]['endTime']
                    wea_63 = i['weatherElement'][10]['time'][6]['elementValue'][0]['value'].split('。')
                    wea_71 = i['weatherElement'][10]['time'][7]['startTime'],'～',i['weatherElement'][10]['time'][7]['endTime']
                    wea_73 = i['weatherElement'][10]['time'][7]['elementValue'][0]['value'].split('。')             
                    wea_81 = i['weatherElement'][10]['time'][8]['startTime'],'～',i['weatherElement'][10]['time'][8]['endTime']
                    wea_83 = i['weatherElement'][10]['time'][8]['elementValue'][0]['value'].split('。')              
                    wea_91 = i['weatherElement'][10]['time'][9]['startTime'],'～',i['weatherElement'][10]['time'][9]['endTime']
                    wea_93 = i['weatherElement'][10]['time'][9]['elementValue'][0]['value'].split('。')               
                    wea_101 = i['weatherElement'][10]['time'][10]['startTime'],'～',i['weatherElement'][10]['time'][10]['endTime']
                    wea_103 = i['weatherElement'][10]['time'][10]['elementValue'][0]['value'].split('。')
                    wea_111 = i['weatherElement'][10]['time'][11]['startTime'],'～',i['weatherElement'][10]['time'][11]['endTime']
                    wea_113 = i['weatherElement'][10]['time'][11]['elementValue'][0]['value'].split('。')
                    wea_121 = i['weatherElement'][10]['time'][12]['startTime'],'～',i['weatherElement'][10]['time'][12]['endTime']
                    wea_123 = i['weatherElement'][10]['time'][12]['elementValue'][0]['value'].split('。')
                    wea_131 = i['weatherElement'][10]['time'][13]['startTime'],'～',i['weatherElement'][10]['time'][13]['endTime']
                    wea_133 = i['weatherElement'][10]['time'][13]['elementValue'][0]['value'].split('。')
                   
                    lst_1.delete(0,tk.END)
                    lst_1.insert(tk.END, tt + '未來一周天氣資訊：','\n')
                    lst_1.insert(tk.END,wea_01,wea_03[:4],'\n',wea_11,wea_13[:4],'\n',wea_21,wea_23[:4],'\n',wea_31,wea_33[:4],'\n',
                                  wea_41,wea_43[:4],'\n',wea_51,wea_53[:4],'\n',wea_61,wea_63[:3],'\n',wea_71,wea_73[:3],'\n',
                                  wea_81,wea_83[:3],'\n',wea_91,wea_93[:3],'\n',wea_101,wea_103[:3],'\n',wea_111,wea_113[:3],'\n',
                                  wea_121,wea_123[:3],'\n',wea_131,wea_133[:3],'\n')

    url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/O-A0003-001?Authorization=CWB-29654F18-4C41-4CE1-BF28-A6889EACDBCD&elementName=TIME,WDSD,TEMP,HUMD,24R&parameterName=CITY'
    re = urllib.request.Request(url)
    req = urllib.request.urlopen(re)
    jsontext = json.loads(req.read())

    for x in loc:
        if tw.get() == x:
            # print('OK')
            for i in jsontext['records']['location']:
                if i['parameter'][0]['parameterValue'] == x:
                    a1 = i['time']['obsTime']
                    a2 = i['weatherElement'][0]['elementValue']
                    a3 = i['weatherElement'][1]['elementValue']
                    a4 = i['weatherElement'][2]['elementValue'] 
                    a5 = i['weatherElement'][3]['elementValue'] 
                    lb_.config(text=a1)
                    lb_6.config(text=a3+'°')
                    lb_7.config(text=a2+'公尺/秒')
                    lb_8.config(text=a4)
                    lb_9.config(text=a5+'毫米')
                    
            
root = tk.Tk()
root.title('My_Weather')
root.geometry('760x623+700+300')
root.resizable(False,False)
root.attributes('-topmost',1)
root.config(bg='#d9b4a2')

# fm1
frm1 = tk.Frame(root, width=900 , height=500, bg='#d9b4a2')
frm1.grid(row=0, rowspan=2, column=0)
lbfrm1 = tk.LabelFrame(frm1, text='台灣各地天氣預測', width=350 , height=615, relief=tk.RIDGE, bd=6, bg='#d9b4a2', font=('標楷體',16)).pack()

tw = tk.StringVar()
tw.set(' ')

tw_1 = tk.Radiobutton(frm1, text='基隆市', variable=tw, value='基隆市', bg='#d9b4a2', font=('標楷體',13), command=set_tw).place(x=22, y=45)
tw_2 = tk.Radiobutton(frm1, text='臺北市', variable=tw, value='臺北市' ,bg='#d9b4a2', font=('標楷體',13), command=set_tw).place(x=136, y=45)
tw_3 = tk.Radiobutton(frm1, text='新北市', variable=tw, value='新北市', bg='#d9b4a2', font=('標楷體',13), command=set_tw).place(x=250, y=45)

tw_4 = tk.Radiobutton(frm1, text='桃園市', variable=tw, value='桃園市', bg='#d9b4a2', font=('標楷體',13), command=set_tw).place(x=22, y=100)
tw_5 = tk.Radiobutton(frm1, text='新竹市', variable=tw, value='新竹市', bg='#d9b4a2', font=('標楷體',13), command=set_tw).place(x=136, y=100)
tw_6 = tk.Radiobutton(frm1, text='新竹縣', variable=tw, value='新竹縣', bg='#d9b4a2', font=('標楷體',13), command=set_tw).place(x=250, y=100)

tw_7 = tk.Radiobutton(frm1, text='苗栗縣', variable=tw, value='苗栗縣', bg='#d9b4a2', font=('標楷體',13), command=set_tw).place(x=22, y=160)
tw_8 = tk.Radiobutton(frm1, text='臺中市', variable=tw, value='臺中市', bg='#d9b4a2', font=('標楷體',13), command=set_tw).place(x=136, y=160)
tw_9 = tk.Radiobutton(frm1, text='彰化縣', variable=tw, value='彰化縣', bg='#d9b4a2', font=('標楷體',13), command=set_tw).place(x=250, y=160)

tw_10 = tk.Radiobutton(frm1, text='南投縣', variable=tw, value='南投縣', bg='#d9b4a2', font=('標楷體',13), command=set_tw).place(x=22, y=220)
tw_11 = tk.Radiobutton(frm1, text='雲林縣', variable=tw, value='雲林縣', bg='#d9b4a2', font=('標楷體',13), command=set_tw).place(x=136, y=220)
tw_12 = tk.Radiobutton(frm1, text='嘉義市', variable=tw, value='嘉義市', bg='#d9b4a2', font=('標楷體',13), command=set_tw).place(x=250, y=220)

tw_13 = tk.Radiobutton(frm1, text='嘉義縣', variable=tw, value='嘉義縣', bg='#d9b4a2', font=('標楷體',13), command=set_tw).place(x=22, y=280)
tw_14 = tk.Radiobutton(frm1, text='臺南市', variable=tw, value='臺南市', bg='#d9b4a2', font=('標楷體',13), command=set_tw).place(x=136, y=280)
tw_15 = tk.Radiobutton(frm1, text='高雄市', variable=tw, value='高雄市', bg='#d9b4a2', font=('標楷體',13), command=set_tw).place(x=250, y=280)

tw_16 = tk.Radiobutton(frm1, text='屏東縣', variable=tw, value='屏東縣', bg='#d9b4a2', font=('標楷體',13), command=set_tw).place(x=22, y=340)
tw_17 = tk.Radiobutton(frm1, text='宜蘭縣', variable=tw, value='宜蘭縣', bg='#d9b4a2', font=('標楷體',13), command=set_tw).place(x=136, y=340)
tw_18 = tk.Radiobutton(frm1, text='花蓮縣', variable=tw, value='花蓮縣', bg='#d9b4a2', font=('標楷體',13), command=set_tw).place(x=250, y=340)

tw_19 = tk.Radiobutton(frm1, text='臺東縣', variable=tw, value='臺東縣', bg='#d9b4a2', font=('標楷體',13), command=set_tw).place(x=12, y=400)
tw_20 = tk.Radiobutton(frm1, text='澎湖縣', variable=tw, value='澎湖縣', bg='#d9b4a2', font=('標楷體',13), command=set_tw).place(x=96, y=400)
tw_21 = tk.Radiobutton(frm1, text='金門縣', variable=tw, value='金門縣', bg='#d9b4a2', font=('標楷體',13), command=set_tw).place(x=180, y=400)
tw_22 = tk.Radiobutton(frm1, text='連江縣', variable=tw, value='連江縣', bg='#d9b4a2', font=('標楷體',13), command=set_tw).place(x=260, y=400)

tw_bnt = tk.Button(frm1, text='搜尋', width=5, fg='#C18265', bg='white', font=('YouYuan',17), relief=tk.RAISED, command=fd_wt).place(x=140, y=450)

lb = tk.Label(frm1, text='已選擇：', bg='#d9b4a2', font=('標楷體',14))
lb.place(x=16,y=560)


# fm2
frm2 = tk.Frame(root, bg='#C2B099', width=410 , height=305)
frm2.grid(row=0, column=1)

lst_1 = tk.Listbox(frm2, width=51 , height=19, bg='#C2B099', font=('YouYuan',12))
lst_1.grid(row=0)

y_scb = tk.Scrollbar(frm2)
y_scb.grid(row=0,sticky= tk.E+tk.N+tk.S)
x_scb = tk.Scrollbar(frm2, orient=tk.HORIZONTAL)
x_scb.grid(row=0,sticky= tk.E+tk.W+tk.S)

y_scb.config(command=lst_1.yview)
lst_1.config(yscrollcommand=y_scb.set)
x_scb.config(command=lst_1.xview)
lst_1.config(xscrollcommand=x_scb.set)


# frm3
frm3 = tk.Frame(root, bg='#F0DFA7', width=410 , height=305)
frm3.grid(row=1, column=1, sticky=tk.W)

lb_1 = tk.Label(frm3, text='即時觀測時間：', font=('YouYuan',16), bg='#F0DFA7').place(x=4, y=10)
lb_2 = tk.Label(frm3, text='溫度', font=('YouYuan',16), bg='#F0DFA7').place(x=10, y=100)
lb_3 = tk.Label(frm3, text='風速', font=('YouYuan',16), bg='#F0DFA7').place(x=105, y=100)
lb_4 = tk.Label(frm3, text='相對溼度', font=('YouYuan',16), bg='#F0DFA7').place(x=195, y=100)
lb_5 = tk.Label(frm3, text='累積雨量', font=('YouYuan',16), bg='#F0DFA7').place(x=305, y=100)

lb_ = tk.Label(frm3, text='', font=('YouYuan',15), bg='#F0DFA7')
lb_.place(x=170, y=12)
lb_6 = tk.Label(frm3, text='--------', font=('YouYuan',15), bg='#F0DFA7')
lb_6.place(x=10, y=150)
lb_7 = tk.Label(frm3, text='--------', font=('YouYuan',15), bg='#F0DFA7')
lb_7.place(x=90, y=150)
lb_8 = tk.Label(frm3, text='--------', font=('YouYuan',15), bg='#F0DFA7')
lb_8.place(x=220, y=150)
lb_9 = tk.Label(frm3, text='--------', font=('YouYuan',15), bg='#F0DFA7')
lb_9.place(x=300, y=150)

root.mainloop()