def homerseklet():
    homersekletC=int(input("Kérek egy hőmérséklet értéket: "))
   

    if homersekletC<=0:
        print("szilárd halmazállapot.")
    elif homersekletC>100:
        print("folyékony halmazállapot.")
    else:
        print ("légnemű halmazállapot. ")


homerseklet()