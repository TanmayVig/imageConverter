import PIL.Image
from tkinter import *
from tkinter.filedialog import askopenfilenames, askdirectory
import os
import shutil


Base_DIR= os.path.dirname(os.path.abspath(__file__))
def find_file():
    global path1
    file_name.config(state=DISABLED)
    path1=askopenfilenames()

def saveFile():
    global path1
    try:
        path=askdirectory()
        fin=final.get()
            # path=path+"/"+fin
        path=os.path.join(path,fin)
            # save file
        img=PIL.Image.open(path1[0])
        img.save(fin)
            # move it to desired dir
        shutil.move(os.path.join(os.path.dirname(os.path.abspath(__file__)),fin),path)
    except:
        err_msg=Label(root, text='Only jpeg to other resters 😑')
        err_msg.config(font=('helvetica',25))
        err_msg.place(x=30,y=250)
#open window
root=Tk()
root.resizable(False,False)
root.geometry('500x300')
root['bg']='black'
root.title('Image Format Convertr')
root.iconbitmap('imcvt.ico')
#ask for file to be converted
signature=Label(root,text="by- Tanmay Vig", fg='white', bg='black')
signature.config(font=('helvetica',10))
signature.place(x=0,y=0)
file_name=Button(root, width=15, height=1, bg='orange',
                    activebackground='red',command=find_file)
file_name.config(text='choose file')
file_name.place(x=30,y=50)
#ask directory where to be saved
txt=Label(root,text='enter name of the file with .format:',fg='white',bg='black')
txt.config(font=('helvetica',15))
txt.place(x=30,y=90)
final=Entry(root,width=60, border=1, relief=GROOVE)
final.place(x=30,y=120)
txt2=Label(root, text="In which foulder you want to save?",fg='white',bg='black')
txt2.config(font=('helvetica',15))
txt2.place(x=30, y=150)
#convert
save_file=Button(root, width=10, height=1, bg='orange',
                    activebackground='red',command=saveFile)
save_file.config(text='choose...')
save_file.place(x=30,y=190)
#close window
root.mainloop()
