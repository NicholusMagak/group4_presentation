def Calculate_Return(beginningVal,endingVal):
	IG = endingVal - beginningVal
	IG_Growth = "{:.2%}".format(IG / beginningVal)
	return IG_Growth

InvestmentGrowth(2000000,4000000)
