from tkinter import *
from web3 import Web3
from PIL import ImageTk, Image

root = Tk()
root.title("Account Details")

ganache_url = 'http://127.0.0.1:7545'

web3 = Web3(Web3.HTTPProvider(ganache_url))

img = ImageTk.PhotoImage(Image.open("image.png"))
panel = Label(root, image=img, bg='white')
panel.pack(side="top")

frame = Frame(
    root,
    bg='white',
    padx=5,
    pady=5
)
# create the labels to hold the account numbers																			
Label("Account number 1: ", frame, fg = 'white', bg = 'blue', grid(0,0),sticky = W, pady =10)
Label("Account number 2: ", frame, fg = 'black', bg = 'red', grid(1,0), sticky = W, pady = 10)
Label("Account number 3: ", frame, grid(2,0))
Label("Account number 4: ", frame, grid(3,0))
Label("Account number 5: ", frame, grid(4,0))



account1 = Entry(frame)
account2 = Entry(frame)
account3 = Entry(frame)
account4 = Entry(frame)
account5 = Entry(frame)

#Create entry elements to get the use input for account addresses 
Entry(account1(grid(0,1),padx=10,pady=20))
Entry(account2(grid(1,1),padx=10,pady=20))
Entry(account3(grid(2,1),padx=10,pady=20))
Entry(account4(grid(3,1),padx=10,pady=20))
Entry(account5(grid(4,1),padx=10,pady=20))




#place the entry elements on the root window
def result(Text()):
	root(window)
	height = 10
	weight = 45
	bg = 'red'
def CHECK_BALANCE(1):
	for i in keyword():
		balance = web3.eth.getBalance(i)
		balance = balance * 0.0000000000000000000.1															
		result.insert(END, f'Account {count} balance is {balance} /n')

pack()





#create the text box

check_balance(Button(),root,width = 15, "CHECK BALANCE", command = CHECK_BALANCE, bg = 'green')
check_balance(pack('both'))
#define a function CHECK_BALANCE() and add the code inside it.

    
   
  
    

    




       
     
        
      

frame.pack()

#Create a button element to call the CHECK_BALANCE()

balance = web3.eth.getBalance(i)
balance = balance * 0.000000000000001
    

result.pack(pady=5)
root.mainloop()

