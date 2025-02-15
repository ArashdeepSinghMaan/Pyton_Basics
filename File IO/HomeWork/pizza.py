from tabulate import tabulate
import sys
import csv
def main():
 if len(sys.argv)>2:
   sys.exit("Too many command-line arguments")
 if len(sys.argv)<2:
    sys.exit("Too few coomand-line arguments")
 file= sys.argv[1] 
 if not file.endswith(".csv"):
    sys.exit("Not a CSV file")
 try:
    with open(file,"r") as csvfile:
       reader=csv.reader(csvfile)
       
    table=list(reader)
    print(tabulate(table) )
   
 except FileNotFoundError :
       sys.exit("File does not exist")




if __name__=="__main__":
    main()