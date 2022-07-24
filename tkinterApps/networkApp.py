from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview


def clear_text():
    brand_entry.delete(0, END)
    hostname_entry.delete(0, END)
    ram_entry.delete(0, END)
    flash_entry.delete(0, END)


app = Tk()
frame_search = Frame(app)
frame_search.grid(row=0, column=0)

lbl_search = Label(frame_search, text='Search by hostname',
                   font=('bold', 12), pady=20)
lbl_search.grid(row=0, column=0, sticky=W)
hostname_search = StringVar()
hostname_search_entry = Entry(frame_search, textvariable=hostname_search)
hostname_search_entry.grid(row=0, column=1)

lbl_search = Label(frame_search, text='Search by Query',
                   font=('bold', 12), pady=20)
lbl_search.grid(row=1, column=0, sticky=W)
query_search = StringVar()
query_search.set("Select * from routers where ram>1024")
query_search_entry = Entry(frame_search, textvariable=query_search, width=40)
query_search_entry.grid(row=1, column=1)

frame_fields = Frame(app)
frame_fields.grid(row=1, column=0)
# hostname
hostname_text = StringVar()
hostname_label = Label(frame_fields, text='hostname', font=('bold', 12))
hostname_label.grid(row=0, column=0, sticky=E)
hostname_entry = Entry(frame_fields, textvariable=hostname_text)
hostname_entry.grid(row=0, column=1, sticky=W)
# BRAND
brand_text = StringVar()
brand_label = Label(frame_fields, text='Brand', font=('bold', 12))
brand_label.grid(row=0, column=2, sticky=E)
brand_entry = Entry(frame_fields, textvariable=brand_text)
brand_entry.grid(row=0, column=3, sticky=W)
# RAM
ram_text = StringVar()
ram_label = Label(frame_fields, text='RAM', font=('bold', 12))
ram_label.grid(row=1, column=0, sticky=E)
ram_entry = Entry(frame_fields, textvariable=ram_text)
ram_entry.grid(row=1, column=1, sticky=W)
# FLASH
flash_text = StringVar()
flash_label = Label(frame_fields, text='Flash', font=('bold', 12), pady=20)
flash_label.grid(row=1, column=2, sticky=E)
flash_entry = Entry(frame_fields, textvariable=flash_text)
flash_entry.grid(row=1, column=3, sticky=W)

frame_router = Frame(app)
frame_router.grid(row=4, column=0, columnspan=4, rowspan=6, pady=20, padx=20)

columns = ['id', 'Hostname', 'Brand', 'Ram', 'Flash']
router_tree_view = Treeview(frame_router, columns=columns, show="headings")
router_tree_view.column("id", width=30)
for col in columns[1:]:
    router_tree_view.column(col, width=120)
    router_tree_view.heading(col, text=col)
router_tree_view.bind('<<TreeviewSelect>>')
router_tree_view.pack(side="left", fill="y")
scrollbar = Scrollbar(frame_router, orient='vertical')
scrollbar.configure(command=router_tree_view.yview)
scrollbar.pack(side="right", fill="y")
router_tree_view.config(yscrollcommand=scrollbar.set)

frame_btns = Frame(app)
frame_btns.grid(row=3, column=0)

add_btn = Button(frame_btns, text='Add Router', width=12)
add_btn.grid(row=0, column=0, pady=20)

remove_btn = Button(frame_btns, text='Remove Router',
                    width=12)
remove_btn.grid(row=0, column=1)

update_btn = Button(frame_btns, text='Update Router',
                    width=12)
update_btn.grid(row=0, column=2)

clear_btn = Button(frame_btns, text='Clear Input',
                   width=12, command=clear_text)
clear_btn.grid(row=0, column=3)

search_btn = Button(frame_search, text='Search',
                    width=12)
search_btn.grid(row=0, column=2)

search_query_btn = Button(frame_search, text='Search Query',
                          width=12)
search_query_btn.grid(row=1, column=2)

app.title('Router Manager')
app.geometry('700x550')

# Start program
app.mainloop()