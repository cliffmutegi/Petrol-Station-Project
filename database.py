"""This program is useful in managing a petrol station. It includes a database and its GUI"""

import sqlite3

#connecting to database
conn = sqlite3.connect('petrolstation.db')

#create a cursor
c = conn.cursor()


'''#TABLES


# 1 TBLCURRENCY # CURRENCY
#Delete table tblCurr if it exists
c.execute("""DROP TABLE IF EXISTS tblCurr""")

#commit our command
conn.commit()

#Create table tblCurr 
c.execute("""CREATE TABLE tblCurr (
        currID integer PRIMARY KEY,
        currSymbol text,
        currName text
    )""")

#commit our command
conn.commit()


# 2 TBLBran # BRANCH
#Delete table tblBran if it exists
c.execute("""DROP TABLE IF EXISTS tblBran""")

#commit our command
conn.commit()

#Create table tblBran 
c.execute("""CREATE TABLE tblBran (
        branID integer PRIMARY KEY,
        branName text
    )""")

#commit our command
conn.commit()


# 3 TBLProd # PRODUCTS
#Delete table tblProd if it exists
c.execute("""DROP TABLE IF EXISTS tblProd""")

#commit our command
conn.commit()

#Create table tblProd 
c.execute("""CREATE TABLE tblProd (
        prodID integer PRIMARY KEY AUTOINCREMENT,
        prodName text
    )""")

#commit our command
conn.commit()


# 4 TBLPRODDETAILS
#Delete table tblProdDetails if it exists
c.execute("""DROP TABLE IF EXISTS tblProdDetails""")

#commit our command
conn.commit()

#Create table tblProdDetails 
c.execute("""CREATE TABLE tblProdDetails (
        prodDetailID integer PRIMARY KEY,
        prodID integer
        prodName text,
        prodCurrID integer,
        branID integer,
        prodWholesalePrice money,
        prodPumpPrice money,
        prodspecialPrice money,
        prodPriceDate date,
        FOREIGN KEY(prodID) REFERENCES tblProd(prodID),
        FOREIGN KEY(prodCurrID) REFERENCES tblCurr(currID),
        FOREIGN KEY(branID) REFERENCES tblBran(branID)
    )""")

#commit our command
conn.commit()


# 5 TBLINDEX
#Delete table tblIndex if it exists
c.execute("""DROP TABLE IF EXISTS tblIndex""")

#commit our command
conn.commit()

#Create table tblIndexes 
c.execute("""CREATE TABLE tblIndex (
        indexID integer PRIMARY KEY,
        indexDate date,
        indexBranID integer,
        indexProdID integer,
        indexPumpNumber integer,
        openingIndex real,
        closingIndex real,
        FOREIGN KEY(indexProdID) REFERENCES tblProd(prodID),
        FOREIGN KEY(indexBranID) REFERENCES tblBran(branID)
    )""")

#commit our command
conn.commit()


# 6 TBLCREDCUST # CREDITCUSTOMER
#Delete table tblCredCust if it exists
c.execute("""DROP TABLE IF EXISTS tblCredCust""")

#commit our command
conn.commit()

#Create table tblCredCust 
c.execute("""CREATE TABLE tblCredCust (
        credCustID integer PRIMARY KEY,
        credCustName text,
        credCustOpeningBalDate date,
        credCustCurrID integer,
        credCustOpeningBal money,
        FOREIGN KEY(credCustCurrID) REFERENCES tblCurr(currID)
    )""")

#commit our command
conn.commit()


# 7 TBLADVCUST # ADVANCECUSTOMER
#Delete table tblAdvCust if it exists
c.execute("""DROP TABLE IF EXISTS tblAdvCust""")

#commit our command
conn.commit()

#Create table tblAdvCust 
c.execute("""CREATE TABLE tblAdvCust (
        advCustID integer PRIMARY KEY,
        advCustName text,
        advCustOpeningBalDate date,
        advCustProdID integer,
        advCustOpeningLtr real,
        advCustOpeningPriceCurrID integer,
        advCustOpeningLtrPrice money,
        advCustOpeningExRate integer,
        FOREIGN KEY(advCustProdID) REFERENCES tblProd(prodID),
        FOREIGN KEY(advCustOpeningPriceCurrID) REFERENCES tblCurr(currID)  
    )""")

#commit our command
conn.commit()


# 8 TBLONEOFFCUST
#Delete table tblOneOffCust if it exists
c.execute("""DROP TABLE IF EXISTS tblOneOffCust""")

#commit our command
conn.commit()

#Create table tblOneOffCust 
c.execute("""CREATE TABLE tblOneOffCust (
        oneOffCustID integer PRIMARY KEY,
        oneOffCustName text,
        oneOffCustBranID integer,
        oneOffCustProdID integer,
        oneOffCustOpeningLtr real,
        oneOffCustOpeningPriceCurrID integer,
        oneOffCustOpeningLtrPrice money,
        oneOffCustOpeningExRate money,
        FOREIGN KEY(oneOffCustBranID) REFERENCES tblBran(branID),
        FOREIGN KEY(oneOffCustProdID) REFERENCES tblProd(prodID),
        FOREIGN KEY(oneOffCustOpeningPriceCurrID) REFERENCES tblCurr(currID)
    )""")

#commit our command
conn.commit()


# 9 TBLINDIRECTCust
#Delete table tblIndirectCust if it exists
c.execute("""DROP TABLE IF EXISTS tblIndirectCust""")

#commit our command
conn.commit()

#Create table tblIndirectCust 
c.execute("""CREATE TABLE tblIndirectCust (
        indirectCustID integer PRIMARY KEY,
        indirectCustName text,
        indirectCustProdID integer,
        indirectCustOpeningBalDate date,
        indirectCustOpeningLtr real,
        FOREIGN KEY(indirectCustProdID) REFERENCES tblProd(ProdID)
    )""")

#commit our command
conn.commit()


# 10 TBLEXRATE
#Delete table tblExRate if it exists
c.execute("""DROP TABLE IF EXISTS tblExRate""")

#commit our command
conn.commit()

#Create table tblExRate 
c.execute("""CREATE TABLE tblExRate (
        exRateID integer PRIMARY KEY,
        exRateDate date,
        exRateBranID integer NULL,
        exRateCredCustID integer NULL,
        exRateAdvCustID integer NULL,
        exRateOneOffCustID integer NULL,
        exRate money,
        FOREIGN KEY(exRateBranID) REFERENCES tblBran(branID),
        FOREIGN KEY(exRateCredCustID) REFERENCES tblCredCust(credCustID),
        FOREIGN KEY(exRateAdvCustID) REFERENCES tblAdvCust(advCustID),
        FOREIGN KEY(exRateOneOffCustID) REFERENCES tblOneOffCust(oneOffCustID)
    )""")

#commit our command
conn.commit()


# 11 TBLDEBTPAY # DEBTPay
#Delete table tblDebtPay if it exists
c.execute("""DROP TABLE IF EXISTS tblDebtPay""")

#commit our command
conn.commit()

#Create table tblDebtPay 
c.execute("""CREATE TABLE tblDebtPay (
        debtPayID integer PRIMARY KEY,
        debtPayDate date,
        debtPayBranID integer,
        credCustID integer,
        debtPayCurrID integer,
        debtPayAmt money,
        debtPayExRateID integer,
        FOREIGN KEY(credCustID) REFERENCES tblCredCust(credCustID)
        FOREIGN KEY(debtPayBranID) REFERENCES tblBran(branID),
        FOREIGN KEY(debtPayCurrID) REFERENCES tblCurr(currID),
        FOREIGN KEY(debtPayExRateID) REFERENCES tblExRate(exRateID)
    )""")

#commit our command
conn.commit()


# 12 TBLADVPAY
#Delete table tblAdvPay if it exists
c.execute("""DROP TABLE IF EXISTS tblAdvPay""")

#commit our command
conn.commit()

#Create table tblAdvPay 
c.execute("""CREATE TABLE tblAdvPay (
        advPayID integer PRIMARY KEY,
        advPayDate date,
        advPayBranID integer,
        advCustID integer,
        oneOffCustID integer,
        advPayProdID integer,
        advPayCurrID integer,
        advPayProdPrice money,
        advPayLtr real,
        advPayExRateID integer,
        FOREIGN KEY(advCustID) REFERENCES tblAdvCust(advCustID),
        FOREIGN KEY(oneOffCustID) REFERENCES tblOneOffCust(oneOffCustID),
        FOREIGN KEY(advPayProdID) REFERENCES tblProd(prodID),
        FOREIGN KEY(advPayBranID) REFERENCES tblBran(branID),
        FOREIGN KEY(advPayCurrID) REFERENCES tblCurr(currID),
        FOREIGN KEY(advPayExRateID) REFERENCES tblExRate(exRateID)
    )""")

#commit our command
conn.commit()


# 13 TBLSALE
#Delete table tblSale if it exists
c.execute("""DROP TABLE IF EXISTS tblSale""")

#commit our command
conn.commit()

#Create table tblSale
c.execute("""CREATE TABLE tblSale (
        saleID integer PRIMARY KEY,
        saleDate date,
        saleBranID integer,
        saleProdID integer,
        wholSaleProdDetailID integer,
        wholSaleLtr real,
        pumpSaleProdDetailID integer,
        pumpSaleLtr real,
        specialSaleProdDetailID integer,
        specialSaleLtr real,
        credCustSaleLtr real,
        advCustSaleLtr real,
        oneOffCustSaleLtr real,
        indirectCustSaleLtr real,
        FOREIGN KEY(saleBranID) REFERENCES tblBran(branID),
        FOREIGN KEY(saleProdID) REFERENCES tblProd(prodID),
        FOREIGN KEY(wholSaleProdDetailID) REFERENCES tblProdDetails(prodDetailID),
        FOREIGN KEY(pumpSaleProdDetailID) REFERENCES tblProdDetails(prodDetailID),
        FOREIGN KEY(specialSaleProdDetailID) REFERENCES tblProdDetails(prodDetailID)
    )""")

#commit our command
conn.commit()


# 14 TBLSALETRANSACTION
#Delete table tblSaleTransaction if it exists
c.execute("""DROP TABLE IF EXISTS tblSaleTransaction""")

#commit our command
conn.commit()

'''#Create table tblSaleTransaction
c.execute("""CREATE TABLE tblSaleTransaction (
        transID integer PRIMARY KEY,
        transDate date,
        transBranID integer,
        transCredCustID integer,
        transAdvCustID integer,
        transOneOffCustID integer,
        transIndirectCustID integer,
        transProdID integer,
        transCurrID integer,
        transPrice real,
        transLtr real,
        transExRateID integer,
        FOREIGN KEY(transBranID) REFERENCES tblBran(branID),
        FOREIGN KEY(transCredCustID) REFERENCES tblCredCust(credCustID),
        FOREIGN KEY(transAdvCustID) REFERENCES tblAdvCust(advCustID),
        FOREIGN KEY(transOneOffCustID) REFERENCES tblOneOffCust(oneOffCustID),
        FOREIGN KEY(transIndirectCustID) REFERENCES tblIndirectCust(indirectCustID),
        FOREIGN KEY(transProdID) REFERENCES tblProd(prodID),
        FOREIGN KEY(transCurrID) REFERENCES tblCurr(currID), 
        FOREIGN KEY(transExRateID) REFERENCES tblExRate(exRateID)       
    )""")

#commit our command
conn.commit()



'''# 15 TBLCredCustDETAILS
#Delete table tblCredCustDetails if it exists
c.execute("""DROP TABLE IF EXISTS tblCredCustDetails""")

#commit our command
conn.commit()


#Create table tblCredCustDetails 
c.execute("""CREATE TABLE tblCredCustDetails (
        credCustDetailID integer PRIMARY KEY,
        credCustID integer,
        credCustProdID integer,
        credCustCurrID integer,
        credCustPrice money,
        credCustPriceDate date,
        transID integer NULL,
        indirectCustID integer NULL,
        debtPayID integer NULL,
        credCustCurrentBal money,
        credCustCurrentBalDate datetime,
        FOREIGN KEY(credCustID) REFERENCES tblCredCust(credCustID),
        FOREIGN KEY(credCustProdID) REFERENCES tblProd(prodID),
        FOREIGN KEY(credCustCurrID) REFERENCES tblCurr(currID),
        FOREIGN KEY(transID) REFERENCES tblSaleTransaction(transID),
        FOREIGN KEY(indirectCustID) REFERENCES tblIndirectCust(indirectCustID),
        FOREIGN KEY(debtPayID) REFERENCES tblDebtPay(debtPayID)
    )""")

#commit our command
conn.commit()


# 16 TBLAdvCustDETAILS
#Delete table tblAdvCustDetails if it exists
c.execute("""DROP TABLE IF EXISTS tblAdvCustDetails""")

#commit our command
conn.commit()

#Create table tblAdvCustDetails 
c.execute("""CREATE TABLE tblAdvCustDetails (
        advCustDetailID integer PRIMARY KEY,
        advCustID integer,
        advCustProdID integer,
        advCustCurrID integer,
        advCustPrice money,
        advCustPriceDate date,
        advPayID integer,
        indirectCustID integer,
        transID integer,
        advCustCurrentLiterBal integer,
        advCustCurrentLiterBalDate datetime,
        FOREIGN KEY(advCustID) REFERENCES tblAdvCust(advCustID)
        FOREIGN KEY(advCustProdID) REFERENCES tblProd(prodID),
        FOREIGN KEY(advCustCurrID) REFERENCES tblCurr(currID),
        FOREIGN KEY(advPayID) REFERENCES tblAdvPay(advPayID),
        FOREIGN KEY(transID) REFERENCES tblSaleTransaction(transID)        
    )""")

#commit our command
conn.commit()


# 17 TBLONEOFFCustDETAIL
#Delete table tblOneOffCustDetail if it exists
c.execute("""DROP TABLE IF EXISTS tblOneOffCustDetail""")

#commit our command
conn.commit()

#Create table tblOneOffCustDetail 
c.execute("""CREATE TABLE tblOneOffCustDetail (
        oneOffCustDetailID integer PRIMARY KEY,
        oneOffCustID integer,
        advPayID integer,
        oneOffCustCurrentLiterBal float,
        oneOffCustCurrentLiterBalDate datetime,
        transID integer,
        FOREIGN KEY(oneOffCustID) REFERENCES tblOneOffCust(oneOffCustID),
        FOREIGN KEY(advPayID) REFERENCES tblAdvPay(advPayID),
        FOREIGN KEY(transID) REFERENCES tblSaleTransaction(transID)
    )""")

#commit our command
conn.commit()


# 18 TBLINDIRECTCustDETAIL
#Delete table tblIndirectCustDetail if it exists
c.execute("""DROP TABLE IF EXISTS tblIndirectCustDetail""")

#commit our command
conn.commit()

#Create table tblIndirectCustDetail 
c.execute("""CREATE TABLE tblIndirectCustDetail (
        indirectCustDetailID integer PRIMARY KEY,
        indirectCustID integer,
        indirectCustCredDetailSponsorID integer NULL,
        indirectCustAdvDetailSponsorID integer NULL,
        indirectCustCurrentLiterBal real,
        indirectCustCurrentLiterBalDate datetime,
        transID integer,
        FOREIGN KEY(indirectCustID) REFERENCES tblCredCust(indirectCustID),
        FOREIGN KEY(indirectCustCredDetailSponsorID) REFERENCES tblCredCustDetail(CredCustDetailID),
        FOREIGN KEY(indirectCustAdvDetailSponsorID) REFERENCES tblAdvCustDetail(AdvCustDetailID),
        FOREIGN KEY(transID) REFERENCES tblSaleTransaction(transID)
    )""")

#commit our command
conn.commit()


# 19 TBLTANKS
#Delete table tblTanks if it exists
c.execute("""DROP TABLE IF EXISTS tblTank""")

#commit our command
conn.commit()

#Create table tblTank 
c.execute("""CREATE TABLE tblTank (
        tankID integer PRIMARY KEY,
        tankBranID integer,
        tankProdID integer,
        tankCapacity integer,
        FOREIGN KEY(tankBranID) REFERENCES tblBran(branID),
        FOREIGN KEY(tankProdID) REFERENCES tblProd(prodID)
    )""")

#commit our command
conn.commit()


# 20 TBLDIP
#Delete table tblDip if it exists
c.execute("""DROP TABLE IF EXISTS tblDip""")

#commit our command
conn.commit()

#Create table tblDip 
c.execute("""CREATE TABLE tblDip (
        dipID integer PRIMARY KEY,
        dipDate date,
        dipBranID integer,
        dipProdID integer,
        dipTankID integer,
        dipQty float,
        FOREIGN KEY(dipBranID) REFERENCES tblBran(BranID),
        FOREIGN KEY(dipProdID) REFERENCES tblProd(ProdID),
        FOREIGN KEY(dipTankID) REFERENCES tblTank(tankID)
    )""")

#commit our command
conn.commit()


# 21 TBLDAILYCOLLECTION
#Delete table tblDailyCollection if it exists
c.execute("""DROP TABLE IF EXISTS tblDailyCollection""")

#commit our command
conn.commit()

#Create table tblDailyCollection
c.execute("""CREATE TABLE tblDailyCollection (
        dailyCollectionID integer PRIMARY KEY,
        dailyCollectionDate date,
        dailyCollectionBranID integer,
        dailyCollectionUSDCurrID integer,
        dailyCollectionUSDAmt money,
        dailyCollectionFCCurrID integer,
        dailyCollectionFCAmt money,
        exRateID integer,
        advPayID integer,
        debtPayID integer,
        FOREIGN KEY(dailyCollectionBranID) REFERENCES tblBran(branID),
        FOREIGN KEY(dailyCollectionUSDCurrID) REFERENCES tblCurr(currID),
        FOREIGN KEY(dailyCollectionFCCurrID) REFERENCES tblCurr(currID),        
        FOREIGN KEY(exRateID) REFERENCES tblExRate(exRateID),
        FOREIGN KEY(advPayID) REFERENCES tblAdvPay(advPayID),
        FOREIGN KEY(debtPayID) REFERENCES tblDebtPay(debtPayID)
    )""")

#commit our command
conn.commit()


# 22 TBLMAINSUPPLYSTOCK
#Delete table tblMainSupplyStock if it exists
c.execute("""DROP TABLE IF EXISTS tblMainSupplyStock""")

#commit our command
conn.commit()

#Create table tblMainSupplyStock 
c.execute("""CREATE TABLE tblMainSupplyStock (
        mainSupplyID integer PRIMARY KEY,
        mainSupplyDate date,
        mainSupplyProdID integer,
        mainSupplyTruckNumber integer,
        mainSupplyCurrID,
        mainSupplyPurchasePrice money,
        mainSupplyLtr real,
        FOREIGN KEY(mainSupplyCurrID) REFERENCES tblCurr(currID),
        FOREIGN KEY(mainSupplyProdID) REFERENCES tblProd(prodID)
    )""")

#commit our command
conn.commit()


# 23 TBLMAINSUPPLYSTOCKTOBran
#Delete table tblMainSupplyStockToBran if it exists
c.execute("""DROP TABLE IF EXISTS tblMainSupplyStockToBran""")

#commit our command
conn.commit()

#Create table tblMainSupplyStockToBran
c.execute("""CREATE TABLE tblMainSupplyStockToBran (
        supplyStockID integer PRIMARY KEY,
        supplyStockDate date,
        mainSupplyID integer,
        supplyStockLtr real,
        FOREIGN KEY(mainSupplyID) REFERENCES tblMainSupplyStock(mainSupplyID)
    )""")

#commit our command
conn.commit()


# 24 TBLINTERBranSUPPLY
#Delete table tblInterBranSupply if it exists
c.execute("""DROP TABLE IF EXISTS tblInterBranSupply""")

#commit our command
conn.commit()

#Create table tblInterBranSupply 
c.execute("""CREATE TABLE tblInterBranSupply (
        interBranSupplyID integer PRIMARY KEY,
        interBranSupplyDate date,
        interBranReceivingBranID integer,
        interBranSupplyingBranID integer,
        mainSupplyStockID integer,
        interBranSupplyLtr real,
        FOREIGN KEY(interBranReceivingBranID) REFERENCES tblBran(branID),
        FOREIGN KEY(interBranSupplyingBranID) REFERENCES tblBran(branID),
        FOREIGN KEY(mainSupplyStockID) REFERENCES tblMainSupplyStock(supplyID)
    )""")

#commit our command
conn.commit()


# 25 TBLRETURNEDFUEL
#Delete table tblReturnedFuel if it exists
c.execute("""DROP TABLE IF EXISTS tblReturnedFuel""")

#commit our command
conn.commit()

#Create table tblReturnedFuel 
c.execute("""CREATE TABLE tblReturnedFuel (
        returnedFuelID integer PRIMARY KEY,
        returnedFuelDate date,
        returnedFuelBranID integer,
        returnedFuelProdID integer,
        returnedFuelPumpID integer,
        returnedFuelLtr real,
        FOREIGN KEY(returnedFuelBranID) REFERENCES tblBran(branID),
        FOREIGN KEY(returnedFuelProdID) REFERENCES tblProd(prodID)        
    )""")

#commit our command
conn.commit()'''


#terminate the connection
conn.close()

