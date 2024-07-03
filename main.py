import mysql.connector
host="localhost"    #change to your machine's host
user="root"         #change to your machine's user
passwd="welcome"    #change to your machine's sql password

#accessing Plane Management
def Table1():
    mycon = mysql.connector.connect(host=host,user=user, passwd=passwd,database='PM')
    c=mycon.cursor()
    print("What would you like to do in this database")
    print("1. Update Record")
    print("2. New Record")
    print("3. Delete Record")
    print("4. Show Records")
    print("5. Exit Program")
    while True:
        ans=int(input("Please choose no."))
        if ans==1:
            identity=int(input("Plane ID"))
            FuelHour=int(input("ENTER FUEL HOUR"))
            HoursFlown=int(input("ENTER HOURS FLOWN"))
            STATUS=input("ENTER STATUS")
            x="update P_Management set Fuel_hour="+str(FuelHour)+" where id="+str(identity)
            c.execute(x)
            y="update P_Management set Hours_Flown="+str(HoursFlown)+" where id="+str(identity)
            c.execute(y)
            z="update P_Management set Status='"+str(STATUS)+"' where id="+str(identity)
            c.execute(z)
            mycon.commit()
        elif ans==2:
            identity=int(input("PLANE ID"))
            Model=input("ENTER MODEL")
            YoM=int(input("ENTER YEAR OF MANAFACTURING"))
            Capacity=int(input("ENTER CAPACITY"))
            ENDURANCE=int(input("ENTER ENDURANCE"))
            FuelHour=int(input("ENTER FUEL HOUR"))
            HoursFlown=int(input("ENTER HOURS FLOWN"))
            STATUS=input("ENTER STATUS")
            x=f" insert into P_Management values({identity},'{Model}',{YoM},{Capacity},{FuelHour},{ENDURANCE},{HoursFlown},'{STATUS}')"
            c.execute(x)
            mycon.commit()
        elif ans==3:
            identity=int(input("PLANE ID TO DELETE FROM DATABASE"))
            x="delete from P_Management where id="+str(identity)
            c.execute(x)
            mycon.commit()
            print("SUCCESS")
        elif ans==4:
            c.execute("select * from P_Management")
            x=c.fetchall()
            for u in x:
                print(u[0],':',u[1],':',u[2],':',u[3],':',u[4],':',u[5],':',u[6],":",u[7])
        else:
            print("EXITING PROGRAM, THANK YOU")
            break
#accessing Passenger Details
def Table2():
    mycon=mysql.connector.connect(host=host,user=user,passwd=passwd,database='PAX')
    c=mycon.cursor()
    print("What would you like to do in this database")
    print("1. New Record")
    print("2. Delete Record")
    print("3. Show Records")
    print("4. Exit Program")
    while True:
        ans=int(input("Please choose no."))
        if ans==1:
            code=int(input("PAX CODE"))
            Fno=int(input("FLIGHT NO."))
            classx=input("CLASS")
            name=input("NAME")
            phone=int(input("PHONE NO."))
            sex=input("sex")
            email=input("email")
            x=f"insert into details values({code},{Fno},'{classx}','{name}',{phone},'{sex}','{email}')"
            c.execute(x)
            mycon.commit()
        elif ans==2:
            code=int(input("Enter pax code"))
            x="delete from details where pax_code="+str(code)
            c.execute(x)
            mycon.commit()
        elif ans==3:
            c.execute("select * from details")
            x=c.fetchall()
            for u in x:
                print(u[0],':',u[1],':',u[2],':',u[3],':',u[4],':',u[5],':',u[6])
            mycon.commit()
        else:
            print("EXITING PROGRAM, THANK YOU")
            break
#accessing Flight and Ticket Details
def Table3():
    mycon=mysql.connector.connect(host=host,user=user,passwd=passwd,database='details')
    c=mycon.cursor()
    print("What would you like to do in this database")
    print("1. New Record")
    print("2. Delete Record")
    print("3. Show Records")
    print("4. Exit Program")
    while True:
        ans=int(input("Please choose no."))
        if ans==1:
            flightid=input("Flight ID")
            Destination=input("Enter destination")
            Departure=input("Enter date")
            gateno=int(input("Enter gate no."))
            time=input("Enter time formatted")
            ticketcost=int(input("Enter ticket cost"))
            x=f"insert into deets values('{flightid}','{Destination}','{Departure}',{gateno},'{time}',{ticketcost})"
            c.execute(x)
            mycon.commit()
        elif ans==2:
            code=input("Enter flight id")
            x="delete from deets where flightid='"+str(code)+"'"
            c.execute(x)
            mycon.commit()
        elif ans==3:
            c.execute("select * from deets")
            x=c.fetchall()
            for u in x:
                print(u[0],':',u[1],':',u[2],':',u[3],':',u[4],':',u[5])
            mycon.commit()
        else:
            print("EXITING PROGRAM, THANK YOU")
            break
#accessing Employee Management
def Table4():
    mycon=mysql.connector.connect(host=host,user=user,passwd=passwd,database='emp')
    c=mycon.cursor()
    print("What would you like to do in this database")
    print("1. New Record")
    print("2. Delete Record")
    print("3. Show Records")
    print("4. Update Records")
    print("5. Exit Program")
    while True:
        ans=int(input("Please choose no."))
        if ans==1:
            empid=int(input("ENTER emp id"))
            name=input("enter name")
            date=input("enter formatted date")
            designation=input("enter designation")
            salary=int(input("enter salary"))
            x=f"insert into info values({empid},'{name}','{date}','{designation}',{salary})"
            c.execute(x)
            mycon.commit()
        elif ans==2:
            code=int(input("Enter empid"))
            x="delete from info where emp_id="+str(code)
            c.execute(x)
            mycon.commit()
        elif ans==3:
            c.execute("select * from info")
            x=c.fetchall()
            for u in x:
                print(u[0],':',u[1],':',u[2],':',u[3],':',u[4])
            mycon.commit()
        elif ans==4:
            code=int(input("enter empid"))
            new1=input("enter new name")
            new2=input("enter new date")
            new3=input("enter new designation")
            new4=int(input("enter new salary"))
            x=f"update info set name='{new1}',D_O_J='{new2}',designation='{new3}',salary={new4} where emp_id="+str(code)
            c.execute(x)
            mycon.commit()
        else:
            print("EXITING PROGRAM, THANK YOU")
            break
#Login Program
while True:
    login={1:['A','admin@A'],2:['B','admin@B'],3:['C','admin@C'],4:['E','admin@E'],5:['F','admin@F']}
    print(' *WELCOME TO ASCY *')
    print(' LOGIN ')
    user=input('Enter Password:')
    for k,v in login.items():
        if v[1]==user:
            assign=k
            print('{}-Level Clearance granted'.format(v[0]))
    msg='''
    ___________________________
    Please select the database
    1. PM
    2. PAX
    3. DETAILS
    4. EMP
    ___________________________'''
    err='You do not have access to this database. Kindly press (0) to login and (1) to exit the program.'
    print(msg)
    choice=int(input(' >'))
    if choice==1:
        if assign==1 or assign==3 or assign==4:
            Table1()
        else:
            print(err)
            final=int(input('>>>'))
            if final==0:
                continue
            elif final==1:
                break
    elif choice==2:
        if assign==1 or assign==2 or assign==5:
            Table2()
        else:
            print(err)
            final=int(input('>>>'))
            if final==0:
                continue
            elif final==1:
                break
    elif choice==3:
        if assign==1 or assign==2 or assign==3:
            Table3()
        else:
            print(err)
            final=int(input('>>>'))
            if final==0:
                continue
            elif final==1:
                break
    elif choice==4:
        if assign==1 or assign==5:
            Table4()
        else:
            print(err)
            final=int(input('>>>'))
            if final==0:
                continue
            elif final==1:
                break
print('Thank you for using ASCY!')
