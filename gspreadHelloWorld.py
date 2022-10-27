import sys
import gspread as gs

gc = gs.service_account()

sh = gc.open("GACL")

print(sh.sheet1.get('A1'))




def main():
    args = sys.argv[1:]




if __name__ == '__main__':
    main()