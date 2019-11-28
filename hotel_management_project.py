class hotelfarecal:

    def __init__(self,rt='',s=0,p=0,r=0,t=0,a=1800,name='',address='',cindate='',coutdate='',rno=101):

        print ("\n\n*****WELCOME TO OUR HOTEL*****\n")

        self.rt=rt

        self.r=r

        self.t=t

        self.p=p

        self.s=s
        self.a=a
        self.name=name
        self.address=address
        self.cindate=cindate
        self.coutdate=coutdate
        self.rno=rno
    def inputdata(self):
        self.name=input("\nEnter your name:")
        self.address=input("\nEnter your address:")
        self.cindate=input("\nEnter your check in date:")
        self.coutdate=input("\nEnter your checkout date:")
        print("Your room no.:",self.rno,"\n")

    def roomrent(self):

        print ("We have the following rooms for you:-")

        print ("1.  type A---->rs 6000 PN\-")

        print ("2.  type B---->rs 5000 PN\-")

        print ("3.  type C---->rs 4000 PN\-")

        print ("4.  type D---->rs 3000 PN\-")

        x=int(input("Enter Your Choice Please->"))

        n=int(input("For How Many Nights Did You Stay:"))

        if(x==1):

            print ("you have opted room type A")

            self.s=6000*n

        elif (x==2):

            print ("you have opted room type B")

            self.s=5000*n

        elif (x==3):

            print ("you have opted room type C")

            self.s=4000*n

        elif (x==4):
            print ("you have opted room type D")

            self.s=3000*n

        else:

            print ("please choose a room")

        print ("your room rent is =",self.s,"\n")

    def restaurantbill(self):

        print("*****RESTAURANT MENU*****")

        print("1.water----->Rs20","2.tea----->Rs10","3.breakfast combo--->Rs90","4.lunch---->Rs110","5.dinner--->Rs150","6.Exit")


        while (1):

            c=int(input("Enter your choice:"))


            if (c==1):
                d=int(input("Enter the quantity:"))
                self.r=self.r+20*d

            elif (c==2):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+10*d


            elif (c==3):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+90*d


            elif (c==4):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+110*d


            elif (c==5):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+150*d


            elif (c==6):
                 break
            else:
                print("Invalid option")

        print ("Total food Cost=Rs",self.r,"\n")

    def	laundrybill(self):
        print ("******LAUNDRY MENU*******")

        print ("1.Shorts----->Rs3","2.Trousers----->Rs4","3.Shirt--->Rs5","4.Jeans---->Rs6","5.Girlsuit--->Rs8","6.Exit")

        while (1):

            e=int(input("Enter your choice:"))

            if (e==1):
                f=int(input("Enter the quantity:"))
                self.t=self.t+3*f

            elif (e==2):
                f=int(input("Enter the quantity:"))
                self.t=self.t+4*f


            elif (e==3):
                f=int(input("Enter the quantity:"))
                self.t=self.t+5*f


            elif (e==4):
                f=int(input("Enter the quantity:"))
                self.t=self.t+6*f


            elif (e==5):
                f=int(input("Enter the quantity:"))
                self.t=self.t+8*f

            elif (e==6):
                break;
            else:

                print ("Invalid option")


        print ("Total Laundary Cost=Rs",self.t,"\n")

    def gamebill(self):
        print ("******GAME MENU*******")

        print ("1.Table tennis----->Rs60","2.Bowling----->Rs80","3.Snooker--->Rs70","4.Video games---->Rs90","5.Pool--->Rs50==6","6.Exit")



        while (1):


            g=int(input("Enter your choice:"))


            if (g==1):
                h=int(input("No. of hours:"))
                self.p=self.p+60*h


            elif (g==2):
                h=int(input("No. of hours:"))
                self.p=self.p+80*h


            elif (g==3):
                h=int(input("No. of hours:"))
                self.p=self.p+70*h


            elif (g==4):
                h=int(input("No. of hours:"))
                self.p=self.p+90*h


            elif (g==5):
                h=int(input("No. of hours:"))
                self.p=self.p+50*h

            elif (g==6):
                break

            else:

                print ("Invalid option")



        print ("Total Game Bill=Rs",self.p,"\n")

    def display(self):
        f=open("contents.txt","w")
        f.write("******HOTEL XPLOSION BILL******")
        f.write("\n")
        f.write("Customer details:")
        f.write("\n")
        f.write("Customer name:")
        f.write(self.name)
        f.write("\n")
        f.write("Customer address:")
        f.write(self.address)
        f.write("\n")
        f.write("Check in date:")
        f.write(self.cindate)
        f.write("\n")
        f.write("Check out date :")
        f.write(self.coutdate)
        f.write("\n")
        f.write("Room no. :")
        #self.rno is integer coversion to string required
        f.write(self.rno+"")
        f.write("\n")
        f.write("Your Room rent is:")
        f.write(self.s)
        f.write("\n")
        f.write("Your Food bill is:")
        f.write(self.r)
        f.write("\n")
        f.write("Your laundary bill is:")
        f.write(self.t)
        f.write("\n")
        f.write("Your Game bill is:")
        f.write(self.p)
        f.write("\n")

        self.rt=self.s+self.t+self.p+self.r

        f.write("Your sub total bill is:")
        f.write(self.rt)
        f.write("\n")
        f.write("Additional Service Charges is :")
        f.write(self.a)
        f.write("Your grand total bill is:")
        f.write(self.rt+self.a)
        f.write("\n")
        self.rno+=1
        fr=open("contents.txt","r")
        print(fr.read())







def main():

    a=hotelfarecal()

    while (1):
        print("1.Enter Customer Data")

        print("2.Calculate room rent")

        print("3.Calculate restaurant bill")

        print("4.Calculate laundry bill")

        print("5.Calculate game bill")

        print("6.Show total cost")

        print("7.EXIT")

        b=int(input("\nEnter your choice:"))
        if (b==1):
            a.inputdata()

        if (b==2):

            a.roomrent()

        if (b==3):

            a.restaurantbill()

        if (b==4):

            a.laundrybill()

        if (b==5):

            a.gamebill()

        if (b==6):

            a.display()


        if (b==7):

            quit()



main()
