weight = float(input('weight : ?'))
height = float(input('height : ?'))
bmi = weight / ((height / 100)*(height / 100))
print('bmi = ', bmi)

if_end = input('if_end : ?')
if if_end == 'if_end':
	raise SystemExit

if bmi < 18.5:
	print('light')
elif bmi >= 18.5 and bmi < 24:
	print('fit')
elif bmi >= 24 and bmi < 27:
	print('overweight')
elif bmi >= 27 and bmi < 30:
	print('light fat')
elif bmi >= 30 and bmi < 35:
	print('medium fat')			
else:
	print('very fat')
 