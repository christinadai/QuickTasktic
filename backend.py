Def timetodec(timestr):

	Try:
		hrs, min = map( int, timestr.split(‘:’)
		Dectime =(hrs+min)/60.0
		Return dectime
	Except value error:
		print(“Invalid time!”)
