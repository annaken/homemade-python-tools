import string
import random
import hashlib
from passlib.hash import md5_crypt

# Input file
shadow_infile = open ("user-details.csv",'r')

# Output csv file with all users and using hashed passwords
shadow_outfile = open("user-details-updated.csv",'w')

# Output file with plaintext passwords and usernames for modified users
plaintext_outfile = open("updated-users.csv",'w')

#	if len(line) > 5:
#		print "BAD: " + line[0]

# Generate actual password
def pw_gen():
	pwUC = ''.join(random.choice(string.ascii_uppercase) for _ in range(3)) 
	pwLC = ''.join(random.choice(string.ascii_lowercase) for _ in range(3)) 
	pwD = ''.join(random.choice(string.digits) for _ in range(3)) 
	return pwUC + pwLC + pwD

# Generate hash of password
def pw_hash(pw_plain):
#	return = hashlib.md5(pw_plain).hexdigest()
	return md5_crypt.encrypt(pw_plain)



# Read in csv in format: E-post;Passord;Navn;Rot-dir;Sub-dir
for line in shadow_infile.readlines():
	line = line.replace("\n","").split(";")

	if not '$' in line[1]:

		plaintext_pw = pw_gen()
		hashed_pw = pw_hash(plaintext_pw)

		plaintext_outfile.write(
				line[0] + "\t" + plaintext_pw + "\t" + hashed_pw + "\n")

		shadow_outfile.write(
				line[0] + ";\"" +		#username
				hashed_pw + "\";" + 	#password
				line[2] + ";" +			#name
				line[3] + ";" +			#root dir
				line[4] + "\n" )		#sub dir

	else:
		shadow_outfile.write(
				line[0] + ";\"" +		#username
				line[1] + "\";" + 	#password
				line[2] + ";" +			#name
				line[3] + ";" +			#root dir
				line[4] + "\n" )		#sub dir
