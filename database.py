"""This program is useful in managing a petrol station. It includes a database and its GUI"""

import sqlite3

#connecting to database
conn = sqlite3.connect('petrolstation.db')

#create a cursor
c = conn.cursor()


'''#TABLES


# 1 TBLCURRENCY
#Delete table tblCurrency if it exists
c.execute("""DROP TABLE IF EXISTS tblCurrency""")

#commit our command
conn.commit()

#Create table tblCurrency 
c.execute("""CREATE TABLE tblCurrency (
        currencyID integer PRIMARY KEY AUTOINCREMENT,
        currencySymbol text,
        currencyName text
    )""")

#commit our command
conn.commit()


# 2 TBLBRANCHES
#Delete table tblBranches if it exists
c.execute("""DROP TABLE IF EXISTS tblBranches""")

#commit our command
conn.commit()

#Create table tblBranches 
c.execute("""CREATE TABLE tblBranches (
        branchID integer PRIMARY KEY AUTOINCREMENT,
        branchName text
    )""")

#commit our command
conn.commit()


# 3 TBLPRODUCTS
#Delete table tblProducts if it exists
c.execute("""DROP TABLE IF EXISTS tblProducts""")

#commit our command
conn.commit()

#Create table tblProducts 
c.execute("""CREATE TABLE tblProducts (
        productID integer PRIMARY KEY AUTOINCREMENT,
        productName text
    )""")

#commit our command
conn.commit()


# 4 TBLPRODUCTDETAILS
#Delete table tblProductDetails if it exists
c.execute("""DROP TABLE IF EXISTS tblProductDetails""")

#commit our command
conn.commit()

#Create table tblProductDetails 
c.execute("""CREATE TABLE tblProductDetails (
        productDetailID integer PRIMARY KEY,
        productID integer
        productName text,
        productCurrencyID integer,
        branchID integer,
        productWholesalePrice money,
        productPumpPrice money,
        productSpecialPrice money,
        productPriceDate date,
        FOREIGN KEY(productID) REFERENCES tblProduct(productID),
        FOREIGN KEY(productCurrencyID) REFERENCES tblCurrency(currencyID),
        FOREIGN KEY(branchID) REFERENCES tblBranches(branchID)
    )""")

#commit our command
conn.commit()


# 5 TBLINDEXES
#Delete table tblIndexes if it exists
c.execute("""DROP TABLE IF EXISTS tblIndexes""")

#commit our command
conn.commit()

#Create table tblIndexes 
c.execute("""CREATE TABLE tblIndexes (
        indexID integer PRIMARY KEY,
        indexDate date,
        indexBranchID integer,
        indexProductID integer,
        indexPumpNumber integer,
        openingIndex real,
        closingIndex real,
        FOREIGN KEY(indexProductID) REFERENCES tblProducts(productID),
        FOREIGN KEY(indexBranchID) REFERENCES tblBranches(branchID)
    )""")

#commit our command
conn.commit()


# 6 TBLEXCHANGERATE
#Delete table tblExchangeRate if it exists
c.execute("""DROP TABLE IF EXISTS tblExchangeRate""")

#commit our command
conn.commit()

#Create table tblExchangeRate 
c.execute("""CREATE TABLE tblExchangeRate (
        exchangeRateID integer PRIMARY KEY,
        exchangeRateDate date,
        exchangeRateBranchID integer,
        exchangeRate money,
        FOREIGN KEY(exchangeRateBranchID) REFERENCES tblBranches(branchID)
    )""")

#commit our command
conn.commit()


# 7 TBLCREDITCUSTOMERS
#Delete table tblCreditCustomers if it exists
c.execute("""DROP TABLE IF EXISTS tblCreditCustomers""")

#commit our command
conn.commit()

#Create table tblCreditCustomers 
c.execute("""CREATE TABLE tblCreditCustomers (
        creditCustomerID integer PRIMARY KEY,
        creditCustomerName text,
        creditCustomerOpeningBalanceDate date,
        creditCustomerCurrencyID integer,
        creditCustomerOpeningBalance money,
        FOREIGN KEY(creditCustomerCurrencyID) REFERENCES tblCurrency(currencyID)
    )""")

#commit our command
conn.commit()


# 8 TBLDEBTPAYMENT
#Delete table tblDebtPayment if it exists
c.execute("""DROP TABLE IF EXISTS tblDebtPayment""")

#commit our command
conn.commit()

#Create table tblDebtPayment 
c.execute("""CREATE TABLE tblDebtPayment (
        debtPaymentID integer PRIMARY KEY,
        debtPaymentDate date,
        debtPaymentBranchID integer,
        creditCustomerID integer,
        debtPaymentCurrencyID integer,
        debtPaymentAmount money,
        exchangeRateID integer,
        FOREIGN KEY(creditCustomerID) REFERENCES tblCreditCustomers(creditCustomerID)
        FOREIGN KEY(debtPaymentBranchID) REFERENCES tblBranches(branchID),
        FOREIGN KEY(debtPaymentCurrencyID) REFERENCES tblCurrency(currencyID),
        FOREIGN KEY(exchangeRateID) REFERENCES tblExchangeRate(exchangeRateID)
    )""")

#commit our command
conn.commit()


# 9 TBLADVANCECUSTOMERS
#Delete table tblAdvanceCustomers if it exists
c.execute("""DROP TABLE IF EXISTS tblAdvanceCustomers""")

#commit our command
conn.commit()

#Create table tblAdvanceCustomers 
c.execute("""CREATE TABLE tblAdvanceCustomers (
        advanceCustomerID integer PRIMARY KEY,
        advanceCustomerName text,
        advanceCustomerOpeningBalanceDate date,
        advanceCustomerCurrencyID integer,
        advanceCustomerOpeningBalance money,
        advanceCustomerOpeningLiters real
    )""")

#commit our command
conn.commit()


# 10 TBLONEOFFCUSTOMERS
#Delete table tblOneOffCustomers if it exists
c.execute("""DROP TABLE IF EXISTS tblOneOffCustomers""")

#commit our command
conn.commit()

#Create table tblOneOffCustomers 
c.execute("""CREATE TABLE tblOneOffCustomers (
        oneOffCustomerID integer PRIMARY KEY,
        oneOffCustomerName text
    )""")

#commit our command
conn.commit()


# 11 TBLADVANCEPAYMENT
#Delete table tblAdvancePayment if it exists
c.execute("""DROP TABLE IF EXISTS tblAdvancePayment""")

#commit our command
conn.commit()

#Create table tblAdvancePayment 
c.execute("""CREATE TABLE tblAdvancePayment (
        advancePaymentID integer PRIMARY KEY,
        advancePaymentDate date,
        advancePaymentBranchID integer,
        advanceCustomerID integer,
        oneOffCustomerID integer,
        advancePaymentProductID integer,
        advancePaymentCurrencyID integer,
        advancePaymentProductPrice money,
        advancePaymentAmount money,
        exchangeRateID integer,
        FOREIGN KEY(advanceCustomerID) REFERENCES tblAdvanceCustomers(advanceCustomerID),
        FOREIGN KEY(oneOffCustomerID) REFERENCES tblOneOffCustomers(oneOffCustomerID),
        FOREIGN KEY(advancePaymentProductID) REFERENCES tblProducts(productID),
        FOREIGN KEY(advancePaymentBranchID) REFERENCES tblBranches(branchID),
        FOREIGN KEY(advancePaymentCurrencyID) REFERENCES tblCurrency(currencyID),
        FOREIGN KEY(exchangeRateID) REFERENCES tblExchangeRate(exchangeRateID)
    )""")

#commit our command
conn.commit()


# 12 TBLSALES
#Delete table tblSales if it exists
c.execute("""DROP TABLE IF EXISTS tblSales""")

#commit our command
conn.commit()

#Create table tblSales
c.execute("""CREATE TABLE tblSales (
        saleID integer PRIMARY KEY,
        saleDate date,
        saleBranchID integer,
        saleProductID integer,
        wholsaleLiters real,
        pumpSaleLiters real,
        specialSaleLiters real,
        creditCustomerID integer,
        creditCustomerSaleLiters real,
        advanceCustomerID integer,
        advanceCustomerSaleLiters real,
        oneOffCustomerID integer,
        oneOffCustomerSaleLiters real,
        indirectCustomerID integer,
        indirectCustomerSaleLiters real,
        FOREIGN KEY(saleBranchID) REFERENCES tblBranches(branchID),
        FOREIGN KEY(saleProductID) REFERENCES tblProducts(productID),
        FOREIGN KEY(creditCustomerID) REFERENCES tblCreditCustomers(creditCustomerID),
        FOREIGN KEY(advanceCustomerID) REFERENCES tblAdvanceCustomers(advanceCustomerID),
        FOREIGN KEY(oneOffCustomerID) REFERENCES tblOneOffCustomers(oneOffCustomerID),
        FOREIGN KEY(indirectCustomerID) REFERENCES tblIndirectCustomers(indirectCustomerID)
    )""")

#commit our command
conn.commit()


# 13 TBLCREDITCUSTOMERDETAILS
#Delete table tblCreditCustomerDetails if it exists
c.execute("""DROP TABLE IF EXISTS tblCreditCustomerDetails""")

#commit our command
conn.commit()

#Create table tblCreditCustomerDetails 
c.execute("""CREATE TABLE tblCreditCustomerDetails (
        creditCustomerDetailID integer PRIMARY KEY,
        creditCustomerID integer,
        creditCustomerProductID integer,
        creditCustomerCurrencyID integer,
        creditCustomerPrice money,
        creditCustomerPriceDate date,
        saleID integer,
        indirectCustomerID integer,
        debtPaymentID integer,
        CreditCustomerCurrentBalance money,
        CreditCustomerCurrentBalanceDate date,
        FOREIGN KEY(creditCustomerID) REFERENCES tblCreditCustomers(creditCustomerID),
        FOREIGN KEY(creditCustomerProductID) REFERENCES tblProducts(productID),
        FOREIGN KEY(creditCustomerCurrencyID) REFERENCES tblCurrency(currencyID),
        FOREIGN KEY(saleID) REFERENCES tblSales(saleID),
        FOREIGN KEY(indirectCustomerID) REFERENCES tblDebtPayment(indirectCustomerID),
        FOREIGN KEY(debtPaymentID) REFERENCES tblDebtPayment(debtPaymentID)
    )""")

#commit our command
conn.commit()


# 14 TBLADVANCECUSTOMERDETAILS
#Delete table tblAdvanceCustomerDetails if it exists
c.execute("""DROP TABLE IF EXISTS tblAdvanceCustomerDetails""")

#commit our command
conn.commit()

#Create table tblAdvanceCustomerDetails 
c.execute("""CREATE TABLE tblAdvanceCustomerDetails (
        advanceCustomerDetailID integer PRIMARY KEY,
        advanceCustomerID integer,
        advanceCustomerProductID integer,
        advanceCustomerCurrencyID integer,
        advanceCustomerPrice money,
        advanceCustomerPriceDate date,
        advancePaymentID integer,
        indirectCustomerID integer,
        saleID integer,
        advanceCustomerCurrentLiterBalance integer,
        advanceCustomerCurrentLiterBalanceDate date,
        FOREIGN KEY(advanceCustomerID) REFERENCES tblAdvanceCustomers(advanceCustomerID)
        FOREIGN KEY(advanceCustomerProductID) REFERENCES tblProducts(productID),
        FOREIGN KEY(advanceCustomerCurrencyID) REFERENCES tblCurrency(currencyID),
        FOREIGN KEY(advancePaymentID) REFERENCES tblAdvancePayment(advancePaymentID),
        FOREIGN KEY(saleID) REFERENCES tblSales(saleID)        
    )""")

#commit our command
conn.commit()


# 15 TBLONEOFFCUSTOMERDETAIL
#Delete table tblOneOffCustomerDetail if it exists
c.execute("""DROP TABLE IF EXISTS tblOneOffCustomerDetail""")

#commit our command
conn.commit()

#Create table tblOneOffCustomerDetail 
c.execute("""CREATE TABLE tblOneOffCustomerDetail (
        oneOffCustomerDetailID integer PRIMARY KEY,
        oneOffCustomerID integer,
        advancePaymentID integer,
        oneOffCustomerCurrentLiterBalance integer,
        oneOffCustomerCurrentLiterBalanceDate date,
        oneOffCustomerProductPrice money,
        saleID integer,
        FOREIGN KEY(oneOffCustomerID) REFERENCES tblOneOffCustomers(oneOffCustomerID),
        FOREIGN KEY(advancePaymentID) REFERENCES tblAdvancePayment(advancePaymentID),
        FOREIGN KEY(saleID) REFERENCES tblSales(saleID)
    )""")

#commit our command
conn.commit()


# 16 TBLINDIRECTCUSTOMERS
#Delete table tblIndirectCustomers if it exists
c.execute("""DROP TABLE IF EXISTS tblIndirectCustomers""")

#commit our command
conn.commit()

#Create table tblIndirectCustomers 
c.execute("""CREATE TABLE tblIndirectCustomers (
        indirectCustomerID integer PRIMARY KEY,
        indirectCustomerName text,
        indirectCustomerProductID integer,
        indirectCustomerOpeningBalanceDate date,
        indirectCustomerOpeningLiters real,
        FOREIGN KEY(indirectCustomerProductID) REFERENCES tblProducts(productID)
    )""")

#commit our command
conn.commit()


# 17 TBLINDIRECTCUSTOMERDETAIL
#Delete table tblIndirectCustomerDetail if it exists
c.execute("""DROP TABLE IF EXISTS tblIndirectCustomerDetail""")

#commit our command
conn.commit()

#Create table tblIndirectCustomerDetail 
c.execute("""CREATE TABLE tblIndirectCustomerDetail (
        indirectCustomerDetailID integer PRIMARY KEY,
        indirectCustomerID integer,
        indirectCustomerCreditDetailSponsorID integer NULL,
        indirectCustomerAdvanceDetailSponsorID integer NULL,
        indirectCustomerCurrentLiterBalance real,
        indirectCustomerCurrentLiterBalanceDate date,
        saleID integer,
        FOREIGN KEY(indirectCustomerID) REFERENCES tblCreditCustomers(indirectCustomerID),
        FOREIGN KEY(indirectCustomerCreditDetailSponsorID) REFERENCES tblCreditCustomerDetail(creditCustomerDetailID),
        FOREIGN KEY(indirectCustomerAdvanceDetailSponsorID) REFERENCES tblAdvanceCustomerDetail(advanceCustomerDetailID),
        FOREIGN KEY(saleID) REFERENCES tblSales(saleID)
    )""")

#commit our command
conn.commit()


# 18 TBLGAUGE
#Delete table tblGauge if it exists
c.execute("""DROP TABLE IF EXISTS tblGauge""")

#commit our command
conn.commit()

#Create table tblGauge 
c.execute("""CREATE TABLE tblGauge (
        gaugeID integer PRIMARY KEY,
        gaugeDate date,
        gaugeBranchID integer,
        gaugeProductID integer,
        gaugeTankNumber integer,
        FOREIGN KEY(gaugeBranchID) REFERENCES tblBranches(branchID),
        FOREIGN KEY(gaugeProductID) REFERENCES tblProducts(productID)
    )""")

#commit our command
conn.commit()


# 19 TBLDAILYCOLLECTION
#Delete table tblDailyCollection if it exists
c.execute("""DROP TABLE IF EXISTS tblDailyCollection""")

#commit our command
conn.commit()

#Create table tblDailyCollection
c.execute("""CREATE TABLE tblDailyCollection (
        dailyCollectionID integer PRIMARY KEY,
        dailyCollectionDate date,
        dailyCollectionBranchID integer,
        dailyCollectionUSDCurrencyID integer,
        dailyCollectionUSDAmount money,
        dailyCollectionFCCurrencyID integer,
        dailyCollectionFCAmount money,
        exchangeRateID integer,
        advancePaymentID,
        debtPaymentID,
        FOREIGN KEY(dailyCollectionBranchID) REFERENCES tblBranches(branchID),
        FOREIGN KEY(dailyCollectionUSDCurrencyID) REFERENCES tblCurrency(currencyID),
        FOREIGN KEY(dailyCollectionFCCurrencyID) REFERENCES tblCurrency(currencyID),        
        FOREIGN KEY(exchangeRateID) REFERENCES tblExchangeRate(exchangeRateID),
        FOREIGN KEY(advancePaymentID) REFERENCES tblAdvancePayment(advancePaymentID),
        FOREIGN KEY(debtPaymentID) REFERENCES tblDebtPayment(debtPaymentID)
    )""")

#commit our command
conn.commit()


# 20 TBLMAINSUPPLYSTOCK
#Delete table tblMainSupplyStock if it exists
c.execute("""DROP TABLE IF EXISTS tblMainSupplyStock""")

#commit our command
conn.commit()

#Create table tblMainSupplyStock 
c.execute("""CREATE TABLE tblMainSupplyStock (
        supplyID integer PRIMARY KEY,
        supplyDate date,
        supplyBranchID integer,
        supplyProductID integer,
        supplyTruckNumber integer,
        supplyCurrencyID,
        supplyPurchasePrice money,
        supplyLiters real,
        FOREIGN KEY(supplyCurrencyID) REFERENCES tblCurrency(currencyID),
        FOREIGN KEY(supplyBranchID) REFERENCES tblBranches(branchID),
        FOREIGN KEY(supplyProductID) REFERENCES tblProducts(productID)
    )""")

#commit our command
conn.commit()


# 21 TBLINTERBRANCHSUPPLY
#Delete table tblInterBranchSupply if it exists
c.execute("""DROP TABLE IF EXISTS tblInterBranchSupply""")

#commit our command
conn.commit()

#Create table tblInterBranchSupply 
c.execute("""CREATE TABLE tblInterBranchSupply (
        interBranchSupplyID integer PRIMARY KEY,
        interBranchSupplyDate date,
        interBranchReceivingBranchID integer,
        interBranchSupplyingBranchID integer,
        interBranchSupplyProductID integer,
        mainSupplyStockID integer,
        interBranchSupplyLiters real,
        FOREIGN KEY(interBranchReceivingBranchID) REFERENCES tblBranches(branchID),
        FOREIGN KEY(interBranchSupplyingBranchID) REFERENCES tblBranches(branchID),
        FOREIGN KEY(interBranchSupplyProductID) REFERENCES tblProducts(productID),
        FOREIGN KEY(mainSupplyStockID) REFERENCES tblMainSupplyStock(supplyID)
    )""")

#commit our command
conn.commit()


# 22 TBLRETURNEDFUEL
#Delete table tblReturnedFuel if it exists
c.execute("""DROP TABLE IF EXISTS tblReturnedFuel""")

#commit our command
conn.commit()

#Create table tblReturnedFuel 
c.execute("""CREATE TABLE tblReturnedFuel (
        returnedFuelID integer PRIMARY KEY,
        returnedFuelDate date,
        returnedFuelBranchID integer,
        returnedFuelProductID integer,
        returnedFuelPumpID integer,
        returnedFuelLiters real,
        FOREIGN KEY(returnedFuelBranchID) REFERENCES tblBranches(branchID),
        FOREIGN KEY(returnedFuelProductID) REFERENCES tblProducts(productID)        
    )""")

#commit our command
conn.commit()
'''
#terminate the connection
conn.close()

