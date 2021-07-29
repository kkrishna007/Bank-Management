from tkinter import *
from datetime import datetime
import mysql.connector

sql_un = input("Enter Your SQL username -> ")
sql_pw = input("Enter Your SQL password -> ")

# Initiate Connection with Server
bank_db = mysql.connector.connect(host = 'localhost', user = sql_un, password = sql_pw)

bank_cursor = bank_db.cursor()


def Table_Check_Database():
	try:
		bank_cursor.execute("USE Bank_DataBase;")
	except:
		bank_cursor.execute("CREATE DATABASE Bank_DataBase;")
		bank_cursor.execute("USE Bank_DataBase;")
		bank_cursor.execute('CREATE TABLE \
				BankDetails(Act_Num INT NOT NULL AUTO_INCREMENT PRIMARY KEY, \
						Name varchar(25), \
						Initial_Deposit decimal, \
						Age int(3), \
						Email varchar(225), \
						UserName varchar(25) NOT NULL UNIQUE, \
						Password varchar(20), \
						Mobile_Number int(12), \
						Date_Of_Birth date, \
						aadhar_Card_Number int(20), \
						Address varchar(225));')

Table_Check_Database()


def Register():
	reg_win = Tk()
	reg_win.geometry("700x710+10+0")
	reg_win.resizable(0, 0)
	reg_win.title("Register Page")

	# Function ->
	def BackHome():
		reg_win.destroy()
		HomePage()

	def UserRegister():
		curdate = datetime.now()
		name = f"{entry_name1.get()} {entry_name2.get()}".title()
		email = entry_email.get()
		un = entry_un.get()
		pw = entry_pw.get() ; cpw = entry_cpw.get()
		dob = entry_dob.get() ; dob = '-'.join(list(reversed(dob.split('-'))))
		yob = dob.split('-')[0]
		age = str(int(curdate.year) - int(yob))
		mobile = entry_mobile.get()
		aadhar = entry_aadhar.get()
		address = entry_address.get(0.0, END)

		lst = [name, email, un, pw, dob, age, mobile, aadhar, address]
		if all(lst) and (" " not in un) and pw == cpw:
			new_data = f"INSERT INTO BankDetails(Name, Initial_Deposit, Age, Email, UserName, Password, Mobile_Number, Date_OF_Birth, aadhar_Card_Number, Address)\
			 		VALUES('{name}', 100, {age}, '{email}', '{un}', '{pw}', {mobile}, '{dob}', {aadhar}, '{address}');"
			try:
				bank_cursor.execute(new_data)
				bank_db.commit()
				reg_win.destroy()
				Login()
			except:
				entry_un.delete(0, END) ; entry_un.insert(0, 'TRY CHANGING UN AND CHECK PW')
				raise


	# Features ->
	label_register = Label(reg_win, text = 'User Registration'.upper(), font = 'times 16 bold', bg = reg_win['bg'])
	label_register.place(x = 220, y = 20)

	lab_name1 = Label(reg_win, text = 'First Name', font = 'times 14 bold', bg = reg_win['bg'])
	lab_name1.place(x = 20, y = 80)

	entry_name1 = Entry(reg_win, font = 'times 14 bold', width = 30)
	entry_name1.place(x = 20, y = 120)
	

	lab_name2 = Label(reg_win, text = 'Last Name', font = 'times 14 bold', bg = reg_win['bg'])
	lab_name2.place(x = 350, y = 80)

	entry_name2 = Entry(reg_win, font = 'times 14 bold', width = 30)
	entry_name2.place(x = 350, y = 120)
	
	
	lab_email = Label(reg_win, text = 'Email', font = 'times 14 bold', bg = reg_win['bg'])
	lab_email.place(x = 20, y = 160)

	entry_email = Entry(reg_win, font = 'times 14 bold', width = 30)
	entry_email.place(x = 20, y = 200)
	
	
	lab_un = Label(reg_win, text = 'Username', font = 'times 14 bold', bg = reg_win['bg'])
	lab_un.place(x = 350, y = 160)

	entry_un = Entry(reg_win, font = 'times 14 bold', width = 30)
	entry_un.place(x = 350, y = 200)
	
	
	lab_pw = Label(reg_win, text = 'Password', font = 'times 14 bold', bg = reg_win['bg'])
	lab_pw.place(x = 20, y = 240)

	entry_pw = Entry(reg_win, font = 'times 14 bold', width = 30, show = '*')
	entry_pw.place(x = 20, y = 280)
	
	
	lab_cpw = Label(reg_win, text = 'Confirm Password', font = 'times 14 bold', bg = reg_win['bg'])
	lab_cpw.place(x = 350, y = 240)

	entry_cpw = Entry(reg_win, font = 'times 14 bold', width = 30, show = '*')
	entry_cpw.place(x = 350, y = 280)
	
	
	lab_dob = Label(reg_win, text = 'Date of Birth(DD-MM-YYYY)', font = 'times 14 bold', bg = reg_win['bg'])
	lab_dob.place(x = 20, y = 320)

	entry_dob = Entry(reg_win, font = 'times 14 bold', width = 30)
	entry_dob.place(x = 20, y = 360)
	
	
	lab_mobile = Label(reg_win, text = 'Mobile Number', font = 'times 14 bold', bg = reg_win['bg'])
	lab_mobile.place(x = 350, y = 320)

	entry_mobile = Entry(reg_win, font = 'times 14 bold', width = 30)
	entry_mobile.place(x = 350, y = 360)
	
	
	lab_aadhar = Label(reg_win, text = 'Aadhar Number', font = 'times 14 bold', bg = reg_win['bg'])
	lab_aadhar.place(x = 20, y = 400)

	entry_aadhar = Entry(reg_win, font = 'times 14 bold', width = 64)
	entry_aadhar.place(x = 20, y = 440)
	

	lab_address = Label(reg_win, text = 'Address', font = 'times 14 bold', bg = reg_win['bg'])
	lab_address.place(x = 20, y = 480)

	entry_address = Text(reg_win, font = 'times 14 bold', width = 65, height = 5)
	entry_address.place(x = 20, y = 520)


	btn_register = Button(reg_win, text = 'Register', width = 20, font = 'times 14 bold', bg = 'black', fg = 'white', command = UserRegister)
	btn_register.place(x = 100, y = 650)

	btn_bhome = Button(reg_win, text = "Back to Home Screen", width = 20, bg = 'black', fg = 'white', font = 'times 14 bold', command = BackHome)
	btn_bhome.place(x = 352, y = 650)

	# The mainloop ->
	reg_win.mainloop()

def Login():
	log_win = Tk()
	log_win.geometry("350x350")
	log_win.resizable(0, 0)
	log_win.title("User Login")

	# Functions ->
	def BackHome():
		log_win.destroy()
		HomePage()

	def User_Login():		
		dic = ['Act_Num', 'Name', 'Deposit', 'Age', 'Email', 'Username', 'Password', 'Mobile', 'DOB', 'Aadhar', 'Address']
		username, pw = entry_user.get(), entry_pw.get()
		bank_cursor.execute(f"SELECT * FROM BankDetails WHERE UserName = '{username}' AND Password = '{pw}'")

		det = bank_cursor.fetchall()
		if det:
			det = list(det[0])
			det = list(det)
			detail_dict = dict(zip(dic, det))
			log_win.destroy()
		else:
			entry_user.delete(0, END) ; entry_pw.delete(0, END)
			entry_user.insert(0, 'INVALID USERNAME OR PASSWORD')
			entry_pw.insert(0, 'INVALID USERNAME OR PASSWORD')
		
		UserAccount(detail_dict)

	# Features ->
	label_login = Label(log_win, text = 'User Login'.upper(), font = 'times 14 bold', bg = log_win['bg'])
	label_login.place(x = 120, y = 20)

	label_user = Label(log_win, text = 'UserName', font = 'times 14 bold', bg = log_win['bg'])
	label_user.place(x = 20, y = 60)

	entry_user = Entry(log_win, font = 'times 13 bold', width = 35)
	entry_user.place(x = 20, y = 100)

	label_pw = Label(log_win, text = 'Password', font = 'times 14 bold', bg = log_win['bg'])
	label_pw.place(x = 20, y = 150)

	entry_pw = Entry(log_win, font = 'times 13 bold', width = 35, show = '*')
	entry_pw.place(x = 20, y = 190)

	btn_ulogin = Button(log_win, text = "Login", width = 15, bg = 'black', fg = 'white', font = 'times 13 bold', command = User_Login)
	btn_ulogin.place(x = 100, y = 240)

	btn_bhome = Button(log_win, text = "Back to Home Screen", width = 20, bg = 'black', fg = 'white', font = 'times 13 bold', command = BackHome)
	btn_bhome.place(x = 72, y = 290)
	
	# The Mainloop ->
	log_win.mainloop()

def Withdraw():
	with_win = Tk()
	with_win.geometry('250x260')
	with_win.title("Withdraw")
	with_win.resizable(0, 0)
	
	# Functions ->
	def Withdraw_Amt():
		if entry_auth.get() == user_details['Password']:
			bank_cursor.execute(f"SELECT Initial_Deposit FROM BankDetails WHERE UserName = '{user_details['Username']}';")
			cur_amt = float(bank_cursor.fetchall()[0][0])
			new_amt = float(entry_amt.get())
			if (new_amt + 100) <= cur_amt:
				with_win.destroy()
				new_bal = cur_amt - new_amt
				bank_cursor.execute(f"UPDATE BankDetails SET Initial_Deposit = {cur_amt - new_amt} WHERE UserName = '{user_details['Username']}'")
				bank_db.commit()
				user_details['Deposit'] = new_bal
				UserAccount(user_details)
			else:
				entry_amt.delete(0, END) ; entry_amt.insert(0, 'INSUFFICIENT BALANCE')
		else:
			entry_amt.delete(0, END) ; entry_amt.insert(0, "INVALID PASSWORD")

	# Features ->
	label_amt = Label(with_win, text = 'Enter Amount', font = 'times 14 bold', bg = with_win['bg'])
	label_amt.place(x = 20, y = 20)

	entry_amt = Entry(with_win, font = 'times 14 bold', width = 20)
	entry_amt.place(x = 20, y = 50)

	label_auth = Label(with_win, text = 'Enter Your Password', bg = with_win['bg'], font = 'times 14 bold')
	label_auth.place(x = 20, y = 100)

	entry_auth = Entry(with_win, width = 20, font = 'times 14 bold', show = '*')
	entry_auth.place(x = 20, y = 130)

	btn_with = Button(with_win, text = 'WITHDRAW', font = 'times 13 bold', bg = 'black', fg = 'white', width = 12, command = Withdraw_Amt)
	btn_with.place(x = 53, y = 170)

	btn_back = Button(with_win, text = 'BACK', font = 'times 13 bold', bg = 'black', fg = 'white', width = 12, command = Withdraw_Amt)
	btn_back.place(x = 53, y = 220)

def Deposit():
	dep_win = Tk()
	dep_win.geometry('250x260')
	dep_win.title("Deposit")
	dep_win.resizable(0, 0)
	
	# Functions ->
	def Deposit_Amt():
		if entry_auth.get() == user_details['Password']:
			bank_cursor.execute(f"SELECT Initial_Deposit FROM BankDetails WHERE UserName = '{user_details['Username']}';")
			cur_amt = float(bank_cursor.fetchall()[0][0])
			new_amt = float(entry_amt.get())
			
			dep_win.destroy()
			new_bal = cur_amt + new_amt
			bank_cursor.execute(f"UPDATE BankDetails SET Initial_Deposit = {cur_amt + new_amt} WHERE UserName = '{user_details['Username']}'")
			bank_db.commit()
			user_details['Deposit'] = new_bal
			UserAccount(user_details)
		
		else:
			entry_amt.delete(0, END) ; entry_amt.insert(0, "INVALID PASSWORD")

	# Features ->
	label_amt = Label(dep_win, text = 'Enter Amount', font = 'times 14 bold', bg = dep_win['bg'])
	label_amt.place(x = 20, y = 20)

	entry_amt = Entry(dep_win, font = 'times 14 bold', width = 20)
	entry_amt.place(x = 20, y = 50)

	label_auth = Label(dep_win, text = 'Enter Your Password', bg = dep_win['bg'], font = 'times 14 bold')
	label_auth.place(x = 20, y = 100)

	entry_auth = Entry(dep_win, width = 20, font = 'times 14 bold', show = '*')
	entry_auth.place(x = 20, y = 130)

	btn_with = Button(dep_win, text = 'Deposit', font = 'times 13 bold', bg = 'black', fg = 'white', width = 12, command = Deposit_Amt)
	btn_with.place(x = 53, y = 170)

	btn_back = Button(dep_win, text = 'BACK', font = 'times 13 bold', bg = 'black', fg = 'white', width = 12, command = Deposit_Amt)
	btn_back.place(x = 53, y = 220)

def Transfer():
	tran_win = Tk()
	tran_win.geometry('250x340')
	tran_win.title("Transfer")
	tran_win.resizable(0, 0)
	
	# Functions ->
	def Transfer_Amt():
		if entry_auth.get() == user_details['Password']:
			ac_num = entry_acno.get()
			ac_num = int(''.join(ac_num.split("XYZ012CC")))
			bank_cursor.execute(f"SELECT Initial_Deposit FROM BankDetails WHERE UserName = '{user_details['Username']}';")
			cur_amt1 = float(bank_cursor.fetchall()[0][0])
			bank_cursor.execute(f"SELECT Initial_Deposit FROM BankDetails WHERE Act_Num = {ac_num};")
			cur_amt2 = float(bank_cursor.fetchall()[0][0])

			new_amt = float(entry_amt.get())
			if (new_amt + 100) <= cur_amt1:
				tran_win.destroy()
				new_bal = cur_amt1 - new_amt
				bank_cursor.execute(f"UPDATE BankDetails SET Initial_Deposit = {cur_amt1 - new_amt} WHERE UserName = '{user_details['Username']}'")
				bank_cursor.execute(f"UPDATE BankDetails SET Initial_Deposit = {cur_amt2 + new_amt} WHERE Act_Num = {ac_num}")
				bank_db.commit()
				user_details['Deposit'] = new_bal
				UserAccount(user_details)
			else:
				entry_amt.delete(0, END) ; entry_amt.insert(0, 'INSUFFICIENT BALANCE')
		
		else:
			entry_amt.delete(0, END) ; entry_amt.insert(0, "INVALID PASSWORD")

	# Features ->
	label_amt = Label(tran_win, text = 'Enter Amount', font = 'times 14 bold', bg = tran_win['bg'])
	label_amt.place(x = 20, y = 20)

	entry_amt = Entry(tran_win, font = 'times 14 bold', width = 20)
	entry_amt.place(x = 20, y = 50)

	label_acno = Label(tran_win, text = 'Enter A/C Number', bg = tran_win['bg'], font = 'times 14 bold')
	label_acno.place(x = 20, y = 100)

	entry_acno = Entry(tran_win, width = 20, font = 'times 14 bold')
	entry_acno.place(x = 20, y = 130)

	label_auth = Label(tran_win, text = 'Enter Your Password', bg = tran_win['bg'], font = 'times 14 bold')
	label_auth.place(x = 20, y = 180)

	entry_auth = Entry(tran_win, width = 20, font = 'times 14 bold', show = '*')
	entry_auth.place(x = 20, y = 210)

	btn_with = Button(tran_win, text = 'Transfer', font = 'times 13 bold', bg = 'black', fg = 'white', width = 12, command = Transfer_Amt)
	btn_with.place(x = 53, y = 250)

	btn_back = Button(tran_win, text = 'BACK', font = 'times 13 bold', bg = 'black', fg = 'white', width = 12, command = Transfer_Amt)
	btn_back.place(x = 53, y = 300)

def UserAccount(details):
	global user_details
	user_details = details

	act_win = Tk()
	act_win.resizable(0, 0)
	act_win.geometry('400x400')
	act_win.title(f"{user_details['Name']}")

	# Functions ->
	def Withdraw_Win():
		act_win.destroy()
		Withdraw()

	def Deposit_Win():
		act_win.destroy()
		Deposit()

	def Transfer_Win():
		act_win.destroy()
		Transfer()

	# Features ->
	label_actnum = Label(act_win, text = f'Account Number >> XYZ012CC{user_details["Act_Num"]}', bg = act_win['bg'], font = 'times 14 bold')
	label_actnum.place(x = 20, y = 20)

	label_name = Label(act_win, text = f'Full Name >> {user_details["Name"]}', bg = act_win['bg'], font = 'times 14 bold')
	label_name.place(x = 20, y = 55)

	label_curbal = Label(act_win, text = f'Current Balance >> {user_details["Deposit"]} INR', bg = act_win['bg'], font = 'times 14 bold')
	label_curbal.place(x = 20, y = 90)

	btn_withdraw = Button(act_win, text = 'Withdraw Money', bg = 'black', fg = 'white', width = 30, font = 'times 13 bold', command = Withdraw_Win)
	btn_withdraw.place(x = 50, y = 160)

	btn_deposit = Button(act_win, text = 'Deposit Money', bg = 'black', fg = 'white', width = 30, font = 'times 13 bold', command = Deposit_Win)
	btn_deposit.place(x = 50, y = 210)

	btn_transfer = Button(act_win, text = 'Transfer Money', bg = 'black', fg = 'white', width = 30, font = 'times 13 bold', command = Transfer_Win)
	btn_transfer.place(x = 50, y = 260)

	# The Mainloop ->
	act_win.mainloop()

def HomePage():
	home_win = Tk()
	home_win.geometry("300x300")
	home_win.resizable(0, 0)
	home_win.title("Home Window")

	# Functions ->
	def Login_Win_Chan():
		home_win.destroy()
		Login()

	def Regis_Win_Chan():
		home_win.destroy()
		Register()

	# Features ->
	label_home = Label(home_win, text = 'HOME PAGE', font = 'times 14 bold', bg = home_win['bg'])
	label_home.place(x = 89, y = 20)

	btn_login = Button(home_win, text = 'Login', font = 'times 13 bold', width = 25, bg = 'black', fg = 'white', command = Login_Win_Chan)
	btn_login.place(x = 20, y = 80)

	btn_regis = Button(home_win, text = 'Register', font = 'times 13 bold', width = 25, bg = 'black', fg = 'white', command = Regis_Win_Chan)
	btn_regis.place(x = 20, y = 120)

	btn_credit = Button(home_win, text = 'XYZ BANK', font = 'times 13 bold', width = 25, bg = 'black', fg = 'white')
	btn_credit.place(x = 20, y = 250)

	# The Mainloop
	home_win.mainloop()

HomePage()
