import re
import numpy as np

print("Question 1")
"""
Question 1
"What will be the output of the following code?
"""
string = 'bat, lat, mat, bet, let, met, bit, lit, mit, bot, lot, mot'
result = re.findall('b[ao]t', string)
print(result)
print()

print("Question 2")
"""
Question 2
Assume a and b are two (20, 20) numpy arrays. The L2-distance (defined above) between two equal dimension arrays can be calculated in python as follows:
"""
def l2_dist(a, b):
    result = ((a - b) * (a - b)).sum()
    result = result ** 0.5
    return result
"""
Which of the following expressions using this function will produce a different result from the rest?

Options:

1. l2_dist(a.T, b.T)


2. l2_dist(np.reshape(a, (20 * 20)), np.reshape(b, (20 * 20)))


3. l2_dist(a, b)


4. l2_dist(np.reshape(a, (20 * 20)), np.reshape(b, (20 * 20, 1)))

"""
a = np.arange(1,401,1).reshape(20,20)
b = np.arange(1,401,1).reshape(20,20)
try:
	print("Option 1")
	print(l2_dist(a.T, b.T))
except Exception as e:
	print(e)
try:
	print("Option 2")
	print(l2_dist(np.reshape(a, (20 * 20)), np.reshape(b, (20 * 20))))
except Exception as e:
	print(e)
try:
	print("Option 3")
	print(l2_dist(a, b))
except Exception as e:
	print(e)
try:
	print("Option 4")
	print(l2_dist(np.reshape(a, (20 * 20)), np.reshape(b, (20 * 20, 1))))
except Exception as e:
	print(e)
print()

print("Question 3")
"""
Question 3
Consider the following variables in Python:
"""
a1 = np.random.rand(4)
a2 = np.random.rand(4, 1)
a3 = np.array([[1, 2, 3, 4]])
a4 = np.arange(1, 4, 1)
a5 = np.linspace(1 ,4, 4)
"""
Which of the following statements regarding these variables is correct?

a5.shape == a1.shape


a1.shape == a2.shape


a3.shape == a4.shape


a4.ndim() == 1
"""
try:
	print("Option 1")
	print(a5.shape == a1.shape)
except Exception as e:
	print(e)
try:
	print("Option 2")
	print(a1.shape == a2.shape)
except Exception as e:
	print(e)
try:
	print("Option 3")
	print(a3.shape == a4.shape)
except Exception as e:
	print(e)
try:
	print("Option 4")
	print(a4.ndim() == 1)
except Exception as e:
	print(e)
print()

print("Question 4")
"""
Question 4
Which of the following is the correct output for the code given below?
"""
old = np.array([[1, 1, 1], [1, 1, 1]])
new = old
new[0, :2] = 0

print(old)
print()

print("Question 6")
"""
Question 6
"""
s = 'ACBCAC'
"""
For the given string, which of the following regular expressions can be used to check if the string starts with 'AC'?
"""
print(re.findall('^AC', s))
print()

print("Question 7")
"""
Question 7
What will be the output of the variable L after the following code is executed?
"""
s = 'ACAABAACAAAB'
result = re.findall('A{1,2}', s)
L = len(result)
print(L)
print()

print("Question 8")
"""
Question 8
Which of the following is the correct regular expression to extract all the phone numbers from the following chunk of text:
"""
text="Office of Research Administration: (734) 647-6333 | 4325 North Quad\nOffice of Budget and Financial Administration: (734) 647-8044 | 309 Maynard, Suite 205\nHealth Informatics Program: (734) 763-2285 | 333 Maynard, Suite 500\nOffice of the Dean: (734) 647-3576 | 4322 North Quad\nUMSI Engagement Center: (734) 763-1251 | 777 North University\nFaculty Adminstrative Support Staff: (734) 764-9376 | 4322 North Quad"
my_code=r"\(\d{3}\) \d{3}-\d{4}"
print(re.findall(my_code,text))
print()
# Find solution
solutions = [r"\d{3}\s\d{3}[-]\d{4}", r"[(]\d{3}[)]\d{3}[-]\d{4}", r"\d{3}[-]\d{3}[-]\d{4}", r"[(]\d{3}[)]\s\d{3}[-]\d{4}"]
for i, solution in enumerate(solutions):
	try:
		print(i+1)
		print(re.findall(solution,text))
	except Exception as e:
		print(e)
print()

print("Question 9")
"""
Question 9
Which of the following regular expressions can be used to get the domain names (e.g. google.com, www.baidu.com) from the following sentence?
"""
text='I refer to https://google.com and I never refer http://www.baidu.com if I have to search anything'
solutions=[r"(?<=https:\/\/)([A-Za-z0-9.]*)", r"(?<=https:\/\/)([.]*)", r"(?<=[https]:\/\/)([A-Za-z0-9.]*)", r"(?<=https:\/\/)([A-Za-z0-9]*)"]
for i,solution in enumerate(solutions):
	try:
		print(i+1)
		print(re.findall(solution,text))
	except Exception as e:
		print(e)
print()

print("Question 10")
"""
Question 10
The text from the Canadian Charter of Rights and Freedoms section 2 lists the fundamental freedoms afforded to everyone. Of the four choices provided to replace X in the code below, which would accurately count the number of fundamental freedoms that Canadians have?
"""
text=r'''Everyone has the following fundamental freedoms:
    (a) freedom of conscience and religion;
    (b) freedom of thought, belief, opinion and expression, including freedom of the press and other media of communication;
    (c) freedom of peaceful assembly; and
    (d) freedom of association.'''

solutions=[r"\(.\)", r"(.)", r'freedom', r'[a-d]']
for i,solution in enumerate(solutions):
	try:
		print(i+1)
		print("count:",len(re.findall(solution,text)))
	except Exception as e:
		print(e)
print()