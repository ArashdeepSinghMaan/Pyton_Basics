import sys
import csv

def main():
    if len(sys.argv)>3:
        sys.exit("Too many command-line arguments")
    if len(sys.argv)<3:
        sys.exit("Too few command-line arguments")
    
    ends=sys.argv[1]
    ends_1=sys.argv[2]

    if not ends.endswith(".csv") or not ends_1.endswith(".csv"):
        sys.exit("Not a CSV file")
    
    output=[]
    try:
        with open(ends,"r") as csvfile:
            reader=csv.DictReader(csvfile)
            for row in reader:
                split_=row["name"].split(",")
                output.append({'first':split_[1].lstrip(),"last":split_[0],"house":row["house"]})
    except FileNotFoundError  :
         sys.exit(f"Could not read {ends}")
    with open(sys.argv[2],"w") as file:
        writer=csv.DictWriter(file,fieldnames=["first","last","house"])
        writer.writerow({"first":"first"})
        for row in output:
            writer.writerow({"first":row["first"],"last":row["last"],"house":row["house"]})
      

if __name__=="__main__":
    main()