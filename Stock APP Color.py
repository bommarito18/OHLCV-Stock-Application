#!/usr/bin/env python
# coding: utf-8

# In[425]:


from yahoo_fin import stock_info
from tkinter import *
import matplotlib.pyplot as plt


# In[426]:


def stock_price():

    price = stock_info.get_live_price(e1.get())
    Current_stock.set(price)
    price1 = stock_info.get_data(e1.get())
    Current_stock1.set(price1['open'].tail(1))
    Current_stock2.set(price1['high'].tail(1))
    Current_stock3.set(price1['low'].tail(1))
    Current_stock4.set(price1['close'].tail(1))
    Current_stock5.set(price1['volume'].tail(1))


# In[427]:


master = Tk()
Current_stock = StringVar()
Current_stock1 = StringVar()
Current_stock2 = StringVar()
Current_stock3 = StringVar()
Current_stock4 = StringVar()
Current_stock5 = StringVar()


# In[428]:


HEIGHT = 750
WIDTH = 900


# In[429]:


canvas = Canvas(master, height=HEIGHT, width=WIDTH)
canvas.grid()


# In[430]:


background_image= PhotoImage(file='C:/Users/tcbom/OneDrive/Desktop/cool.png')
background_label = Label(master, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


# In[431]:


frame = Frame(master, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')


# In[432]:


lower_frame = Frame(master, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


# In[433]:


#Label(frame, bg='red', text="Company Symbol : ").grid(row=0, sticky=W)
Label(lower_frame, bg='#008ae6', fg='White', font=20, text="Current Stock Price:").grid(row=3, padx=10, sticky=W)
Label(lower_frame,bg='#008ae6', fg='White', font=20, text="Stock Open:").grid(row=4, padx=10, sticky=W)
Label(lower_frame,bg='#008ae6', fg='White', font=20, text="Stock High:").grid(row=5, padx=10, sticky=W)
Label(lower_frame,bg='#008ae6', fg='White', font=20, text="Stock Low:").grid(row=6, padx=10, sticky=W)
Label(lower_frame,bg='#008ae6', fg='White', font=20, text="Stock Close:").grid(row=7, padx=10, sticky=W)
Label(lower_frame,bg='#008ae6', fg='White', font=20, text="Stock Volume:").grid(row=8, padx=10, sticky=W)


# In[434]:


result2 = Label(lower_frame, bg='cyan', text="", textvariable=Current_stock,
                ).grid(row=3, column=1,padx=100, pady=20, sticky=W)


# In[435]:


result3 = Label(lower_frame, bg='cyan', text="", textvariable=Current_stock1,
                ).grid(row=4, column=1, padx=100, pady=20, sticky=W)


# In[436]:


result4 = Label(lower_frame, bg='cyan', text="", textvariable=Current_stock2,
                ).grid(row=5, column=1, padx=100, pady=20, sticky=W)


# In[437]:


result5 = Label(lower_frame, bg='cyan', text="", textvariable=Current_stock3,
                ).grid(row=6, column=1, padx=100, pady=20, sticky=W)


# In[438]:


result6 = Label(lower_frame, bg='cyan', text="", textvariable=Current_stock4,
                ).grid(row=7, column=1, padx=100, pady=20, sticky=W)


# In[439]:


result7 = Label(lower_frame, bg='cyan', text="", textvariable=Current_stock5,
                ).grid(row=8, column=1, padx=100, pady=20, sticky=W)


# In[440]:


e1 = Entry(frame, bg='cyan', font=40)
#e1.grid(row=0, column=1)
e1.place(relwidth=0.65, relheight=1)


# In[441]:


b = Button(frame, bg='#008ae6', fg='White', text="Enter Stock Ticker ", font=20, command=stock_price)
#b.grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5)
b.place(relx=0.7, relheight=1, relwidth=0.3)


# In[442]:


master.title("Valuation By: Taylor Bommarito")
master.iconbitmap("C:/Users/tcbom/OneDrive/Desktop/dollar.ico")
mainloop()


# In[ ]:





# In[ ]:





# In[ ]:




