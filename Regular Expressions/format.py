import re

name=input("What is your name?").strip()
if matches:=re.search(r"^(.+), ?(.+)$",name):
    name=matches.group


print(f"hello,{first}{last}")