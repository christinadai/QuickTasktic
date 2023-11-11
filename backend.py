Def timetodec(timestr):

	Try:
		hrs, mins = map(int, timestr.split(‘:’))
		dectime =(hrs+mins)/60.0
		Return dectime
	Except value error:
		print(“Invalid time!”)
