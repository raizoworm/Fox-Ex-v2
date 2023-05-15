import sys, os

def input_Fox(txt):
	try :
		if (sys.version_info[0] < 3):
			return raw_input(txt).strip()
		else :
			sys.stdout.write(txt)
			return input()
	except:
		return False

print """  
  [#] Create By ::
	  ___                                                    ______        
	 / _ \                                                   |  ___|       
	/ /_\ \_ __   ___  _ __  _   _ _ __ ___   ___  _   _ ___ | |_ _____  __
	|  _  | '_ \ / _ \| '_ \| | | | '_ ` _ \ / _ \| | | / __||  _/ _ \ \/ /
	| | | | | | | (_) | | | | |_| | | | | | | (_) | |_| \__ \| || (_) >  < 
	\_| |_/_| |_|\___/|_| |_|\__, |_| |_| |_|\___/ \__,_|___/\_| \___/_/\_\ 
	                          __/ | Lists Splitter
	                         |___/ 
"""
	
	
if(len(sys.argv) != 4):
    yList = str(input_Fox('   Your List --> : '))
    maxi = int(input_Fox('   Maximum of every list --> : '))
    exp = str(input_Fox('   Your Exploiter --> : '))
else:
     yList = str(sys.argv[1])
     maxi = int(sys.argv[2])
     exp = str(sys.argv[3])

def run(yList, maxi, exp):
	sites = open(yList,'r')
	number = 1
	counter = 1
	for site in sites :
		try :
			site = site.strip()
			if counter <= maxi:
				open('list-'+str(number)+'.txt', 'a').write(site+'\n')
				counter = counter + 1
			else :
				os.system("start cmd /c " + exp + ' list-'+str(number)+'.txt')
				number = number + 1
				open('list-'+str(number)+'.txt', 'a').write(site+'\n')
				counter = 2
		except :
			pass
	os.system("start cmd /c " + exp + ' list-'+str(number)+'.txt')
	print ('\n   ./Done')
run(yList, maxi, exp)