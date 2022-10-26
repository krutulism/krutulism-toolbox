import gspread

gc = gspread.service_account()

sh = gc.open("GACL")

print(sh.sheet1.get('A1'))