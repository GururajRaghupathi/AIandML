'''
Credit Card Loan Approver
2 classes: Good Credit, Bad Credit
2 Features: Average Monthly Spend, NumLatePayments
We have scaled all the features so that Average Monthly Spend is between 1, and 12, and
NumLatePayments is between 1 and 12
X axis = NumLatePayments in last 2 years,
Y Axis = Avg MonthlySpend in Last2 years
TrainingData:
{"Good": [ (0, 1), (0,2), (0,3), (0,4), (0, 5), (0, 6), (0, 7), (1, 7), (2,7), (2, 10), (3, 10), (4, 12), (1,8), (2, 9), (1, 5), (1,6)],
"Bad": [ ( 0, 0), (1,1), (1, 2), (1,3), (2,3), (2,4), (3, 4), (3, 5), (3,6), (3,7), (4, 8), (5,6), (5,8), (6, 9), (6,10), (6, 12), (7,12)]
'''

import csv
import random
import math
import operator

class Good():

    def __init__(self,NumLatePayments=[],Avg_MonthlySpend=[]):
        self.NumLatePayments = NumLatePayments
        self.Avg_MonthlySpend = Avg_MonthlySpend

    def getNumLatePayments(self):
        return self.NumLatePayments

    def getAvg_MonthlySpend(self):
        return self.Avg_MonthlySpend

class Bad():

    def __init__(self,NumLatePayments=[],Avg_MonthlySpend=[]):
        self.NumLatePayments = NumLatePayments
        self.Avg_MonthlySpend = Avg_MonthlySpend

    def getNumLatePayments(self):
        return self.NumLatePayments

    def getAvg_MonthlySpend(self):
        return self.Avg_MonthlySpend


class CreditCardLoanApprover:

    def loadGoodDataSet(self,goodList=[]):
        self.gooList = goodList
        numLatePaymentsList = []
        avg_MonthlySpendList = []
        for x in range(len(goodList)):
            row = goodList[x][0]
            col = goodList[x][1]
            numLatePaymentsList.append(row)
            avg_MonthlySpendList.append(col)
        return(numLatePaymentsList,avg_MonthlySpendList)

    def loadBadDataSet(self,badList=[]):
        self.badList = badList
        numLatePaymentsList = []
        avg_MonthlySpendList = []
        for x in range(len(badList)):
            row = badList[x][0]
            col = badList[x][1]
            numLatePaymentsList.append(row)
            avg_MonthlySpendList.append(col)
        return(numLatePaymentsList,avg_MonthlySpendList)

    def euclideanDistance(instance1, instance2, length):
        distance = 0
        for x in range(length):
            distance += pow((instance1 - instance2[x]), 2)
        return math.sqrt(distance)

    def getNeighbors(self,testList=[],goodObj=Good(),badObj=Bad()):
        print("Good Class Row: ", goodObj.getNumLatePayments())
        print("Good Class Col: ", goodObj.getAvg_MonthlySpend())
        print("Bad Class Row: ", badObj.getNumLatePayments())
        print("Bad Class Col: ", badObj.getAvg_MonthlySpend())
        distance = []
        len_good = len(goodObj.getNumLatePayments())
        print(testList)
        for x in range(len_good):
            dist_row = self.euclideanDistance(testList[0][0], goodObj.getNumLatePayments(), int(len_good))
            distance.append(dist_row)
        print(distance)


    def main(self):
        goodList = [(0, 1), (0,2), (0,3), (0,4), (0, 5), (0, 6), (0, 7), (1, 7), (2,7), (2, 10), (3, 10), (4, 12), (1,8), (2, 9), (1, 5), (1,6)]
        badList = [(0, 0), (1,1), (1, 2), (1,3), (2,3), (2,4), (3, 4), (3, 5), (3,6), (3,7), (4, 8), (5,6), (5,8), (6, 9), (6,10), (6, 12),(7,12)]
        #self.loadDataSet(goodList, badList)
        #creditCardLoanObj = CreditCardLoan()
        goodObj =  Good(self.loadGoodDataSet(goodList)[0],self.loadGoodDataSet(goodList)[1])
        badObj = Bad(self.loadBadDataSet(badList)[0],self.loadBadDataSet(badList)[1])
        testList = [(2,6)]
        for x in range(len(testList)):
            neighbors =  self.getNeighbors(testList[x],goodObj,badObj)


creditCardLoanApproverObj = CreditCardLoanApprover()
creditCardLoanApproverObj.main()
