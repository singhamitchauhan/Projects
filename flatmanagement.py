from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
import mysql.connector


mainwindow=Tk()
mainwindow.title("Flat Management System")
mainwindow.geometry("720x240")
mainwindow.configure(background="#8e5f3a")
mainwindow.minsize(720, 240)
mainwindow.maxsize(720, 240)

#####################REMOVE ALL WIDGETS###################

def remove_all_widgets():
    for widget in frame333.winfo_children():
        widget.grid_remove()

#####################LOGIN WINDOW#########################

def login():

    loginwindow = Tk()
    loginwindow.title("LOGIN")
    loginwindow.geometry("250x200")
    loginwindow.configure(background="#8e5f3a")
    loginwindow.minsize(250, 200)
    loginwindow.maxsize(250, 200)
    loginframe=Frame(loginwindow)
    loginframe.place(x=30,y=30)


    UserID = Label(loginframe, text="Enter The User Id")
    UserID.pack()
    UserIDentry = Entry(loginframe)
    UserIDentry.pack()
    Password = Label(loginframe, text="Enter The Password")
    Password.pack()
    Passwordentry = Entry(loginframe,show="*")
    Passwordentry.pack()

    def loginsubmit():
        mydb = mysql.connector.connect(
            host="localhost",
            database="Flat",
            user="root",
            passwd="4270307l"
        )
        usernamedata = UserIDentry.get()
        passdata = Passwordentry.get()
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM login WHERE username= %s and pass= %s",(usernamedata, passdata))
        found = mycursor.fetchone()
        if found:
            loginwindow.destroy()
            home()
        else:
            messagebox.showinfo("LOGIN", "Invalid Credential. Please check your username or password.")
        mydb.commit()


    loginsubmit=Button(loginframe,text="Login", height=2, width=15,command=loginsubmit)
    loginsubmit.pack()
    loginwindow.mainloop()
#############################################################
def home():

    window= Tk()
    window.title("HOME")
    window.geometry("520x440")
    window.configure(background="#8e5f3a")
    topframe = Frame(window)
    topframe.pack()
    bottomframe = Frame(window)
    bottomframe.pack(side=BOTTOM)

########################################MAIN FRAME###########################################

    notebook = ttk.Notebook(topframe)
    frame1 = ttk.Frame(notebook)
    frame2 = ttk.Frame(notebook)
    frame3 = ttk.Frame(notebook)
    frame4 = ttk.Frame(notebook)
    frame5 = ttk.Frame(notebook)
    notebook.add(frame1, text="Security")
    notebook.add(frame2, text='Flat occupancy')
    notebook.add(frame3, text='Bill')
    notebook.add(frame4, text='Parking')
    notebook.add(frame5, text='Register')
    ##########################################PARKING#######################################
    parkingframe = Frame(frame4)
    parkingframe.pack()
    parkingframeb = Frame(frame4)
    parkingframeb.pack(side=BOTTOM)

    pflatno = Label(parkingframe, text="Vehicle no")
    pflatno.pack()
    pentryflat = Entry(parkingframe)
    pentryflat.pack()

    def parkingsubmit():
        mydb = mysql.connector.connect(
            host="localhost",
            database="Flat",
            user="root",
            passwd="4270307l"
        )
        pdata1 = pentryflat.get()
        mycursor = mydb.cursor()
        sql="SELECT * FROM flat WHERE vno=%s and vno1=%s"
        val=(pdata1,pdata1)
        mycursor.execute(sql,val)
        for i in mycursor:
            data = Label(parkingframeb, text="Vehicle Type")
            data.grid(row=1, column=0)
            data = Label(parkingframeb, text=i[7])
            data.grid(row=1, column=1)
            data = Label(parkingframeb, text="Flat no")
            data.grid(row=2, column=0)
            data = Label(parkingframeb, text=i[0])
            data.grid(row=2, column=1)
            data = Label(parkingframeb, text="Name")
            data.grid(row=3, column=0)
            data = Label(parkingframeb, text=i[1])
            data.grid(row=3, column=1)
            data = Label(parkingframeb, text="Address")
            data.grid(row=4, column=0)
            data = Label(parkingframeb, text=i[2])
            data.grid(row=4, column=1)
            data = Label(parkingframeb, text="Office address")
            data.grid(row=5, column=0)
            data = Label(parkingframeb, text=i[3])
            data.grid(row=5, column=1)
            data = Label(parkingframeb, text="Phone")
            data.grid(row=6, column=0)
            data = Label(parkingframeb, text=i[4])
            data.grid(row=6, column=1)
            data = Label(parkingframeb, text="Gov Id type")
            data.grid(row=7, column=0)
            data = Label(parkingframeb, text=i[5])
            data.grid(row=7, column=1)
            data = Label(parkingframeb, text="Gov Id no.")
            data.grid(row=8, column=0)
            data = Label(parkingframeb, text=i[6])
            data.grid(row=8, column=1)



    parking = Button(parkingframe, text="Submit", height=2, width=15, command=parkingsubmit)
    parking.pack()

    notebook.pack()

    #########################################REGISTER########################################
    registerframe=Frame(frame5)
    registerframe.pack()

    enterusername = Label(registerframe, text="Enter Username")
    enterusername.pack()
    userentry = Entry(registerframe)
    userentry.pack()
    enterpass = Label(registerframe, text="Enter Password")
    enterpass.pack()
    passentry = Entry(registerframe)
    passentry.pack()
    def registersubmit():
        mydb = mysql.connector.connect(
            host="localhost",
            database="Flat",
            user="root",
            passwd="4270307l"
        )
        userdata = userentry.get()
        passdata = passentry.get()
        mycursor = mydb.cursor()
        if len(userdata) >=4 and len(passdata) >=4:
            messagebox.showinfo("REGISTER", "Kudos!! Successfully Registered")
            sql = "INSERT INTO login (username,pass) VALUES(%s,%s)"
            val = (userdata,passdata)
            mycursor.execute(sql, val)
            mydb.commit()
        else:
            messagebox.showinfo("REGISTER","Enter Username and password of length greater than or equal to 4 ")

    registerbutton = Button(registerframe, text="Register", height=2, width=15, command=registersubmit)
    registerbutton.pack()

    notebook.pack()
    ##########################################################################################
    notebook = ttk.Notebook(frame1)
    frame11 = ttk.Frame(notebook)
    frame22 = ttk.Frame(notebook)
    frame33 = ttk.Frame(notebook)
    notebook.add(frame11, text="Guest Entry")
    notebook.add(frame22, text='Guest Exit ')
    notebook.add(frame33, text='Guest Details')
    #############################################GUEST ENTRY################################
    flatno = Label(frame11, text="Flat")
    flatno.grid(row=2, column=0)
    entryflat = ttk.Combobox(frame11,
                        values=[
                            "101",
                            "102",
                            "103",
                            "104",
                            "105",
                            "106",
                            "107",
                            "108",
                            "109",
                            "110"])
    entryflat.set("Choose flat no")
    entryflat.grid(row=2, column=1)

    entrypersonname = Label(frame11, text="Enter Name of Guest")
    entrypersonname.grid(row=3, column=0)
    entrypersonnameentry = Entry(frame11)
    entrypersonnameentry.grid(row=3, column=1)

    entryphone = Label(frame11, text="Phone")
    entryphone.grid(row=6, column=0)
    entryphoneentry = Entry(frame11)
    entryphoneentry.grid(row=6, column=1)

    entryaddress = Label(frame11, text="Enter Address Of Guest")
    entryaddress.grid(row=4, column=0)
    entryaddressentry = Entry(frame11)
    entryaddressentry.grid(row=4, column=1)

    entrypurpose = Label(frame11, text="Purpose Of visit")
    entrypurpose.grid(row=5, column=0)
    entrypurposeentry= Entry(frame11)
    entrypurposeentry.grid(row=5, column=1)

    import time
    localtime = time.asctime(time.localtime(time.time()))

    intime = Label(frame11, text="In time is ")
    intime.grid(row=8, column=0)
    time = Label(frame11, text=localtime)
    time.grid(row=8, column=1)

    def guestsubmit():
        mydb = mysql.connector.connect(
            host="localhost",
            database="Flat",
            user="root",
            passwd="4270307l"
        )
        entry1 = entryflat.get()
        entry2 = entrypersonnameentry.get()
        entry3 = entryphoneentry.get()
        entry4 = entryaddressentry.get()
        entry5 = entrypurposeentry.get()
        mycursor = mydb.cursor()
        sql = "INSERT INTO GUEST (name,idflat,phone,address,purpose,intime,idflat2) VALUES(%s,%s,%s,%s,%s,%s,%s)"
        val = (entry2,entry1,entry3, entry4, entry5, localtime,entry1)
        mycursor.execute(sql, val)
        mydb.commit()

    submitguest = Button(frame11, text="submit", height=2, width=15, command=guestsubmit)
    submitguest.grid(row=10, column=1)

    #################################GUEST EXIT##########################################################
    guestexittop=Frame(frame22)
    guestexittop.pack()
    guestexitbottom = Frame(frame22)
    guestexitbottom.pack(side=BOTTOM)
    exitflatno = Label(guestexittop, text="Flat")
    exitflatno.grid(row=0, column=0)
    exitflat = ttk.Combobox(guestexittop,
                             values=[
                                 "101",
                                 "102",
                                 "103",
                                 "104",
                                 "105",
                                 "106",
                                 "107",
                                 "108",
                                 "109",
                                 "110"])
    exitflat.set("Choose flat no")
    exitflat.grid(row=0, column=1)
    def submitexit():
        mydb = mysql.connector.connect(
            host="localhost",
            database="Flat",
            user="root",
            passwd="4270307l"
        )
        exitdata=exitflat.get()
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM guest WHERE idflat=%s and idflat2=%s and outtime is null",(exitdata,exitdata))
        a=0
        for widget in guestexitbottom.winfo_children():
            widget.grid_remove()

        radiobuttons=[]
        def shell():
            for i in radiobuttons:
                print(i.get())
        var = IntVar()
        for i in mycursor:
            import time
            localtime = time.asctime(time.localtime(time.time()))
            a+=1
            for x in [i[0]]:
                Rbutton=Radiobutton(guestexitbottom,text=i[1],variable=var,value=x,command=shell)
                Rbutton.grid(row=a,column=0)
            radiobuttons.append(var)
            ###################################
            outtimelabel = Label(guestexittop, text="Out time")
            outtimelabel.grid(row=1, column=0)
            outtime = Label(guestexittop, text=localtime)
            outtime.grid(row=1, column=1)
            exitbutton = Button(guestexittop, text="Guest leaving", height=2, width=10)
            exitbutton.grid(row=1, column=2)
            ######################################
    submitexitbutton = Button(guestexittop, text="submit", height=2, width=10, command=submitexit)
    submitexitbutton.grid(row=0, column=2)
    #####################################GUEST DETAILS####################################################
    guestdetails = Frame(frame33)
    guestdetails.pack()
    guestdetailsbottom = Frame(frame33)
    guestdetailsbottom.pack(side=BOTTOM)
    guestD = Label(guestdetails, text="Flat")
    guestD.grid(row=0, column=0)
    flatdetails = ttk.Combobox(guestdetails,
                            values=[
                                "101",
                                "102",
                                "103",
                                "104",
                                "105",
                                "106",
                                "107",
                                "108",
                                "109",
                                "110"],height=2, width=6)
    flatdetails.set("Choose")
    flatdetails.grid(row=1, column=0)
    fdateentry = Label(guestdetails, text="Date")
    fdateentry.grid(row=0, column=2)
    fdateentry=Entry(guestdetails,width="10")
    fdateentry.grid(row=1,column=2)
    monentry = Label(guestdetails, text="Month")
    monentry.grid(row=0, column=3)
    monthentry = ttk.Combobox(guestdetails,
                               values=[
                                   "jan",
                                   "feb",
                                   "mar",
                                   "apr",
                                   "may",
                                   "jun",
                                   "jul",
                                   "aug",
                                   "sep",
                                   "oct",
                                   "nov",
                                   "dec"],height=2, width=6)
    monthentry.set("Month")
    monthentry.grid(row=1, column=3)
    yearentry = Label(guestdetails, text="Year")
    yearentry.grid(row=0, column=4)
    yearentry = Entry(guestdetails,width="10")
    yearentry.grid(row=1, column=4)
    def GDsubmit():
        mydb = mysql.connector.connect(
            host="localhost",
            database="Flat",
            user="root",
            passwd="4270307l"
        )
        GDentry1 = flatdetails.get()
        GDentry2 = fdateentry.get()
        GDentry3 = monthentry.get()
        GDentry4 = yearentry.get()
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM guest WHERE intime LIKE %s and intime LIKE %s and intime LIKE %s and idflat=%s",('%'+str(GDentry4),'%'+str(GDentry3)+'%','%'+str(GDentry2)+'%',GDentry1))
        found = mycursor.fetchone()
        if found:
            a = 1
            namelabel = Label(guestdetailsbottom, text="name")
            namelabel.grid(row=0, column=0)
            for i in mycursor:
                a += 1
                namelabel = Label(guestdetailsbottom, text=i[1])
                namelabel.grid(row=a, column=0)

        else:
            messagebox.showinfo("GUEST DETAILS","No guest came for this date for this flat")


        mydb.commit()


    submitguestdetails = Button(guestdetails, text="submit", height=2, width=6,command=GDsubmit)
    submitguestdetails.grid(row=2, column=4)
    notebook.pack()

####################################FLAT OCCUPANCY########################################################
    notebook = ttk.Notebook(frame2)
    frame111 = ttk.Frame(notebook)
    frame222 = ttk.Frame(notebook)
    frame333 = ttk.Frame(notebook)
    notebook.add(frame111, text="Fill Flat")
    notebook.add(frame222, text='Vacant Flat ')
    notebook.add(frame333, text='Flat Details')
    ##########################################FILL FLAT#####################################
    chooseflat = Label(frame111, text="Flat")
    chooseflat.grid(row=2, column=0)
    flatfill = ttk.Combobox(frame111,
                        values=[
                            "101",
                            "102",
                            "103",
                            "104",
                            "105",
                            "106",
                            "107",
                            "108",
                            "109",
                            "110"])
    flatfill.set("Choose flat no")
    flatfill.grid(row=2, column=1)

    personnamefill = Label(frame111, text="Enter Name of person")
    personnamefill.grid(row=3, column=0)
    personnameentryfill = Entry(frame111)
    personnameentryfill.grid(row=3, column=1)

    addressfill = Label(frame111, text="Enter Address")
    addressfill.grid(row=4, column=0)
    addressentryfill = Entry(frame111)
    addressentryfill.grid(row=4, column=1)

    oaddfill = Label(frame111, text="Enter Office Address")
    oaddfill.grid(row=5, column=0)
    oaddentryfill = Entry(frame111)
    oaddentryfill.grid(row=5, column=1)

    phonefill = Label(frame111, text="Phone")
    phonefill.grid(row=6, column=0)
    phoneentryfill = Entry(frame111)
    phoneentryfill.grid(row=6, column=1)

    govidfill = Label(frame111, text="Govt Id Type")
    govidfill.grid(row=7, column=0)
    govidtypefill = ttk.Combobox(frame111,
                             values=[
                                 "DL",
                                 "Aadhar",
                                 "PAN",
                                 "Voter ID",
                                 "Ration Card"])
    govidtypefill.set("Choose Govt Id")
    govidtypefill.grid(row=7, column=1)

    gov = Label(frame111, text="Govt Id no.")
    gov.grid(row=8, column=0)
    goventryfill = Entry(frame111)
    goventryfill.grid(row=8, column=1)

    Vtype = Label(frame111, text="Vehicle Type")
    Vtype.grid(row=9, column=0)
    VtypeEntry = ttk.Combobox(frame111,
                             values=[
                                 "2 Wheeler",
                                 "4 Wheeler",])
    VtypeEntry.set("Choose")
    VtypeEntry.grid(row=9, column=1)

    vno = Label(frame111, text="Vehicle no.")
    vno.grid(row=10, column=0)
    vnoentry = Entry(frame111)
    vnoentry.grid(row=10, column=1)

    def fillsubmit():
        print("hi")
        mydb = mysql.connector.connect(
            host="localhost",
            database="Flat",
            user="root",
            passwd="4270307l"
        )
        entry1 = flatfill.get()
        entry2 = personnameentryfill.get()
        entry3 = addressentryfill.get()
        entry4 = oaddentryfill.get()
        entry5 = phoneentryfill.get()
        entry6 = govidtypefill.get()
        entry7 = goventryfill.get()
        entry8 = VtypeEntry.get()
        entry9 = vnoentry.get()
        mycursor = mydb.cursor()
        sql = "UPDATE flat SET name = %s, address=%s, officeadd=%s, phone=%s, govid=%s, govidno=%s, vtype=%s, vno=%s WHERE idflat= %s"
        val = (entry2, entry3, entry4, int(entry5), entry6, entry7, entry8, entry9, int(entry1))
        mycursor.execute(sql, val)
        mydb.commit()

    submitfillflat = Button(frame111, text="submit",height=2, width=15, command=fillsubmit)
    submitfillflat.grid(row=11, column=1)
    ##########################################VACANT FLAT###################################
    flat = ttk.Combobox(frame222,
                        values=[
                            "101",
                            "102",
                            "103",
                            "104",
                            "105",
                            "106",
                            "107",
                            "108",
                            "109",
                            "110"])
    flat.set("Choose Flat No To Vaccant")
    flat.grid(row=1, column=0)

    def submit():
        if int(flat.get()) >=101:
            headingLabel = Label(frame222, text="Successfully Vacant !!!!")
            headingLabel.grid(row=2, column=0)
            mydb = mysql.connector.connect(
                host="localhost",
                database="Flat",
                user="root",
                passwd="4270307l"
            )
            entry = flat.get()
            mycursor = mydb.cursor()
            sql = "UPDATE flat SET name = %s, address=%s, officeadd=%s, phone=%s, govid=%s, govidno=%s WHERE idflat= %s"
            val = (None, None, None, None, "None", "None", int(entry))
            mycursor.execute(sql, val)
            mydb.commit()
        else:
            headingLabel = Label(frame222, text="Please Select flat no to vacant")
            headingLabel.grid(row=2, column=0)

    submit = Button(frame222, text="submit",height=2, width=15, command=submit)
    submit.grid(row=1, column=2 )
    ########################################FLAT DETAILS################################
    headingLabel = Label(frame333, text="Enter Flat No:")
    headingLabel.grid(row=1, column=0)

    flatEntry = Entry(frame333)
    flatEntry.grid(row=1, column=1)

    def buttonFlatOcupancy():
        mydb = mysql.connector.connect(
            host="localhost",
            database="Flat",
            user="root",
            passwd="4270307l"
        )

        mycursor = mydb.cursor()
        mycursor.execute("select * from flat ")
        entry = flatEntry.get()
        for i in mycursor:
            if i[0] == int(entry):
                if i[1] != None:
                    data = Label(frame333, text="|Flat no|")
                    data.grid(row=2, column=0)
                    data = Label(frame333, text=i[0])
                    data.grid(row=2, column=1)
                    data = Label(frame333, text="|Name|")
                    data.grid(row=3, column=0)
                    data = Label(frame333, text=i[1])
                    data.grid(row=3, column=1)
                    data = Label(frame333, text="|Address|")
                    data.grid(row=4, column=0)
                    data = Label(frame333, text=i[2])
                    data.grid(row=4, column=1)
                    data = Label(frame333, text="|Office address|")
                    data.grid(row=5, column=0)
                    data = Label(frame333, text=i[3])
                    data.grid(row=5, column=1)
                    data = Label(frame333, text="|Phone|")
                    data.grid(row=6, column=0)
                    data = Label(frame333, text=i[4])
                    data.grid(row=6, column=1)
                    data = Label(frame333, text="|Gov Id type|")
                    data.grid(row=7, column=0)
                    data = Label(frame333, text=i[5])
                    data.grid(row=7, column=1)
                    data = Label(frame333, text="|Gov Id no.|")
                    data.grid(row=8, column=0)
                    data = Label(frame333, text=i[6])
                    data.grid(row=8, column=1)
                else:
                    data = Label(frame333, text="Flat is empty!!")
                    data.grid(row=2, column=1)

    buttonFlatOcupancy = Button(frame333, text="Submit", command=buttonFlatOcupancy)
    buttonFlatOcupancy.grid(row=1, column=3)
    notebook.pack()
    #######################################BILL############################################
    notebook = ttk.Notebook(frame3)
    frame1111 = ttk.Frame(notebook)
    frame2222 = ttk.Frame(notebook)
    frame3333 = ttk.Frame(notebook)
    frame4444 = ttk.Frame(notebook)
    notebook.add(frame1111, text="Water Bill")
    notebook.add(frame2222, text='Electricity Bill')
    notebook.add(frame3333, text='Gas Bill')
    notebook.add(frame4444, text='View bill')
    wbflat = Label(frame1111, text="Flat")
    wbflat.grid(row=0, column=0)
    wbflat = ttk.Combobox(frame1111,
                               values=[
                                   "101",
                                   "102",
                                   "103",
                                   "104",
                                   "105",
                                   "106",
                                   "107",
                                   "108",
                                   "109",
                                   "110"], height=2, width=6)
    wbflat.set("Choose")
    wbflat.grid(row=1, column=0)
    wbamountentry = Label(frame1111, text="Amount")
    wbamountentry.grid(row=0, column=2)
    wbamountentry = Entry(frame1111, width="10")
    wbamountentry.grid(row=1, column=2)
    wbmonentry = Label(frame1111, text="Month")
    wbmonentry.grid(row=0, column=3)
    wbmonthentry = ttk.Combobox(frame1111,
                              values=[
                                  "jan",
                                  "feb",
                                  "mar",
                                  "apr",
                                  "may",
                                  "jun",
                                  "jul",
                                  "aug",
                                  "sep",
                                  "oct",
                                  "nov",
                                  "dec"], height=2, width=6)
    wbmonthentry.set("Month")
    wbmonthentry.grid(row=1, column=3)
    wbyearentry = Label(frame1111, text="Year")
    wbyearentry.grid(row=0, column=4)
    wbyearentry = Entry(frame1111, width="10")
    wbyearentry.grid(row=1, column=4)
    def WBsubmit():
        mydb = mysql.connector.connect(
            host="localhost",
            database="Flat",
            user="root",
            passwd="4270307l"
        )
        WBentry1 = wbflat.get()
        WBentry2 = wbamountentry.get()
        WBentry3 = wbmonthentry.get()
        WBentry4 = wbyearentry.get()
        WBentry5 = "W"
        mycursor = mydb.cursor()
        sql="INSERT INTO bill (billtype,month,year,amount,idflat) VALUES(%s,%s,%s,%s,%s)"
        val=(WBentry5,WBentry3 ,WBentry4,WBentry2,WBentry1)
        mycursor.execute(sql,val)
        mydb.commit()
        messagebox.showinfo("WATER BILL","Bill successfully updated")

    submitWB = Button(frame1111, text="submit", height=2, width=6, command=WBsubmit)
    submitWB.grid(row=2, column=4)
    ########################################ELECTRICITY BILL###################################
    ebflat = Label(frame2222, text="Flat")
    ebflat.grid(row=0, column=0)
    ebflat = ttk.Combobox(frame2222,
                          values=[
                              "101",
                              "102",
                              "103",
                              "104",
                              "105",
                              "106",
                              "107",
                              "108",
                              "109",
                              "110"], height=2, width=6)
    ebflat.set("Choose")
    ebflat.grid(row=1, column=0)
    ebamountentry = Label(frame2222, text="Amount")
    ebamountentry.grid(row=0, column=2)
    ebamountentry = Entry(frame2222, width="10")
    ebamountentry.grid(row=1, column=2)
    ebmonentry = Label(frame2222, text="Month")
    ebmonentry.grid(row=0, column=3)
    ebmonthentry = ttk.Combobox(frame2222,
                                values=[
                                    "jan",
                                    "feb",
                                    "mar",
                                    "apr",
                                    "may",
                                    "jun",
                                    "jul",
                                    "aug",
                                    "sep",
                                    "oct",
                                    "nov",
                                    "dec"], height=2, width=6)
    ebmonthentry.set("Month")
    ebmonthentry.grid(row=1, column=3)
    ebyearentry = Label(frame2222, text="Year")
    ebyearentry.grid(row=0, column=4)
    ebyearentry = Entry(frame2222, width="10")
    ebyearentry.grid(row=1, column=4)

    def EBsubmit():
        mydb = mysql.connector.connect(
            host="localhost",
            database="Flat",
            user="root",
            passwd="4270307l"
        )
        EBentry1 = ebflat.get()
        EBentry2 = ebamountentry.get()
        EBentry3 = ebmonthentry.get()
        EBentry4 = ebyearentry.get()
        EBentry5 = "E"
        mycursor = mydb.cursor()
        sql = "INSERT INTO bill (billtype,month,year,amount,idflat) VALUES(%s,%s,%s,%s,%s)"
        val = (EBentry5, EBentry3, EBentry4, EBentry2, EBentry1)
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("ELECTRICITY BILL", "Bill successfully updated")

    submitEB= Button(frame2222, text="submit", height=2, width=6, command=EBsubmit)
    submitEB.grid(row=2, column=4)
    ########################################GAS###########################################
    gbflat = Label(frame3333, text="Flat")
    gbflat.grid(row=0, column=0)
    gbflat = ttk.Combobox(frame3333,
                          values=[
                              "101",
                              "102",
                              "103",
                              "104",
                              "105",
                              "106",
                              "107",
                              "108",
                              "109",
                              "110"], height=2, width=6)
    gbflat.set("Choose")
    gbflat.grid(row=1, column=0)
    gbamountentry = Label(frame3333, text="Amount")
    gbamountentry.grid(row=0, column=2)
    gbamountentry = Entry(frame3333, width="10")
    gbamountentry.grid(row=1, column=2)
    gbmonentry = Label(frame3333, text="Month")
    gbmonentry.grid(row=0, column=3)
    gbmonthentry = ttk.Combobox(frame3333,
                                values=[
                                    "jan",
                                    "feb",
                                    "mar",
                                    "apr",
                                    "may",
                                    "jun",
                                    "jul",
                                    "aug",
                                    "sep",
                                    "oct",
                                    "nov",
                                    "dec"], height=2, width=6)
    gbmonthentry.set("Month")
    gbmonthentry.grid(row=1, column=3)
    gbyearentry = Label(frame3333, text="Year")
    gbyearentry.grid(row=0, column=4)
    gbyearentry = Entry(frame3333, width="10")
    gbyearentry.grid(row=1, column=4)

    def GBsubmit():
        mydb = mysql.connector.connect(
            host="localhost",
            database="Flat",
            user="root",
            passwd="4270307l"
        )
        GBentry1 = gbflat.get()
        GBentry2 = gbamountentry.get()
        GBentry3 = gbmonthentry.get()
        GBentry4 = gbyearentry.get()
        GBentry5 = "G"
        mycursor = mydb.cursor()
        sql = "INSERT INTO bill (billtype,month,year,amount,idflat) VALUES(%s,%s,%s,%s,%s)"
        val = (GBentry5, GBentry3, GBentry4, GBentry2, GBentry1)
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("GAS BILL", "Bill successfully updated")

    submitGB = Button(frame3333, text="submit", height=2, width=6, command=GBsubmit)
    submitGB.grid(row=2, column=4)
    #######################################BILL DETAILS#####################################
    dbtopframe=Frame(frame4444)
    dbtopframe.pack()
    dbbottomframe=Frame(frame4444)
    dbbottomframe.pack(side=BOTTOM)
    Dbflat = Label(dbtopframe, text="Flat")
    Dbflat.grid(row=0, column=0)
    Dbflat = ttk.Combobox(dbtopframe,
                          values=[
                              "101",
                              "102",
                              "103",
                              "104",
                              "105",
                              "106",
                              "107",
                              "108",
                              "109",
                              "110"], height=2, width=6)
    Dbflat.set("Choose")
    Dbflat.grid(row=1, column=0)
    Dbmonentry = Label(dbtopframe, text="Month")
    Dbmonentry.grid(row=0, column=1)
    Dbmonthentry = ttk.Combobox(dbtopframe,
                                values=[
                                    "jan",
                                    "feb",
                                    "mar",
                                    "apr",
                                    "may",
                                    "jun",
                                    "jul",
                                    "aug",
                                    "sep",
                                    "oct",
                                    "nov",
                                    "dec"], height=2, width=6)
    Dbmonthentry.set("Month")
    Dbmonthentry.grid(row=1, column=1)
    Dbyearentry = Label(dbtopframe, text="Year")
    Dbyearentry.grid(row=0, column=2)
    Dbyearentry = Entry(dbtopframe, width="10")
    Dbyearentry.grid(row=1, column=2)
    def submitDB():
        mydb = mysql.connector.connect(
            host="localhost",
            database="Flat",
            user="root",
            passwd="4270307l"
        )
        DBentry1 = Dbflat.get()
        DBentry3 = Dbmonthentry.get()
        DBentry4 = Dbyearentry.get()
        mycursor = mydb.cursor()
        sql = "SELECT * FROM bill where idflat=%s and month=%s and year= %s "
        val = (DBentry1, DBentry3, DBentry4)
        mycursor.execute(sql, val)
        value=[]
        for i in mycursor:
            if i[1]=='W':
                waterbill = Label(dbbottomframe, text="Water bill")
                waterbill.grid(row=0, column=0,sticky="W")
                waterbill = Label(dbbottomframe, text=i[4])
                waterbill.grid(row=0, column=1,sticky="W")
                value.append(int(i[4]))
            if i[1]=='E':
                waterbill = Label(dbbottomframe, text="Electricity bill")
                waterbill.grid(row=1, column=0,sticky="W")
                waterbill = Label(dbbottomframe, text=i[4])
                waterbill.grid(row=1, column=1,sticky="W")
                value.append(int(i[4]))
            if i[1]=='G':
                waterbill = Label(dbbottomframe, text="Gas bill")
                waterbill.grid(row=2, column=0,sticky="W")
                waterbill = Label(dbbottomframe, text=i[4])
                waterbill.grid(row=2, column=1,sticky="W")
                value.append(int(i[4]))
            line = Label(dbbottomframe, text="--------")
            line.grid(row=3, column=0,sticky="W")
            line = Label(dbbottomframe, text="--------")
            line.grid(row=3, column=1,sticky="W")

        total = Label(dbbottomframe, text="Total bill")
        total.grid(row=4, column=0,sticky="W")
        total = Label(dbbottomframe, text=sum(value))
        total.grid(row=4, column=1,sticky="W")

    submitDB = Button(dbtopframe, text="submit", height=2, width=6,command=submitDB)
    submitDB.grid(row=1, column=3)

    notebook.pack()

    exitbutton=Button(bottomframe,text="EXIT", height=2, width=20,command=window.destroy)
    exitbutton.pack()

    window.mainloop()
#####################MAIN WINDOW##########################
topframe=Frame(mainwindow)
topframe.pack()
bottomframe=Frame(mainwindow)
bottomframe.pack(side=BOTTOM)


C = Canvas(topframe, bg="blue", height=200, width=720)
filename = PhotoImage(file = "/Users/amitsingh/Downloads/neww.png")
background_label = Label(topframe, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()

#Buttons
loginButton=Button(bottomframe,text="Log in",height=2, width=25,command=home)
loginButton.grid(row=0,column=0)
def about():
    messagebox.showinfo("ABOUT ME", "Hello!! I'm Amit Singh. And this is my Python Tkinter project. My Instagram ID is @singhamitchauhan and email is amitsingh.chauhan@hotmail.com")
aboutButton=Button(bottomframe,text="About me",height=2, width=25,command=about)
aboutButton.grid(row=0,column=1)

exitButton=Button(bottomframe,text="Exit",height=2, width=25, command=mainwindow.destroy)
exitButton.grid(row=0,column=2)
###########################################################

mainwindow.mainloop()
