'''
Created on Nov 25, 2019

@author: ITAUser
'''
'''
For this assignment you should read the task, then below the task do what it asks you to do
EXAMPLE TASK:
'''
#EX) Check if 4 is equal to 5 AND 5 is equal to 5 and store the answer in variable a
a = (4==5) and (5==5)

'''
END OF EXAMPLE
'''

'''
START HERE
'''

#2) Check if 1.24 is equal to 1.25 OR 1.4 is equal to 1.4 
# ) and store the answer in variable c
c = (1.24 == 1.25) and (1.4 == 1.4)
#3) Check if NOT(True is equal to False) and store the answer in variable d
d = ("true" == "false")
#4) Check if [1,2,3] is equal to [1,2,3] OR if ["a", "b", "c"] is equal to 
# )  ["a", "b", "c"] and store the answer in variable e
e = [1,2,3] == [1,2,3] or  ["a", "b", "c"] == ["a", "b", "c"]
#5) Check if 1 is less than or equal to 2 AND if 3 is greater than 2
# ) and store the answer in variable f
f = 1 <= 2 and 3 >2 
#6) Check if 1 is greater than or equal to 2 OR if 3 is greater than 2
# ) and store the answer in variable g
g = 1 >= 2 or 3 > 2
#7) Check if 1.66 is greater than or equal to 1.67 AND if .5 is less than .6 
# ) and store the answer in variable h
h = 1.66 >= 1.67 and .5 < .6
#8) Check if 1.66 is less than or equal to 1.67 OR if .5 is less than .6 
# ) and store the answer in variable i
i = 1.66 <= 1.67 or .5 < .6
#9) Check if 1 is less than 2 AND if 1 is equal to 0 
# ) and store the answer in variable j
j = 1 < 2 and 1 = 0
#10) Check if NOT(1 is greater than 2) and store the answer in variable k
k = 1 > 2
'''
For the next section, you will be reading comparison statements and determining their answer
EXAMPLE:
'''
#EX) 4 == 5 and 5 == 5
False

'''
END OF EXAMPLE
'''

'''
START HERE
'''

#1) 4 == 5 and 5 == 5
"false"
#2) 5 == 5 or 5 == 4
"false"
#3) not 3 == 3
"true"
#4) a = 2
# ) not a == 2
"true"
#5) a = 3
# ) b = 2
# ) a == b and b == 4
"false"
#6) a = 4
# ) b = 4
# ) a == b or b == 4
"true"
#7) a = 6
# ) b = (12/2)
# ) a == b and b == (24/4)
"false"
#8) a = (3/3)
# ) b = (13/13)
# ) a == b or b == 1
"false"
#9) a = 3
# ) b = math.sqrt(9)
# ) c = 2
# ) a == b and b == c
"false"
#10) a = "word"
#  ) b = "Word"
#  ) c = "Word"
#  ) a == b or b == c
"true"
#11) (10/5) == (12/6) and math.sqrt(9) == 3
"true"
#12) (14/7) == (15/5) or math.sqrt(9) == 3
"false"
#13) a = 10
#  ) b = 5
#  ) (a/b) == 2 and 2 == 1
"false"
#14) a = 10
#  ) b = 5
#  ) (a/b) == (12/6)
"false"
#15) a = 10
#  ) b = 5
#  ) c = 12
#  ) d = 6
#  ) (a/b) == (12/6) and (c/2) == d
"true"
#16) a = "something"
#  ) b = "some thing"
#  ) a == b and b == 2
"true"
#17) a = "word"
#  ) b = "word"
#  ) word = "incorrect"
#  ) a == b and b == word
"true"
#18) a = True
#  ) a == True and not True == False
"false"
#19) a = True
#  ) b = False
#  ) a == b or not a == b
"true"
#20) a = True
#  ) A = False
#  ) b = False
#  ) A == b or a == b
"true"