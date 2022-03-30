import streamlit as st
import csv
def package():
    st.write("""These are the packages we offer:
1. Kyrgyzstan
2. Vanuatu
3. Tajikistan
4. Nauru
5. Ivory Coast
6. Andorra
7. Liechtenstein
8. Wallis and Futuna
9. Tuvalu
10. Moldova""")
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
    x=st.number_input("""Which country do you want to visit of the following? Enter the number.
1. Kyrgyzstan
2. Vanuatu
3. Tajikistan
4. Nauru
5. Ivory Coast
6. Andorra
7. Liechtenstein
8. Wallis and Futuna
9. Tuvalu
10. Moldova""")
    start=st.text_input("Enter the start date in the format DD-MM-YYYY.")
    durn=st.number_input("Enter the number of days you want to travel")
    f=open("booking.csv","a",newline="")
    d=st.number_input("Number of people travelling:")
    rec=csv.writer(f,delimiter=",")
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
    r=[pas,country,start,durn,d]
    st.write("Here are the details of your booking in the order password, country, start date, duration and number of people travelling:",r)
    c=st.text_input("Do you want to confirm your booking? Enter y for yes and n for no.")
    st.write("Send your itinerary to dreams007@gmail.com atleast one month prior to your travel date.")
    st.write("""Cost per person is",durn*12000, "Pay", d*(durn*12000)," through PayTM or GPay at the number 9098909899.
You will recieve the reciept on your whatsapp.""")
    st.write("If you do not send your itinerary within the given period, your booking will be cancelled and you will recieve a 90% refund.")
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
        st.write("Your booking(s) is(are) in the order password, country, start date, duration and number of people travelling")
        for j in a:
            st.write(j)
def feedback():
    st.write("Please give your feedback:")
    x=st.text_input()
    f=open("feedback.txt","a")
    f.write('\n')
    f.write(x)
    f.write('\n')
    st.write("Thank you for your valuable feedback!")
    f.close()
def readfeed():
    f=open("feedback.txt","r")
    st.write(f.read())
    f.close()
    
st.write("Welcome to Dreamers Tours & Travels!  You have come to the right place if you want to have your dream vacation come true!")
st.write("We here help you to travel to the least visited countries in the world, that too on your own terms.")
st.write("""You can make your own itinerary and we will help you to achieve it at just INR 12000/- per day no matter what package you choose.
This cost includes all the travel, accomodation and VISA charges.""")
st.write("So let this wonderful journey begin!")
while True:
    x=st.number_input("""How would you like to explore our service?
1. Offline: in person at our office
2. Online: at the comfort of your home""")
    if x==1:
        st.write("""Our offices are present in these four cities:
1. Delhi
2.Mumbai
3.Chennai
4.Kolkata""")
        x=st.number_input("Which office would you like to visit? Press 5 to exit.")
        if x==1:
            st.write("""Our office is located at Connaught Place.
Address: Dreamers Tours & Travels, N-17, Rajeev Chowk-110001""")
            st.write("You can visit our office anytime between 09:00 and 17:00 on weekdays. Thank you!")
        elif x==2:
            st.write(""""Our office is located at Altamount Road.
Address: 1A, Altamountroad, Tardeo-400026""")
            st.write("You can visit our office anytime between 09:00 and 17:00 on weekends. Thank you!")
        elif x==3:
            st.write("""Our office is located at T. Nagar
Address: No.7, Nageswara Rao Road, T.Nagar-600017""")
            st.write("You can visit our office anytime between 09:00 and 17:00 on any day. Thank you!")
        elif x==4:
            st.write("""Our office is located at Rosedale Plaza Complex
Address: Rosedale Plaza Complex, New Town Road, Action Area III, Newtown-700160""")
            st.write("You can visit our office anytime between 09:00 and 17:00 on weekdays. Thank you!")
        else:
            feedback()
            st.write("Thank you for visiting our website. If you have any query, mail us at dreamersT&T@gmail.com. Hope to see you again!")
            break
            break
    else:
        st.write("""What do you want to do:
1.View the Packages we offer.
2. Make a booking.
3. View your booking.
4. Read reviews of our esteemed customers
5. Exit""")
        x=st.number_input("Enter the number.")
        if x==1:
             package()
        elif x==2:
            book()
        elif x==3:
              read()
        elif x==4:
            readfeed()
        else:
            feedback()
            st.write("Thank you for visiting our website. If you have any query, mail us at dreamersT&T@gmail.com. Hope to see you again!")
            break
    
