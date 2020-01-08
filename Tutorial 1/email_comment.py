#Given a file "idlist.txt" with student id numbers of many students,
#add "@link.cuhk.edu.cn" after them to get a list of email addresses
#in a file "emailist.txt", output the number of students on the shell.
position=0    # position of the element in a string
email=""      # the string of an email address
email_list=[] # the list of all email addresses

#U forgot cross platform support u fool
import os
this_folder = os.path.dirname(os.path.abspath(__file__))
id_list = os.path.join(this_folder, 'idlist.txt')

# to generate a full list of email addresses of students
while email!="@link.cuhk.edu.cn":
    # open the file for reading in text mode
    with open(id_list,'rt') as f: #Changed to reference os.path
        # +9 equals to the length of a student id, e.g, 118010242
        studentid=f.read()[position:(position+9)]
        # print('studentid:', studentid)
        email=studentid + "@link.cuhk.edu.cn"
        # print('email:', email)
        email_list.append(email)
        # 10 equals to the length of a student id and '\n' symbol
        position+=10

# print("email_list:", email_list)
# print("length/len:", len(email_list))

# to convert email_list to a file named emaillist.txt

# open the file for writing in text mode
with open('emaillist.txt','wt') as f:
    amount=0                    # the number of students
    email=email_list[amount]    # email equals to the first element of email_list 
    
    while email!="@link.cuhk.edu.cn":
        f.write(email)
        f.write('\n')
        amount+=1
        email=email_list[amount]    # email is equals to the amount-th element of email_list
        # print('email', email)
print('amount:', amount)
