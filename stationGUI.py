"""Petrol station database GUI"""
from tkinter import *
import sqlite3

# I MAIN WINDOW

root = Tk() #this is the main window its also the first line to put when working with tkinter
root.title('Petrol Station GUI') #this is the title of the window
root.geometry("400x400") #specifying the size of the root window
#root.config(font=('Times', 15))

# Database

# Creating a connection to a database
conn = sqlite3.connect('petrolstation.db')

# Create a cursor
c = conn.cursor()

# Getting branch values from table branches
branchList =[]
c.execute("SELECT branchName FROM tblBranches")

branches = c.fetchall()
#print(branches)
for branch in branches:
    branchList += branch

#print(branchList)

# A function that will get the selected value
def branchFtn():
    #myLabel = Label(root, text=clicked.get()).pack()

    #Need to have an if / else statement to bring up different windows based on the branch selected
    #the if/else should intialize another function that will take the input of the selected branch
    #and launch the desired branch window

    # II EDITOR_BRANCH1 WINDOW

    # Creating a new window for updating records
    global editor_branch1 #need it to be global so that we can use editor.destroy 
    editor_branch1 = Tk() #this is the main window its also the first line to put when working with tkinter
    editor_branch1.title('Enter Branch Place Data') #this is the title of the window
    editor_branch1.geometry("1000x1000") #specifying the size of the root window

    # Retrieving and saving the previous indexes
    
    # Creating a database or connect to one
    conn = sqlite3.connect('petrolstation.db')

    # Create a cursor
    c = conn.cursor()
    
    c.execute("SELECT *, oid FROM tblIndexes WHERE indexDate IN (SELECT MAX(indexDate) FROM tblIndexes)") #oid means include the default primary key. MAX(indexDate) ensures we only return results from the last date entered
    records = c.fetchall() #this will store all the records
    #print(records) #this will print the records in the terminal

    # Declare and initialize global variables
    global ClosingIndexesLstBranch1
    global LastIndexIDLstBranch1
    global LastIndexIDBranch1

    ClosingIndexesLstBranch1 = []
    LastIndexIDLstBranch1 = []
    LastIndexIDBranch1 = 0
    
    # Retrieving closing indexes and assigning them to branch1ClosingIndexesLst
    for record in records:
        index = record[6]
        #print("index: ", type(index), index)
        ClosingIndexesLstBranch1.append(index)
        #print("closingIndexLst: ", type(closingIndexesLst), closingIndexesLst)

    #print("Printing closing indexes List:\n", branch1ClosingIndexesLst)

    # Retrieving the last IndexID from tblIndexes
    for record in records:
        indexID = record[0]
        LastIndexIDLstBranch1.append(indexID)

    #print("Printing closing indexID List:\n", branch1LastIndexIDLst)
    LastIndexIDBranch1 = LastIndexIDLstBranch1[len(LastIndexIDLstBranch1)-1]
    #print("Printing last IndexID: ", type(branch1LastIndexID), branch1LastIndexID)

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()

    # Creating submit function
    def indexSubmitFtn():
        global LastIndexID_branch1
        LastIndexID_branch1 = LastIndexIDBranch1
        # Creating a database or connect to one
        conn = sqlite3.connect('petrolstation.db')

        # Create a cursor
        c = conn.cursor()
    
        # Insert entered indexes into tblIndexes in the database

        # Using if/else to fill data for the three pumps without repetition
        # Closing Index values are taken from the branch1ClosingIndexesLst
        
        total_day_pms_liters_branch1 = 0 #this variable will be used in calculating the total pms liters sold for a particular day
        total_day_ago_liters_branch1 = 0 #this variable will be used in calculating the total ago liters sold for a particular day
        
        while len(ClosingIndexesLstBranch1) > 0: #this ensures that all the indexes are uploaded to the tblIndexes
            if len(ClosingIndexesLstBranch1) == 6:
                LastIndexID_branch1 += 1
                #print(LastIndexID_branch1)
                            
                c.execute("INSERT INTO tblIndexes VALUES (:indexID, :indexDate, :indexBranchID, :indexProductID, :indexPumpNumber, :openingIndex, :closingIndex)",
                    {
                        'indexID': LastIndexID_branch1,
                        'indexDate': date_editor_branch1.get(),
                        'indexBranchID': 1,
                        'indexProductID': 1,
                        'indexPumpNumber': pump1_editor_branch1.get(),
                        'openingIndex': ClosingIndexesLstBranch1[0],
                        'closingIndex': pump1_pms_editor_branch1.get()
                    })
                total_day_pms_liters_branch1 = (float(pump1_pms_editor_branch1.get()) - ClosingIndexesLstBranch1[0])
                #print("Pump 1 PMS: ", branch1_total_day_pms_liters)
                ClosingIndexesLstBranch1.pop(0)
                LastIndexID_branch1 += 1
                #print(LastIndexID_branch1)
            elif len(ClosingIndexesLstBranch1) == 5:
                c.execute("INSERT INTO tblIndexes VALUES (:indexID, :indexDate, :indexBranchID, :indexProductID, :indexPumpNumber, :openingIndex, :closingIndex)",
                    {
                        'indexID': LastIndexID_branch1,
                        'indexDate': date_editor_branch1.get(),
                        'indexBranchID': 1,
                        'indexProductID': 2,
                        'indexPumpNumber': pump1_editor_branch1.get(),
                        'openingIndex': ClosingIndexesLstBranch1[0],
                        'closingIndex': pump1_ago_editor_branch1.get()
                    })
                total_day_ago_liters_branch1 = (float(pump1_ago_editor_branch1.get()) - ClosingIndexesLstBranch1[0])
                #print("Pump 1 AGO: ", branch1_total_day_ago_liters)
                ClosingIndexesLstBranch1.pop(0)
                LastIndexID_branch1 += 1
                #print(LastIndexID_branch1)
            elif len(ClosingIndexesLstBranch1) == 4:
                c.execute("INSERT INTO tblIndexes VALUES (:indexID, :indexDate, :indexBranchID, :indexProductID, :indexPumpNumber, :openingIndex, :closingIndex)",
                    {
                        'indexID': LastIndexID_branch1,
                        'indexDate': date_editor_branch1.get(),
                        'indexBranchID': 1,
                        'indexProductID': 1,
                        'indexPumpNumber': pump2_editor_branch1.get(),
                        'openingIndex': ClosingIndexesLstBranch1[0],
                        'closingIndex': pump2_pms_editor_branch1.get()
                    })
                total_day_pms_liters_branch1 = total_day_pms_liters_branch1 + (float(pump2_pms_editor_branch1.get()) - ClosingIndexesLstBranch1[0])
                ClosingIndexesLstBranch1.pop(0)
                LastIndexID_branch1 += 1
                #print(LastIndexID_branch1)
            elif len(ClosingIndexesLstBranch1) == 3:
                c.execute("INSERT INTO tblIndexes VALUES (:indexID, :indexDate, :indexBranchID, :indexProductID, :indexPumpNumber, :openingIndex, :closingIndex)",
                    {
                        'indexID': LastIndexID_branch1,
                        'indexDate': date_editor_branch1.get(),
                        'indexBranchID': 1,
                        'indexProductID': 2,
                        'indexPumpNumber': pump2_editor_branch1.get(),
                        'openingIndex': ClosingIndexesLstBranch1[0],
                        'closingIndex': pump2_ago_editor_branch1.get()
                    })
                total_day_ago_liters_branch1 = total_day_ago_liters_branch1 + (float(pump2_ago_editor_branch1.get()) - ClosingIndexesLstBranch1[0])
                ClosingIndexesLstBranch1.pop(0)
                LastIndexID_branch1 += 1
                #print(LastIndexID_branch1)
            elif len(ClosingIndexesLstBranch1) == 2:
                c.execute("INSERT INTO tblIndexes VALUES (:indexID, :indexDate, :indexBranchID, :indexProductID, :indexPumpNumber, :openingIndex, :closingIndex)",
                    {
                        'indexID': LastIndexID_branch1,
                        'indexDate': date_editor_branch1.get(),
                        'indexBranchID': 1,
                        'indexProductID': 1,
                        'indexPumpNumber': pump3_editor_branch1.get(),
                        'openingIndex': ClosingIndexesLstBranch1[0],
                        'closingIndex': pump3_pms_editor_branch1.get()
                    })
                total_day_pms_liters_branch1 = total_day_pms_liters_branch1 + (float(pump3_pms_editor_branch1.get()) - ClosingIndexesLstBranch1[0])
                ClosingIndexesLstBranch1.pop(0)
                LastIndexID_branch1 += 1
                #print(LastIndexID_branch1)
            elif len(ClosingIndexesLstBranch1) == 1:
                c.execute("INSERT INTO tblIndexes VALUES (:indexID, :indexDate, :indexBranchID, :indexProductID, :indexPumpNumber, :openingIndex, :closingIndex)",
                    {
                        'indexID': LastIndexID_branch1,
                        'indexDate': date_editor_branch1.get(),
                        'indexBranchID': 1,
                        'indexProductID': 2,
                        'indexPumpNumber': pump3_editor_branch1.get(),
                        'openingIndex': ClosingIndexesLstBranch1[0],
                        'closingIndex': pump3_ago_editor_branch1.get()
                    })
                total_day_ago_liters_branch1 = total_day_ago_liters_branch1 + (float(pump3_ago_editor_branch1.get()) - ClosingIndexesLstBranch1[0])
                ClosingIndexesLstBranch1.pop(0)
                #print(LastIndexID_branch1)
                
        # Commit changes
        conn.commit()

        # Close connection
        conn.close()

        # Clear the text boxes
        #date_editor_branch1.delete(0, END)
        pump1_pms_editor_branch1.delete(0, END)
        pump1_ago_editor_branch1.delete(0, END)
        pump2_pms_editor_branch1.delete(0, END)
        pump2_ago_editor_branch1.delete(0, END)
        pump3_pms_editor_branch1.delete(0, END)
        pump3_ago_editor_branch1.delete(0, END)

        # Declaring and initializing global variables and assigning them fuel returned from the returned fuel text box
        global total_fuel_returned_pms_branch1
        global total_fuel_returned_ago_branch1

        total_fuel_returned_pms_branch1 = 0
        total_fuel_returned_ago_branch1 = 0

        total_fuel_returned_pms_branch1 = fuel_returned_pms_branch1.get()
        total_fuel_returned_ago_branch1 = fuel_returned_ago_branch1.get()

        # updating variables used in displaying the total pms and ago sales liters when factoring total returned fuel
        day_sale_liters_pms_branch1 = total_day_pms_liters_branch1 - total_fuel_returned_pms_branch1
        day_sale_liters_ago_branch1 = total_day_ago_liters_branch1 - total_fuel_returned_ago_branch1

        # updating the total sales labels to update with the new values
        total_sales_result_pms_label.config(text=day_sale_liters_pms_branch1)
        total_sales_result_ago_label.config(text=day_sale_liters_ago_branch1)

    # Creating indexCancelFtn function
    def indexCancelFtn():
        date_editor_branch1.delete(0, END)
        pump1_pms_editor_branch1.delete(0, END)
        pump1_ago_editor_branch1.delete(0, END)
        pump2_pms_editor_branch1.delete(0, END)
        pump2_ago_editor_branch1.delete(0, END)
        pump3_pms_editor_branch1.delete(0, END)
        pump3_ago_editor_branch1.delete(0, END)
    
    # Creating restockSubmit function
    # For interbranch supply, I need a way to calculate the fuel used for a branch so that I can determine the mainStockSupplyID
    def restockSubmitFtn():
        return
    
    # Creating restockCancel function
    def restockCancelFtn():
        return
    
    # Creating advancePaymentFtn function
    def advancePaymentFtn():
        # EDITOR_ADVANCE_PAYMENT WINDOW

        # Creating a new window advance payments
        global editor_advance_payment #need it to be global so that we can use editor.destroy 
        editor_advance_payment = Tk() #this is the main window its also the first line to put when working with tkinter
        editor_advance_payment.title('Enter Advance Payments Data') #this is the title of the window
        editor_advance_payment.geometry("700x700") #specifying the size of the root window

       
     # Creating debtPaymentFtn function
    def debtPaymentFtn():
        return
    
    # INDEX AREA

    # Creating Labels
    date_label = Label(editor_branch1, text="Date")
    date_label.grid(row=0, column=0)
    branch_label = Label(editor_branch1, text="Place")
    branch_label.grid(row=1, column=0)
    pump1_label = Label(editor_branch1, text="Pump I")
    pump1_label.grid(row=2, column=0, pady=(10,0))
    pump2_label = Label(editor_branch1, text="Pump II")
    pump2_label.grid(row=5, column=0)
    pump3_label = Label(editor_branch1, text="Pump III")
    pump3_label.grid(row=8, column=0)

    pump1_pms_label = Label(editor_branch1, text="PMS")
    pump1_pms_label.grid(row=3, column=1)
    pump1_ago_label = Label(editor_branch1, text="AGO")
    pump1_ago_label.grid(row=4, column=1)
    pump2_pms_label = Label(editor_branch1, text="PMS")
    pump2_pms_label.grid(row=6, column=1)
    pump2_ago_label = Label(editor_branch1, text="AGO")
    pump2_ago_label.grid(row=7, column=1)
    pump3_pms_label = Label(editor_branch1, text="PMS")
    pump3_pms_label.grid(row=9, column=1)
    pump3_ago_label = Label(editor_branch1, text="AGO")
    pump3_ago_label.grid(row=10, column=1, pady=(0,10))

    # Creating global variables for text box names
    global date_editor_branch1
    global branch_editor_branch1
    global pump1_editor_branch1
    global pump1_pms_editor_branch1
    global pump1_ago_editor_branch1
    global pump2_editor_branch1
    global pump2_pms_editor_branch1
    global pump2_ago_editor_branch1
    global pump3_editor_branch1
    global pump3_pms_editor_branch1
    global pump3_ago_editor_branch1

    # Creating text boxes
    date_editor_branch1 = Entry(editor_branch1, width=30)
    date_editor_branch1.grid(row=0, column=2, padx=20)
    branch_editor_branch1 = Entry(editor_branch1, width=30)
    branch_editor_branch1.grid(row=1, column=2)
    branch_editor_branch1.insert(0, str(clicked.get())) #this inserts the clicked branch into the text box
    branch_editor_branch1.config(state="disabled") #this prevents users from changing this value

    pump1_editor_branch1 = Entry(editor_branch1, width=30)
    pump1_editor_branch1.grid(row=2, column=2, pady=(10,0))
    pump1_editor_branch1.insert(0, str(1)) #this inserts the pump no. "1" into the text box
    pump1_editor_branch1.config(state="disabled") #this prevents users from changing this value
    pump1_pms_editor_branch1 = Entry(editor_branch1, width=30)
    pump1_pms_editor_branch1.grid(row=3, column=2)
    pump1_ago_editor_branch1 = Entry(editor_branch1, width=30)
    pump1_ago_editor_branch1.grid(row=4, column=2)

    pump2_editor_branch1 = Entry(editor_branch1, width=30)
    pump2_editor_branch1.grid(row=5, column=2)
    pump2_editor_branch1.insert(0, str(2)) #this inserts the pump no. "2" into the text box
    pump2_editor_branch1.config(state="disabled") #this prevents users from changing this value
    pump2_pms_editor_branch1 = Entry(editor_branch1, width=30)
    pump2_pms_editor_branch1.grid(row=6, column=2)
    pump2_ago_editor_branch1 = Entry(editor_branch1, width=30)
    pump2_ago_editor_branch1.grid(row=7, column=2)

    pump3_editor_branch1 = Entry(editor_branch1, width=30)
    pump3_editor_branch1.grid(row=8, column=2)
    pump3_editor_branch1.insert(0, str(3)) #this inserts the pump no. "3" into the text box
    pump3_editor_branch1.config(state="disabled") #this prevents users from changing this value
    pump3_pms_editor_branch1 = Entry(editor_branch1, width=30)
    pump3_pms_editor_branch1.grid(row=9, column=2)
    pump3_ago_editor_branch1 = Entry(editor_branch1, width=30)
    pump3_ago_editor_branch1.grid(row=10, column=2, pady=(0,10))

    # Creating buttons for Index
    index_cancel_btn = Button(editor_branch1, text="Cancel", command=indexCancelFtn)
    index_cancel_btn.grid(row=11, column=1, pady=10, padx=(0,5), ipadx=50)

    index_submit_btn = Button(editor_branch1, text="Submit", command=indexSubmitFtn)
    index_submit_btn.grid(row=11, column=2, pady=10, padx=(5,0), ipadx=60)

    
    # CREATING FUEL RETURNED / AMORSAGE
    
    # Creating labels
    fuel_returned_pms_label = Label(editor_branch1, text="Amorsage")
    fuel_returned_pms_label.grid(row=12, column=0, pady=5, columnspan=4)
    fuel_returned_pms_label = Label(editor_branch1, text="PMS")
    fuel_returned_pms_label.grid(row=13, column=0, pady=5)
    fuel_returned_pms_label = Label(editor_branch1, text="AGO")
    fuel_returned_pms_label.grid(row=13, column=2, pady=5)

    # Creating global variable
    global fuel_returned_pms_branch1
    global fuel_returned_ago_branch1

    fuel_returned_pms_branch1 = 0
    fuel_returned_ago_branch1 = 0

    # Creating text box
    fuel_returned_pms_branch1 = Entry(editor_branch1, width=30)
    fuel_returned_pms_branch1.grid(row=13, column=1)
    fuel_returned_ago_branch1 = Entry(editor_branch1, width=30)
    fuel_returned_ago_branch1.grid(row=13, column=3)

    
    # CREATING TOTAL SALES 

    #creating global variables for total sales
    global day_sale_liters_pms_branch1
    global day_sale_liters_ago_branch1

    day_sale_liters_pms_branch1 = 0
    day_sale_liters_ago_branch1 = 0

    total_sales_label = Label(editor_branch1, text="Total Sales (Liters)")
    total_sales_label.grid(row=14, column=0, pady=5, columnspan=4)

    total_sales_pms_label = Label(editor_branch1, text="PMS")
    total_sales_pms_label.grid(row=15, column=0, padx=10, pady=5)
    total_sales_ago_label = Label(editor_branch1, text="AGO")
    total_sales_ago_label.grid(row=15, column=2, padx=10)

    total_sales_result_pms_label = Label(editor_branch1, text=day_sale_liters_pms_branch1, borderwidth=3, relief="sunken")
    total_sales_result_pms_label.grid(row=15, column=1, padx=20, ipadx=87)
    total_sales_result_ago_label = Label(editor_branch1, text=day_sale_liters_ago_branch1, borderwidth=3, relief="sunken")
    total_sales_result_ago_label.grid(row=15, column=3, padx=20, ipadx=87)

    # RESTOCKING / DECHARGEMENT
    
    # Creating global variables for text box names
    global total_restock_liters_pms_branch1 #this variable will be used to keep track of the total liters restock for a particular day
    global total_restock_liters_ago_branch1

    total_restock_liters_pms_branch1 = 0
    total_restock_liters_ago_branch1 = 0

    # Creating Labels
    restocking_label = Label(editor_branch1, text="Dechargement")
    restocking_label.grid(row=16, column=0, columnspan=4, pady=(10,0))
    
    pms_label = Label(editor_branch1, text="PMS")
    pms_label.grid(row=17, column=0, columnspan=2, pady=(10,0))
    restock_branch_label = Label(editor_branch1, text="Branch")
    restock_branch_label.grid(row=18, column=0)
    restock_truck_label = Label(editor_branch1, text="Plaque")
    restock_truck_label.grid(row=19, column=0)
    restock_amount_label = Label(editor_branch1, text="Quantite (L)")
    restock_amount_label.grid(row=20, column=0)
    restock_total_label = Label(editor_branch1, text="Total (L)")
    restock_total_label.grid(row=21, column=0)
    restock_total_pms_label = Label(editor_branch1, text=total_restock_liters_pms_branch1, borderwidth=3, relief="sunken")
    restock_total_pms_label.grid(row=21, column=1, ipadx=87)

    ago_label = Label(editor_branch1, text="AGO")
    ago_label.grid(row=17, column=2, columnspan= 2, pady=(10,0))
    restock_branch_label = Label(editor_branch1, text="Branch")
    restock_branch_label.grid(row=18, column=2)
    restock_truck_label = Label(editor_branch1, text="Plaque")
    restock_truck_label.grid(row=19, column=2)
    restock_amount_label = Label(editor_branch1, text="Quantite (L)")
    restock_amount_label.grid(row=20, column=2)
    restock_total_label = Label(editor_branch1, text="Total (L)")
    restock_total_label.grid(row=21, column=2)
    restock_total_ago_label = Label(editor_branch1, text=total_restock_liters_ago_branch1, borderwidth=3, relief="sunken")
    restock_total_ago_label.grid(row=21, column=3, ipadx=87)

    # Creating text boxes
    # PMS
    restock_branch_source_pms_tbx = Entry(editor_branch1, width=30)
    restock_branch_source_pms_tbx.grid(row=18, column=1, padx=20)
    restock_truck_pms_tbx = Entry(editor_branch1, width=30)
    restock_truck_pms_tbx.grid(row=19, column=1)
    restock_amount_pms_tbx = Entry(editor_branch1, width=30)
    restock_amount_pms_tbx.grid(row=20, column=1)  
    # AGO
    restock_branch_source_ago_tbx = Entry(editor_branch1, width=30)
    restock_branch_source_ago_tbx.grid(row=18, column=3, padx=20)
    restock_truck_ago_tbx = Entry(editor_branch1, width=30)
    restock_truck_ago_tbx.grid(row=19, column=3)
    restock_amount_ago_tbx = Entry(editor_branch1, width=30)
    restock_amount_ago_tbx.grid(row=20, column=3)
    
    
    # Creating buttons for Restocking
    cancel_btn = Button(editor_branch1, text="Cancel", command=restockCancelFtn)
    cancel_btn.grid(row=22, column=0, columnspan=2, pady=10, ipadx=80)

    submit_btn = Button(editor_branch1, text="Submit", command=restockSubmitFtn)
    submit_btn.grid(row=22, column=2, columnspan=2, pady=10, ipadx=90)

    # payments
    
    #Creating buttons to launch the advanced and debt payments windows
    advance_payment_btn = Button(editor_branch1, text="Advance Payments", command=advancePaymentFtn)
    advance_payment_btn.grid(row=23,column=0, columnspan=3, pady=15, padx=5, ipadx=180)

    debt_payment_btn = Button(editor_branch1, text="Debt Payments", command=debtPaymentFtn)
    debt_payment_btn.grid(row=24,column=0, columnspan=3, pady=5, padx=5, ipadx=190)


#a Tkinter variable
#global variable
global clicked #will need its value for the editor_branch windows

clicked = StringVar()
clicked.set(branchList[0])

#creating a drop down widget
drop = OptionMenu(root, clicked, *branchList) #we have to put an asterik infront of options
drop.pack()

#creating a button widget for prompting user to go to selected branch
go_to_branch_btn = Button(root, text="Go to Branch", command=branchFtn).pack()


# Commit changes
conn.commit()

# Close connection
conn.close()

#creating the main GUI loop this has to be there in all GUIs
root.mainloop()