password = "a123456"
i = 3
while i > 0:
	i = i - 1
	pwd = input("請輸入登入密碼:")
	if pwd == password:
		print("登入成功")
		break
	else:
		print("密碼錯誤!")
		if i > 0:
			print("還有", i, "次機會")
		else:
			print("錯誤已達上限")
		# if i > 0:		
		# 	print("密碼錯誤,還有", i, "次機會")
		# elif i <= 0:
		# 	print("密碼錯誤已達上限")



	