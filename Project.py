# -*- coding: utf-8 -*-
"""
Created on Mon May 24 09:51:46 2021

@author: DELL
"""

import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='absinha%',database='Grocery_Shop')
if conn.is_connected():
    print('successfully connected')
c=conn.cursor()

print("\n")
print("\n")
print("*******************************************")
print("*-----Grocery Shop Management System------*")
print("*******************************************")

print("\n")
print("For login-1\nFor exit-2")
a= int(input("Pls enter your choice : "))

if a==1:
    user_name=str(input("Please enter user name : "))
    passwd=str(input("Please enter password : "))
    ans='y'
    while ans.lower()=="y":
        
        if user_name=='Shop' and passwd=='Abhi0910' :
            print("\nSuccessfully Connected.\n****Welcome!!!****")
            print("\n")
            print("\n")
            print("--------------------------------------")
            print("    Grocery Shop management system    ")
            print("--------------------------------------")
            
            print("\n")
            print("1.Upload Customer Details                 *")
            print("2.Upload Worker Details                   *")
            print("3.Upload Product Details                  *")
            print("4.Update Customer Details                 *")
            print("5.Update Worker Details                   *")
            print("6.Update Product Details                  *")
            print("7.Workers account details                 *")
            print("8.Show all customer detais                *")
            print("9.Show all worker details                 *")
            print("10.Show all product details               *")
            print("11.Stocks availability                    *")
            print("12.Update Total stocks availibility       *")
            print("13.Upload profit details per day          *")
            print("14.Upload loss details per day            *")
            print("15.Salary details of each worker          *")
            print("\n")

        
            print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
            choice=int(input("Please enter your choice : "))
            print("\n")
            print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
         
            if choice==1:
            
            # Accepting details from the user
                k='t'
            
                while k.lower()=='t':
                    
                    cust_name=str(input("Enter your name : "))
                    phone_no=int(input("Enter your mobile number : "))
                    billing_cost=float(input("Enter Bill amount : "))
                
                    sql_insert="insert into customer_details values('"+(cust_name)+"',"+str(phone_no)+","+str(billing_cost)+")"
                    c.execute(sql_insert)
                    conn.commit()
                    print("\n")
                    print('-----Data is uploaded-----')
                    
                    print("\n")
                
                    k=input("Add more(t)?? : ")
             
            
            elif choice==2:
              
            # Accepting details from the user
                o='z'
            
                while o.lower()=='z':
                
                    wk_name=str(input("Enter your name : "))
                    wk_work=str(input("Enter your work : "))
                    wk_age=int(input("Enter your age : "))
                    wk_salary=int(input("Enter your salary : "))
                    wk_phone=int(input("Enter your phone no. : "))
            
                # Inserting data into MySQL in Grocery_Shop database
            
                    sql_insert="insert into worker_details values ('"+(wk_name)+"','"+(wk_work)+"',"+str(wk_age)+","+str(wk_salary)+","+str(wk_phone)+")"
            
                # Executing the above statement 
            
                    c.execute(sql_insert)
                    conn.commit()
                    print("\n----Data is Uploaded----")
                
                    print("\n")
                
                    o=input("Add more(z)?? : ")
                
                
            elif choice==3:
            
                tom='j'
            
                while tom.lower()=='j' :
                
            
                # Accepting details from the user
            
                    pr_name=str(input("Pls enter product name : "))
                    pr_id=str(input("Pls enter product ID : "))
                    pr_type=str(input("Enter  product type : "))
                    pr_cost=int(input("Enter product cost : "))
            
                #Inserting data into MySQL in Grocery_Shop database
            
                    sql_insert="insert into product_details values ('"+(pr_name)+"','"+(pr_id)+"','"+(pr_type)+"',"+str(pr_cost)+")"
            
                # Executing the above statement
            
                    c.execute(sql_insert)
                    conn.commit()
                    print("\n----Data is Uploaded----")
                
                    print("\n")
                    tom=input("Add More (j)?? : ")
            
            
            elif choice==4:
            
            # Accepting details from the user
            
                cust_name =input("Enter your updated name : ")
                phone_no=input("Enter your phone no. : ")
            
            #Updating customer's data into MySQL in Grocery_Shop database
            
                sqlFormula="UPDATE customer_details SET cust_name=%s WHERE phone_no = %s"
            
            # Executing the above statement
            
                c.execute(sqlFormula,(cust_name,phone_no))
                conn.commit()
            
                print("*\*\*\*\*\*\*\*\*\*\*\*")
                print("Record updated.")
                print("*\*\*\*\*\*\*\*\*\*\*\*")
            
            
            elif choice==5:
            
            # Accepting details from the user
            
                wk_name=input("Enter your updated name : ")
                wk_phone=input("Enter your phone no. : ")
            
            #Updating Worker's data into MySQL in Grocery_Shop database
            
                sqlUp="UPDATE worker_details SET wk_name=%s WHERE wk_phone = %s"
            
            # Executing the above statement
            
                c.execute(sqlUp,(wk_name,wk_phone))
                conn.commit()
            
                print("*\*\*\*\*\*\*\*\*\*\*\*")
                print("Record updated.")
                print("*\*\*\*\*\*\*\*\*\*\*\*")
            
            
            elif choice==6:
                
            
            # Accepting details from the user
            
                pr_name=input("Enter your updated product name : ")
                pr_id=input("Enter product ID : ")
            
            #Updating Product's data into MySQL in Grocery_Shop database
            
                sql_update="UPDATE product_details SET pr_name=%s WHERE pr_id = %s"
            
            # Executing the above statement
            
                c.execute(sql_update,(pr_name,pr_id))
                conn.commit()
            
                print("*\*\*\*\*\*\*\*\*\*\*\*")
                print("Record updated.")
                print("*\*\*\*\*\*\*\*\*\*\*\*")
                
            
            elif choice==7:
            
            # Accepting details from the user
             
                wk_name=input("Enter your name : ")
                wk_ac=input("Enter your acccount number : ")
                wk_cd=input("Enter your account code : ")
            
            # Displaying the account details from table Workers_account
            
                sql_show='select*from workers_account where wk_cd=%s AND wk_ac=%s'
            
            # Executing the above statement
            
                c.execute(sql_show,(wk_cd,wk_ac))
                a=c.fetchall()
            
                for x in a:
                    print("   Name  account number  account code  salary    dues")
                    print(x)
                
            
            elif choice==8:
            
                c.execute("select*from customer_details")
            
                a=c.fetchall()
            
            # Displaying the Content from Customer_details table here
            
                for x in a :
                    print("  Name      Mobile_No.  Bill_amt")
                    print(x)
            
            
            elif choice==9:
            
            # Displaying the Content from worker_details table here
            
                c.execute("select * from worker_details")
                p=c.fetchall()
            
                for x in p:
                    print("  Wk_name     Wk_work      age salary   WK_phone")
                    print(x)
                
                
            elif choice==10:
            
                c.execute("select*from product_details")
                m=c.fetchall()
            
            # Displaying the Content from Customer_details table here
            
                for x in m:
                    print("  pr_name   pr_id      type    cost")
                    print(x)
                
                
            elif choice==11:
              
                c.execute("select*from stocks")
                a=c.fetchall()
            
            # Displaying the Content from Stocks table here
        
            
                print(" Product  Total  Cost per  Total cost ")
                print("  Name   stocks    item                ")
            
                print("*****************************")
                for i in a:
                
                    print(i,"\n")
                print("*****************************")
              
            
            elif choice==12:
            
                cat='q'
            # Accepting details from the user
                while cat.lower()=='q':
                
                    pr_nm=input("Enter product name : ")
                    pr_no=input("Enter updated stocks available : ")
            
                    s_update="Update stocks SET pr_no=%s where pr_nm=%s"
            
                # Executing the above statement
            
                    c.execute(s_update,(pr_no,pr_nm))
                    conn.commit()
            
                    print("*\*\*\*\*\*\*\*\*\*\*\*")
                    print("Record updated.")
                    print("*\*\*\*\*\*\*\*\*\*\*\*")
            
                    print("\n")
                    cat=input("Add More(q) ?? : ")
              
            elif choice==13:
            
            # Accepting details from the user
                mop='p'
            
                while mop.lower()=='p' :
                
                    total_products=input("Enter total products : ")
                    products_sold=input("Enter products sold : ")
                    total_profit=input("Enter Total profit gained : ")
            
                # Inserting values int the Grocery shop database inn profit_values table
            
                    sql_insert="Insert into profit_values values("+str(total_products)+","+str(products_sold)+","+str(total_profit)+")"
            
                    c.execute(sql_insert)
            
                    conn.commit()
            
                    print("\n")
                    print('-----Data is uploaded-----')
                
                
                    print("\n")
                
                    mop=input("Add more (p) ?? : ")
            
            elif choice==14:
            
            # Accepting values from User
                doc='g'
            
                while doc.lower()=='g' :
                
                    total_products=input("Enter total products : ")
                    products_sold=input("Enter products sold : ")
                    total_loss=input("Enter Total loss : ")
            
            
                # Inserting values int the Grocery shop database inn loss_values table
            
                    sql_insert="Insert into loss_values values ("+str(total_products)+","+str(products_sold)+","+str(total_loss)+")"
            
                # Executing the above statement
            
                    c.execute(sql_insert)
                    conn.commit()
            
                    print("\n")
                    print("----Data Uploaded-----")
                
                    print("\n")
                
                    doc=input("Add More (g) ?? : ")
            
            
            
            elif choice ==15:
            
                ans='y'
            
            # Verifying User name and Password
                while ans.lower()=='y':
                
                    a=input("Enter your User namer : ")
                    b=input("Enter your password : ")
                
                    if a=='User' and b=='pass' :
                    
                
                    #Showing all details of workers account
                
                        sql_show="select* from workers_account "

                    # Executing the above statement
                
                        c.execute(sql_show)
                        k=c.fetchall()
                
                        for x in k:
                    
                            print('\n')
                            print(x)
                    
                    else:
                        
                        print("    INVALID CHOICE    ")
                
                
            
                    
                    
            else:
            
                print("------INVALID USERNAME or PASSWORD-----")
                print("\n")
                ans=input("Retry (y) ?? : ")
            
            
elif a==2:
    print("---------------------GOOD BYE !!---------------------")
    print("            -----------------------------")
    
    
            
            
            
                
            
            
        
            
            

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
            
            
            
            
        
            
            
            
            

    

        
        
       
        
