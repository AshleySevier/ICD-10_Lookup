
import tkinter as tk
from tkinter import LEFT, Label

# UI

# tk.Tk(screenName=None,  baseName=None,  className='Tk',  useTk=1)

win=tk.Tk() #creating the main window and storing the window object in 'win'
win.geometry('500x200') #setting the size of the window
win.title("ICD-10 Lookup")
win.config(background='white')
frame1 = tk.Frame(win)
frame2 = tk.Frame(win)
frame3 = tk.Frame(win)
label= Label(frame1,text="Label",justify=LEFT)
label.pack(side=LEFT)
frame1.pack(padx=1,pady=1)
frame2.pack(padx=10,pady=10)
frame3.pack(padx=10,pady=10)
label = tk.Label(frame1, text = '5555555555555555555555555555555555', 
background='pink', foreground= 'white', justify= LEFT) 
label.pack(side=LEFT)
btn = tk.Button(frame2, text='option 1', width=10,height=5, command = win.destroy).pack() #button
btn2 = tk.Button(frame3, text='option 2', width=10,height=5, command = win.destroy).pack() #button


win.mainloop() #running the loop that works as a trigger






# # import raw txt
# path_import = r'/Users/ashleylumpkin/Downloads/2018 Code Descriptions/icd10cm_codes_2018.txt'
# with open(path_import, 'r') as _f:
#     raw = _f.read()
#     _f.close()

# # convert raw txt to dictionary
# data = {}
# for rcd in raw.split('\n'):
#     if rcd:
#         data[rcd[:8].strip()] = rcd[8:]

# def find_code(data, userInputDesc):
#     returnValues = ''
#     for key,val in data.items():
#         if userInputDesc in val:
#             returnValues += f'{key} - {val} \n'
#         elif userInputDesc not in val:
#             if userInputDesc in key:
#                 returnValues = f'not found, did you mean to search for {val}?'
           
#     return returnValues

# while True: 
#     #intitial user prompt
#     userPrompt = input("Search for a code (type 1) or search for a description (type 2)? ").strip() 

#     if userPrompt == '1': #search for code based on code description
#         userInputDesc = input("Type in a code description. ").capitalize().strip()
#         print(find_code(data, userInputDesc))
#         break
#     elif userPrompt == '2': #search for the code description based on code
#         findDesc = input("Type in a code. ").upper().replace(".", "").strip()
#         if data[findDesc] == None:
#             print('None found.') 
#         print(data[findDesc])
#         break
#     elif userPrompt != '1' or '2':
#         print('Not an option, try again') #returns to initial prompt

