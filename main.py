import random
import time
from colorama import Fore, Back, Style
from os import system
from statistics import mean


system('title MATHEMATICS TRAINING')

max_value = 20

points = 0
mistakes = 0
corrects = 0
tries = 0

timestat = []


colx = [Fore.MAGENTA, Fore.BLUE, Fore.WHITE,  Fore.CYAN, Fore.YELLOW]

while True:
	system('cls')
	if points >= 0:
		s3s = Fore.MAGENTA
	else:
		s3s = Fore.RED
	print ('\n\n\t\t[ ' + Fore.YELLOW + str(tries) + Fore.GREEN + ' ] ', end='')
	print(' [ ' + s3s + str(points) + Fore.GREEN +' :: ' + Fore.RED+  str(mistakes) + Fore.GREEN+ ' :: ' + Fore.WHITE + str(corrects) + Fore.GREEN + ' ]', end='')
	if tries > 0:
		perc = ((corrects/tries) * 100)
		if perc >= 50:
			s4s = Fore.MAGENTA
		else:
			s4s = Fore.RED
		print('  [ ' + s4s +  str(round(perc, 2)) + '%' + Fore.GREEN +' ]', end='')


	if tries > 1:
		t_stat = mean(timestat)
		print(' [ ' + Fore.CYAN +  str(round(t_stat, 2)) + 's' + Fore.GREEN +' ]')


	print ('\n\t\t' + Back.WHITE + Fore.BLACK + 'Which of the following is bigger? 0 if equal.\n\n' + Fore.RESET + Back.RESET)

	# flag for choice 1
	flag = random.randint(1, 4)
	dxc1 = random.choice(colx)
	print (dxc1 + '\t\t[1]\t', end='')
	if flag == 1: # sum choice
		n1 = random.randint(1, max_value)
		n2 = random.randint(1, max_value)
		n3 = n1 + n2
		ans1 = n3
		print ('( ' + str(n1) + '  +  ' + str(n2) + ' )')
	elif flag == 2: # subtraction choice
		n1 = random.randint(1, max_value)
		n2 = random.randint(1, max_value)
		if n2 > n1:
			a = n1
			n1 = n2 
			n2 = a
		n3 = n1 - n2
		ans1 = n3
		print ('( ' + str(n1) + '  -  ' + str(n2) + ' )')
	elif flag == 3: # mix choice 1 (x - y) + z
		n1 = random.randint(1, max_value)
		n2 = random.randint(1, max_value)
		if n2 > n1:
			a = n1
			n1 = n2 
			n2 = a
		n3 = random.randint(1, max_value)
		n4 = (n1 - n2) + n3
		ans1 = n4
		print ('( ' + str(n1) + '  -  ' + str(n2) + ' ) + ' + str(n3))
	elif flag == 4: # mix choice 2 (x + y) - z
		n1 = random.randint(1, max_value)
		n2 = random.randint(1, max_value)
		n3 = random.randint(1, max_value)
		while (n3 > (n1 + n2)):
			n3 = random.randint(1, max_value)
		n4 = (n1 + n2) - n3
		ans1 = n4
		print ('( ' + str(n1) + ' + ' + str(n2) + ' ) - ' + str(n3))

	# flag for choice 2
	flag2 = random.randint(1, 4)
	ss = [Fore.MAGENTA, Fore.BLUE, Fore.WHITE,  Fore.CYAN, Fore.YELLOW]
	ss.remove(dxc1)
	aaa = random.choice(ss)
	print (aaa + '\t\t[2]\t', end='')
	if flag2 == 1: # sum choice

		m1 = random.randint(1, max_value)
		m2 = random.randint(1, max_value)
		m3 = m1 + m2
		ans2 = m3
		print ('( ' + str(m1) + '  +  ' + str(m2) + ' )')
	elif flag2 == 2: # subtraction choice
		m1 = random.randint(1, max_value)
		m2 = random.randint(1, max_value)
		if m2 > m1:
			a = m1
			m1 = m2 
			m2 = a
		m3 = m1 - m2
		ans2 = m3
		print ('( ' + str(m1) + '  -  ' + str(m2) + ' )')
	elif flag2 == 3: # mix choice 1 (x - y) + z
		m1 = random.randint(1, max_value)
		m2 = random.randint(1, max_value)
		if m2 > m1:
			a = m1
			m1 = m2 
			m2 = a
		m3 = random.randint(1, max_value)
		m4 = (m1 - m2) + m3
		ans2 = m4
		print ('( ' + str(m1) + '  -  ' + str(m2) + ' ) + ' + str(m3))
	elif flag2 == 4: # mix choice 2 (x + y) - z
		m1 = random.randint(1, max_value)
		m2 = random.randint(1, max_value)
		m3 = random.randint(1, max_value)
		while (m3 > (m1 + m2)):
			m3 = random.randint(1, max_value)
		m4 = (m1 + m2) - m3
		ans2 = m4
		print ('( ' + str(m1) + '  +  ' + str(m2) + ' ) - ' + str(m3))


	if ans1 > ans2:
		cor_ans = 1
	elif ans1 < ans2:
		cor_ans = 2
	elif ans1 == ans2:
		cor_ans = 0

	print(Fore.GREEN, end='')
	start = time.time()
	us_ans = input('\n\n\t\t[::>     ')
	end = time.time()
	stat_temp = end - start
	timestat.append(stat_temp)
	dxc1 = colx
	ss = colx
	aaa = colx

	if str(us_ans) != str(cor_ans):
		print (Fore.RED + '\n\t\tWRONG!' + Fore.GREEN)
		time.sleep(.25)
		print('\n\t\t[1]\t', ans1)
		print('\t\t[2]\t', ans2)
		mistakes = mistakes + 1
		points = points - 1
		s = input('\n\t\tPRESS ENTER TO CONTINUE.')
		dxc1 = colx
		ss = colx
		aaa = colx
	else:
		points = points + 1
		corrects = corrects + 1
		dxc1 = colx
		ss = colx
		aaa = colx

	tries = tries + 1
