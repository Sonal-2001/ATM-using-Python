# -*- coding: utf-8 -*-
"""ATM.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1H6rLDaFMWtUHnd18BfTH4XSesu9-o64b
"""

while True:
  balance=10000
  print("  ATM  ")
  print("""
  1)    Balance
  2)    Withdraw
  3)    Deposit
  4)    Quit
  """)
  try:
    Option= int(input("Enter Option:  "))
  except Exception as e:
    print("Error:",e)
    print("Enter 1,2,3 or 4 only")
    continue
  if Option==1:
    print("Balance Rs",balance)
  if Option==2:
    print("Balance Rs ",balance)
    Withdraw=float(input("Enter Withdraw amount Rs "))
    if Withdraw > 0:
      forewardbalance=(balance - Withdraw)
      print("Foreward Balance Rs ",forewardbalance)
    elif Withdraw>balance:
      print("No funs in account")
    else:
      print("None withdraw made")
  if Option==3:
    print("Balance Rs ",balance)
    Deposit=float(input("Enter deposit amount Rs "))
    if Deposit>0:
      forewardbalance=(balance+Deposit)
      print("Forewardbalance Rs ",forewardbalance)
    else:
      print("None deposit made")
  if Option==4:
    exit()