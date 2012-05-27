def get_sampled_users():
	ratings_file = open('sampleRatings.dat')
	users = [(line.split(','))[0].strip() for line in ratings_file.readlines()]
	user_file = open('users.dat')
	user_info = [x for x in user_file.readlines() if x.split(',')[0] in users]
	sampled_user = open('sampled_users','wb')
	for u in user_info:
		sampled_user.write(u)
	sampled_user.close()

get_sampled_users()
