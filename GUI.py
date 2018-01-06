import tkinter as tk 
import os
import time
from weather import Weather 
from distance import Distance
from tkinter import messagebox

def new_window():
    os.system("python3 ./GUI.py")

def choose_start():
    global start
    start=place_from.get(place_from.curselection())
    choosef_string.set(start)
    print(start)

def choose_destination():
    global destination
    destination=place_to.get(place_to.curselection())
    chooset_string.set(destination)
    print(destination)

def update_clock():
    now = time.strftime("%H:%M:%S")
    time_nowlabel.configure(text="current time : "+now)
    time_nowlabel.after(1000,update_clock)

def foot():
    global by_what
    by_what=1
def car():
    global by_what
    by_what=2
def public():
    global by_what
    by_what=3
def fore_submit():
    
    global weather_descr
    weather_descr=[]
    f_p=forecast_place.get(forecast_place.curselection())
    fore_name.set('Loaction : '+f_p)
    place=Weather(f_p)
    place.getWeekForecast()
    for i in range(7):
        forecast_weekimg[i].config(file=place.fore_week[i]['icon128_url'])
    place.getHourlyForecast()
    for i in range(24):
        forecast_hourimg[i].config(file=place.fore_hourly[i]['icon64_url'])
    for i in range(7):
        weather_descr.append(place.fore_week[i]['fcttext'])

def show1():
    messagebox.showinfo("Weather description", weather_descr[0])
def show2():
    messagebox.showinfo("Weather description", weather_descr[1])
def show3():
    messagebox.showinfo("Weather description", weather_descr[2])
def show4():
    messagebox.showinfo("Weather description", weather_descr[3])
def show5():
    messagebox.showinfo("Weather description", weather_descr[4])
def show6():
    messagebox.showinfo("Weather description", weather_descr[5])
def show7():
    messagebox.showinfo("Weather description", weather_descr[6])

def flush():
    global start
    global destination
    global arrival_time
    global by_what
    start=""
    destination=""
    choosef_string.set(start)
    chooset_string.set(destination)
    arrival_time=0
    for i in range(8):
        Asugglb_list[i].set("")
    for i in range(8):
        Bsugglb_list[i].set("")
    for i in range(5):
        Asuggimg_list[i].config(file='question32.png')
        #Asuggimg_list[i].blank()
    for i in range(5):
        Bsuggimg_list[i].config(file='question32.png')
        #Bsuggimg_list[i].blank()
    sta_landmark_img.config(file='cityscape.png')
    sta_weather_img.config(file='question-sign.png')
    des_landmark_img.config(file='cityscape.png')
    des_weather_img.config(file='question-sign.png')
    by_what=0

def helpme():
    framehelp.tkraise()
def back_to_1():
    frame1.tkraise()
def forecast():
    frameforecase.tkraise()

def print_selection():
    global arrival_time
    arrival_time=arrival_hour.get()
    print(arrival_time)
    pass

def print_APM():
    global arrival_time
    if arrival_APM.get()==1:
        arrival_time+=12
    print(arrival_time)
    
def submit():
    global arrival_time
    global by_what
    arrival_time=0

    for i in range(8):
        Asugglb_list[i].set("")
        Bsugglb_list[i].set("")
    suggestion_list=[]
    sufimg_list=[]
    sug_num=0
    bring_umbra=0
    bring_coat=0
    bring_pills=0
    wind_Description=""
    home=Weather(start)
    imagenum=1
    
    localtime = time.localtime(time.time())
    
    google_desname=destination
    if google_desname=='Yun-lin':
        google_desname='Yunlin'

    google_toname=start
    if google_toname=='Yun-lin':
        google_toname='Yunlin'

    if by_what==0:
        arrival_time=arrival_hour.get()
        if arrival_APM.get()==1:
            arrival_time+=12
    elif by_what==1:
        if localtime[4]>30:
            arrival_time+=1
        transport=Distance(google_toname,google_desname,2)
        arrival_time+=localtime[3]
        if transport.duration_hour<24:
            arrival_time+=transport.duration_hour
    elif by_what==2:
        if localtime[4]>30:
            arrival_time+=1
        transport=Distance(google_toname,google_desname,0)
        arrival_time+=localtime[3]
        if transport.duration_hour<24:
            arrival_time+=transport.duration_hour
    elif by_what==3 :  
        if localtime[4]>30:
            arrival_time+=1
        transport=Distance(google_toname,google_desname,1)
        arrival_time+=localtime[3]
        if transport.duration_hour<24:
            arrival_time+=transport.duration_hour

    arrival_time%=24

    print(arrival_time)
    
    
    if home.wind_kph<1:
        wind_Description='Calm'
    elif home.wind_kph<5:
        wind_Description='Light air'
    elif home.wind_kph<11:
        wind_Description='Gentle breeze'
    elif home.wind_kph<19:
        wind_Description='Moderate breeze'
    elif home.wind_kph<28:
        wind_Description='Fresh breeze'
    elif home.wind_kph<38:
        wind_Description='Strong breeze'
    elif home.wind_kph<49:
        wind_Description='High wind'
    elif home.wind_kph<61:
        wind_Description='High wind'
    elif home.wind_kph<74:
        wind_Description='Gale'
    elif home.wind_kph<88:
        wind_Description='severe gale'
    elif home.wind_kph<102:
        wind_Description='Storm'
    elif home.wind_kph<117:
        wind_Description='Violent storm'
    elif home.wind_kph>118:
        wind_Description='Hurricane force'

    Asugglb_list[0].set('the weather of '+home.location+' now is '+home.condition)
    Asugglb_list[1].set('Temp : '+str(home.temp_c)+'.c')
    Asugglb_list[2].set('Wind scale : '+wind_Description+" "+str(home.wind_kph))
    Asugglb_list[3].set('humidity : '+str(home.humidity))

    to=Weather(destination)
    to.getHourForecast(int(arrival_time))
    Bsugglb_list[0].set('the forecast weather of '+to.location+' now is '+to.hour_condition)
    Bsugglb_list[1].set('forecast Temp : '+str(to.hour_temp)+'.c')
    Bsugglb_list[2].set('forecast Rainfall probability : '+str(to.poprec)+'%')
    Bsugglb_list[3].set('forecast humidity : '+str(to.hour_humidity)+'%')

    if by_what!=0:
        Asugglb_list[4].set('Distance : '+transport.distance)
        Asugglb_list[5].set('Duration : '+transport.duration_text)
        if by_what==3 and transport.has_fare==True:
            Asugglb_list[6].set('Fare : '+transport.fare_text)

    if destination=='Taipei' or start=='Taipei' :
        Asugglb_list[7].set('Bring your passport!!!!!!')

    if to.poprec>0 :
        sug='Bring your umbrella!!'
        suggestion_list.append(sug)
        sug_num+=1
        bring_umbra=1
        sufimg_list.append('umbrella.png')
    if float(to.hour_temp)-home.temp_c<0 :
        sug='Bring a coat'
        suggestion_list.append(sug)
        sug_num+=1
        bring_coat=1
        sufimg_list.append('hoodie.png')
    if by_what!=0 and transport.duration_hour>2:
        sug='Bring Motion sickness pills if you need'
        suggestion_list.append(sug)
        sug_num+=1
        bring_pills=1
        sufimg_list.append('pills.png')
    if by_what==3:
        sug='Bring easycard if you need'
        suggestion_list.append(sug)
        sug_num+=1
        bring_card=1
        sufimg_list.append('easycard.png')
    

    for i in range(sug_num) :
        Bsugglb_list[4+i].set(suggestion_list[i])

    Asuggimg_list[0].config(file=home.icon32_url)
    Bsuggimg_list[0].config(file=to.hour32_icon_url)
    for i in range(1,5):
        Bsuggimg_list[i].blank()

    for i in range(4) :
        if(i<sug_num):
            Asuggimg_list[1+i].config(file=sufimg_list[i])
        else:
            Asuggimg_list[1+i].blank()
    sta_landmark_img.config(file=home.location_url)
    sta_weather_img.config(file=home.icon128_url)
    des_landmark_img.config(file=to.location_url)
    des_weather_img.config(file=to.hour128_icon_url)

    



    A_place_name.set(start)
    B_place_name.set(destination)
    by_what=0



#arrival_hour=tk.IntVar()
window=tk.Tk()
window.title('旅行小幫手')
window.geometry('1368x768')
window.resizable(0,0)


##variable
by_what=0
start=""
destination=""
arrival_time=0
arrival_hour=tk.IntVar()
arrival_APM=tk.IntVar()
A_place_name=tk.StringVar()
B_place_name=tk.StringVar()
fore_name=tk.StringVar()
Asugglb_list=[]
Asuggimg_list=[]
Bsugglb_list=[]
Bsuggimg_list=[]
place_list=[
    'Keelung',
    'Taipei',
    'Yilan',
    'Hsin-chu',
    'Miao-li',
    'Taichung',
    'Chang-hua',
    'Nantou',
    'Yun-lin',
    'Tainan',
    'Kao-hsiung',
    'Hualien'
]
forecast_weekimg=[]
forecast_hourlab=[]
forecast_hourimg=[]
weather_descr=[]
sta_landmark_img=tk.PhotoImage(file='cityscape.png')
sta_weather_img=tk.PhotoImage(file='question-sign.png')
des_landmark_img=tk.PhotoImage(file='cityscape.png')
des_weather_img=tk.PhotoImage(file='question-sign.png')

###




menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
modemenu= tk.Menu(menubar, tearoff=0)

menubar.add_cascade(label='File', menu=filemenu)
menubar.add_cascade(label='Mode', menu=modemenu)

filemenu.add_command(label='New', command=new_window)
filemenu.add_command(label='Help', command=helpme)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=window.quit)

modemenu.add_command(label='travel',command=back_to_1)
modemenu.add_command(label='forecast',command=forecast)
'''
00394d
80bfff
'''
### frame 1 
frame1= tk.Frame(window,bg='#00394d',width=1368,height=768)
frame1.place(anchor='nw')



labelframe = tk.LabelFrame(frame1,text = "Suggestion",font=('Arial',16),bg="#00394d",fg='red',height="768",width='684')
labelframe.place(anchor='nw')


Asugg_frame=tk.Frame(labelframe,bg='#00394d',width=680,height=300)
Bsugg_frame=tk.Frame(labelframe,bg='#00394d',width=680,height=300)

Asugg_frame.place(x=0,y=0)
Bsugg_frame.place(x=0,y=300)


##Asugg_frame

for i in range(5):
    test=tk.PhotoImage()
    Asuggimg_list.append(test)

for i in range(5):
    Asuggimg_list[i].config(file='question32.png')

for i in range(8):
    choosef_string=tk.StringVar()
    Asugglb_list.append(choosef_string)


A_name=tk.Label(Asugg_frame,bg='#e6f2ff',fg='black',font=('Arial',16),textvariable=A_place_name,width=35,height=1).place(x=230,y=10)


A_p1=tk.Label(Asugg_frame,bg='#00394d',image=Asuggimg_list[0],width=32,height=32).place(x=5,y=5)
A_p2=tk.Label(Asugg_frame,bg='#00394d',image=Asuggimg_list[1],width=32,height=32).place(x=47,y=5)
A_p3=tk.Label(Asugg_frame,bg='#00394d',image=Asuggimg_list[2],width=32,height=32).place(x=89,y=5)
A_p4=tk.Label(Asugg_frame,bg='#00394d',image=Asuggimg_list[3],width=32,height=32).place(x=131,y=5)
A_p5=tk.Label(Asugg_frame,bg='#00394d',image=Asuggimg_list[4],width=32,height=32).place(x=173,y=5)

A_1=tk.Label(Asugg_frame,bg='#ffffff',fg='black',font=('Arial',16),width=55,height=1,textvariable = Asugglb_list[0]).place(x=5,y=47)
A_2=tk.Label(Asugg_frame,bg='#ffffff',fg='black',font=('Arial',16),width=55,height=1,textvariable = Asugglb_list[1]).place(x=5,y=74)
A_3=tk.Label(Asugg_frame,bg='#ffffff',fg='black',font=('Arial',16),width=55,height=1,textvariable = Asugglb_list[2]).place(x=5,y=101)
A_4=tk.Label(Asugg_frame,bg='#ffffff',fg='black',font=('Arial',16),width=55,height=1,textvariable = Asugglb_list[3]).place(x=5,y=128)
A_5=tk.Label(Asugg_frame,bg='#ffffff',fg='black',font=('Arial',16),width=55,height=1,textvariable = Asugglb_list[4]).place(x=5,y=155)
A_6=tk.Label(Asugg_frame,bg='#ffffff',fg='black',font=('Arial',16),width=55,height=1,textvariable = Asugglb_list[5]).place(x=5,y=182)
A_7=tk.Label(Asugg_frame,bg='#ffffff',fg='black',font=('Arial',16),width=55,height=1,textvariable = Asugglb_list[6]).place(x=5,y=209)
A_8=tk.Label(Asugg_frame,bg='#ffffff',fg='red',font=('Arial',16),width=55,height=1,textvariable = Asugglb_list[7]).place(x=5,y=236)


test=tk.PhotoImage()
##Bsugg_frame

for i in range(5):
    test=tk.PhotoImage()
    Bsuggimg_list.append(test)

for i in range(5):
    Bsuggimg_list[i].config(file='question32.png')

for i in range(8):
    choosef_string=tk.StringVar()
    Bsugglb_list.append(choosef_string)


B_name=tk.Label(Bsugg_frame,bg='#e6f2ff',font=('Arial',16),textvariable=B_place_name,width=35,height=1).place(x=230,y=10)

B_p1=tk.Label(Bsugg_frame,bg='#00394d',image=Bsuggimg_list[0],width=32,height=32).place(x=5,y=5)
B_p2=tk.Label(Bsugg_frame,bg='#00394d',image=Bsuggimg_list[1],width=32,height=32).place(x=47,y=5)
B_p3=tk.Label(Bsugg_frame,bg='#00394d',image=Bsuggimg_list[2],width=32,height=32).place(x=89,y=5)
B_p4=tk.Label(Bsugg_frame,bg='#00394d',image=Bsuggimg_list[3],width=32,height=32).place(x=131,y=5)
B_p5=tk.Label(Bsugg_frame,bg='#00394d',image=Bsuggimg_list[4],width=32,height=32).place(x=173,y=5)


B_1=tk.Label(Bsugg_frame,bg='#ffffff',fg='black',font=('Arial',16),width=55,height=1,textvariable = Bsugglb_list[0]).place(x=5,y=47)
B_2=tk.Label(Bsugg_frame,bg='#ffffff',fg='black',font=('Arial',16),width=55,height=1,textvariable = Bsugglb_list[1]).place(x=5,y=74)
B_3=tk.Label(Bsugg_frame,bg='#ffffff',fg='black',font=('Arial',16),width=55,height=1,textvariable = Bsugglb_list[2]).place(x=5,y=101)
B_4=tk.Label(Bsugg_frame,bg='#ffffff',fg='black',font=('Arial',16),width=55,height=1,textvariable = Bsugglb_list[3]).place(x=5,y=128)
B_5=tk.Label(Bsugg_frame,bg='#ffffff',fg='red',font=('Arial',16),width=55,height=1,textvariable = Bsugglb_list[4]).place(x=5,y=155)
B_6=tk.Label(Bsugg_frame,bg='#ffffff',fg='red',font=('Arial',16),width=55,height=1,textvariable = Bsugglb_list[5]).place(x=5,y=182)
B_7=tk.Label(Bsugg_frame,bg='#ffffff',fg='red',font=('Arial',16),width=55,height=1,textvariable = Bsugglb_list[6]).place(x=5,y=209)
B_8=tk.Label(Bsugg_frame,bg='#ffffff',fg='red',font=('Arial',16),width=55,height=1,textvariable = Bsugglb_list[7]).place(x=5,y=236)


##lavelframe


##from_frame
from_frame=tk.Frame(frame1,bg='#ffffff',width=684,height=250)
from_frame.place(x=684,y=10)


place_from= tk.Listbox(from_frame,bg='#ffffff',font=('Arial',12),width=50,height=10)
for line in range(12):
   place_from.insert('end',place_list[line])
place_from.place(x=230,y=0)

from_button=tk.Button(from_frame,text='choose your starting point',width=61,height=1,command=choose_start)
from_button.place(x=230,y=185)


p1f_image=tk.PhotoImage(file='home.png')
p1f=tk.Label(from_frame,image=p1f_image,bg='#ffffff',width=64,height=64).place(x=6,y=10)


p2f_image=tk.PhotoImage(file='airport.png')
p2f=tk.Label(from_frame,image=p2f_image,bg='#ffffff',width=64,height=64).place(x=82,y=10)


p3f_image=tk.PhotoImage(file='bus-stop.png')
p3f=tk.Label(from_frame,image=p3f_image,bg='#ffffff',width=64,height=64).place(x=158,y=10)



'''
from_string=tk.StringVar()
from_string.set('starting point')
from_label=tk.Label(from_frame,bg='white',font=('Arial',16),width=18,height=3,textvariable=from_string)
from_label.place(x=6,y=5)
'''
choosef_string=tk.StringVar()
choosef_string.set('')
choosef_label=tk.Label(from_frame,bg='#ffffff',font=('Arial',16),width=18,height=5,textvariable=choosef_string)
choosef_label.place(x=6,y=100)

split=tk.Frame(frame1,bg='#000000',width=684,height=3)
split.place(x=684,y=242)

##to_frame
to_frame=tk.Frame(frame1,bg='#ffffff',width=684,height=250)
to_frame.place(x=684,y=260)

place_to= tk.Listbox(to_frame,bg='#ffffff',font=('Arial',12),width=50,height=10)
for line in range(12):
   place_to.insert('end',place_list[line])
place_to.place(x=230,y=0)

to_button=tk.Button(to_frame,text='choose your destination',width=61,height=1,command=choose_destination)
to_button.place(x=230,y=185)

'''
to_string=tk.StringVar()
to_string.set('destination')
to_label=tk.Label(to_frame,bg='white',font=('Arial',16),width=18,height=3,textvariable=to_string)
to_label.place(x=6,y=5)'''

p1_image=tk.PhotoImage(file='sports-car.png')
p1=tk.Label(to_frame,image=p1_image,bg='#ffffff',width=64,height=64).place(x=6,y=10)

p2_image=tk.PhotoImage(file='airplane-shape.png')
p2=tk.Label(to_frame,image=p2_image,bg='#ffffff',width=64,height=64).place(x=82,y=10)


p3_image=tk.PhotoImage(file='bus.png')
p3=tk.Label(to_frame,image=p3_image,bg='#ffffff',width=64,height=64).place(x=158,y=10)



chooset_string=tk.StringVar()
chooset_string.set('')
chooset_label=tk.Label(to_frame,bg='#ffffff',font=('Arial',16),width=18,height=5,textvariable=chooset_string)
chooset_label.place(x=6,y=100)



##weather_picture

picture_frame=tk.Frame(labelframe,bg='#00394d',width=665,height=150)
picture_frame.place(x=5,y=588)



sta_landmark_lab=tk.Label(picture_frame,image= sta_landmark_img,bg = "#00394d", height = 128, width = 128)
sta_landmark_lab.place(x=30,y=4)


sta_weather_lab=tk.Label(picture_frame,image= sta_weather_img,bg = "#00394d", height = 128, width = 128)
sta_weather_lab.place(x=168,y=12)


sta_to_img=tk.PhotoImage(file='arror_to.png')
sta_to_lab=tk.Label(picture_frame,image= sta_to_img,bg = "#00394d", height = 64, width = 64)
sta_to_lab.place(x=306,y=50)


des_landmark_lab=tk.Label(picture_frame,image= des_landmark_img,bg = "#00394d", height = 128, width = 128)
des_landmark_lab.place(x=380,y=4)

des_weather_lab=tk.Label(picture_frame,image= des_weather_img,bg = "#00394d", height = 128, width = 128)
des_weather_lab.place(x=518,y=12)


#sta_weather=tk.Label(picture_frame,image= sta_wea_file,bg = "white", height = 160, width = 160)
#sta_weather.place(x=10,y=2)


##time

time_frame=tk.Frame(frame1,bg='#80bfff',width=684,height=190)
time_frame.place(x=683,y=490)

time_nowlabel=tk.Label(time_frame,text="54545",font=('Arial',14),bg='#80bfff',width=20,height=3)
time_nowlabel.place(x=10,y=10)
update_clock()

time_p1_image=tk.PhotoImage(file='exit.png')
time_p1=tk.Button(time_frame,bg='#80bfff',image=time_p1_image,width=64,height=64,command=foot).place(x=13,y=85)

time_p2_image=tk.PhotoImage(file='sedan-car-model.png')
time_p2=tk.Button(time_frame,bg='#80bfff',image=time_p2_image,width=64,height=64,command=car).place(x=89,y=85)

time_p3_image=tk.PhotoImage(file='bus(1).png')
time_p3=tk.Button(time_frame,bg='#80bfff',image=time_p3_image,width=64,height=64,command=public).place(x=165,y=85)


time_Labelframe=tk.LabelFrame(time_frame,text = "arrival time",font=('Arial',14),bg='#62b4f4',fg='red',height="140",width='400')
time_Labelframe.place(x=274,y=10)


r1 = tk.Radiobutton(time_Labelframe,variable=arrival_hour ,bg='#80bfff',text='0', value=0,command=print_selection)
r1.grid(row=0,column=0, padx=10, pady=10)
r2 = tk.Radiobutton(time_Labelframe, bg='#80bfff',text='1',variable=arrival_hour , value=1,command=print_selection)
r2.grid(row=0,column=1, padx=10, pady=10)
r3 = tk.Radiobutton(time_Labelframe, bg='#80bfff',text='2',variable=arrival_hour , value=2,command=print_selection)
r3.grid(row=0,column=2, padx=15, pady=10)
r4 = tk.Radiobutton(time_Labelframe,bg='#80bfff', text='3',variable=arrival_hour , value=3,command=print_selection)
r4.grid(row=0,column=3, padx=15, pady=15)
r5 = tk.Radiobutton(time_Labelframe, bg='#80bfff',text='4',variable=arrival_hour , value=4,command=print_selection)
r5.grid(row=0,column=4, padx=10, pady=10)
r6 = tk.Radiobutton(time_Labelframe, bg='#80bfff',text='5',variable=arrival_hour , value=5,command=print_selection)
r6.grid(row=0,column=5, padx=10, pady=10)
r7 = tk.Radiobutton(time_Labelframe,bg='#80bfff', text='6',variable=arrival_hour , value=6,command=print_selection)
r7.grid(row=1,column=0, padx=10, pady=10)
r8 = tk.Radiobutton(time_Labelframe,bg='#80bfff', text='7',variable=arrival_hour , value=7,command=print_selection)
r8.grid(row=1,column=1, padx=10, pady=10)
r9 = tk.Radiobutton(time_Labelframe, bg='#80bfff',text='8',variable=arrival_hour , value=8,command=print_selection)
r9.grid(row=1,column=2, padx=10, pady=10)
r10 = tk.Radiobutton(time_Labelframe,bg='#80bfff', text='9',variable=arrival_hour , value=9,command=print_selection)
r10.grid(row=1,column=3, padx=10, pady=10)
r11 = tk.Radiobutton(time_Labelframe, bg='#80bfff',text='10',variable=arrival_hour , value=10,command=print_selection)
r11.grid(row=1,column=4, padx=10, pady=10)
r12 = tk.Radiobutton(time_Labelframe, bg='#80bfff',text='11',variable=arrival_hour , value=11,command=print_selection)
r12.grid(row=1,column=5, padx=10, pady=10)
r13 = tk.Radiobutton(time_Labelframe, bg='#80bfff',text='AM',variable=arrival_APM , value=0,command=print_APM)
r13.grid(row=2,column=4, padx=10, pady=10)
r14 = tk.Radiobutton(time_Labelframe, bg='#80bfff',text='PM',variable=arrival_APM , value=1,command=print_APM)
r14.grid(row=2,column=5, padx=10, pady=10)

##submit

submit_frame=tk.Frame(frame1,bg='#80bfff',width=684,height=90)
submit_frame.place(x=683,y=680)


submit_img=tk.PhotoImage(file='./image/submit.png')
submit_button=tk.Button(submit_frame,image=submit_img,width=420,height=64,command=submit)
submit_button.place(x=215,y=10)


flush_img=tk.PhotoImage(file='redo.png')
flush_button=tk.Button(submit_frame,image=flush_img,width=160,height=64,command=flush)
flush_button.place(x=20,y=10)


###frame1

###frameforecase
frameforecase= tk.Frame(window,bg='white',width=1368,height=768)
frameforecase.place(anchor='nw')

day_1=tk.Frame(frameforecase,bg='white',width=195,height=384)
day_2=tk.Frame(frameforecase,bg='white',width=195,height=384)
day_3=tk.Frame(frameforecase,bg='white',width=195,height=384)
day_4=tk.Frame(frameforecase,bg='white',width=195,height=384)
day_5=tk.Frame(frameforecase,bg='white',width=195,height=384)
day_6=tk.Frame(frameforecase,bg='white',width=195,height=384)
day_7=tk.Frame(frameforecase,bg='white',width=198,height=384)
day_1.place(x=0,y=0)
day_2.place(x=195,y=0)
day_3.place(x=390,y=0)
day_4.place(x=585,y=0)
day_5.place(x=780,y=0)
day_6.place(x=975,y=0)
day_7.place(x=1170,y=0)

d1_image=tk.PhotoImage(file='./number/1.png')
d1_label=tk.Label(day_1,image=d1_image,width=64,height=64).place(x=0,y=0)

d2_image=tk.PhotoImage(file='./number/2.png')
d2_label=tk.Label(day_2,image=d2_image,width=64,height=64).place(x=0,y=0)

d3_image=tk.PhotoImage(file='./number/3.png')
d3_label=tk.Label(day_3,image=d3_image,width=64,height=64).place(x=0,y=0)

d4_image=tk.PhotoImage(file='./number/4.png')
d4_label=tk.Label(day_4,image=d4_image,width=64,height=64).place(x=0,y=0)

d5_image=tk.PhotoImage(file='./number/5.png')
d5_label=tk.Label(day_5,image=d5_image,width=64,height=64).place(x=0,y=0)

d6_image=tk.PhotoImage(file='./number/6.png')
d6_label=tk.Label(day_6,image=d6_image,width=64,height=64).place(x=0,y=0)

d7_image=tk.PhotoImage(file='./number/7.png')
d7_label=tk.Label(day_7,image=d7_image,width=64,height=64).place(x=0,y=0)

for i in range(7):
    test=tk.PhotoImage()
    forecast_weekimg.append(test)
for i in range(7):
    forecast_weekimg[i].config(file='question-sign.png')


d1w_label=tk.Label(day_1,image=forecast_weekimg[0],bg='white',width=128,height=128).place(x=26,y=130)
d2w_label=tk.Label(day_2,image=forecast_weekimg[1],bg='white',width=128,height=128).place(x=26,y=130)
d3w_label=tk.Label(day_3,image=forecast_weekimg[2],bg='white',width=128,height=128).place(x=26,y=130)
d4w_label=tk.Label(day_4,image=forecast_weekimg[3],bg='white',width=128,height=128).place(x=26,y=130)
d5w_label=tk.Label(day_5,image=forecast_weekimg[4],bg='white',width=128,height=128).place(x=26,y=130)
d6w_label=tk.Label(day_6,image=forecast_weekimg[5],bg='white',width=128,height=128).place(x=26,y=130)
d7w_label=tk.Label(day_7,image=forecast_weekimg[6],bg='white',width=128,height=128).place(x=26,y=130)

det=tk.PhotoImage(file='q32.png')
d1_button=tk.Button(day_1,image=det, relief = 'flat' ,bg='white',width=32,height=32,command=show1).place(x=150,y=250)
d2_button=tk.Button(day_2,image=det, relief = 'flat' ,bg='white',width=32,height=32,command=show2).place(x=150,y=250)
d3_button=tk.Button(day_3,image=det, relief = 'flat' ,bg='white',width=32,height=32,command=show3).place(x=150,y=250)
d4_button=tk.Button(day_4,image=det, relief = 'flat' ,bg='white',width=32,height=32,command=show4).place(x=150,y=250)
d5_button=tk.Button(day_5,image=det, relief = 'flat' ,bg='white',width=32,height=32,command=show5).place(x=150,y=250)
d6_button=tk.Button(day_6,image=det, relief = 'flat' ,bg='white',width=32,height=32,command=show6).place(x=150,y=250)
d7_button=tk.Button(day_7,image=det, relief = 'flat' ,bg='white',width=32,height=32,command=show7).place(x=150,y=250)

hour_frame=tk.Frame(frameforecase,bg='#00394d',width=905,height=454)
hour_frame.place(x=0,y=320)

for i in range(24):
    test=tk.PhotoImage()
    forecast_hourimg.append(test)

for i in range(24):
    label=tk.Label(hour_frame,image=forecast_hourimg[i],bg='#00394d',width=64,height=64)
    forecast_hourlab.append(label)

for i in range(24):
    forecast_hourlab[i].place(x=(i%8)*107+43,y=int(i/8)*112+83)

for i in range(24):
    label=tk.Label(hour_frame,text=str(i+1),width=4,height=1,font=('Arial',12)).place(x=(i%8)*107+55,y=int(i/8)*112+53)
'''
for i in range(3):
    label=tk.Label(hour_frame,text=str(i*8+1)+' to '+str((i+1)*8),width=10,height=1,font=('Arial',12)).place(x=5,y=20+i*110)
'''
#,bg='black'
last_frame=tk.Frame(frameforecase,bg='#80bfff',width=463,height=454)
last_frame.place(x=905,y=320)


forecast_place= tk.Listbox(last_frame,font=('Arial',12),width=50,height=10)
for line in range(12):
   forecast_place.insert('end',place_list[line])
forecast_place.place(x=5,y=5)

fore_submit_img=tk.PhotoImage(file='./image/submit.png')
fore_submit_button=tk.Button(last_frame,image=fore_submit_img,width=420,height=64,command=fore_submit)
fore_submit_button.place(x=20,y=350)


fore_flush_label=tk.Label(last_frame,textvariable=fore_name,font=('Arial',16),width=35,height=3)
fore_flush_label.place(x=20,y=250)



framehelp= tk.Frame(window,bg='#00394d',width=1368,height=768)
framehelp.place(anchor='nw')

help_f1=tk.Frame(framehelp,bg='#00394d',width=800,height=768)
help_f1.place(anchor='nw')

help_f2=tk.Frame(framehelp,bg='white',width=568,height=484)
help_f2.place(x=800,y=0)

help_f3=tk.Frame(framehelp,bg='#80bfff',width=568,height=284)
help_f3.place(x=800,y=484)

img=[
    
    tk.PhotoImage(file='./icon-64/clear.png'),
    tk.PhotoImage(file='./icon-64/cloudy.png'),
    tk.PhotoImage(file='./icon-64/fog.png'),
    tk.PhotoImage(file='./icon-64/mostlycloudy.png'),
    tk.PhotoImage(file='./icon-64/mostlysunny.png'),
    tk.PhotoImage(file='./icon-64/rain.png'),
    tk.PhotoImage(file='./icon-64/snow.png'),
    tk.PhotoImage(file='./icon-64/tstorms.png')
]

img_name=[
    'clear',
    'cloudy',
    'fog',
    'mostlycloudy',
    'mostlysunny',
    'rain',
    'snow',
    'tstorms'
]
notie_img=[
    tk.PhotoImage(file='hoodie.png'),
    tk.PhotoImage(file='umbrella.png'),
    tk.PhotoImage(file='pills.png'),
    tk.PhotoImage(file='easycard.png')
]
notie_name=[
    'Bring coat',
    'Bring umbrella',
    'Bring pills',
    'Bring easycard'
]


for i in range(8):
    l=tk.Label(help_f1,image=img[i],bg='#00394d',width=64,height=64).place(y=28+(64+28)*i,x=20)

for i in range(8):
    l=tk.Label(help_f1,text=img_name[i],bg='#00394d',fg='white',font=('Arial',20),width=20,height=1).place(y=48+(64+28)*i,x=80)

for  i in range(4):
    l=tk.Label(help_f1,image=notie_img[i],bg='#00394d',fg='white',width=32,height=32).place(y=40+(64+28)*i,x=420)


for i in range(4):
    l=tk.Label(help_f1,text=notie_name[i],bg='#00394d',fg='white',font=('Arial',20),width=20,height=1).place(y=45+(64+28)*i,x=470)


step=[
    'steps for travel mode',
    '1. choose your starting point',
    '2. choose your destination',
    '3. choose your arrival time or transport',
    '4. press submit',
    '5. see the notice in suggestion label'
]

for i in range(6):
    l=tk.Label(help_f2,text=step[i],font=('Arial',15),width=45,height=1).place(y=45+(65)*i,x=30)
step2=[
    'steps for forecast mode',
    '1. choose your place and press submit',
    '2. the following 7days weather are in the top part',
    '3. the following 24hours weather are in the left  part'
]
for i in range(4):
    l=tk.Label(help_f3,text=step2[i],font=('Arial',15),width=45,height=1).place(y=45+(65)*i,x=30)
frame1.tkraise()

window.config(menu=menubar)
window.mainloop()


















'''
sta_weather=tk.Canvas(picture_frame, bg = "blue", height = 160, width = 160)
sta_landmark=tk.Canvas(picture_frame, bg = "blue", height = 160, width = 160)

des_weather=tk.Canvas(picture_frame, bg = "blue", height = 160, width = 160)
des_landmark=tk.Canvas(picture_frame, bg = "blue", height = 160, width = 160)

sta_weather.place(x=10,y=2)
sta_landmark.place(x=175,y=2)
des_weather.place(x=349,y=2)
des_landmark.place(x=514,y=2)

sta_wea_file=tk.PhotoImage(file='sun.gif')
sta_wea_image=sta_weather.create_image(160,160,anchor='nw',image=sta_wea_file)
'''