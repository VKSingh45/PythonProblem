import sys
fh=open(r"C:/Users/Annu/Desktop/Book1.xlsx")
line1=fh.read()
line2=fh.read()
sys.stdout.write(line1)
sys.stdout.write(line2)
sys.stderr.write("No Error Occured "'\n')
