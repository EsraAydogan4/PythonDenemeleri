from datetime import datetime

result = datetime.now()
simdi = result.day
simdi = result.second

simdi = datetime.ctime(result)
simdi = datetime.strftime(result,"%Y")
simdi = datetime.strftime(result,"%X") # güncel saat
simdi = datetime.strftime(result,"%d")
simdi = datetime.strftime(result,"%A") # günlerden ne bugun
simdi = datetime.strftime(result,"%B") # aylardan ne peki
simdi = datetime.strftime(result,"%Y %B %d")


t = "15 April 2014 hour 10:12:30"
simdi = datetime.strptime(t, "%d %B %Y hour %H:%M:%S")
print(simdi)