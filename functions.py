import streamlit as st
import csv
def package():
    st.write("There are the following packages: \n 1. Kyrgyzstan \n 2. Vanuatu \n 3. Tajikistan \n 4. Nauru \n 5. Ivory Coast \n 6. Andorra \n 7. Liechtenstein \n 8. Wallis and Futuna \n 9. Tuvalu \n 10. Moldova")
    y=1
    while y==1:
        x=st.number_input("Which package would you like to know more about? Enter the number of the package. Enter 0 to exit.")
        if x==1:
            f=open("Kyrgyzstan.txt","r")
            st.write(f.read())
            f.close()
        elif x==2:
            f=open("Vanuatu.txt","r")
            st.write(f.read())
            f.close()
        elif x==3:
            f=open("Tajikistan.txt","r")
            st.write(f.read())
            f.close()
        elif x==4:
            f=open("Nauru.txt","r")
            st.write(f.read())
            f.close()
        elif x==5:
            f=open("Ivory Coast.txt","r")
            st.write(f.read())
            f.close()
        elif x==6:
            f=open("Andorra.txt","r")
            st.write(f.read())
            f.close()
        elif x==7:
            f=open("Liechtenstein.txt","r")
            st.write(f.read())
            f.close()
        elif x==8:
            f=open("Wallis and Futuna.txt","r")
            st.write(f.read())
            f.close()
        elif x==9:
            f=open("Tuvalu.txt","r")
            st.write(f.read())
            f.close()
        elif x==10:
            f=open("Moldova.txt","r")
            st.write(f.read())
            f.close()
        elif x==0:
            y=0
        else:
            st.write("Invalid input")

def book():
    pas=st.text_input("Set a strong password. Enter your old password if you have already made a booking")
    st.write("Make sure you do your booking atleast 45 days before the date of travel.")
    x=st.number_input("Which country do you want to visit of the following? Enter the number.  \n 1. Kyrgyzstan \n 2. Vanuatu \n 3. Tajikistan \n 4. Nauru \n 5. Ivory Coast \n 6. Andorra \n 7. Liechtenstein \n 8. Wallis and Futuna \n 9. Tuvalu \n 10. Moldova")
    start=st.text_input("Enter the start date in the format DD/MM/YYYY.")
    durn=st.number_input("Enter the number of days you want to travel")
    f=open("booking.csv","a",newline="")
    d=st.number_input("Number of people travelling:")
    rec=csv.writer(f,delimiter=",")
    rec.writerow(["Password","COUNTRY","START","DURATION"])
    if x==1:
        country='Kyrgyzstan'
    elif x==2:
        country='Vanuatu'
    elif x==3:
        country='Tajikistan'
    elif x==4:
        country='Nauru'
    elif x==5:
        country='Ivory Coast'
    elif x==6:
        country='Andorra'
    elif x==7:
        country='Liechtenstein'
    elif x==8:
        country='Wallis and Futuna'
    elif x==9:
        country='Tuvalu'
    elif x==10:
        country='Moldova'
    else:
        st.write("Invalid input")
    r=[pas,country,start,durn]
    c=st.text_input("Do you want to confirm your booking? Enter y for yes.")
    st.write("Send your itenary to dreams007@gmail.com atleast one month prior to your travel date.")
    st.write("Cost per person is",durn*12000, "Pay", d*(durn*12000)," through PayTM or GPay at the number 9098909899 and you will recieve the reciept on your whatsapp.")
    st.write("If you do not send your itenary within the given period, you will recieve a 90% refund.")
    if c in 'yY':
        rec.writerow(r)
    else:
        pass
    f.close()
def read():
    f=open("booking.csv","r",newline="")
    x=csv.reader(f)
    y=st.text_input("Enter your password to see your bookings.")
    a=[]
    for i in x:
        if i[0]==y:
            a.append(i)
        else:
            pass
    if len(a)==0:
        st.write("Invalid Password")
    else:
        for j in a:
            st.write(j)
