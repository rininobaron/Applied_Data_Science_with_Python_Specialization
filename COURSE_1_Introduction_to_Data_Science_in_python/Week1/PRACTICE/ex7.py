lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

correct_answer=[]

for i in lowercase:
	for j in lowercase:
		for k in digits:
			for m in digits:
				correct_answer.append(i+j+k+m)

answer = [i+j+k+m for i in lowercase for j in lowercase for k in digits for m in digits]
print(correct_answer == answer)