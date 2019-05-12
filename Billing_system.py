def exit():
    print('thank you for visiting')
#-----------------------------CART---------------------------------------------------------------------------------------------------
a=[]
def cart():
    print('CART'.center(70,'*'))
    if len(a)==0:
        print('Cart is Empty')
        x=input('Do you want to add Food y/n:')
        if x=='y':
            main()
        else:
            print('Thank you for visiting')
    else:
        count=0
        print()
        print('-'.center(65,'-'))
        print('SI.N |','Item name          |','Item size |','price |','Qty  |','Total    |')
        print('-'.center(65,'-'))
        for i in a:
            count+=1
            print(count,'   | ',i[0],' |',i[1],'    |',i[2],'  |',i[3],'  |',i[4],'      |')
        print('-'.center(65,'-'))
        s=input('Do you want to Order more food or bill y/n:')
        print()
        if s=='y':
            main()
        else:
            bill()
#------------------------------------------------------BILLING-----------------------------------------------------------------------------------        
def bill():
    print('BILL'.center(70,'*'))
    print()
    if len(a)==0:
        print('There is no item to bill')
        x=input('Do you want to add Food y/n:')
        if x=='y':
            main()
        else:
            print('Thank you for visiting')
    else:
        Total=0
        count=0
        print('SI.N |','Item name          |','Item size |','price |','Qty  |','Total    |')
        print('-'.center(65,'-'))
        for i in a:
            count+=1
            print(count,'   | ',i[0],' |',i[1],'    |',i[2],'  |',i[3],'  |',i[4],'      |')
            print('-'.center(65,'-'))
            Total+=i[4]
        gst=Total*0.06
        print('GST','=6%','                                                  ',gst,'|')
        print('                                                    Total=',Total,'|')
        print('*'.center(70,'*'))
        print('Thank you for shoping with us'.center(70,'-'))
exit()
#--------------------------------------------------PIZZA MENU--------------------------------------------------------------------------:
b=True
name=''
def pizza_menu():
            l=[[1,'Neapolitan pizza |',150,220,350],[2,'chikago pizza    |',165,195,265],
               [3,'sicilian pizza   |',220,350,462],[4,'greek pizza      |',125,199,299]]           
            print("Select Today's Special Pizza")
            print()
            b=True
            sum=0
            l1=[]
            while b:
                print("*".center(25,'*'))
                for i in l:
                    print(i[0],'    ',i[1],)
                    print('-'.center(25,'-'))
                    print('small | medium | large  |')
                    print(i[2],'  |',i[3],'   | ',i[4],'  |')
                    print('-'.center(25,'-'))
                b=False
                print('''choose option  1.Contn
                2.PrevPage
                3.Main Menu 
                4.Cart''')
                s=input()
                v=True
                while v:
                    if len(s)!=0:
                        if s=='1':
                            c=input("Enter your valid choice 1,2,3,4:")
                            if c=='1':
                                l1.append('Neapolitan pizza')
                                s=input('select size: s,m,l:')
                                if s=='s':
                                    sum+=l[0][2]
                                    l1.append('small')
                                    l1.append(sum)
                                elif s=='m':
                                    sum+=l[0][3]
                                    l1.append('medium')
                                    l1.append(sum)
                                elif s=='l':
                                    sum+=l[0][4]
                                    l1.append('large')
                                    l1.append(sum)
                                else:
                                    y=input('Invalid input,do you wish to continue y/n')
                                    if y=='y':
                                        pizza_menu()
                                    else:
                                        print('thank you for visiting')
                                i=int(input('select the number of items'))
                                l1.append(i)
                                l1.append(i*sum)
                                a.append(l1)
                            elif c=='2':
                                l1.append('chikago pizza   ')
                                s=input('select size: s,m,l:')
                                if s=='s':
                                    sum+=l[0][2]
                                    l1.append('small')
                                    l1.append(sum)
                                elif s=='m':
                                    sum+=l[0][3]
                                    l1.append('medium')
                                    l1.append(sum)
                                elif s=='l':
                                    sum+=l[0][4]
                                    l1.append('large')
                                    l1.append(sum)
                                else:
                                    y=input("invalid opion,Do you want to continue y/n:")
                                    if y=='y':
                                        pizza_menu()
                                    else:
                                        print('thamk you for visiting')
                                        break
                                i=int(input('select the number of items'))
                                l1.append(i)
                                l1.append(i*sum)
                                a.append(l1)
                            elif c=='3':
                                l1.append('sicilian pizza  ')
                                s=input('select size: s,m,l:')
                                if s=='s':
                                    sum+=l[0][2]
                                    l1.append('small')
                                    l1.append(sum)
                                elif s=='m':
                                    sum+=l[0][3]
                                    l1.append('medium')
                                    l1.append(sum)
                                elif s=='l':
                                    sum+=l[0][4]
                                    l1.append('large')
                                    l1.append(sum)
                                else:
                                    y=input("invalid opion,Do you want to continue y/n:")
                                    if y=='y':
                                        pizza_menu()
                                    else:
                                        print('thamk you for visiting')
                                i=int(input('select the number of items'))
                                l1.append(i)
                                l1.append(i*sum)
                                a.append(l1)
                            elif c=='4':
                                l1.append('greek pizza     ')
                                s=input('select size: s,m,l:')
                                if s=='s':
                                    sum+=l[0][2]
                                    l1.append('small')
                                    l1.append(sum)
                                elif s=='m':
                                    sum+=l[0][3]
                                    l1.append('medium')
                                    l1.append(sum)
                                elif s=='l':
                                    sum+=l[0][4]
                                    l1.append('large')
                                    l1.append(sum)
                                else:
                                    y=input("invalid opion,Do you want to continue y/n:")
                                    if y=='y':
                                        pizza_menu()
                                    else:
                                        print('thamk you for visiting')
                                i=int(input('select the number of items'))
                                l1.append(i)
                                l1.append(i*sum)
                                a.append(l1)
                            else:
                                y=input("invalid opion,Do you want to continue y/n:")
                                if y=='y':
                                    pizza_menu()
                                else:
                                    print("Thank you for visiting")
                            s=input('Do you want to order more pizza from pizza menu  y/n:')
                            if len(s)!=0:
                                if s=='y':
                                   pizza_menu()
                                elif s=='n':
                                    main()
                                else:
                                    y=input("invalid opion,Do you want to continue y/n:")
                                    if y=='y':
                                        pizza_menu()
                                    else:
                                        print("Thank you for visiting")
                        elif s=='2':
                            main()
                        elif s=='3':
                            main()
                        elif s=='4':
                            cart()
                        else:
                            z=input('inalid input,Do you want to continue y/n:')
                            if z=='y':
                                pizza_menu()
                            else:
                                print('thank you for visiting')
                                v=False
#menu for the drinks-----------------------------------------------------------------------------------------------------------:              
def drinks_menu():
            d=[[1,'coke    |',60,99],[2,'fanta   |',45,80],
               [3,'pepsi   |',49,89],[4,'sprite  |',69,89]]
            l1=[]
            print("select yot favrite drink")
            b=True
            sum=0
            while b:
                print("*".center(15,'*'))
                
                for i in d:
                    print(i[0],'   ',i[1],)
                    print('-'.center(15,'-'))
                    print('half | full   |' )
                    print(i[2],'  |',i[3],'    |')
                    print('-'.center(15,'-'))
                b=False
                print('''choose option  1.Contn
                2.PrevPage
                3.Main Menu 
                4.Cart''')
                s=input()
                v=True
                while v:
                    if len(s)!=0:
                        if s=='1':
                           break
                        elif s=='2':
                            main()
                        elif s=='3':
                            main()
                        elif s=='4':
                            cart()
                        else:
                            z=input('inalid input,Do you want to continue y/n:')
                            if z!='y':
                                v=False
                c=input("enter you choice,1,2,3,4:")
                if c=='1':
                    l1.append('coke            ')
                    s=input('select the Quantity h,f:')
                    if s=='h':
                        sum+=d[0][2]
                        l1.append('Half')
                        l1.append(sum)
                    elif s=='f':
                        sum+=d[0][3]
                        l1.append('Full')
                        l1.append(sum)
                    else:
                        y=input("invalid opion,Do you want to continue y/n:")
                        if y=='y':
                            drinks_menu()
                        else:
                            print('thamk you for visiting')
                    i=int(input('select the number of items'))
                    l1.append(i)
                    l1.append(i*sum)
                    a.append(l1)
                elif c=='2':
                    l1.append('fanta           ')
                    s=input('select the Quantity h,f:')
                    if s=='h':
                        sum+=d[0][2]
                        l1.append('Half')
                        l1.append(sum)
                    elif s=='f':
                        sum+=d[0][3]
                        l1.append('Full')
                        l1.append(sum)
                    else:
                        y=input("invalid opion,Do you want to continue y/n:")
                        if y=='y':
                            drinks_menu()
                        else:
                            print('thamk you for visiting')
                    i=int(input('select the number of items'))
                    l1.append(i)
                    l1.append(i*sum)
                    a.append(l1)
                elif c=='3':
                    l1.append('pepsi           ')
                    s=input('select the Quantity h,f:')
                    if s=='h':
                        sum+=d[0][2]
                        l1.append('Half')
                        l1.append(sum)
                    elif s=='f':
                        sum+=d[0][3]
                        l1.append('Full')
                        l1.append(sum)
                    else:
                        y=input("invalid opion,Do you want to continue y/n:")
                        if y=='y':
                            drinks_menu()
                        else:
                            print('thamk you for visiting')
                    i=int(input('select the number of items'))
                    l1.append(i)
                    l1.append(i*sum)
                    a.append(l1)
                elif c=='4':
                    l1.append('sprite          ')
                    s=input('select the Quantity h,f:')
                    if s=='h':
                        sum+=d[0][2]
                        l1.append('Half')
                        l1.append(sum)
                    elif s=='f':
                        sum+=d[0][3]
                        l1.append('Full')
                        l1.append(sum)
                    else:
                        y=input("invalid opion,Do you want to continue y/n:")
                        if y=='y':
                            drinks_menu()
                        else:
                            print('thamk you for visiting')
                    i=int(input('select the number of items'))
                    l1.append(i)
                    l1.append(i*sum)
                    a.append(l1)
                else:
                    y=input("invalid opion,Do you want to continue y/n:")
                    if y=='y':
                        drinks_menu()
                    else:
                        print("Thank you for visiting")
                s=input('Do you want to order more drinks from menu  y/n:')
                if len(s)!=0:
                    if s=='y':
                       drinks_menu()
                    elif s=='n':
                        main()
                    else:
                        y=input("invalid opion,Do you want to continue y/n:")
                        if y=='y':
                            drinks_menu()
                        else:
                            print("Thank you for visiting")
                            break
#menu for the sides -----------------------------------------------------------------------------------------------------------                      
def sides_menu():
            m=[[1,'chicken strips      |',30,60,185],
               [2,'masala wedges       |',65,99,156],
               [3,'fries               |',49,89,149],
               [4,'mexican cheesy fries|',59,99,199]]           
            print("select yot favrite drink")
            b=True
            sum=0
            l1=[]
            while b:
                print('*'.center(26,'*'))             
                for i in m:
                    print(i[0],'  ',i[1],)
                    print('-'.center(26,'-'))
                    print('small | medium | large   |' )
                    print(i[2],'   |  ',i[3],'  | ',i[4],'   |')
                    print("-".center(26,'-'))
                b=False
                print('''choose option  1.Contn
                2.PrevPage
                3.Main Menu 
                4.Cart''')
                s=input()
                v=True
                while v:
                    if len(s)!=0:
                        if s=='1':
                           break
                        elif s=='2':
                            main()
                        elif s=='3':
                            main()
                        elif s=='4':
                            cart()
                        else:
                            z=input('inalid input,Do you want to continue y/n:')
                            if z!='y':
                                v=False
                c=input("enter you choice,1,2,3,4")
                if c=='1':
                    l1.append('chicken strips  ')
                    s=input('select size: s,m,l:')
                    if s=='s':
                        sum+=m[0][2]
                        l1.append('small')
                        l1.append(sum)
                    elif s=='m':
                        sum+=m[0][3]
                        l1.append('medium')
                        l1.append(sum)
                    elif s=='l':
                        sum+=m[0][4]
                        l1.append('large')
                        l1.append(sum)
                    else:
                        y=input('Invalid input,do you wish to continue y/n')
                        if y=='y':
                            sides_menu()
                        else:
                            print('thamk you for visiting')
                    i=int(input('select the number of items'))
                    l1.append(i)
                    l1.append(i*sum)
                    a.append(l1)
                elif c=='2':
                    l1.append('masala wedges   ')
                    s=input('select size: s,m,l:')
                    if s=='s':
                        sum+=m[0][2]
                        l1.append('small')
                        l1.append(sum)
                    elif s=='m':
                        sum+=m[0][3]
                        l1.append('medium')
                        l1.append(sum)
                    elif s=='l':
                        sum+=m[0][4]
                        l1.append('large')
                        l1.append(sum)
                    else:
                        y=input('Invalid input,do you wish to continue y/n')
                        if y=='y':
                            sides_menu()
                        else:
                            print('thamk you for visiting')
                    i=int(input('select the number of items'))
                    l1.append(i)
                    l1.append(i*sum)
                    a.append(l1)
                elif c=='3':
                    l1.append('fries            ')
                    s=input('select size: s,m,l:')
                    if s=='s':
                        sum+=m[0][2]
                        l1.append('small')
                        l1.append(sum)
                    elif s=='m':
                        sum+=m[0][3]
                        l1.append('medium')
                        l1.append(sum)
                    elif s=='l':
                        sum+=m[0][4]
                        l1.append('large')
                        l1.append(sum)
                    else:
                        y=input('Invalid input,do you wish to continue y/n')
                        if y=='y':
                            sides_menu()
                        else:
                            print('thamk you for visiting')
                    i=int(input('select the number of items'))
                    l1.append(i)
                    l1.append(i*sum)
                    a.append(l1)
                elif c=='4':
                    l1.append('mexican cheesy f')
                    s=input('select size: s,m,l:')
                    if s=='s':
                        sum+=m[0][2]
                        l1.append('small')
                        l1.append(sum)
                    elif s=='m':
                        sum+=m[0][3]
                        l1.append('medium')
                        l1.append(sum)
                    elif s=='l':
                        sum+=m[0][4]
                        l1.append('large')
                        l1.append(sum)
                    else:
                        y=input('Invalid input,do you wish to continue y/n')
                        if y=='y':
                           sides_menu()
                        else:
                            print('thamk you for visiting')
                    i=int(input('select the number of items'))
                    l1.append(i)
                    l1.append(i*sum)
                    a.append(l1)
                else:
                    y=input("invalid opion,Do you want to continue y/n:")
                    if y=='y':
                        sides_menu()
                    else:
                        print("Thank you for visiting")
                s=input('Do you want to order more sides from menu  y/n:')
                print()
                if len(s)!=0:
                    if s=='y':
                       sides_menu()
                    elif s=='n':
                        main()
                    else:
                        y=input("invalid opion,Do you want to continue y/n:")
                        if y=='y':
                            sides_menu()
                        else:
                           exit()
                else:
                    exit()
#menu for the deserts:               
def deserts_menu():
            des=[[1,'choco lava cake   |',50,90],[2,'butter scotch cake|',64,105],
               [3,'chocalte cake     |',49,89],[4,'black forest      |',99,199]]
            
            print("select yot favrite drink")
            print()
            b=True
            sum=0
            l1=[]
            while b:
                print("*".center(26,'*'))
                for i in des:
                    print(i[0],'    ',i[1],)
                    print("-".center(26,'-'))
                    print('half | full              |' )
                    print(i[2],'  | ' ,i[3])
                    print("-".center(26,'-'))
                b=False
                print('''choose option  1.Contn
                2.PrevPage
                3.Main Menu 
                4.Cart''')
                s=input()
                v=True
                while v:
                    if len(s)!=0:
                        if s=='1':
                           break
                        elif s=='2':
                            main()
                        elif s=='3':
                            main()
                        elif s=='4':
                            cart()
                        else:
                            z=input('inalid input,Do you want to continue y/n:')
                            if z!='y':
                                v=False
                print("enter you choice,1,2,3,4")
                c=input()
                if c=='1':
                    l1.append('choco lava cake ')
                    s=input('select the Quantity h,f:')
                    if s=='h':
                        sum+=des[0][2]
                        l1.append('half')
                        l1.append(sum)
                    elif s=='f':
                        sum+=des[0][3]
                        l1.append('full')
                        l1.append(sum)
                    else:
                        y=input('Invalid input,do you wish to continue y/n')
                        if y=='y':
                           deserts_menu()
                        else:
                            print('thamk you for visiting')
                    i=int(input('select the number of items'))
                    l1.append(i)
                    l1.append(i*sum)
                    a.append(l1)
                elif c=='2':
                    l1.append('butter scotch   ')
                    print('select the Quantity h,f:')
                    s=input()
                    if s=='h':
                        sum+=des[0][2]
                        l1.append('half')
                        l1.append(sum)
                    elif s=='f':
                        sum+=des[0][3]
                        l1.append('full')
                        l1.append(sum)
                    else:
                        y=input('Invalid input,do you wish to continue y/n')
                        if y=='y':
                           deserts_menu()
                        else:
                            print('thamk you for visiting')
                    i=int(input('select the number of items'))
                    l1.append(i)
                    l1.append(i*sum)
                    a.append(l1)
                elif c=='3':
                    l1.append('chocalte cake   ')
                    print('select the Quantity h,f:')
                    s=input()
                    if s=='h':
                        sum+=des[0][2]
                        l1.append('half')
                        l1.append(sum)
                    elif s=='f':
                        sum+=des[0][3]
                        l1.append('full')
                        l1.append(sum)
                    else:
                        y=input('Invalid input,do you wish to continue y/n')
                        if y=='y':
                           deserts_menu()
                        else:
                            print('thamk you for visiting')
                    i=int(input('select the number of items'))
                    l1.append(i)
                    l1.append(i*sum)
                    a.append(l1)
                elif c=='4':
                    l1.append('black forest    ')
                    print('select the Quantity h,f:')
                    s=input()
                    if s=='h':
                        sum+=des[0][2]
                        l1.append('half')
                        l1.append(sum)
                    elif s=='f':
                        sum+=des[0][3]
                        l1.append('full')
                        l1.append(sum)
                    else:
                        y=input('Invalid input,do you wish to continue y/n')
                        if y=='y':
                           deserts_menu()
                        else:
                            print('thamk you for visiting')
                    i=int(input('select the number of items'))
                    l1.append(i)
                    l1.append(i*sum)
                    a.append(l1)
                else:
                    y=input("invalid opion,Do you want to continue y/n:")
                    if y=='y':
                        deserts_menu()
                    else:
                        print("Thank you for visiting")
                s=input('Do you want to order more desert from menu  y/n:')
                if len(s)!=0:
                    if s=='y':
                       deserts_menu()       
                    elif s=='n':
                        main()
                    else:
                        y=input("invalid opion,Do you want to continue y/n:")
                        if y=='y':
                            deserts_menu()
                        else:
                            print("Thank you for visiting")
#for display menu items 
def main():
    cat=[[1,"pizza |"],[2,"drinks|"],[3,"sides |"],
         [4,"desert|"],[5,'cart  |'],[6,"exit  |"]]
    b=True
    while b:    
        print("choose the category:")
        print("*************")
        print("No's| Items |")
        print("*************")
        for i in cat: 
            print(i[0],'  |',i[1])
        print("*************")
        choose_cat=input("Select your option:")
        print()
        if choose_cat=='1':      
            pizza_menu() 
        elif choose_cat=='2':
            drinks_menu()      
        elif choose_cat=='3':
            sides_menu()
        elif choose_cat=='4':
             deserts_menu()
        elif choose_cat=='5':
            cart()
        elif choose_cat=='6':
            bill()
        else:
            print("Invalid Choice,Do you wish to continue y/n")
            x=input()
            if x=='y':
                main()
            else:
                print("Thank You For Visiting, Come again")
                b=False
        b=False

#taking name of the user:
b=True
while b:
    name=input("Enter your name :")
    if len(name)==0 or not(name.isalpha()):
        a=input("Invalid name.Do you want to continue? y/n")
        if a!='y':
            b=False
            print("Thank you for vising")
    else:
        b=False
        print()
        print()
        print('*'.center(51,'*'))
        print("Welcome to Dominos".center(51,' '))
        print('*'.center(51,'*'))
        print()
        print("Welcome Mr/Ms.",name.upper(),",we are happy to serve you")
        print()
        main()
   