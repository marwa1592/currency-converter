import os 
import time 

coins = {'USD': 1.0,
  'EUR': 0.85,
  'EGP': 30.9,
  'RMB': 6.5,

      }
currency = """
USD: 1.0
EUR: 0.85
EGP: 30.9
RMB: 6.5

"""
def clean_screen (): 
    os.system ("cls" if os.name =='nt'  else  "clear")
print("WELCOME TO CURRENCY CONVERTER: ")
pic =("""
||====================================================================||
   ||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\||
   ||(100)==================| FEDERAL RESERVE NOTE |================(100)||
   ||\\$//        ~         '------========--------'                \\$//||
   ||<< /        /$\              // ____ \\                         \ >>||
   ||>>|  12    //L\\            // ///..) \\         L38036133B   12 |<<||
   ||<<|        \\ //           || <||  >\  ||                        |>>||
   ||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<||
||====================================================================||>||
||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\||<||
||(100)==================| FEDERAL RESERVE NOTE |================(100)||>||
||\\$//        ~         '------========--------'                \\$//||\||
||<< /        /$\              // ____ \\                         \ >>||)||
||>>|  12    //L\\            // ///..) \\         L38036133B   12 |<<||/||
||<<|        \\ //           || <||  >\  ||                        |>>||=||
||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<||
||<<|      L38036133B        *\\  |\_/  //* series                 |>>||
||>>|  12                     *\\/___\_//*   1989                  |<<||
||<<\      Treasurer     ______/Franklin\________     Secretary 12 />>||
||//$\                 ~|UNITED STATES OF AMERICA|~               /$\\||
||(100)===================  ONE HUNDRED DOLLARS =================(100)||
||\\$//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\$//||
||====================================================================||
""")
print(pic)

print("-------------------------------------------------")

# السوال عن العمله المحول منها : 
while True:  
  print(currency)
  convert_from = input("Choose a cruuency to convert from: ").upper()
# ارجع اسأله عن الكميه تاني: 
  while True: 
      amount = float (input("Enter the amount:  "))
      confirm = input(f"you entered {amount} {convert_from}. Confirm? (y/n)").lower()
      if confirm =='y': 
          clean_screen()
          break
  print(currency) 
  convert_to = input("choose a currency to convert to: ").upper()
  # الصبر : 
  print("Analyzing your request .... please wait.")
  time.sleep(2)
  print(f"Checking for {convert_to}'s best rates available .... please wait.")
  time.sleep(2)


  if convert_from not in coins:
    print("Invalid currency.Conversion canceled!")
    time.sleep(1)
    clean_screen()
    print(currency)
    continue
  else: 
    print(f"Getting a discoundt price for {convert_from}...please wait.")
    time.sleep(2)
    clean_screen()
    print(f"Preparing the deal from {convert_from} to {convert_to} .... please wait.\n")
    time.sleep(2)
    
  def exchange_rate(x,y):
     return x/y
  rate = exchange_rate(coins[convert_to],coins[convert_from])
  
  print (f"\n\nExchange Rate: 1 {convert_from} = {rate} {convert_to}")

  def whole_money (v,c):
     return v * c
  print(f"\n{amount} {convert_from} is equal to {whole_money(amount,rate)} {convert_to}")

  accept = input("Do you accept this transaction? (y/n): ")
  if accept == "n":
    print("Transaction canceled.")

  perform = input ("\nDo you want to perform another conversion? (y/n): ")
  if perform !="y":
     break

  else: 
     clean_screen()
     print(pic)
     
