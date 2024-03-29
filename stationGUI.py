"""Petrol station database GUI"""
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import datetime
import re # used in regular expressios for storing and finding stringss
# I MAIN WINDOW

root = Tk() #this is the main window its also the first line to put when working with tkinter
root.title('Petrol Station GUI') #this is the title of the window
root.geometry("400x400") #specifying the size of the root window
#root.config(font=('Times', 15))


# GLOBAL FUNCTIONS

# a) lastIDFtn
global lastIDFtn 
def lastIDFtn(tblName, idName, databaseName, lastIDName):
    '''This function will return the lastIndex when provided with a table name, IDName, databaseName and the lastIndexName'''
    # Creating a database or connect to one
    conn = sqlite3.connect(databaseName)

    # Create a cursor
    c = conn.cursor()
            
    c.execute("SELECT {0} FROM {1} WHERE {0} IN (SELECT MAX({0}) FROM {1})".format(idName, tblName)) # MAX(dipID) ensures we only return results from the last id entered. Used string formating for the table name as placeholders are not allowed in sqlite for table and column names
                
    try:
        recordslst = list(c.fetchone()) #this will store all the records
    except TypeError:
        recordslst = [] # this will run when there are no entries in the tblName
        
    #print("Printing recordslst: ", recordslst) #this will print the records in the terminal

                            
    # Retrieving last index and assigning it to lastIDName
    try:
        lastIDName = int(recordslst[0])
        #print("Printing lastindexName: ", lastIDName)
    except IndexError:
        lastIDName = 0 #this means there are no other indexes
        #print("Printing lastIDName: ", lastIDName)
            
        # Commit changes
        conn.commit()

        # Close connection
        conn.close()

    return lastIDName
                

# b) function to retrieve list of customers
global custFtn
def custFtn(tblName, custName, databaseName, nameLst):
    '''This function provides the current list of customers when input the table name, customer name column, database name and nameLst'''
    
    # Creating a database or connect to one
    conn = sqlite3.connect(databaseName)

    # Create a cursor
    c = conn.cursor()
            
    c.execute("SELECT {} FROM {}".format(custName, tblName))
                
    recordsLst = c.fetchall() #this will store all the records
    #print("Printing recordsLst: ", recordsLst) #this will print the records in the terminal
    #print("Printing type: ", type(recordsLst))
              
    # Retrieving customer names and assigning nameLst
    for record in recordsLst:
        cName = record[0]
        nameLst.append(cName)
                
    #print("Printing nameLst: ", nameLst)
                       
    # Commit changes
    conn.commit()

    # Close connection
    conn.close()
            
    return nameLst


# c) prodFtn
global prodFtn
def prodFtn(tblName, prodName, databaseName, prodLst):
    '''This function will return the list of available products'''
    # Creating a database or connect to one
    conn = sqlite3.connect(databaseName)

    # Create a cursor
    c = conn.cursor()
            
    c.execute("SELECT {} FROM {}".format(prodName, tblName))
                
    recordsLst = c.fetchall() #this will store all the records
    #print("Printing recordsLst: ", recordsLst) #this will print the records in the terminal
    #print("Printing type: ", type(recordsLst))

               
    # Retrieving product names and assigning prodLst
    for record in recordsLst:
        pName = record[0]
        prodLst.append(pName)
                
    #print("Printing prodLst: ", prodLst)
                       
    # Commit changes
    conn.commit()

    # Close connection
    conn.close()
            
    return prodLst


# d) currSymbolFtn
global currSymbolFtn
def currSymbolFtn(tblName, currSymbol, databaseName, currSymbolLst):
    '''This function returns a list of currency symbols when provided the table name, currency symbol column, database, and currency symbol list name'''
    # Creating a database or connect to one
    conn = sqlite3.connect(databaseName)

    # Create a cursor
    c = conn.cursor()
            
    c.execute("SELECT {} FROM {}".format(currSymbol, tblName))
    
    recordsLst = c.fetchall() #this will store all the records
    #print("Printing recordsLst: ", recordsLst) #this will print the records in the terminal
    #print("Printing type: ", type(recordsLst))
                
    # Retrieving currency symbols and assigning currSymbolLst
    for record in recordsLst:
        cSymbol = record[0]
        currSymbolLst.append(cSymbol)
                
    #print("Printing currSymbolLst: ", currSymbolLst)
                       
    # Commit changes
    conn.commit()

    # Close connection
    conn.close()
            
    return currSymbolLst

# e) exRateIDFtn
global exRateIDFtn
def exRateIDFtn (tblName, customerID, branchID, databaseName, exchangeRate):
    '''This function returns the exchange rate ID list given exchange rate table, customerID, branchID,
    database name and exchange rate'''
    # Creating a database or connect to one
    conn = sqlite3.connect(databaseName)

    # Create a cursor
    c = conn.cursor()
            
    c.execute("SELECT exRateID FROM {0} WHERE (exRateAdvCustID = {1} OR exRateBranID = {2}) AND exRate = {3} ORDER BY exRateDate DESC".format(tblName, customerID, branchID, exchangeRate))
    
    recordsLst = list(c.fetchall()) #this will store all the records
    #print("Printing recordsLst: ", recordsLst) #this will print the records in the terminal
    #print("Printing type: ", type(recordsLst))
    exRateIDLst = []            
    for item in recordsLst:
        exRateID = item[0]
        exRateIDLst.append(exRateID) 
    #print("Printing exRateID: ", exRateID)
    #print("Printing exRateIDLst: ", exRateIDLst)
    # Commit changes
    conn.commit()

    # Close connection
    conn.close()
            
    return exRateIDLst

# f) lastOpeningLtrBalFtn
global lastOpeningLtrBalFtn

def lastOpeningLtrBalFtn(tblName, IDName, lastOpeningLtrBal, databaseName, customerID):
    '''This function will return the lastOpeningLtrBal given the table name, IDName, lastOpeningLtrBal, databaseName, customerID'''
    # Creating a database or connect to one
    conn = sqlite3.connect(databaseName)

    # Create a cursor
    c = conn.cursor()
            
    c.execute("SELECT {0} FROM {1} WHERE {2} = {3}".format(lastOpeningLtrBal, tblName, IDName, customerID)) 
                
    recordslst = list(c.fetchone()) #this will store all the records
    #print("Printing recordslst line 196 lastOpeningLtrBalFtn: ", recordslst) #this will print the records in the terminal

    # Retrieving last and assigning it to lastIDName
    lastOpeningLtrBal = 0.0
    try:
        lastOpeningLtrBal = float(recordslst[0])
        #print("Printing lastOpeningLtrBal from lastOpeningLtrBalFtn line 202: ", lastOpeningLtrBal)
    except IndexError:
        lastOpeningLtrBal = 0.0 #this means there are no previous entries
        #print("Printing lastOpeningLtrBal from lastOpeningLtrBalFtn line 205: ", lastOpeningLtrBal)
            
        # Commit changes
        conn.commit()

        # Close connection
        conn.close()

    return lastOpeningLtrBal


# f) lastCurrentLiterBalFtn
global lastCurrentLtrBalFtn 
def lastCurrentLtrBalFtn(tblName, IDName, lastCurrentLtrBal, databaseName, customerID):
    '''This function will return the lastCurrentLtrBal when provided with a table name, IDName, lastCurrentLtrBal, and databaseName
    The customerID is provided so be used in lastOpeningLtrBalFtn incase there are no lastcurrentltrbal'''
    # Creating a database or connect to one
    conn = sqlite3.connect(databaseName)

    # Create a cursor
    c = conn.cursor()
            
    c.execute("SELECT {0} FROM {1} WHERE advCustID = {2} ORDER BY {3} DESC".format(lastCurrentLtrBal, tblName, customerID, IDName)) # Used string formating for the table name as placeholders are not allowed in sqlite for table and column names
                
    try:
        recordslst = list(c.fetchone()) #this will store all the records
    except TypeError:
        recordslst = []
    #print("Printing recordslst line 232: ", recordslst) #this will print the records in the terminal

                            
    # Retrieving last liter balance and assigning it to lastCurrentLtrBal
    lastCurrentLtrBal = 0.0
    try:
        lastCurrentLtrBal = float(recordslst[0])
        #print("Printing lastCurrentLtrBal line 238: ", lastCurrentLtrBal)
    except IndexError: #this will mean there are no entries in the tblName
        if tblName == 'tblAdvCustDetails':
            tblName = 'tblAdvCust'
            IDName = 'advCustID'
            customerID = customerID
            lastOpeningLtrBal = 'advCustOpeningLtr'
            float_lastOpeningLtrBalFtn = float(lastOpeningLtrBalFtn(tblName, IDName, lastOpeningLtrBal, databaseName, customerID))
            #print("Printing float_lastOpeningLtrBalFtn line 247: ", float_lastOpeningLtrBalFtn)
            lastCurrentLtrBal = 0.0
            lastCurrentLtrBal += float_lastOpeningLtrBalFtn

        elif tblName == 'tblOneOffCustDetail':
            tblName = 'tblAdvCust'
            IDName = 'advCustID'
            customerID = customerID
            lastOpeningLtrBal = 'advCustOpeningLtr'
            float_lastOpeningLtrBalFtn = float(lastOpeningLtrBalFtn(tblName, IDName, lastOpeningLtrBal, databaseName, customerID))
            #print("Printing float_lastOpeningLtrBalFtn: ", type(float_lastOpeningLtrBalFtn))
            lastCurrentLtrBal = 0.0
            lastCurrentLtrBal += float_lastOpeningLtrBalFtn
        
        #print("Printing lastCurrentLtrBal line 262: ", lastCurrentLtrBal)
            
        # Commit changes
        conn.commit()

        # Close connection
        conn.close()

    return lastCurrentLtrBal

# DATABASE

# Creating a connection to a database
conn = sqlite3.connect('petrolstation.db')

# Create a cursor
c = conn.cursor()

# Getting branch values from table branches
branchList =[]
c.execute("SELECT branName FROM tblBran")

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

    # Retrieving and saving the previous Index
    
    # Creating a database or connect to one
    conn = sqlite3.connect('petrolstation.db')

    # Create a cursor
    c = conn.cursor()
    
    c.execute("SELECT *, oid FROM tblIndex WHERE indexDate IN (SELECT MAX(indexDate) FROM tblIndex)") #oid means include the default primary key. MAX(indexDate) ensures we only return results from the last date entered
    records = c.fetchall() #this will store all the records
    #print(records) #this will print the records in the terminal

    # Declare and initialize global variables
    global ClosingIndexLstBranch1
    global LastIndexIDLstBranch1
    global LastIndexIDBranch1

    ClosingIndexLstBranch1 = []
    LastIndexIDLstBranch1 = []
    LastIndexIDBranch1 = 0
    
    # Retrieving closing Index and assigning them to branch1ClosingIndexLst
    for record in records:
        index = record[6]
        #print("index: ", type(index), index)
        ClosingIndexLstBranch1.append(index)
        #print("closingIndexLst: ", type(closingIndexLst), closingIndexLst)

    #print("Printing closing Index List:\n", branch1ClosingIndexLst)

    # Retrieving the last IndexID from tblIndex
    for record in records:
        indexID = record[0]
        LastIndexIDLstBranch1.append(indexID)

    #print("Printing closing indexID List:\n", branch1LastIndexIDLst)
    try:
        LastIndexIDBranch1 = LastIndexIDLstBranch1[len(LastIndexIDLstBranch1)-1]
    except:
        LastIndexIDBranch1 = 0 #this means that there are no previous index 
    #print("Printing last IndexID: ", type(branch1LastIndexID), branch1LastIndexID)

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()

    # Creating submit function
    def indexSubmitFtn():
        global LastIndexID_branch1
        global total_day_pms_liters_branch1
        global total_day_ago_liters_branch1
        global currentDateBranch1
        global currentBranchIDBranch1

        currentDateBranch1 = ""
        currentBranchIDBranch1 = 1

        LastIndexID_branch1 = LastIndexIDBranch1
        # Creating a database or connect to one
        conn = sqlite3.connect('petrolstation.db')

        # Create a cursor
        c = conn.cursor()
    
        # Insert entered Index into tblIndex in the database

        # Using if/else to fill data for the three pumps without repetition
        # Closing Index values are taken from the branch1ClosingIndexLst
        
        total_day_pms_liters_branch1 = 0 #this variable will be used in calculating the total pms liters sold for a particular day
        total_day_ago_liters_branch1 = 0 #this variable will be used in calculating the total ago liters sold for a particular day
        
        currentDateBranch1 = date_editor_branch1.get()

        while len(ClosingIndexLstBranch1) > 0: #this ensures that all the Index are uploaded to the tblIndex
            if len(ClosingIndexLstBranch1) == 6:
                LastIndexID_branch1 += 1
                #print(LastIndexID_branch1)
                            
                c.execute("INSERT INTO tblIndex VALUES (:indexID, :indexDate, :indexBranID, :indexProdID, :indexPumpNumber, :openingIndex, :closingIndex)",
                    {
                        'indexID': LastIndexID_branch1,
                        'indexDate': date_editor_branch1.get(),
                        'indexBranID': 1,
                        'indexProdID': 1,
                        'indexPumpNumber': pump1_editor_branch1.get(),
                        'openingIndex': ClosingIndexLstBranch1[0],
                        'closingIndex': pump1_pms_editor_branch1.get()
                    })
                total_day_pms_liters_branch1 = (float(pump1_pms_editor_branch1.get()) - ClosingIndexLstBranch1[0])
                #print("Pump 1 PMS: ", branch1_total_day_pms_liters)
                ClosingIndexLstBranch1.pop(0)
                LastIndexID_branch1 += 1
                #print(LastIndexID_branch1)
            elif len(ClosingIndexLstBranch1) == 5:
                c.execute("INSERT INTO tblIndex VALUES (:indexID, :indexDate, :indexBranID, :indexProdID, :indexPumpNumber, :openingIndex, :closingIndex)",
                    {
                        'indexID': LastIndexID_branch1,
                        'indexDate': date_editor_branch1.get(),
                        'indexBranID': 1,
                        'indexProdID': 2,
                        'indexPumpNumber': pump1_editor_branch1.get(),
                        'openingIndex': ClosingIndexLstBranch1[0],
                        'closingIndex': pump1_ago_editor_branch1.get()
                    })
                total_day_ago_liters_branch1 = (float(pump1_ago_editor_branch1.get()) - ClosingIndexLstBranch1[0])
                #print("Pump 1 AGO: ", branch1_total_day_ago_liters)
                ClosingIndexLstBranch1.pop(0)
                LastIndexID_branch1 += 1
                #print(LastIndexID_branch1)
            elif len(ClosingIndexLstBranch1) == 4:
                c.execute("INSERT INTO tblIndex VALUES (:indexID, :indexDate, :indexBranID, :indexProdID, :indexPumpNumber, :openingIndex, :closingIndex)",
                    {
                        'indexID': LastIndexID_branch1,
                        'indexDate': date_editor_branch1.get(),
                        'indexBranID': 1,
                        'indexProdID': 1,
                        'indexPumpNumber': pump2_editor_branch1.get(),
                        'openingIndex': ClosingIndexLstBranch1[0],
                        'closingIndex': pump2_pms_editor_branch1.get()
                    })
                total_day_pms_liters_branch1 = total_day_pms_liters_branch1 + (float(pump2_pms_editor_branch1.get()) - ClosingIndexLstBranch1[0])
                ClosingIndexLstBranch1.pop(0)
                LastIndexID_branch1 += 1
                #print(LastIndexID_branch1)
            elif len(ClosingIndexLstBranch1) == 3:
                c.execute("INSERT INTO tblIndex VALUES (:indexID, :indexDate, :indexBranID, :indexProdID, :indexPumpNumber, :openingIndex, :closingIndex)",
                    {
                        'indexID': LastIndexID_branch1,
                        'indexDate': date_editor_branch1.get(),
                        'indexBranID': 1,
                        'indexProdID': 2,
                        'indexPumpNumber': pump2_editor_branch1.get(),
                        'openingIndex': ClosingIndexLstBranch1[0],
                        'closingIndex': pump2_ago_editor_branch1.get()
                    })
                total_day_ago_liters_branch1 = total_day_ago_liters_branch1 + (float(pump2_ago_editor_branch1.get()) - ClosingIndexLstBranch1[0])
                ClosingIndexLstBranch1.pop(0)
                LastIndexID_branch1 += 1
                #print(LastIndexID_branch1)
            elif len(ClosingIndexLstBranch1) == 2:
                c.execute("INSERT INTO tblIndex VALUES (:indexID, :indexDate, :indexBranID, :indexProdID, :indexPumpNumber, :openingIndex, :closingIndex)",
                    {
                        'indexID': LastIndexID_branch1,
                        'indexDate': date_editor_branch1.get(),
                        'indexBranID': 1,
                        'indexProdID': 1,
                        'indexPumpNumber': pump3_editor_branch1.get(),
                        'openingIndex': ClosingIndexLstBranch1[0],
                        'closingIndex': pump3_pms_editor_branch1.get()
                    })
                total_day_pms_liters_branch1 = total_day_pms_liters_branch1 + (float(pump3_pms_editor_branch1.get()) - ClosingIndexLstBranch1[0])
                ClosingIndexLstBranch1.pop(0)
                LastIndexID_branch1 += 1
                #print(LastIndexID_branch1)
            elif len(ClosingIndexLstBranch1) == 1:
                c.execute("INSERT INTO tblIndex VALUES (:indexID, :indexDate, :indexBranID, :indexProdID, :indexPumpNumber, :openingIndex, :closingIndex)",
                    {
                        'indexID': LastIndexID_branch1,
                        'indexDate': date_editor_branch1.get(),
                        'indexBranID': 1,
                        'indexProdID': 2,
                        'indexPumpNumber': pump3_editor_branch1.get(),
                        'openingIndex': ClosingIndexLstBranch1[0],
                        'closingIndex': pump3_ago_editor_branch1.get()
                    })
                total_day_ago_liters_branch1 = total_day_ago_liters_branch1 + (float(pump3_ago_editor_branch1.get()) - ClosingIndexLstBranch1[0])
                ClosingIndexLstBranch1.pop(0)
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

       
        # updating variables used in displaying the total pms and ago sales liters 
        day_sale_liters_pms_branch1 = total_day_pms_liters_branch1 
        day_sale_liters_ago_branch1 = total_day_ago_liters_branch1 

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
    
    
    # Creating fuelReturnedFtn function
    def fuelReturnedBranch1Ftn():
        '''This function creates a fuel returned window that is used in entering and updating fuel returned data'''
        # EDITOR_FUEL_RETURNED_BRANCH1 WINDOW

        # Creating a new window fuel returned
        global editor_fuel_returned_branch1 #need it to be global so that we can use editor.destroy 
        editor_fuel_returned_branch1 = Tk() #this is the main window its also the first line to put when working with tkinter
        editor_fuel_returned_branch1.title('Amorsage Place') #this is the title of the window
        editor_fuel_returned_branch1.geometry("400x260") #specifying the size of the root window

        
        # Retrieving and saving the previous fuel returned ID    
        # Declare and initialize global variables
        global LastReturnedFuelIDBranch1

        LastReturnedFuelIDBranch1 = 0
        
        lastIDFtn('tblReturnedFuel', 'returnedFuelID', 'petrolstation.db', LastReturnedFuelIDBranch1)

        
        # Creating fuelReturnedSubmit function
        def fuelReturnedSubmitFtn():
             # Declaring and initializing global variables and assigning them fuel returned from the returned fuel text box
            global total_fuel_returned_pms_branch1
            global total_fuel_returned_ago_branch1
            global currentLastReturnedFuelID
            global cummulative_fuel_returned_pms_branch1
            global cummulative_fuel_returned_ago_branch1 

            currentLastReturnedFuelID = LastReturnedFuelIDBranch1

            total_fuel_returned_pms_branch1 = 0
            total_fuel_returned_ago_branch1 = 0
            cummulative_fuel_returned_pms_branch1 = 0
            cummulative_fuel_returned_ago_branch1 = 0

                        
            # Updating the database
            # Using a while statement to loop through until we fill all entries i.e. pms and ago
            # Using an if/else statement to allow the correct identification of the product 
            entries = 4
            while entries > 0:
                if entries == 4:
                    #print("Entries before: ", entries)
                    entries -= 1
                    #print("Entries after: ", entries)

                    if fuel_returned_pump_pms.get() != "": #means we have an entry in the pms section
                        #print("Lastreturned fuel before: ",currentLastReturnedFuelID)
                        currentLastReturnedFuelID += 1 #adds one to the last returnedFuelID
                        #print("Lastreturned After: ", currentLastReturnedFuelID)
                        
                        # Creating a database or connect to one
                        conn = sqlite3.connect('petrolstation.db')

                        # Create a cursor
                        c = conn.cursor()
                        #print("this is pms 1")
                        # Updating the tblReturnedFuel table                    
                        c.execute("INSERT INTO tblReturnedFuel VALUES (:returnedFuelID, :returnedFuelDate, :returnedFuelBranID, :returnedFuelProdID, :returnedFuelPumpID, :returnedFuelLtr)",
                            {
                                'returnedFuelID': currentLastReturnedFuelID,
                                'returnedFuelDate': currentDateBranch1,
                                'returnedFuelBranID': 1,
                                'returnedFuelProdID': 1,
                                'returnedFuelPumpID': fuel_returned_pump_pms.get(),
                                'returnedFuelLtr': fuel_returned_pms_branch1.get()
                            })

                        # Commit changes
                        conn.commit()

                        # Close connection
                        conn.close()

                        continue
                
                elif entries == 3:
                    #print("Entries before: ", entries)
                    entries -= 1
                    #print("Entries after: ", entries)

                    if fuel_returned_pump_pms.get() == "": #means we don't have an entry in the pms section
                        #print("pms 2")                    
                        continue

                elif entries == 2:
                    #print("Entries before: ", entries)
                    entries -= 1
                    #print("Entries after: ", entries)

                    if fuel_returned_pump_ago.get() != "": #means there is an entry in the ago section

                        currentLastReturnedFuelID += 1 #adds one to the last returnedFuelID

                        # Creating a database or connect to one
                        conn = sqlite3.connect('petrolstation.db')

                        # Create a cursor
                        c = conn.cursor()
                        #print("ago 1")
                        # Updating the tblReturnedFuel table                      
                        c.execute("INSERT INTO tblReturnedFuel VALUES (:returnedFuelID, :returnedFuelDate, :returnedFuelBranID, :returnedFuelProdID, :returnedFuelPumpID, :returnedFuelLtr)",
                                {
                                    'returnedFuelID': currentLastReturnedFuelID,
                                    'returnedFuelDate': currentDateBranch1,
                                    'returnedFuelBranID': 1,
                                    'returnedFuelProdID': 2,
                                    'returnedFuelPumpID': fuel_returned_pump_ago.get(),
                                    'returnedFuelLtr': fuel_returned_ago_branch1.get()
                                })

                        # Commit changes
                        conn.commit()

                        # Close connection
                        conn.close()
                        
                        continue

                else: #means there is no entry  in the ago section
                    #print("ago 2")
                    #print("Entries before: ", entries)
                    entries -= 1
                    #print("Entries after: ", entries)
                    break
            
                        
            # Updating the total returned fuel label to show the actual returned fuel
            # Use try/except to ensure the program runs when there is an error due to empty string
                
            try: #this will run well where there is an input
                total_fuel_returned_pms_branch1 = float(fuel_returned_pms_branch1.get())
            except: #this will run when there is no input == empty string
                total_fuel_returned_pms_branch1 += 0
            
            try:
                total_fuel_returned_ago_branch1 = float(fuel_returned_ago_branch1.get())
            except:
                total_fuel_returned_ago_branch1 += 0

                      
            cummulative_fuel_returned_pms_branch1 += total_fuel_returned_pms_branch1
            cummulative_fuel_returned_ago_branch1 += total_fuel_returned_ago_branch1
                        
            total_fuel_returned_pms_label.config(text=cummulative_fuel_returned_pms_branch1)   
            total_fuel_returned_ago_label.config(text=cummulative_fuel_returned_ago_branch1)
            
            # updating variables used in displaying the total pms and ago sales liters when factoring total returned fuel
            day_sale_liters_pms_branch1 = total_day_pms_liters_branch1 - cummulative_fuel_returned_pms_branch1
            day_sale_liters_ago_branch1 = total_day_ago_liters_branch1 - cummulative_fuel_returned_ago_branch1
        
            # updating the total sales labels to update with the new values
            total_sales_result_pms_label.config(text=day_sale_liters_pms_branch1)
            total_sales_result_ago_label.config(text=day_sale_liters_ago_branch1)
            
            # Exiting the returned fuel window
            editor_fuel_returned_branch1.destroy()

        
        # Creating fuelReturnedCancel function
        def fuelReturnedCancelFtn():
            fuel_returned_pump_pms.delete(0, END)
            fuel_returned_pms_branch1.delete(0, END)
            fuel_returned_pump_ago.delete(0, END)
            fuel_returned_ago_branch1.delete(0, END)
            
        
        # Creating labels
        
        fuel_returned_pms_label = Label(editor_fuel_returned_branch1, text="PMS")
        fuel_returned_pms_label.grid(row=1, column=0, pady=5, columnspan=2)
        fuel_returned_pump_number_label = Label(editor_fuel_returned_branch1, text="Pump No.")
        fuel_returned_pump_number_label.grid(row=2, column=0)
        fuel_returned_liter_pms_label = Label(editor_fuel_returned_branch1, text="Liters")
        fuel_returned_liter_pms_label.grid(row=3, column=0)

        fuel_returned_pms_label = Label(editor_fuel_returned_branch1, text="AGO")
        fuel_returned_pms_label.grid(row=4, column=0, columnspan=2)
        fuel_returned_pump_number_label = Label(editor_fuel_returned_branch1, text="Pump No.")
        fuel_returned_pump_number_label.grid(row=5, column=0)
        fuel_returned_liter_ago_label = Label(editor_fuel_returned_branch1, text="Liters")
        fuel_returned_liter_ago_label.grid(row=6, column=0)
   
        # Creating text box
        fuel_returned_pump_pms = Entry(editor_fuel_returned_branch1, width=30)
        fuel_returned_pump_pms.grid(row=2, column=1)
        fuel_returned_pms_branch1 = Entry(editor_fuel_returned_branch1, width=30)
        fuel_returned_pms_branch1.grid(row=3, column=1)
        

        fuel_returned_pump_ago = Entry(editor_fuel_returned_branch1, width=30)
        fuel_returned_pump_ago.grid(row=5, column=1)
        fuel_returned_ago_branch1 = Entry(editor_fuel_returned_branch1, width=30)
        fuel_returned_ago_branch1.grid(row=6, column=1)
    
        # Creating buttons for Fuel Returned
        cancel_btn = Button(editor_fuel_returned_branch1, text="Cancel", command=fuelReturnedCancelFtn)
        cancel_btn.grid(row=7, column=0, pady=10, padx=(10,0), ipadx=40)

        submit_btn = Button(editor_fuel_returned_branch1, text="Submit", command=fuelReturnedSubmitFtn)
        submit_btn.grid(row=7, column=1, pady=10, padx=(10,0), ipadx=60)
  

    # Creating restockSubmit function
    # For interbranch supply, I need a way to calculate the fuel used for a branch so that I can determine the mainStockSupplyID
    def restockingBranch1Ftn():
        '''This function creates a restocking window that enables the manupulation of restocking data'''
        # EDITOR_RESTOCKING_BRANCH1 WINDOW

        # Creating a new window advance payments
        global editor_restocking_branch1 #need it to be global so that we can use editor.destroy 
        editor_restocking_branch1 = Tk() #this is the main window its also the first line to put when working with tkinter
        editor_restocking_branch1.title('Dechargement Place') #this is the title of the window
        editor_restocking_branch1.geometry("400x260") #specifying the size of the root window
                      
        
        #  I) Retrieving and saving the previous interBranchSupplyID
    
        # Declare and initialize global variables
        global LastInterBranchSupplyIDBranch1

        LastInterBranchSupplyIDBranch1 = 0
        
        lastIDFtn('tblInterBranSupply', 'interBranSupplyID', 'petrolstation.db', 'LastInterBranchSupplyIDBranch1')
        
        
        #  II) Retrieving and saving the previous mainSupplyToBranchID
    
        # Declare and initialize global variables
        global LastSupplyStockIDBranch1

        LastSupplyStockIDBranch1 = 0
        
        lastIDFtn('tblMainSupplyStockToBran', 'supplyStockID', 'petrolstation.db', 'LastSupplyStockIDBranch1')
        

        #  III) Determining the mainSupplyID for interbranch supplies
        # Will need to come up with a function that will compute the mainsupplyid for interbranch supplies
    

        #  IV) Determining the mainSupplyID for truck supplies
    
        def ComputeMainSupplyIDTruckSuppliesFtn(userDate, product, truckNo):
            '''This function returns the mainSupplyID given the date, product and truck number'''
            #print("UserDate: ", userDate)
            #print("UserProductIDAgo: ", product)
            #print("UserTruckNoAgo: ", truckNo)

            # Creating a database or connect to one
            conn = sqlite3.connect('petrolstation.db')

            # Create a cursor
            c = conn.cursor()
            
            c.execute("SELECT *, oid FROM tblMainSupplyStock WHERE ((mainSupplyDate = :UserDate OR mainSupplyDate < :UserDate) AND mainSupplyProdID = :UserProdID AND mainSupplyTruckNumber = :UserTruckNo)",
                    {
                        'UserDate': userDate,
                        'UserProdID': product,
                        'UserTruckNo': truckNo
                        
                    }) #finds data where a supply happened the samedate or later than the supply truck arrival date
            
            mainSupplyTruckRecords = c.fetchall() #this will store all the records
            #print("Printing mainSupplyTruckRecords: ", mainSupplyTruckRecords) #this will print the records in the terminal

            # Declare and initialize global variables
            global mainSupplyIDBranch1

            mainSupplyIDBranch1 = 0
            
            # Retrieving mainSupplyID and assigning it to mainSupplyIDBranch1
            for record in mainSupplyTruckRecords:
                id = record[0]
                mainSupplyIDBranch1 = id
                
            #print("Printing mainSupplyIDBranch1: ", mainSupplyIDBranch1)
            
            # Commit changes
            conn.commit()

            # Close connection
            conn.close()

            return mainSupplyIDBranch1


       
        # V) Creating restockSubmit function
        def restockSubmitFtn():
            '''This function updates the database with the provided restocking data'''
            # Declaring and initializing global variables 
            global total_supply_stock_pms_branch1
            global total_supply_stock_ago_branch1
            global currentLastSupplyStockIDBranch1
            global currentLastInterBranchSupplyIDBranch1
            global cummulative_restock_amount_pms_branch1
            global cummulative_restock_amount_ago_branch1

            currentLastInterBranchSupplyIDBranch1 = LastInterBranchSupplyIDBranch1
            currentLastSupplyStockIDBranch1 = LastSupplyStockIDBranch1

            total_supply_stock_pms_branch1 = 0
            total_supply_stock_ago_branch1 = 0
            cummulative_restock_amount_pms_branch1 = 0
            cummulative_restock_amount_ago_branch1 = 0

                        
            # Updating the database
            # Using a while statement to loop through until we fill all entries i.e. pms and ago
            # Using an if/else statement to allow the correct identification of the product 
            entries = 8
            while entries > 0:
                if entries == 8:
                    #print("Entries before: ", entries)
                    entries -= 1
                    #print("Entries after: ", entries)
                    '''
                    if restock_branch_source_pms_branch1.get() != "": #means we have an entry in the pms section
                        currentLastInterBranchSupplyIDBranch1 += 1 #adds one to the last returnedFuelID
                                                
                        # Creating a database or connect to one
                        conn = sqlite3.connect('petrolstation.db')

                        # Create a cursor
                        c = conn.cursor()
                        #print("this is pms 1")

                        # Updating the tblInterBranSupply table                    
                        c.execute("INSERT INTO tblInterBranSupply VALUES (:interBranSupplyID, :interBranSupplyDate, :interBranReceivingBranID, :interBranSupplyingBranID, :mainSupplyStockID, :interBranSupplyLtr)",
                            {
                                'interBranSupplyID': currentLastInterBranchSupplyIDBranch1,
                                'interBranSupplyDate': currentDateBranch1,
                                'interBranReceivingBranID': 1,
                                'interBranSupplyingBranID': restock_branch_source_pms_branch1.get(),
                                'mainSupplyStockID': fuel_returned_pump_pms.get(),
                                'interBranchSupplyLtr': restock_amount_pms_branch1.get()
                            })

                        # Commit changes
                        conn.commit()

                        # Close connection
                        conn.close()

                        continue'''
                
                elif entries == 7:
                    #print("Entries before: ", entries)
                    entries -= 1
                    #print("Entries after: ", entries)

                    if restock_branch_source_pms_branch1.get() == "": #means we don't have an entry in the pms section
                        #print("pms 2  branch")                    
                        continue

                elif entries == 6:
                    #print("Entries before: ", entries)
                    entries -= 1
                    #print("Entries after: ", entries)

                    if restock_truck_pms_branch1.get() != "": #means there is an entry in the pms truck section

                        currentLastSupplyStockIDBranch1 += 1 #adds one to the currentLastSupplyStockIDBranch1

                        # Creating a database or connect to one
                        conn = sqlite3.connect('petrolstation.db')

                        # Create a cursor
                        c = conn.cursor()
                        #print("pms 1 truck")

                        # Updating the tblMainSupplyStockToBranch table                      
                        c.execute("INSERT INTO tblMainSupplyStockToBran VALUES (:supplyStockID, :supplyStockDate, :mainSupplyID, :supplyStockLtr)",
                                {
                                    'supplyStockID': currentLastSupplyStockIDBranch1,
                                    'supplyStockDate': currentDateBranch1,
                                    'mainSupplyID': ComputeMainSupplyIDTruckSuppliesFtn(currentDateBranch1, 1, restock_truck_pms_branch1.get()),
                                    'supplyStockLtr': restock_amount_pms_branch1.get()
                                })

                        # Commit changes
                        conn.commit()

                        # Close connection
                        conn.close()
                        
                        continue

                elif entries == 5:
                    #print("Entries before: ", entries)
                    entries -= 1
                    #print("Entries after: ", entries)

                    if restock_truck_pms_branch1.get() == "": #means we don't have an entry in the pms section
                        #print("pms 2 truck")                    
                        continue

                if entries == 4:
                    #print("Entries before: ", entries)
                    entries -= 1
                    #print("Entries after: ", entries)
                    '''
                    if restock_branch_source_ago_branch1.get() != "": #means we have an entry in the pms section
                        currentLastInterBranchSupplyIDBranch1 += 1 #adds one to the last returnedFuelID
                                                
                        # Creating a database or connect to one
                        conn = sqlite3.connect('petrolstation.db')

                        # Create a cursor
                        c = conn.cursor()
                        #print("this is ago 1")

                        # Updating the tblInterBranSupply table                    
                        c.execute("INSERT INTO tblInterBranSupply VALUES (:interBranSupplyID, :interBranSupplyDate, :interBranReceivingBranID, :interBranSupplyingBranID, :mainSupplyStockID, :interBranSupplyLtr)",
                            {
                                'interBranSupplyID': currentLastInterBranchSupplyIDBranch1,
                                'interBranSupplyDate': currentDateBranch1,
                                'interBranReceivingBranID': 1,
                                'interBranSupplyingBranID': restock_branch_source_ago_branch1.get(),
                                'mainSupplyStockID': fuel_returned_pump_pms.get(),
                                'interBranSupplyLtr': restock_amount_ago_branch1.get()
                            })

                        # Commit changes
                        conn.commit()

                        # Close connection
                        conn.close()

                        continue'''
                
                elif entries == 3:
                    #print("Entries before: ", entries)
                    entries -= 1
                    #print("Entries after: ", entries)

                    if restock_branch_source_ago_branch1.get() == "": #means we don't have an entry in the pms section
                        #print("ago 2 branch")                    
                        continue

                elif entries == 2:
                    #print("Entries before: ", entries)
                    entries -= 1
                    #print("Entries after: ", entries)

                    if restock_truck_ago_branch1.get() != "": #means there is an entry in the pms truck section

                        currentLastSupplyStockIDBranch1 += 1 #adds one to the currentLastSupplyStockIDBranch1

                        # Creating a database or connect to one
                        conn = sqlite3.connect('petrolstation.db')

                        # Create a cursor
                        c = conn.cursor()
                        #print("ago 1 truck")

                        # Updating the tblMainSupplyStockToBranch table                      
                        c.execute("INSERT INTO tblMainSupplyStockToBran VALUES (:supplyStockID, :supplyStockDate, :mainSupplyID, :supplyStockLtr)",
                                {
                                    'supplyStockID': currentLastSupplyStockIDBranch1,
                                    'supplyStockDate': currentDateBranch1,
                                    'mainSupplyID': ComputeMainSupplyIDTruckSuppliesFtn(currentDateBranch1, 2, restock_truck_ago_branch1.get()),
                                    'supplyStockLtr': restock_amount_ago_branch1.get()
                                })

                        # Commit changes
                        conn.commit()

                        # Close connection
                        conn.close()
                        
                        continue

                else: #means there is no entry  in the ago truck section
                    #print("ago 2 truck")
                    #print("Entries before: ", entries)
                    entries -= 1
                    #print("Entries after: ", entries)

            # Updating the total returned fuel label to show the actual returned fuel
            # Use try/except to ensure the program runs when there is an error due to empty string
                
            try: #this will run well where there is an input
                total_supply_stock_pms_branch1 = float(restock_amount_pms_branch1.get())
            except: #this will run when there is no input == empty string
                total_supply_stock_pms_branch1 += 0.0
            
            try:
                total_supply_stock_ago_branch1 = float(restock_amount_ago_branch1.get())
            except:
                total_supply_stock_ago_branch1 += 0.0

                        
            cummulative_restock_amount_pms_branch1 += total_supply_stock_pms_branch1
            cummulative_restock_amount_ago_branch1 += total_supply_stock_ago_branch1
                        
            restock_total_pms_label.config(text=cummulative_restock_amount_pms_branch1)   
            restock_total_ago_label.config(text=cummulative_restock_amount_ago_branch1)
            
                       
            # Exiting the fuel restocking window
            editor_restocking_branch1.destroy()
    
        
        # Creating restockCancel function
        def restockCancelFtn():
            restock_branch_source_pms_branch1.delete(0, END)
            restock_truck_pms_branch1.delete(0, END)
            restock_amount_pms_branch1.delete(0, END)
            restock_branch_source_ago_branch1.delete(0, END)
            restock_truck_ago_branch1.delete(0, END)
            restock_amount_ago_branch1.delete(0, END)
        
        
        # Creating Labels
        #restocking_label = Label(editor_branch1, text="Dechargement")
        #restocking_label.grid(row=1, column=0, columnspan=4, pady=(10,0))
        
        pms_label = Label(editor_restocking_branch1, text="PMS")
        pms_label.grid(row=1, column=0, columnspan=2, pady=(10,0))
        restock_branch_label = Label(editor_restocking_branch1, text="Branch")
        restock_branch_label.grid(row=2, column=0)
        restock_truck_label = Label(editor_restocking_branch1, text="Plaque")
        restock_truck_label.grid(row=3, column=0)
        restock_amount_label = Label(editor_restocking_branch1, text="Quantite (L)")
        restock_amount_label.grid(row=4, column=0)
        

        ago_label = Label(editor_restocking_branch1, text="AGO")
        ago_label.grid(row=5, column=0, columnspan= 2, pady=(10,0))
        restock_branch_label = Label(editor_restocking_branch1, text="Branch")
        restock_branch_label.grid(row=6, column=0)
        restock_truck_label = Label(editor_restocking_branch1, text="Plaque")
        restock_truck_label.grid(row=7, column=0)
        restock_amount_label = Label(editor_restocking_branch1, text="Quantite (L)")
        restock_amount_label.grid(row=8, column=0)
        
        
        # Creating global variables (will be useful in entering data to db) and in the user entry text boxes
        global restock_branch_source_pms_branch1
        global restock_truck_pms_branch1
        global restock_amount_pms_branch1
        global restock_branch_source_ago_branch1
        global restock_truck_ago_branch1
        global restock_amount_ago_branch1


        # Creating text boxes
        # PMS
        restock_branch_source_pms_branch1 = Entry(editor_restocking_branch1, width=30)
        restock_branch_source_pms_branch1.grid(row=2, column=1, padx=20)
        restock_truck_pms_branch1 = Entry(editor_restocking_branch1, width=30)
        restock_truck_pms_branch1.grid(row=3, column=1)
        restock_amount_pms_branch1 = Entry(editor_restocking_branch1, width=30)
        restock_amount_pms_branch1.grid(row=4, column=1)  
        # AGO
        restock_branch_source_ago_branch1 = Entry(editor_restocking_branch1, width=30)
        restock_branch_source_ago_branch1.grid(row=6, column=1, padx=20)
        restock_truck_ago_branch1 = Entry(editor_restocking_branch1, width=30)
        restock_truck_ago_branch1.grid(row=7, column=1)
        restock_amount_ago_branch1 = Entry(editor_restocking_branch1, width=30)
        restock_amount_ago_branch1.grid(row=8, column=1)
       
       # Creating buttons for Restocking
        cancel_btn = Button(editor_restocking_branch1, text="Cancel", command=restockCancelFtn)
        cancel_btn.grid(row=9, column=0, pady=5, padx=(10,0), ipadx=40)

        submit_btn = Button(editor_restocking_branch1, text="Submit", command=restockSubmitFtn)
        submit_btn.grid(row=9, column=1, pady=5, padx=(10,0), ipadx=60)
    
    
    # Creating dipsBranch1Ftn function
    
    def dipsBranch1Ftn():
        # EDITOR_DIPS_BRANCH1 WINDOW

        # Creating a new window dips
        global editor_dips_branch1 #need it to be global so that we can use editor.destroy 
        editor_dips_branch1 = Tk() #this is the main window its also the first line to put when working with tkinter
        editor_dips_branch1.title('Jauge Place') #this is the title of the window
        editor_dips_branch1.geometry("500x200") #specifying the size of the root window
    
        
        # Creating dipsCancel function
        def dipsCancelFtn():
            dips_wholenumber_tank1_pms_branch1.delete(0, END)
            dips_numerator_tank1_pms_branch1.delete(0, END)
            dips_denominator_tank1_pms_branch1.delete(0, END)
            dips_wholenumber_tank1_ago_branch1.delete(0, END)
            dips_numerator_tank1_ago_branch1.delete(0, END)
            dips_denominator_tank1_ago_branch1.delete(0, END)
            dips_wholenumber_tank2_ago_branch1.delete(0, END)
            dips_numerator_tank2_ago_branch1.delete(0, END)
            dips_denominator_tank2_ago_branch1.delete(0, END)
        
        
         # Creating restockSubmitFtn function
        def dipsSubmitFtn():
            # Declaring and initializing global variables
            global cummulative_dips_pms_branch1
            global cummulative_dips_ago_branch1
            global total_dips_tank1_pms_branch1
            global total_dips_tank1_ago_branch1
            global total_dips_tank2_ago_branch1

            cummulative_dips_pms_branch1 = 0
            cummulative_dips_ago_branch1 = 0
            total_dips_tank1_pms_branch1 = 0
            total_dips_tank1_ago_branch1 = 0
            total_dips_tank2_ago_branch1 = 0

            # I) Function to compute the total dips per tank

            def DipsTotalFtn(wholenumber, numerator, denominator, multiplier):
                return (wholenumber*multiplier) + ((numerator/denominator)*multiplier)
            
            # II) Updating variables for the total and cummulative dip liters

            # PMS
            # Dealing with empty user inputs
            try:
                wholenumber_tank1_pms = float(dips_wholenumber_tank1_pms_branch1.get())
            except:
                wholenumber_tank1_pms = 0

            try: 
                numerator_tank1_pms = float(dips_numerator_tank1_pms_branch1.get())
            except:
                numerator_tank1_pms = 0

            try:
                denominator_tank1_pms = float(dips_denominator_tank1_pms_branch1.get())
            except:
                denominator_tank1_pms = 1

            total_dips_tank1_pms_branch1 = DipsTotalFtn(wholenumber_tank1_pms, numerator_tank1_pms, denominator_tank1_pms, 450)
            cummulative_dips_pms_branch1 = total_dips_tank1_pms_branch1
            
            # AGO
            # Dealing with empty user inputs
            try:
                wholenumber_tank1_ago = float(dips_wholenumber_tank1_ago_branch1.get())
            except:
                wholenumber_tank1_ago = 0

            try: 
                numerator_tank1_ago = float(dips_numerator_tank1_ago_branch1.get())
            except:
                numerator_tank1_ago = 0

            try:
                denominator_tank1_ago = float(dips_denominator_tank1_ago_branch1.get())
            except:
                denominator_tank1_ago = 1

            try:
                wholenumber_tank2_ago = float(dips_wholenumber_tank2_ago_branch1.get())
            except:
                wholenumber_tank2_ago = 0

            try: 
                numerator_tank2_ago = float(dips_numerator_tank2_ago_branch1.get())
            except:
                numerator_tank2_ago = 0

            try:
                denominator_tank2_ago = float(dips_denominator_tank2_ago_branch1.get())
            except:
                denominator_tank2_ago = 1

            total_dips_tank1_ago_branch1 = DipsTotalFtn(wholenumber_tank1_ago, numerator_tank1_ago, denominator_tank1_ago, 450)
            total_dips_tank2_ago_branch1 = DipsTotalFtn(wholenumber_tank2_ago, numerator_tank2_ago, denominator_tank2_ago, 450)
            cummulative_dips_ago_branch1 = total_dips_tank1_ago_branch1 + total_dips_tank2_ago_branch1


            # Updating the total dips labels to show the actual dips for the day
            dips_total_pms_label.config(text=cummulative_dips_pms_branch1)
            dips_total_ago_label.config(text=cummulative_dips_ago_branch1)


            # III) # Retrieving and saving the last DipID
            
            # Declare and initialize global variables
            global LastDipIDBranch1

            LastDipIDBranch1 = 0
            
            lastIDFtn('tblDip', 'dipID', 'petrolstation.db', LastDipIDBranch1)
            
                        
            # IV) Updating the tblDips in the Database

            # Using a while statement to loop through until we fill all entries i.e. pms and ago
            # Using an if/else statement to allow the correct identification of the product 
            
            global currentLastDipIDBranch1

            currentLastDipIDBranch1 = LastDipIDBranch1

            entries = 3
            while entries > 0:
                if entries == 3:
                    #print("Entries before: ", entries)
                    entries -= 1
                    #print("Entries after: ", entries)
                                  
                    currentLastDipIDBranch1 += 1 #adds one to the last dipID
                                                
                    # Creating a database or connect to one
                    conn = sqlite3.connect('petrolstation.db')

                    # Create a cursor
                    c = conn.cursor()
                    #print("this is pms 1")

                    # Updating the tblDip table                    
                    c.execute("INSERT INTO tblDip VALUES (:dipID, :dipDate, :dipBranID, :dipProdID, :dipTankID, :dipQty)",
                        {
                            'dipID': currentLastDipIDBranch1,
                            'dipDate': currentDateBranch1,
                            'dipBranID': 1,
                            'dipProdID': 1,
                            'dipTankID': 1,
                            'dipQty': total_dips_tank1_pms_branch1
                        })

                    # Commit changes
                    conn.commit()

                    # Close connection
                    conn.close()

                    continue
                
                elif entries == 2:
                    #print("Entries before: ", entries)
                    entries -= 1
                    #print("Entries after: ", entries)
                                  
                    currentLastDipIDBranch1 += 1 #adds one to the last dipID
                                                
                    # Creating a database or connect to one
                    conn = sqlite3.connect('petrolstation.db')

                    # Create a cursor
                    c = conn.cursor()
                    #print("this is ago 1")

                    # Updating the tblDip table                    
                    c.execute("INSERT INTO tblDip VALUES (:dipID, :dipDate, :dipBranID, :dipProdID, :dipTankID, :dipQty)",
                        {
                            'dipID': currentLastDipIDBranch1,
                            'dipDate': currentDateBranch1,
                            'dipBranID': 1,
                            'dipProdID': 2,
                            'dipTankID': 1,
                            'dipQty': total_dips_tank1_ago_branch1
                        })

                    # Commit changes
                    conn.commit()

                    # Close connection
                    conn.close()

                    continue

                else:
                    #print("Entries before: ", entries)
                    entries -= 1
                    #print("Entries after: ", entries)
                                  
                    currentLastDipIDBranch1 += 1 #adds one to the last dipID
                                                
                    # Creating a database or connect to one
                    conn = sqlite3.connect('petrolstation.db')

                    # Create a cursor
                    c = conn.cursor()
                    #print("this is ago 2")

                    # Updating the tblDip table                    
                    c.execute("INSERT INTO tblDip VALUES (:dipID, :dipDate, :dipBranID, :dipProdID, :dipTankID, :dipQty)",
                        {
                            'dipID': currentLastDipIDBranch1,
                            'dipDate': currentDateBranch1,
                            'dipBranID': 1,
                            'dipProdID': 2,
                            'dipTankID': 2,
                            'dipQty': total_dips_tank2_ago_branch1
                        })

                    # Commit changes
                    conn.commit()

                    # Close connection
                    conn.close()

            # V) Exiting the Dips Window
            editor_dips_branch1.destroy()
            
        
        # Creating Labels
                
        pms_label = Label(editor_dips_branch1, text="PMS")
        pms_label.grid(row=1, column=0, columnspan=6, pady=(10,0))
        dips_tank1_pms_label = Label(editor_dips_branch1, text="Tank 1")
        dips_tank1_pms_label.grid(row=2, column=0)
        dips_plus_label = Label(editor_dips_branch1, text=" + ")
        dips_plus_label.grid(row=2, column=2)
        dips_divide_label = Label(editor_dips_branch1, text=" / ")
        dips_divide_label.grid(row=2, column=4)
        

        ago_label = Label(editor_dips_branch1, text="AGO")
        ago_label.grid(row=3, column=0, columnspan=6, pady=(10,0))
        dips_tank1_ago_label = Label(editor_dips_branch1, text="Tank 1")
        dips_tank1_ago_label.grid(row=4, column=0)
        dips_plus_label = Label(editor_dips_branch1, text=" + ")
        dips_plus_label.grid(row=4, column=2)
        dips_divide_label = Label(editor_dips_branch1, text=" / ")
        dips_divide_label.grid(row=4, column=4)

        dips_tank2_ago_label = Label(editor_dips_branch1, text="Tank 2")
        dips_tank2_ago_label.grid(row=5, column=0)
        dips_plus_label = Label(editor_dips_branch1, text=" + ")
        dips_plus_label.grid(row=5, column=2)
        dips_divide_label = Label(editor_dips_branch1, text=" / ")
        dips_divide_label.grid(row=5, column=4)
        
        
        # Creating global variables (will be useful in entering data to db) and in the user entry text boxes
        global dips_wholenumber_tank1_pms_branch1
        global dips_numerator_tank1_pms_branch1
        global dips_denominator_tank1_pms_branch1
        global dips_wholenumber_tank1_ago_branch1
        global dips_numerator_tank1_ago_branch1
        global dips_denominator_tank1_ago_branch1
        global dips_wholenumber_tank2_ago_branch1
        global dips_numerator_tank2_ago_branch1
        global dips_denominator_tank2_ago_branch1


        # Creating text boxes
        # PMS
        dips_wholenumber_tank1_pms_branch1 = Entry(editor_dips_branch1, width=30)
        dips_wholenumber_tank1_pms_branch1.grid(row=2, column=1, padx=20)
        dips_numerator_tank1_pms_branch1 = Entry(editor_dips_branch1, width=10)
        dips_numerator_tank1_pms_branch1.grid(row=2, column=3)
        dips_denominator_tank1_pms_branch1 = Entry(editor_dips_branch1, width=10)
        dips_denominator_tank1_pms_branch1.grid(row=2, column=5)  
        # AGO
        dips_wholenumber_tank1_ago_branch1 = Entry(editor_dips_branch1, width=30)
        dips_wholenumber_tank1_ago_branch1.grid(row=4, column=1, padx=20)
        dips_numerator_tank1_ago_branch1 = Entry(editor_dips_branch1, width=10)
        dips_numerator_tank1_ago_branch1.grid(row=4, column=3)
        dips_denominator_tank1_ago_branch1 = Entry(editor_dips_branch1, width=10)
        dips_denominator_tank1_ago_branch1.grid(row=4, column=5)
        dips_wholenumber_tank2_ago_branch1 = Entry(editor_dips_branch1, width=30)
        dips_wholenumber_tank2_ago_branch1.grid(row=5, column=1, padx=20)
        dips_numerator_tank2_ago_branch1 = Entry(editor_dips_branch1, width=10)
        dips_numerator_tank2_ago_branch1.grid(row=5, column=3)
        dips_denominator_tank2_ago_branch1 = Entry(editor_dips_branch1, width=10)
        dips_denominator_tank2_ago_branch1.grid(row=5, column=5)    
       
       # Creating buttons for Restocking
        cancel_btn = Button(editor_dips_branch1, text="Cancel", command=dipsCancelFtn)
        cancel_btn.grid(row=6, column=0, columnspan=3, pady=10, padx=(10,0), ipadx=40)

        submit_btn = Button(editor_dips_branch1, text="Submit", command=dipsSubmitFtn)
        submit_btn.grid(row=6, column=3, columnspan=3, pady=10, padx=(10,0), ipadx=60)
    
    
           
    # Creating debtPaymentFtn function
    def debtPaymentFtn():
        '''This function launches the debt payment window which is used in entering debt payment data'''
        # EDITOR_DEBT_PAYMENT_BRANCH1 WINDOW

        # Creating a new window Debt Payment
        global editor_debt_payment_branch1 #need it to be global so that we can use editor.destroy 
        editor_debt_payment_branch1 = Tk() #this is the main window its also the first line to put when working with tkinter
        editor_debt_payment_branch1.title('Debt Payment Place') #this is the title of the window

        
        # FUNCTIONS
        # Function for providing credit customer ID given customer name
        def credCustIDFtn():
            '''This function returns a credit customer ID given the customer name'''
            # getting customer name from cred_cust_combo
            cred_cust_name = cred_cust_combo.get()

            # Querying the credit customer table to find customer ID 
            # Creating a database or connect to one
            conn = sqlite3.connect('petrolstation.db')

            # Create a cursor
            c = conn.cursor()
            
            c.execute("SELECT credCustID FROM tblCredCust WHERE credCustName = :cred_cust_name", 
                      {
                          'cred_cust_name': cred_cust_name
                      }) 
            
            credCustIDRecords = c.fetchall() #this will store all the records
            #print("Printing credCustIDRecords: ", credCustIDRecords) #this will print the records in the terminal
            #print("Printing credCustIDRecords type: ", type(credCustIDRecords))

            global cred_custID
            
            try:
                credit_customer_ID = credCustIDRecords[0]
            except:
                credit_customer_ID = ''

            credit_customer_ID_str = ''.join(map(str,(credit_customer_ID))) #converting credit_customer_ID tuple to string then int
        
            cred_custID = credit_customer_ID_str
            
            # Commit changes
            conn.commit()

            # Close connection
            conn.close()
            
            #print("Printing cred_custID type: ", type(cred_custID))
            return cred_custID

        
        # Function to retrieve applicable exchange rate
        def credExRateFtn(cred_custID, branchID):
            '''This function should check the tblExRate and provide the client rate or the branch rate'''

            # Creating a database or connect to one
            conn = sqlite3.connect('petrolstation.db')

            # Create a cursor
            c = conn.cursor()
            
            c.execute("SELECT exRateID, exRate FROM tblExRate WHERE (exRateCredCustID = :cred_custID OR exRateBranID = :branchID)",
                      {
                          'cred_custID': cred_custID,
                          'branchID': branchID
                      })
            
            global exRateRecords
            exRateRecords = []

            exRateRecords = c.fetchall() #this will store all the records
            #print("Printing exRateRecords: ", exRateRecords) #this will print the records in the terminal
                                  
            # Commit changes
            conn.commit()

            # Close connection
            conn.close()

            # getting exRates only
            global exRateLstCredCust
            exRateLstCredCust = []
            for record in exRateRecords:
                rate = record[1]
                exRateLstCredCust.append(rate)
            
            return exRateLstCredCust
               
       
        # combinded function 
        def combinedCustIDExRate(e):
            '''This function listens for an event and returns the applicable exchange rate for the respective credit customer'''
            if cred_cust_combo.get() != cred_cust_name: 
                cred_pay_exrate_combo.config(values=credExRateFtn(credCustIDFtn(),1))  
        

        # clear payment function
        def clearPaymentFtn():
            '''This function clears the payment amount text boxes'''
            cred_pay_dollar_branch1.delete(0,END)
            cred_pay_cdf_branch1.delete(0,END)
        
        
        # Add payment function
        def addPaymentFtn():
            '''This function will get entries and add their values to the TreeView'''
                                  
            # Retriving the curreny symbols
            currSymbolLst = []
            currSymbolLst = currSymbolFtn('tblCurr', 'currSymbol', 'petrolstation.db', currSymbolLst)
           
            # Retriving the debt payment list                       
            global debt_pay_items_lst_branch1

            # use a while statement to loop thro' 
            entries = 2
            while entries > 0:
                if entries == 2:
                    if cred_pay_dollar_branch1.get() != '':
                        customer_ID = cred_custID
                        customer_name = cred_cust_combo.get()
                        debt_pay_date = date_editor_branch1.get() #currentDateBranch1
                        currency_symbol = currSymbolLst[0]
                        debt_pay_amount = f'{float(cred_pay_dollar_branch1.get()):,.2f}'
                        exchange_rate = cred_pay_exrate_combo.get()
                        debt_pay_item = [customer_ID,customer_name,debt_pay_date,currency_symbol,debt_pay_amount,exchange_rate]
                        cred_pay_tree.insert('',END, values=debt_pay_item) #this inserts the debt_pay_item into the end of the treeview
                                                
                        cred_pay_dollar_branch1.delete(0,END) # clears the dollar entry
                        
                        debt_pay_items_lst_branch1.append(debt_pay_item)

                        entries -= 1

                    else:
                        entries -= 1
                else:
                    if cred_pay_cdf_branch1.get() != '':
                        customer_ID = cred_custID
                        customer_name = cred_cust_combo.get()
                        debt_pay_date = date_editor_branch1.get() #currentDateBranch1
                        currency_symbol = currSymbolLst[1]
                        debt_pay_amount = f'{float(cred_pay_cdf_branch1.get()):,.0f}'
                        exchange_rate = cred_pay_exrate_combo.get()
                        debt_pay_item = [customer_ID,customer_name,debt_pay_date,currency_symbol,debt_pay_amount,exchange_rate]
                        cred_pay_tree.insert('',END, values=debt_pay_item)
                                                
                        cred_pay_cdf_branch1.delete(0,END) # clears the cdf entry
                        
                        debt_pay_items_lst_branch1.append(debt_pay_item)

                        entries -= 1
                    else:
                        entries -= 1

            #print("Printing debt_pay_items_lst_branch1 after adding item: ", debt_pay_items_lst_branch1)

        
        # cancelPayment function
        def debtPayCancelFtn():
            '''This function clears all the fields'''
            clearPaymentFtn()

            # clearing everything from Treeview
            cred_pay_tree.delete(*cred_pay_tree.get_children()) # * means all. get.children() will get all the children in each item 

            # clearing debt_pay_items_lst_branch1
            global debt_pay_items_lst_branch1
            #print("Printing debt_pay_items_lst_branch1 before canceling: ", debt_pay_items_lst_branch1)
            debt_pay_items_lst_branch1.clear()
            #print("Printing debt_pay_items_lst_branch1 after canceling: ", debt_pay_items_lst_branch1)
            
        # debtRemoveSelected function
        def debtRemoveSelectedFtn():
            ''''This function will remove all the selected records in the Treeview'''
            # declaring and initializing a variable to keep track of selected items
            removed_records_lst = cred_pay_tree.selection() # selection() returns a list of treeview indexes of selected items
            #print('Printing removed records lst: ', removed_records_lst)

            # Defining and initializing a list to store the treeview values of removed items
            tree_removed_records_lst = []

            # Retrieving the treeview values of removed records
            tree_removed_records_lst = [list(cred_pay_tree.item(record, 'values')) for record in removed_records_lst] #tree.item(index,'values') will return the values of the tree item with the specified index
            # list(cred_pay_tree.item(record, 'values')) ensures that the values are wrapped in a list instead of having a list of tupples

            #print("Printing tree_remeoved_records_lst: ", tree_removed_records_lst)                  
            # updating the debt payment details list to exclude the removed items
            global debt_pay_items_lst_branch1
            #print("Printing debt_pay_items_lst_branch1 before removing: ", debt_pay_items_lst_branch1)
            for item in tree_removed_records_lst:
                #print("Printing item: ", item)
                if item in debt_pay_items_lst_branch1: # check if the item is in the list
                    debt_pay_items_lst_branch1.remove(item) # remove it from the list


            #print("Printing Debt payment list After removal: ", debt_pay_items_lst_branch1)
            
            # removing selected records in treeview
            x = cred_pay_tree.selection() 
            for record in x:
                #print('Printing index: ', record)
                #print('Printing treeview values of removed items: ', cred_pay_tree.item(record))
                cred_pay_tree.delete(record) #will remove each selected record
            
          
        # debtPaySubmit function
        def debtPaySubitFtn():
            '''This function will update the database with the credit customer payment details'''

            # a) Retrieve the last debt payment ID and saving last debt payment ID 
            lastDebtPayID = 0           
            lastDebtPayID = lastIDFtn('tblDebtPay', 'debtPayID', 'petrolstation.db', lastDebtPayID)
            print("Printing lastDebtPayID after lastIDFtn: ", lastDebtPayID)

            # Declaring and assigning currentDebtPayID
            try:
                currentLastDebtPayID = lastDebtPayID
            except:
                currentLastDebtPayID = 0 #this will apply when there are no previous records

            #print("Printing currentLastDebtPayID: ", currentLastDebtPayID)
                
            # b) Updating the database with the provided debt payment data
            # debt_pay_item = [customer_ID,customer_name,debt_pay_date,currency_symbol,debt_pay_amount,exchange_rate]
            
            # Declaring and initializing variales for keeping track of total amount paid
            total_debt_dollar_payment = 0
            total_debt_cdf_payment = 0
            
            for item in debt_pay_items_lst_branch1:
                           
                # ensuring we have a unique currentLastDebtPayID for every entry
                currentLastDebtPayID += 1
                #print("Printing currentLastDebtPayID after + 1: ", currentLastDebtPayID)

                # I) Retrieving the debtPayExRateID
                #print("Printing exRateLstCredCust: ", exRateLstCredCust)
                exchangeRateIndex = exRateLstCredCust.index(int(item[5]))
                #print("Printing exchangeRateIndex: ", exchangeRateIndex)
                idRecord = exRateRecords[exchangeRateIndex]
                #print("Printing idRecord: ", idRecord)
                id = idRecord[0]
                #print("Printing id: ", id)
                
                # II) Retriving the curreny symbols
                currSymbolLst = []
                currSymbolLst = currSymbolFtn('tblCurr', 'currSymbol', 'petrolstation.db', currSymbolLst)
                
                # III) Updating the Debt Payment table
                # Creating a database or connect to one
                conn = sqlite3.connect('petrolstation.db')

                # Create a cursor
                c = conn.cursor()
                
                # Updating the tblDebtPay table                
                c.execute("INSERT INTO tblDebtPay VALUES (:debtPayID, :debtPayDate, :debtPayBranID, :credCustID, :debtPayCurrID, :debtPayAmt, :debtPayExRateID)",
                    {
                        'debtPayID': currentLastDebtPayID,
                        'debtPayDate': item[2],
                        'debtPayBranID': 1,
                        'credCustID': item[0],
                        'debtPayCurrID': currSymbolLst.index(item[3]) + 1, #index returns the index of the first occurence of the thing being searched for. we add 1 since list index starts with 0
                        'debtPayAmt': item[4],
                        'debtPayExRateID': id
                    })

                # Commit changes
                conn.commit()

                # Close connection
                conn.close()


                # IV) Keeping track of the total amount of money paid
                # using a while and an if/else to differenciate the currencies
                print("Printing item: ", item)
                entries = 2
                while entries > 0:
                    if item[3] == '$':
                        total_debt_dollar_payment += float(item[4].replace(',',''))
                        print("Printing total_debt_dollar_payment: ", total_debt_dollar_payment)
                        item[3] = ''
                        entries -= 1
                    elif item[3] == 'CDF':
                        total_debt_cdf_payment += int(item[4].replace(',',''))
                        print("Printing total_debt_cdf_payment: ", total_debt_cdf_payment)
                        item[3] = ''
                        entries -= 1
                    else:
                        entries -= 1
                           
                # V) Updating the credit customer details table with the debt payment data
                
                # Retrieving last credit customer detail ID
                lastCredCustDetailID = 0
                lastCredCustDetailID = lastIDFtn('tblCredCustDetails', 'credCustDetailID', 'petrolstation.db', lastCredCustDetailID)

                # Declaring and assigning currentDebtPayID
                try:
                    currentLastCredCustDetailID = lastCredCustDetailID
                except:
                    currentLastCredCustDetailID = 0 #this will apply when there are no previous records

                currentLastCredCustDetailID += 1

                # Creating a database or connect to one
                conn = sqlite3.connect('petrolstation.db')

                # Create a cursor
                c = conn.cursor()
                
                # Updating the tblCredCustDetail table                    
                c.execute("INSERT INTO tblCredCustDetails VALUES (:credCustDetailID, :credCustID, :credCustProdID, :credCustCurrID, :credCustPrice, :credCustPriceDate, :saleID, :indirectCustID, :debtPayID, :credCustCurrentBal, :credCustCurrentBalDate)",
                          {
                              'credCustDetailID': currentLastCredCustDetailID,
                              'credCustID': item[0],
                              'credCustProdID': 'NULL',
                              'credCustCurrID': 'NULL',
                              'credCustPrice': 'NULL',
                              'credCustPriceDate': 'NULL',
                              'saleID': 'NULL',
                              'indirectCustID': 'NULL',
                              'debtPayID': currentLastDebtPayID,
                              'credCustCurrentBal': 'NULL',
                              'credCustCurrentBalDate': 'NULL'
                          })

                # Commit changes
                conn.commit()

                # Close connection
                conn.close()
                

                # VI) Clear all text boxes and the treeview
                debtPayCancelFtn()

            # c) Updating the cummulative payments label 
            global total_cummulative_dollar_payments_branch1
            global total_cummulative_cdf_payments_branch1

            if total_debt_dollar_payment != 0:
                total_cummulative_dollar_payments_branch1 = total_cummulative_dollar_payments_branch1 + total_debt_dollar_payment
            else:
                total_cummulative_dollar_payments_branch1 = total_cummulative_dollar_payments_branch1
                
            if total_debt_cdf_payment != 0:    
                total_cummulative_cdf_payments_branch1 = total_cummulative_cdf_payments_branch1 + total_debt_cdf_payment
            else:
                total_cummulative_cdf_payments_branch1 = total_cummulative_cdf_payments_branch1

            print("Printing total_cummulative_dollar_payments_branch1: ", total_cummulative_dollar_payments_branch1)
            print("Printing total_cummulative_cdf_payments_branch1: ", total_cummulative_cdf_payments_branch1)
            
            cummulative_dollar_payments_branch1.config(text=total_cummulative_dollar_payments_branch1)
            cummulative_cdf_payments_branch1.config(text=total_cummulative_cdf_payments_branch1)    

            # d) close debt pay window
            editor_debt_payment_branch1.destroy()


        # MAIN FRAME
        frame = Frame(editor_debt_payment_branch1)
        frame.pack()

        # creating labels
        cred_cust_name_label = Label(frame, text="Customer Name")
        cred_cust_name_label.grid(row=0, column=0)
        dollar_sign_label = Label(frame, text=" $ ")
        dollar_sign_label.grid(row=0, column=1)
        cdf_sign_label = Label(frame, text="CDF")
        cdf_sign_label.grid(row=0, column=2)
        exRate_label    = Label(frame, text="Exchange Rate")
        exRate_label.grid(row=0, column=3)

        #global               
        global cred_cust_name         
        cred_cust_name = ""

        global credCustLst
        credCustLst = []

        # creating combobox
        cred_cust_combo = ttk.Combobox(frame, values=custFtn('tblCredCust', 'credCustName','petrolstation.db', credCustLst))
        cred_cust_combo.grid(row=1, column=0)
        cred_cust_combo.current(0) #this sets the first value as the default
        cred_cust_combo.bind('<<ComboboxSelected>>', combinedCustIDExRate) #binding tires this combobox to another action. <<ComboboxSelected>> is the binding and credCustIDFtn() is the action to be taken when the binding occurs

        # creating text box
        cred_pay_dollar_branch1 = Entry(frame, width=30)
        cred_pay_dollar_branch1.grid(row=1, column=1)
        cred_pay_cdf_branch1 = Entry(frame, width=30)
        cred_pay_cdf_branch1.grid(row=1, column=2)

        # creating combobox
        cred_pay_exrate_combo = ttk.Combobox(frame, values=[""])
        cred_pay_exrate_combo.current(0) #setting default value
        cred_pay_exrate_combo.grid(row=1, column=3)
        
        
        # Declare and initialize variable for storing debt payment details
        global debt_pay_items_lst_branch1
        debt_pay_items_lst_branch1 = []

        # creating button
        cred_pay_addpayment_btn = Button(frame, text="Add Payment", command=addPaymentFtn)
        cred_pay_addpayment_btn.grid(row=2, column=3, pady=5)

        # TREEVIEW FRAME
        treeview_frame = Frame(frame)
        treeview_frame.grid(row=3, column=0, columnspan=4, padx=20, pady=10)
        
        # creating treeview scrollbar
        tree_scroll = Scrollbar(treeview_frame)
        tree_scroll.pack(side=RIGHT, fill=Y) #fill=Y means it scroll vertically
        
        # add some style
        style = ttk.Style()

        # pick a theme
        style.theme_use('default')

        # creating Treeview
        columns = ["credCustID", "credCustName", "debtPayDate", "currSymbol", "debtPayAmt", "debtPayExRateID"]
        cred_pay_tree = ttk.Treeview(treeview_frame, yscrollcommand=tree_scroll.set, columns=columns, show="headings")
        cred_pay_tree.pack()
        
        # configure scrollbar
        tree_scroll.config(command=cred_pay_tree.yview)
        
        cred_pay_tree.heading('credCustID', text='CustomerID')
        cred_pay_tree.heading('credCustName', text='Customer Name')
        cred_pay_tree.heading('debtPayDate', text='Date')
        cred_pay_tree.heading('currSymbol', text='Currency Symbol')
        cred_pay_tree.heading('debtPayAmt', text='Amount')
        cred_pay_tree.heading('debtPayExRateID', text='Exchange Rate')

       
        # THIRD FRAME
        button_frame = Frame(frame)
        button_frame.grid(row=4, column=0, columnspan=4, pady=(10,10), sticky="news", padx=20)
        
        # creating buttons
        remove_selected = Button(button_frame, text="Remove Selected", command=debtRemoveSelectedFtn)
        remove_selected.grid(row=0, column=0, padx=10, ipadx=160)
        
        cancel_btn = Button(button_frame, text="Cancel", command=debtPayCancelFtn)
        cancel_btn.grid(row=0, column=1, padx=10, ipadx=160)

        submit_btn = Button(button_frame, text="Submit", command=debtPaySubitFtn)
        submit_btn.grid(row=0, column=2, padx=10, ipadx=160)

       # DATA QUALITY CHECK
        # Ensuring any user input in the cdf text box is divisible by 50; there lowest denomination
        """ if cred_pay_cdf_branch1.get() != '':
            print("Printing the cred_pay if statement running: ")
            if cred_pay_cdf_branch1.get().isnumeric() == 'false':
                print("Printing isnumeric ran: ")
                messagebox.showwarning("This is a warning!", "Enter a number") #this method has two arguements: Title and message
                cred_pay_cdf_branch1.delete(0,END)
            elif cred_pay_cdf_branch1.get() % 50 != 0:
                messagebox.showwarning("This is a warning!", "Enter a number that is divisible by 50")
                cred_pay_cdf_branch1.delete(0,END)
            else:
                print("code ok") """
    
    # Creating advancePaymentFtn function
    def advancePaymentFtn():
        '''This function launches an advanced payment window which is used in entering advanced payment data'''
        # EDITOR_ADVANCE_PAYMENT_BRANCH1 WINDOW

        # Creating a new window advance payments
        global editor_advance_payment_branch1 #need it to be global so that we can use editor.destroy 
        editor_advance_payment_branch1 = Tk() #this is the main window its also the first line to put when working with tkinter
        editor_advance_payment_branch1.title('Enter Advance Payments Data') #this is the title of the window
        #editor_advance_payment_branch1.geometry("700x700") #specifying the size of the root window

        # FUNCTIONS 
        
        # a) advaPrice
        def advaPriceFtn(event):
            '''This function returns a list of price ptions based on the customer name, product and currency with the the 
            user being able to input a different price if its not among the provided options'''
            
            global prodLst
            #print('Printing prodLst: ', prodLst)

            # Retriving the curreny symbols
            currSymbolLst = []
            currSymbolLst = currSymbolFtn('tblCurr', 'currSymbol', 'petrolstation.db', currSymbolLst)

            # Get values from the other combo boxes
            customerName = adva_cust_combo.get()
            #print("Printing customerName: ", customerName)
            product = adva_prod_combo.get()
            #print('Printing product: ', product)
            #print('Printing int(prodLst.index(product)) + 1:', int(prodLst.index(product)) + 1)
            currency = adva_curr_combo.get()
            #print('Printing currency:', currency)
            #print('Printing int(currSymbolLst.index(currency)) + 1: ', int(currSymbolLst.index(currency)) + 1)
            try:
                productID = int(prodLst.index(product)) + 1 
            except ValueError:
                productID = None

            try:
                currencyID = int(currSymbolLst.index(currency)) + 1
            except ValueError:
                currencyID = None

            # Query the advance customer table for available prices for this client
            # Connect to database
            conn = sqlite3.connect('petrolstation.db')
            
            # Create cursor
            c = conn.cursor()

            # Querying database
            c.execute("SELECT tblAdvCust.advCustOpeningLtrPrice, tblAdvPay.advPayProdPrice FROM tblAdvCust FULL JOIN tblAdvPay ON tblAdvCust.advCustID = tblAdvPay.advCustID WHERE ((tblAdvCust.advCustName = :customerName) AND (tblAdvCust.advCustProdID = :productID OR tblAdvPay.advPayProdID = :productID) AND (tblAdvCust.advCustOpeningPriceCurrID = :currency OR tblAdvPay.advPayCurrID = :currency))", 
                      {
                          "customerName": customerName, 
                          "productID": productID, 
                          "currency": currencyID
                      })

                                  
            recordsLst = c.fetchall()
            #print("Printing recordsLst: ", recordsLst)
            
            # Commit changes
            conn.commit()

            # Close connection
            conn.close()
            
            advaPriceLst = []
            for record in recordsLst:
                advaOp = record[0]
                advaPr = record[1]

                # use if/else to ensure we don't include duplicates
                if advaOp != advaPr:
                    advaPriceLst.append(advaOp)
                    advaPriceLst.append(advaPr)
                else:
                    advaPriceLst.append(advaOp)
            
            #print('Printing advaPriceLst: ', advaPriceLst)    
            adva_price_combo.config(values=advaPriceLst)


        # b) advaExRateFtn
        def advaExRateFtn(event):
            '''This function returns a list of exchange rates based on the customer name, product, currency 
            and price with the the  user being able to input a different exchange rate if its not among the provided options'''
            # Get values from the other combo boxes
            customerName = adva_cust_combo.get()
            #print("Printing customerName: ", customerName)
            product = adva_prod_combo.get()
            #print('Printing product: ', product)
            #print('Printing int(prodLst.index(product)) + 1:', int(prodLst.index(product)) + 1)
            currency = adva_curr_combo.get()
            #print('Printing currency:', currency)
            #print('Printing int(currSymbolLst.index(currency)) + 1: ', int(currSymbolLst.index(currency)) + 1)
            price = adva_price_combo.get()
            #print("Printing price: ", price)
            # Retriving the curreny symbols
            currSymbolLst = []
            currSymbolLst = currSymbolFtn('tblCurr', 'currSymbol', 'petrolstation.db', currSymbolLst)

            try:
                productID = int(prodLst.index(product)) + 1 
            except ValueError:
                productID = None

            try:
                currencyID = int(currSymbolLst.index(currency)) + 1
            except ValueError:
                currencyID = None

            try:
                customerID = int(advaCustLst.index(customerName)) + 1
            except ValueError:
                customerID = None

            # Connect to database
            conn = sqlite3.connect('petrolstation.db')
            
            # Create cursor
            c = conn.cursor()

            # Querying database
            c.execute("SELECT tblAdvCust.advCustOpeningExRate, tblExRate.exRate FROM tblAdvCust FULL JOIN tblAdvPay ON tblAdvCust.advCustID = tblAdvPay.advCustID FULL JOIN tblExRate ON tblAdvPay.advPayExRateID = tblExRate.exRateID WHERE ((tblAdvCust.advCustName = :customerName  OR tblAdvPay.advCustID = :customerID) AND (tblAdvCust.advCustProdID = :productID OR tblAdvPay.advPayProdID = :productID) AND (tblAdvCust.advCustOpeningPriceCurrID = :currency OR tblAdvPay.advPayCurrID = :currency) AND (tblAdvCust.advCustOpeningLtrPrice = :price OR tblAdvPay.advPayProdPrice = :price))", 
                      {
                          "customerName": customerName,
                          "customerID": customerID, 
                          "productID": productID, 
                          "currency": currencyID,
                          "price": price
                      })                
           
            recordsExRaLst = c.fetchall()
            #print("Printing recordsLst: ", recordsExRaLst)
            
            # Commit changes
            conn.commit()

            # Close connection
            conn.close()
            
            advaExRateLst = []
            for record in recordsExRaLst:
                advaRa = record[0]
                advaPayRa = record[1]

                # use if/else to ensure we don't include duplicates
                if advaRa != advaPayRa:
                    advaExRateLst.append(advaRa)
                    advaExRateLst.append(advaPayRa)
                else:
                    advaExRateLst.append(advaRa)
            
            #print('Printing advaExRateLst: ', advaExRateLst)    
            adva_exrate_combo.config(values=advaExRateLst)
        

        # c) addAdvaPaymentFtn
        def addAdvaPaymentFtn():
            '''This function will get entries from advance pay combo boxes and text boxes and add their 
            values to the  advaPayTreeView'''
                                  
            # Retriving the curreny symbols
            currSymbolLst = []
            currSymbolLst = currSymbolFtn('tblCurr', 'currSymbol', 'petrolstation.db', currSymbolLst)
                        
            # retrieving advance pay list variable
            global adva_pay_items_lst_branch1
                        
            # Get values from combo boxes
            customerName = adva_cust_combo.get()
            
            product = adva_prod_combo.get()
            
            currency = adva_curr_combo.get()
            
            price = adva_price_combo.get()

            exrate = adva_exrate_combo.get()
            
            # Get values from text boxes
            dollar_amount = adva_pay_dollar_branch1.get()
            cdf_amount = adva_pay_cdf_branch1.get()

            # preventing value errors
            try:
                productID = int(prodLst.index(product)) + 1 
            except ValueError:
                productID = None

            try:
                currencyID = int(currSymbolLst.index(currency)) + 1
            except ValueError:
                currencyID = None

            try:
                customerID = int(advaCustLst.index(customerName)) + 1
            except ValueError:
                customerID = None
            
            
            # Calculating the liters
            if currencyID == 1:
                # converting values from string to float
                try:
                    dollar_amount = float(dollar_amount)
                except:
                    dollar_amount = 0

                try:
                    cdf_amount = float(cdf_amount)
                except:
                    cdf_amount = 0
                
                advLiters = (dollar_amount + (cdf_amount/float(exrate))) / float(price)

            else:
                # converting values from string to float
                try:
                    dollar_amount = float(dollar_amount)
                except:
                    dollar_amount = 0

                try:
                    cdf_amount = float(cdf_amount)
                except:
                    cdf_amount = 0                
                
                try:
                    price = float(price)
                except:
                    price = float(price.replace(',',''))

                advLiters = ((dollar_amount * float(exrate)) + cdf_amount) / price
                
            # adding values to Treeview
            # use a while statement to loop thro' 
            entries = 3
            while entries > 0:
                if entries == 3:
                    if (adva_pay_dollar_branch1.get() != '') and (adva_pay_cdf_branch1.get() != ''):
                        advCustID = customerID
                        advCustName = customerName
                        advPayDate = date_editor_branch1.get() #currentDateBranch1
                        advPayProdID = productID
                        advPayLtr = f'{advLiters:,.2f}' # the , means format in thousands and .2f means limit to 2 decimal places
                        advPayCurrID = currencyID
                        advPayProdPrice = f'{float(price):,.2f}'
                        advPayUSD = f'{dollar_amount:,.2f}'
                        advPayCDF = f'{float(cdf_amount):,.0f}'
                        advExRate = f'{float(exrate):,.0f}'
                        adv_pay_item = [advCustID, advCustName, advPayDate, advPayProdID, advPayLtr, advPayCurrID, advPayProdPrice, advPayUSD, advPayCDF, advExRate]
                        adva_pay_tree.insert('',END, values=adv_pay_item) #this inserts the adv_pay_item into the end of the treeview
                                                
                        adva_pay_dollar_branch1.delete(0,END) # clears the dollar entry
                        adva_pay_cdf_branch1.delete(0,END) # clears the CDF entry
                        
                        adva_pay_items_lst_branch1.append(adv_pay_item)

                        entries -= 1

                    else:
                        entries -= 1
                elif entries == 2:
                    if adva_pay_dollar_branch1.get() != '':
                        advCustID = customerID
                        advCustName = customerName
                        advPayDate = date_editor_branch1.get() #currentDateBranch1
                        advPayProdID = productID
                        advPayLtr = f'{advLiters:,.2f}'
                        advPayCurrID = currencyID
                        advPayProdPrice = f'{float(price):,.2f}'
                        advPayUSD = f'{dollar_amount:,.2f}'
                        advPayCDF = 0
                        advExRate = f'{float(exrate):,.0f}'
                        adv_pay_item = [advCustID, advCustName, advPayDate, advPayProdID, advPayLtr, advPayCurrID, advPayProdPrice, advPayUSD, advPayCDF, advExRate]
                        adva_pay_tree.insert('',END, values=adv_pay_item) #this inserts the adv_pay_item into the end of the treeview
                                                
                        adva_pay_dollar_branch1.delete(0,END) # clears the dollar entry
                        # adva_pay_cdf_branch1.delete(0,END) # clears the CDF entry
                        
                        adva_pay_items_lst_branch1.append(adv_pay_item)

                        entries -= 1
                    else:
                        entries -= 1
                else:
                    if adva_pay_cdf_branch1.get() != '':
                        advCustID = customerID
                        advCustName = customerName
                        advPayDate = date_editor_branch1.get() #currentDateBranch1
                        advPayProdID = productID
                        advPayLtr = f'{advLiters:,.2f}'
                        advPayCurrID = currencyID
                        advPayProdPrice = f'{float(price):,.2f}'
                        advPayUSD = 0.0
                        advPayCDF = f'{float(cdf_amount):,.0f}'
                        advExRate = f'{float(exrate):,.0f}'
                        adv_pay_item = [advCustID, advCustName, advPayDate, advPayProdID, advPayLtr, advPayCurrID, advPayProdPrice, advPayUSD, advPayCDF, advExRate]
                        adva_pay_tree.insert('',END, values=adv_pay_item) #this inserts the adv_pay_item into the end of the treeview
                                                
                        #adva_pay_dollar_branch1.delete(0,END) # clears the dollar entry
                        adva_pay_cdf_branch1.delete(0,END) # clears the CDF entry
                        
                        adva_pay_items_lst_branch1.append(adv_pay_item)

                        entries -= 1
                    else:
                        entries -= 1

            #print("Printing adva_pay_items_lst_branch1 after adding item: ", adva_pay_items_lst_branch1)
                        
            # resetting combo boxes to default
            adva_cust_combo.current(0)
            adva_prod_combo.current(0)
            adva_curr_combo.current(0)
            #adva_price_combo.current(0)
        
        
        # d) advaRemoveSelectedFtn
        def advaRemoveSelectedFtn():
            ''''This function will remove all the selected records in the Treeview'''
            # declaring and initializing a variable to keep track of selected items
            removed_records_lst = adva_pay_tree.selection() # selection() returns a list of treeview indexes of selected items
            #print('Printing removed records lst: ', removed_records_lst)

            # Defining and initializing a list to store the treeview values of removed items
            tree_removed_records_lst = []

            # Retrieving the treeview values of removed records
            tree_removed_records_lst = [list(adva_pay_tree.item(record, 'values')) for record in removed_records_lst] #tree.item(index,'values') will return the values of the tree item with the specified index
            # list(adva_pay_tree.item(record, 'values')) ensures that the values are wrapped in a list instead of having a list of tupples
            
            # updating the advance payment details list to exclude the removed items
            global adva_pay_items_lst_branch1
            #print("Printing adva_pay_items_lst_branch1 before removal: ", adva_pay_items_lst_branch1)
            for item in tree_removed_records_lst:
                #print("Printing item: ", item)
                # changing some values to ensure item matches adva_pay_items_lst_branch1
                new_item = []
                value1 = int(item[0])
                new_item.append(value1)
                value2 = item[1]
                new_item.append(value2)
                value3 = item[2]
                new_item.append(value3)
                value4 = int(item[3])
                new_item.append(value4)
                value5 = item[4]
                new_item.append(value5)
                value6 = int(item[5])
                new_item.append(value6)
                if re.search(r"\d+\.\d+", item[6]) is not None: # r"\d+\.\d+" checks for a decimal number (float) with at least one digit before and after the decimal point
                    value7 = item[6] # is not None condition ensures that we correctly identify whether the input is a float or an integer
                else:
                    value7 = int(item[6])
                new_item.append(value7)
                if re.search(r"\d+\.\d+", item[7]) is not None and item[7] != '0.0': # r"\d+\.\d+" checks for a decimal number (float) with at least one digit before and after the decimal point
                    value8 = item[7] # is not None condition ensures that we correctly identify whether the input is a float or an integer
                else:
                    value8 = float(item[7])
                new_item.append(value8)
                if re.search(r"\d+\,\d+", item[8]) is not None: # r"\d+\.\d+" checks for a decimal number (float) with at least one digit before and after the decimal point
                    value9 = item[8] # is not None condition ensures that we correctly identify whether the input is a float or an integer
                else:
                    value9 = int(item[8])
                new_item.append(value9)
                value10 = item[9]
                new_item.append(value10)
                #print("Printing new_item: ", new_item)
                if new_item in adva_pay_items_lst_branch1: # check if the item is in the list
                    adva_pay_items_lst_branch1.remove(new_item) # remove it from the list


            #print("Printing Advance payment list After removal: ", adva_pay_items_lst_branch1)
            
            # removing selected records in treeview
            x = adva_pay_tree.selection() 
            for record in x:
                #print('Printing index: ', record)
                #print('Printing treeview values of removed items: ', adva_pay_tree.item(record))
                adva_pay_tree.delete(record) #will remove each selected record

            #print("Printing tree_removed_records_lst: ", tree_removed_records_lst)  

            # resetting combo boxes to default
            adva_cust_combo.current(0)
            adva_prod_combo.current(0)
            adva_curr_combo.current(0)
            #adva_price_combo.current(0)


        # e) advaPayCancelFtn
        def advaPayCancelFtn():
            '''This function clears the text boxes and the Treeview'''
            # clearing text boxes
            adva_pay_dollar_branch1.delete(0,END) # clears the dollar entry
            adva_pay_cdf_branch1.delete(0,END) # clears the CDF entry

            # resetting combo boxes to default
            adva_cust_combo.current(0)
            adva_prod_combo.current(0)
            adva_curr_combo.current(0)
            adva_price_combo.current(0)
            #adva_exrate_combo.current(0)

            # clearing treeview
            adva_pay_tree.delete(*adva_pay_tree.get_children()) # * means all. get.children() will get all the children in each item 

            # clearing adva_pay_items_lst_branch1
            global adva_pay_items_lst_branch1
            adva_pay_items_lst_branch1.clear()
            #print("Printing adva_pay_items_lst_branch1 after clearing: ", adva_pay_items_lst_branch1)

        # f) exRateAdditionFtn
        def exRateAdditionFtn(rateID, rateDate, branchID, customerID, rate):
            '''This function inserts a new entry into the exchange rate table given the rateID, date, 
            branchID, customerID and exchage rate'''
                    
            # Creating a database or connect to one
            conn = sqlite3.connect('petrolstation.db')

            # Create a cursor
            c = conn.cursor()
                
            # Updating the tblDebtPay table 
                           
            c.execute("INSERT INTO tblexRate VALUES (:exRateID, :exRateDate , :exRateBranID, :exRateCredCustID, :exRateAdvCustID, :exRateOneOffCustID, :exRate)",
                    {
                        'exRateID': rateID,
                        'exRateDate': rateDate,
                        'exRateBranID': branchID,
                        'exRateCredCustID': 'NULL',
                        'exRateAdvCustID': customerID,
                        'exRateOneOffCustID': 'NULL',
                        'exRate': rate
                    })
            #print("Printing add exRate succesfully: ",rateID)
            # Commit changes
            conn.commit()

            # Close connection
            conn.close()
        
        # g) advaPaySubitFtn
        def advaPaySubitFtn():
            # Need to check the exchange rate values if they exist in the exchange rate table and update that table if not available
            # For instances where a customer is present in both the advPay and indirectPay tables then the liters purchased should automatically be transfered to the indirect table
            # need to update the advpay 
            '''This function will update the database with the advance customer payment details'''
                       
            # a) Retrieve the last advance payment ID and saving last advance payment ID   
            lastAdvPayID = 0         
            lastAdvPayID = lastIDFtn('tblAdvPay', 'advPayID', 'petrolstation.db', lastAdvPayID)
            #print("Finished step1: ")
            # Declaring and assigning currentAdvPayID
            try:
                currentLastAdvPayID = lastAdvPayID
            except:
                currentLastAdvPayID = 0 #this will apply when there are no previous records

            #print("Finished step2")
            # b) Updating the database with the provided debt payment data
            # adv_pay_item = [advCustID, advCustName, advPayDate, advPayProdID, advPayLtr, advPayCurrID, advPayProdPrice, advPayUSD, advPayCDF, advExRate]
            
            # Declaring and initializing variales for keeping track of total amount paid
            total_adva_dollar_payment = 0
            total_adva_cdf_payment = 0

            global adva_pay_items_lst_branch1
            #print("Printing adva_pay_items_lst_branch1: ",adva_pay_items_lst_branch1)
            for item in adva_pay_items_lst_branch1:
                #print("Printing Item: ", item)      
                # ensuring we have a unique currentLastAdvPayID for every entry
                currentLastAdvPayID += 1
                #print("Printing currentLastAdvPayID after + 1: ", currentLastAdvPayID)

                # i) Checking the exchange rate provided to ensure that they are all in tblExRate
                exRate = item[9].replace(',','')
                #print("Printing exRate: ", exRate)
                exRateAdvCustID = int(item[0])
                branchID = 1
                #print("finished step 3")
                
                # retrieve exchange rate IDs from database
                exRateIDLst = exRateIDFtn ('tblexRate', exRateAdvCustID, branchID, 'petrolstation.db', exRate)
                #print("Printing exRateIDLst: ", exRateIDLst)
                #print("finished step 4")

                # retrieve last exchange rate ID
                lastExRateID = 0
                lastExRateID = lastIDFtn('tblexRate', 'exRateID', 'petrolstation.db', lastExRateID)
                #print("Finished step 5")

                # checking whether the current exRate is in the exchange rate table and entering it if its not available
                rateID = 0
                if exRateIDLst != []:
                    exchangeRateID = exRateIDLst[0] # this means the exchange rate was in the exchange rate table
                    #print("Printing exchangeRateID: ",exchangeRateID)
                else:
                    rateID = int(lastExRateID) + 1
                    rateDate = item[2]
                    customerID = exRateAdvCustID
                    rate = exRate
                    # adding the exchange rate
                    exRateAdditionFtn(rateID, rateDate, branchID, customerID, rate)
                #print("finished step 6")
                
                
                # determining the exchange rate id
                if rateID == 0: 
                    exchangeRateID # this means the exchange rate id was present in the exchange rate table
                    #print("Printing the exchangeRateID: ", exchangeRateID)
                else:
                    exchangeRateID = rateID # this means the exchange rate id is the last exchange rate id entered into the exchange rate table
                    #print("Printing exchangeRateID: ", exchangeRateID)
                #print("Finished step 7")

                # II) Updating the Advance Payment table
                # Creating a database or connect to one
                conn = sqlite3.connect('petrolstation.db')

                # Create a cursor
                c = conn.cursor()
                
                # Updating the tblAdvPay table
                        
                c.execute("INSERT INTO tblAdvPay VALUES (:advPayID, :advPayDate, :advPayBranID, :advCustID, :oneOffCustID, :advPayProdID, :advPayCurrID, :advPayProdPrice, :advPayLtr, :advPayExRateID)",
                    {
                        'advPayID': currentLastAdvPayID,
                        'advPayDate': item[2],
                        'advPayBranID': 1,
                        'advCustID': item[0],
                        'oneOffCustID': 'NULL', 
                        'advPayProdID': item[3],
                        'advPayCurrID': item[5],
                        'advPayProdPrice': item[6],
                        'advPayLtr': item[4],
                        'advPayExRateID': exchangeRateID
                    })
                #print("Printing added advancePay: ",currentLastAdvPayID)
                # Commit changes
                conn.commit()

                # Close connection
                conn.close()

                #print("Finished step 8")

                # III) Keeping track of the total amount of money paid
                # using a while and an if/else to differenciate the currencies
                #print("Printing item: ", item)
                entries = 2
                while entries > 0:
                    if item[7] != 0.0:
                        total_adva_dollar_payment += float(item[7].replace(',',''))
                        #print("Printing total_adva_dollar_payment: ", total_adva_dollar_payment)
                        item[7] = 0.0
                        entries -= 1
                    elif item[8] != 0:
                        total_adva_cdf_payment += int(item[8].replace(',',''))
                        #print("Printing total_adva_cdf_payment: ", total_adva_cdf_payment)
                        item[8] = 0
                        entries -= 1
                    else:
                        entries -= 1
                #print("Finished step 9")  

                # IV) Updating the advance customer details table with the advance payment data
                
                # Retrieving last advance customer detail ID
                lastAdvaCustDetailID = 0
                lastAdvaCustDetailID = lastIDFtn('tblAdvCustDetails', 'advCustDetailID', 'petrolstation.db', lastAdvaCustDetailID)
                #print("Finished step 10")

                # Declaring and assigning currentLastAdvaCustDetailID
                try:
                    currentLastAdvaCustDetailID = lastAdvaCustDetailID
                except:
                    currentLastAdvaCustDetailID = 0 #this will apply when there are no previous records

                currentLastAdvaCustDetailID += 1
                #print("Finished step 11")
                                
                # Determining the Current Liter Balance
                currentLtrBal = 0.0 #ensuring every time this function runs the currentLtrBal is 0.0 liters
                float_lastCurrentLtrBalFtn = 0.0
                try:
                    cleaned_item = float(item[4].replace(',',''))
                except:
                    cleaned_item = item[4]

                #print("Printing cleaned_item: ",cleaned_item)
                #print("Pringint item[0] line 2455: ", item[0])
                #print("Printing float_lastCurrentLtrBalFtn Before function line 2457: ", float_lastCurrentLtrBalFtn)
                float_lastCurrentLtrBalFtn = float(lastCurrentLtrBalFtn('tblAdvCustDetails', 'advCustDetailID', 'advCustCurrentLiterBal', 'petrolstation.db', item[0]))
                #print("Printing float_lastCurrentLtrBalFtn After line 2458: ", float_lastCurrentLtrBalFtn)
                #print("Printing currentLtrBal Before addition line 2445: ", currentLtrBal)
                currentLtrBal =  float_lastCurrentLtrBalFtn + cleaned_item
                #print("Printing currentLtrBal After addition line 2447: ", currentLtrBal)
                currentLtrBalDatetime = datetime.datetime.now()
                #print("Finished step 12")
                
                # Creating a database or connect to one
                conn = sqlite3.connect('petrolstation.db')

                # Create a cursor
                c = conn.cursor()
                
                # Updating the tblAdvCustDetails table          
                                    
                c.execute("INSERT INTO tblAdvCustDetails VALUES (:advCustDetailID, :advCustID, :advCustProdID, :advCustCurrID, :advCustPrice, :advCustPriceDate, :advPayID, :indirectCustID, :saleID, :advCustCurrentLiterBal, :advCustCurrentLiterBalDate)",
                          {
                              'advCustDetailID': currentLastAdvaCustDetailID,
                              'advCustID': item[0],
                              'advCustProdID': 'NULL',
                              'advCustCurrID': 'NULL',
                              'advCustPrice': 'NULL',
                              'advCustPriceDate': 'NULL',
                              'advPayID': currentLastAdvPayID,
                              'indirectCustID': 'NULL',
                              'saleID': 'NULL',
                              'advCustCurrentLiterBal': currentLtrBal,
                              'advCustCurrentLiterBalDate': currentLtrBalDatetime
                          })
                #print("Printing added new data in advcustDetails: ", currentLastAdvaCustDetailID)
                
                # Commit changes
                conn.commit()

                # Close connection
                conn.close()
                #print("Finished one item _____________________________________")
            #print("Finished step 13")

            # c) Clear all text boxes and the treeview
            advaPayCancelFtn()

            # clear adva_pay_items_lst_branch1
            adva_pay_items_lst_branch1.clear()
            #print("Finished step 14")

            # d) Updating the cummulative payments label 
            global total_cummulative_dollar_payments_branch1
            global total_cummulative_cdf_payments_branch1

            if total_adva_dollar_payment != 0:
                total_cummulative_dollar_payments_branch1 += total_adva_dollar_payment
            else:
                total_cummulative_dollar_payments_branch1
                
            if total_adva_cdf_payment != 0:    
                total_cummulative_cdf_payments_branch1 += total_adva_cdf_payment
            else:
                total_cummulative_cdf_payments_branch1

            #print("Printing total_cummulative_dollar_payments_branch1: ", total_cummulative_dollar_payments_branch1)
            #print("Printing total_cummulative_cdf_payments_branch1: ", total_cummulative_cdf_payments_branch1)
            #print("Finished step 15")
            cummulative_dollar_payments_branch1.config(text=total_cummulative_dollar_payments_branch1)
            cummulative_cdf_payments_branch1.config(text=total_cummulative_cdf_payments_branch1)    
            #print("Finished step 16")

            # e) close debt pay window
            editor_advance_payment_branch1.destroy() 
            #print("Finished step 17")
        
        # MAIN FRAME
        frame = Frame(editor_advance_payment_branch1)
        frame.pack()

        # creating labels
        adva_cust_name_label = Label(frame, text="Customer Name")
        adva_cust_name_label.grid(row=0, column=0)
        prod_name_label = Label(frame, text='Product')
        prod_name_label.grid(row=0, column=1)
        curr_sign_label = Label(frame, text='Currency')
        curr_sign_label.grid(row=0, column=2)
        adva_price_label = Label(frame, text='Price')
        adva_price_label.grid(row=0, column=3)
        dollar_sign_label = Label(frame, text=" $ ")
        dollar_sign_label.grid(row=0, column=4)
        cdf_sign_label = Label(frame, text="CDF")
        cdf_sign_label.grid(row=0, column=5)
        exRate_label    = Label(frame, text="Exchange Rate")
        exRate_label.grid(row=0, column=6)

        # global variables
        global adva_cust_name 
        adva_cust_name = ""
        
        global advaCustLst
        advaCustLst = []

        global prodLst
        prodLst = []

        # Retriving the curreny symbols
        currSymbolLst = []
        currSymbolLst = currSymbolFtn('tblCurr', 'currSymbol', 'petrolstation.db', currSymbolLst)

        # creating combobox
        adva_cust_combo = ttk.Combobox(frame, values=custFtn('tblAdvCust', 'advCustName', 'petrolstation.db', advaCustLst))
        adva_cust_combo.grid(row=1, column=0)
        #adva_cust_combo.current(0) #this sets the first value as the default
        adva_cust_combo.bind('<<ComboboxSelected>>', advaPriceFtn, ) #binding tires this combobox to another action. <<ComboboxSelected>> is the binding and credCustIDFtn() is the action to be taken when the binding occurs
        adva_cust_combo.bind('<<ComboboxSelected>>', advaExRateFtn, add='+')

        adva_prod_combo = ttk.Combobox(frame, values=prodFtn('tblProd', 'prodName', 'petrolstation.db', prodLst))
        adva_prod_combo.grid(row=1, column=1)
        #adva_prod_combo.current(0)
        adva_prod_combo.bind('<<ComboboxSelected>>', advaPriceFtn)
        adva_prod_combo.bind('<<ComboboxSelected>>', advaExRateFtn, add='+')

        adva_curr_combo = ttk.Combobox(frame, values= currSymbolLst)
        adva_curr_combo.grid(row=1, column=2)
        #adva_curr_combo.current(0)
        adva_curr_combo.bind('<<ComboboxSelected>>', advaPriceFtn)
        adva_curr_combo.bind('<<ComboboxSelected>>', advaExRateFtn, add='+')

        adva_price_combo = ttk.Combobox(frame, values=[""])
        adva_price_combo.grid(row=1, column=3) 
        #adva_price_combo.current(0)
        adva_price_combo.bind('<<ComboboxSelected>>', advaExRateFtn)

        adva_exrate_combo = ttk.Combobox(frame, values=[""])
        #adva_exrate_combo.current(0) #setting default value
        adva_exrate_combo.grid(row=1, column=6)
        
        # creating text box
        adva_pay_dollar_branch1 = Entry(frame, width=30)
        adva_pay_dollar_branch1.grid(row=1, column=4)
        adva_pay_cdf_branch1 = Entry(frame, width=30)
        adva_pay_cdf_branch1.grid(row=1, column=5)          
        
        # Declare and initialize variable for storing debt payment details
        global adva_pay_items_lst_branch1
        adva_pay_items_lst_branch1 = []

        # # creating button
        adva_pay_addpayment_btn = Button(frame, text="Add Payment", command=addAdvaPaymentFtn)
        adva_pay_addpayment_btn.grid(row=2, column=6, pady=5)

        # TREEVIEW FRAME
        treeview_frame = Frame(frame)
        treeview_frame.grid(row=3, column=0, columnspan=7, padx=10, pady=10)
        
        # creating treeview scrollbar
        tree_scroll = Scrollbar(treeview_frame)
        tree_scroll.pack(side=RIGHT, fill=Y) #fill=Y means it scroll vertically
        
        # add some style
        style = ttk.Style()

        # pick a theme
        style.theme_use('default')
        
        # creating Treeview
        columns = ["advCustID", "advCustName", "advPayDate", "advPayProdID", "advPayLtr", "advPayCurrID", "advPayProdPrice", "advPayUSD", "advPayCDF", "advExRate"]
        adva_pay_tree = ttk.Treeview(treeview_frame, yscrollcommand=tree_scroll.set, columns=columns, show="headings")
        adva_pay_tree.pack()

        # configure scrollbar
        tree_scroll.config(command=adva_pay_tree.yview)

        # format Treeview columns
        adva_pay_tree.column("advCustID", anchor=E, width=90)
        adva_pay_tree.column("advCustName", anchor=CENTER, width=170)
        adva_pay_tree.column("advPayDate", anchor=CENTER, width=120)
        adva_pay_tree.column("advPayProdID", anchor=E, width=120)
        adva_pay_tree.column("advPayLtr", anchor=CENTER, width=120)
        adva_pay_tree.column("advPayCurrID", anchor=E, width=90)
        adva_pay_tree.column("advPayProdPrice", anchor=E, width=120)
        adva_pay_tree.column("advPayUSD", anchor=E, width=120)
        adva_pay_tree.column("advPayCDF", anchor=E, width=150)
        adva_pay_tree.column("advExRate", anchor=E, width=120)
      
        # Create Treeview headings
        adva_pay_tree.heading('advCustID', text='CustomerID')
        adva_pay_tree.heading('advCustName', text='Customer Name')
        adva_pay_tree.heading('advPayDate', text='Date')
        adva_pay_tree.heading('advPayProdID', text='ProductID')
        adva_pay_tree.heading('advPayLtr', text='Liters')
        adva_pay_tree.heading('advPayCurrID', text='CurrencyID')
        adva_pay_tree.heading('advPayProdPrice', text='Price')
        adva_pay_tree.heading('advPayUSD', text='$')
        adva_pay_tree.heading('advPayCDF', text='CDF')
        adva_pay_tree.heading('advExRate', text='Exchange Rate')


       
        # THIRD FRAME
        button_frame = Frame(frame)
        button_frame.grid(row=4, column=0, columnspan=7, pady=(10,10), sticky="news", padx=20)
        
        # creating buttons
        remove_selected = Button(button_frame, text="Remove Selected", command=advaRemoveSelectedFtn)
        remove_selected.grid(row=0, column=0, padx=10, ipadx=160)
        
        cancel_btn = Button(button_frame, text="Cancel", command=advaPayCancelFtn)
        cancel_btn.grid(row=0, column=1, padx=10, ipadx=160)

        submit_btn = Button(button_frame, text="Submit", command=advaPaySubitFtn)
        submit_btn.grid(row=0, column=2, padx=10, ipadx=160)

    
    # Creating oneOffPaymentFtn function
    def oneOffPaymentFtn():
        return
    
    
    # MAIN FRAME

    frame = Frame(editor_branch1)
    frame.pack()

    # INDEX AREA FRAME

    index_info_frame = LabelFrame(frame, text="Index Data")
    index_info_frame.grid(row=0, column=0, sticky="news", pady=3, padx=3)

    # Creating Labels
    date_label = Label(index_info_frame, text="Date")
    date_label.grid(row=0, column=0)
    branch_label = Label(index_info_frame, text="Branch")
    branch_label.grid(row=0, column=2)
    pump1_label = Label(index_info_frame, text="Pump I")
    pump1_label.grid(row=1, column=0, pady=(5,0), columnspan=2, ipadx=120)
    pump1_pms_label = Label(index_info_frame, text="PMS")
    pump1_pms_label.grid(row=2, column=0)
    pump1_ago_label = Label(index_info_frame, text="AGO")
    pump1_ago_label.grid(row=2, column=2)
        
    pump2_label = Label(index_info_frame, text="Pump II")
    pump2_label.grid(row=3, column=0, columnspan=2, ipadx=120)
    pump2_pms_label = Label(index_info_frame, text="PMS")
    pump2_pms_label.grid(row=4, column=0)
    pump2_ago_label = Label(index_info_frame, text="AGO")
    pump2_ago_label.grid(row=4, column=2)

    pump3_label = Label(index_info_frame, text="Pump III")
    pump3_label.grid(row=5, column=0, columnspan=2, ipadx=120)    
    pump3_pms_label = Label(index_info_frame, text="PMS")
    pump3_pms_label.grid(row=6, column=0)
    pump3_ago_label = Label(index_info_frame, text="AGO")
    pump3_ago_label.grid(row=6, column=2)

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
    date_editor_branch1 = Entry(index_info_frame, width=30)
    date_editor_branch1.grid(row=0, column=1, padx=20)
    branch_editor_branch1 = Entry(index_info_frame, width=30)
    branch_editor_branch1.grid(row=0, column=3)
    branch_editor_branch1.insert(0, str(clicked.get())) #this inserts the clicked branch into the text box
    branch_editor_branch1.config(state="disabled") #this prevents users from changing this value

    pump1_editor_branch1 = Entry(index_info_frame, width=30)
    pump1_editor_branch1.grid(row=1, column=2, pady=(5,0), columnspan=2, ipadx=90)
    pump1_editor_branch1.insert(0, str(1)) #this inserts the pump no. "1" into the text box
    pump1_editor_branch1.config(state="disabled") #this prevents users from changing this value
    pump1_pms_editor_branch1 = Entry(index_info_frame, width=30)
    pump1_pms_editor_branch1.grid(row=2, column=1)
    pump1_ago_editor_branch1 = Entry(index_info_frame, width=30)
    pump1_ago_editor_branch1.grid(row=2, column=3)

    pump2_editor_branch1 = Entry(index_info_frame, width=30)
    pump2_editor_branch1.grid(row=3, column=2, columnspan=2, ipadx=90)
    pump2_editor_branch1.insert(0, str(2)) #this inserts the pump no. "2" into the text box
    pump2_editor_branch1.config(state="disabled") #this prevents users from changing this value
    pump2_pms_editor_branch1 = Entry(index_info_frame, width=30)
    pump2_pms_editor_branch1.grid(row=4, column=1)
    pump2_ago_editor_branch1 = Entry(index_info_frame, width=30)
    pump2_ago_editor_branch1.grid(row=4, column=3)

    pump3_editor_branch1 = Entry(index_info_frame, width=30)
    pump3_editor_branch1.grid(row=5, column=2, columnspan=2, ipadx=90)
    pump3_editor_branch1.insert(0, str(3)) #this inserts the pump no. "3" into the text box
    pump3_editor_branch1.config(state="disabled") #this prevents users from changing this value
    pump3_pms_editor_branch1 = Entry(index_info_frame, width=30)
    pump3_pms_editor_branch1.grid(row=6, column=1)
    pump3_ago_editor_branch1 = Entry(index_info_frame, width=30)
    pump3_ago_editor_branch1.grid(row=6, column=3)

    # Creating buttons for Index
    index_cancel_btn = Button(index_info_frame, text="Cancel", command=indexCancelFtn)
    index_cancel_btn.grid(row=7, column=1, pady=5, padx=(0,5), ipadx=50)

    index_submit_btn = Button(index_info_frame, text="Submit", command=indexSubmitFtn)
    index_submit_btn.grid(row=7, column=2, pady=5, padx=(5,0), ipadx=60)

    
    # ADDITIONAL INFO FRAME

    additional_info_frame = LabelFrame(frame, text="Additional Data")
    additional_info_frame.grid(row=1, column=0, sticky="news", pady=3, padx=3)
    
    # CREATING FUEL RETURNED / AMORSAGE
    
    # Creating global variables for text box names (will be used to store and display total returned fuel)
    global fuel_returned_pms_branch1
    global fuel_returned_ago_branch1
    global cummulative_fuel_returned_pms_branch1 #used in calculating the cummulative returned fuel especially where multiple pumps in a branch have returned fuel
    global cummulative_fuel_returned_ago_branch1 #used in calculating the cummulative returned fuel especially where multiple pumps in a branch have returned fuel

    fuel_returned_pms_branch1 = 0
    fuel_returned_ago_branch1 = 0

    cummulative_fuel_returned_pms_branch1 = 0
    cummulative_fuel_returned_ago_branch1 = 0

    
    # Creating a button to launch the restocking window 
    fuel_returned_branch1_btn = Button(additional_info_frame, text="Amorsage", command=fuelReturnedBranch1Ftn)
    fuel_returned_branch1_btn.grid(row=0,column=0, columnspan=4, pady=5, padx=5, ipadx=315)

    # Creating Fuel Returned Total (L) labels
    fuel_returned_label = Label(additional_info_frame, text="Total (L) PMS")
    fuel_returned_label.grid(row=1, column=0, pady=5)
    total_fuel_returned_pms_label = Label(additional_info_frame, text=fuel_returned_pms_branch1, borderwidth=3, relief="sunken")
    total_fuel_returned_pms_label.grid(row=1, column=1, ipadx=87)

    fuel_returned_label = Label(additional_info_frame, text="Total (L) AGO")
    fuel_returned_label.grid(row=1, column=2)
    total_fuel_returned_ago_label = Label(additional_info_frame, text=fuel_returned_ago_branch1, borderwidth=3, relief="sunken")
    total_fuel_returned_ago_label.grid(row=1, column=3, ipadx=87)
    
        
    # CREATING TOTAL SALES 

    # Creating global variables for total sales
    global day_sale_liters_pms_branch1
    global day_sale_liters_ago_branch1

    day_sale_liters_pms_branch1 = 0
    day_sale_liters_ago_branch1 = 0

    # Creating total sales labels
    total_sales_label = Label(additional_info_frame, text="Total Sales (Liters)")
    total_sales_label.grid(row=2, column=0, pady=5, columnspan=4)

    total_sales_pms_label = Label(additional_info_frame, text="PMS")
    total_sales_pms_label.grid(row=3, column=0, padx=10, pady=5)
    total_sales_ago_label = Label(additional_info_frame, text="AGO")
    total_sales_ago_label.grid(row=3, column=2, padx=10)

    total_sales_result_pms_label = Label(additional_info_frame, text=day_sale_liters_pms_branch1, borderwidth=3, relief="sunken")
    total_sales_result_pms_label.grid(row=3, column=1, padx=20, ipadx=87)
    total_sales_result_ago_label = Label(additional_info_frame, text=day_sale_liters_ago_branch1, borderwidth=3, relief="sunken")
    total_sales_result_ago_label.grid(row=3, column=3, padx=20, ipadx=87)

    # RESTOCKING / DECHARGEMENT
    
    # Creating global variables for text box names
    global total_restock_liters_pms_branch1 #this variable will be used to keep track of the total liters restock for a particular day
    global total_restock_liters_ago_branch1

    total_restock_liters_pms_branch1 = 0
    total_restock_liters_ago_branch1 = 0
    
    # Creating a button to launch the restocking window 
    restocking_branch1_btn = Button(additional_info_frame, text="Dechargement", command=restockingBranch1Ftn)
    restocking_branch1_btn.grid(row=4,column=0, columnspan=4, pady=5, padx=5, ipadx=310)

    # Creating Total (L) labels
    restock_total_label = Label(additional_info_frame, text="Total (L) PMS")
    restock_total_label.grid(row=5, column=0, pady=5)
    restock_total_pms_label = Label(additional_info_frame, text=total_restock_liters_pms_branch1, borderwidth=3, relief="sunken")
    restock_total_pms_label.grid(row=5, column=1, ipadx=87)

    restock_total_label = Label(additional_info_frame, text="Total (L) AGO")
    restock_total_label.grid(row=5, column=2)
    restock_total_ago_label = Label(additional_info_frame, text=total_restock_liters_ago_branch1, borderwidth=3, relief="sunken")
    restock_total_ago_label.grid(row=5, column=3, ipadx=87)

    
     # DIPS / JAUGE
    
    # Creating global variables for text box names
    global total_dips_liters_pms_branch1 #this variable will be used to keep track of the total dip liters for a particular day
    global total_dips_liters_ago_branch1

    total_dips_liters_pms_branch1 = 0
    total_dips_liters_ago_branch1 = 0
    
    # Creating a button to launch the dips window 
    dips_branch1_btn = Button(additional_info_frame, text="Jauge", command=dipsBranch1Ftn)
    dips_branch1_btn.grid(row=6,column=0, columnspan=4, pady=5, padx=5, ipadx=330)

    # Creating Total (L) labels
    dips_total_label = Label(additional_info_frame, text="Total (L) PMS")
    dips_total_label.grid(row=7, column=0, pady=5)
    dips_total_pms_label = Label(additional_info_frame, text=total_dips_liters_pms_branch1, borderwidth=3, relief="sunken")
    dips_total_pms_label.grid(row=7, column=1, ipadx=87)

    dips_total_label = Label(additional_info_frame, text="Total (L) AGO")
    dips_total_label.grid(row=7, column=2)
    dips_total_ago_label = Label(additional_info_frame, text=total_dips_liters_ago_branch1, borderwidth=3, relief="sunken")
    dips_total_ago_label.grid(row=7, column=3, ipadx=87)
    
    # PAYMENTS INFO FRAME

    payments_info_frame = LabelFrame(frame, text="Payments Data")
    payments_info_frame.grid(row=2, column=0, sticky="news", pady=3, padx=3)
    
    # Creating buttons to launch the advanced and debt payments windows
    debt_payment_btn = Button(payments_info_frame, text="Debt Payments", command=debtPaymentFtn)
    debt_payment_btn.grid(row=0,column=0, pady=5, padx=5, ipadx=70)

    advance_payment_btn = Button(payments_info_frame, text="Advance Payments", command=advancePaymentFtn)
    advance_payment_btn.grid(row=0,column=1, pady=5, padx=5, ipadx=60)

    oneoff_payment_btn = Button(payments_info_frame, text="One Off Payments", command=oneOffPaymentFtn)
    oneoff_payment_btn.grid(row=0,column=2, pady=5, padx=5, ipadx=50)

    # TOTAL PAYMENTS FRAME
    total_payments_frame = LabelFrame(payments_info_frame)
    total_payments_frame.grid(row=1, column=0, columnspan=3, padx=(40,0))
    
    # Global variables
    global total_cummulative_dollar_payments_branch1
    global total_cummulative_cdf_payments_branch1

    total_cummulative_dollar_payments_branch1 = 0
    total_cummulative_cdf_payments_branch1 = 0

    # Creating labels to show the cummulative payments
    total_dollar_payments_label = Label(total_payments_frame, text=" $ ")
    total_dollar_payments_label.grid(row=0, column=0, pady=5)
    cummulative_dollar_payments_branch1 = Label(total_payments_frame, text="0", borderwidth=3, relief="sunken")
    cummulative_dollar_payments_branch1.grid(row=0, column=1, ipadx=87)

    total_cdf_payments_label = Label(total_payments_frame, text=" CDF ")
    total_cdf_payments_label.grid(row=0, column=2)
    cummulative_cdf_payments_branch1 = Label(total_payments_frame, text="0", borderwidth=3, relief="sunken")
    cummulative_cdf_payments_branch1.grid(row=0, column=3, ipadx=87)

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