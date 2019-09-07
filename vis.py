import os

all_dirs = [x[0] for x in os.walk("./")]

cwd = "/afs/hephy.at/user/m/msajatovic/www/php-plots"
for directory in all_dirs :
	if ("res" in directory) or (".git" in directory) or (directory=="./") : 
		continue
	print directory

	os.chdir(directory)
	if os.path.isfile("index.php") == False :
		#os.system("rm index.php")
	 	os.system("ln -s {0}/index.php".format(cwd))
	if os.path.isfile("res") == False : 	
	 	os.system("ln -s {0}/res".format(cwd))
	os.chdir(cwd)
print "your plots are online"
