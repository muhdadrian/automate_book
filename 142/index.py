# optionally, a str arg will specify which chars on the ends should be stripped.

spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('ampS'))

# passing strip() the arg 'ampS' will tell it to strip occurences of a,m,p, and capital S from the ends of the str stored in spam. 

# the order of the chars in the str passed to strip() does not matter: strip('ampS') will do the same things as strip('mapS') or strip('Spam').