import sys
import datetime as dt
import argparse as ap
import gspread as gs


filename = 'GACL'
firstColInd = 'A'
lastRowCell = 'K2'
maxCol = 'J'


def main():

    gc = gs.service_account()

    sh = gc.open(filename)
    nextRowInd = str(int(sh.sheet1.get(lastRowCell)[0][0])+1)

    # Add arguments for sheet name, event label, and traits of commonly logged events
    parser = ap.ArgumentParser(
                                prog = 'logEvent',
                                description = 'Krutulism-toolbox script to log events to a Google Sheet',
                                epilog = 'author Mark Krutulis')
    parser.add_argument('sheetName')
    parser.add_argument('eventType')
    parser.add_argument('-d','--duration')
    parser.add_argument('-r', '--reps')
    parser.add_argument('-n', '-notes')

    args = parser.parse_args()

    datetimestamp = dt.datetime.now().isoformat()
    worksheet = sh.worksheet(args.sheetName)
    rowContents = [[]]

    match args.sheetName:
        case 'Exercises'':
            rowContents = [[datetimestamp, args.eventType, args.duration, args.reps]]

        case 'Nuisances':
            rowContents = [[datetimestamp, args.eventType]]

        case other:
            print('No such sheet name found')

    indexStr = firstColInd + nextRowInd + ':' + maxCol + nextRowInd
    worksheet.update(indexStr, rowContents)


if __name__ == '__main__':
    main()