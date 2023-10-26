from sys import exit as sexit # XD
from os import system

# -- Macro
def clrscr():					system("clear")
def pressEnter():				input()
#def exec_file(namefile)		exec(open(namefile).read())
#def add_cashfund(cf, value):	return cf+value

# ---------- 

def main(void):
	cf = 20 #default cash fund
	choice = 0
	
	
	while choice != "0":
		print_banner(cf)
		choice = print_trunk_menu()
		cf = select_trunk_menu(choice,cf)
		
	return 0
	
def print_banner(cf):
	#clrscr()
	print(f""" 
\t $$$$$$\                      $$\       $$$$$$$$\ $$\      $$\ 
\t$$  __$$\                     $$ |      $$  _____|$$ | $\  $$ |
\t$$ /  \__| $$$$$$\   $$$$$$$\ $$$$$$$\  $$ |      $$ |$$$\ $$ |
\t$$ |       \____$$\ $$  _____|$$  __$$\ $$$$$\    $$ $$ $$\$$ |
\t$$ |       $$$$$$$ |\$$$$$$\  $$ |  $$ |$$  __|   $$$$  _$$$$ |
\t$$ |  $$\ $$  __$$ | \____$$\ $$ |  $$ |$$ |      $$$  / \$$$ |
\t $$$$$$  |\$$$$$$$ |$$$$$$$  |$$ |  $$ |$$ |      $$  /   \$$ |
\t \______/  \_______|\_______/ \__|  \__|\__|      \__/     \__|

 
 FONDO CASSA: {cf}€ 
 -----------------------------------------------------------------------
                                                              """)
def print_trunk_menu():
	done = input("""
 [0] Esci
 [1] Fondo Cassa
 [2] Servizi

 > """)
	return done

def select_trunk_menu(c, cf):
	if c == "1":
		cf = fc_menu("cash fund menu", cf)
	elif c == "2":
		cf = service_menu("service menu", cf) #call servizi
	elif c == "":
		pass
		
	return cf


def fc_menu(banner, cf):
	#clrscr()		 
	print("\n"+banner)
	print("="*len(banner))
	print(" 1. aggiundi cash fund")
	print(" 2. svuota cash fund")
	print(" 3. modifica cash fund\n")
	c = input("cf> ")
	
	if c == "1":
		new_value = int(input("quanto euro vuoi aggiungere al fondo cassa?: "))
		cf += new_value
		
	if c == "2":
		cf = 0
	elif c == "3":
		new_cashfund = int(input("specifica la somma del nuovo fondo cassa: "))
		cf = new_cashfund
	return cf
	

def service_menu(banner, c):		 
	print("\n"+banner)
	print("="*len(banner))
	print(" 1. aggiundi servizi")
	print(" 2. lista servizi lasciati")
	print(" 3. modifica cash fund\n")
	c = input("service> ")
	
if __name__ == '__main__':
	sexit(main(None))
