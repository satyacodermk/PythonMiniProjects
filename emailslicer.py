#========= Email Slicer is the Program to get the domain name and user name ==========

#get user email address
email=input('Enter your Email =').strip()

#slice out user name
user=email[:email.index("@")]

#slice out domain name
domain=email[email.index('@')+1:]

#format the message and print the result

output="Your User name is: {} \n Your domain name is: {}".format(user,domain)

#Finally Printing the result
print(output)
