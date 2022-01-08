from Other_GUI import *

class GUI_system:
    def __init__(self, root):
        self.root = root
        root.geometry("600x400")
        root.title('Shortcut Menu Assistant')
        root.iconbitmap(r'logo.ico')
        root.configure(bg='ghost white')
        wishme()
        #**********left block********
        left_root = Frame(root, bg="ghost white", height=400, width=150)
        #button for chrome websites chr_button
        home_button = Button(left_root, text="Home", width=15, height=2, bg="cornflower blue",
                                 font=('arial', 11, 'bold'), activebackground="medium aquamarine",
                                 activeforeground="white", border=2)
        micro_off_button = Button(left_root, text="MS Office", width=15, height=2, bg="cornflower blue",
                            font=('arial',11,'bold'), activebackground="medium aquamarine",
                            activeforeground="white", border=2, command=
                                  lambda : [root.destroy(),speak("Showing MS Office Applications"),MS_app(root)]
                                  )
        app_button = Button(left_root, text="Applications", width=15, height=2, bg="cornflower blue",
                            font=('arial', 11, 'bold'), activebackground="medium aquamarine", activeforeground="white",
                            border=2, command=
                                  lambda : [root.destroy(),speak("Showing Laptop Applications"),app_gui(root)])
        web_button = Button(left_root, text="Websites", width=15, height=2, bg="cornflower blue",
                            font=('arial', 11, 'bold'), activebackground="medium aquamarine", activeforeground="white",
                            border=2, command=
                        lambda: [root.destroy(),speak("Showing Websites"),web_gui(root)]
                              )
        wiki_button = Button(left_root, text="Wikipedia Search", width=15, height=2, bg="cornflower blue",
                                font=('arial', 11, 'bold'), activebackground="medium aquamarine",
                                activeforeground="white", border=2, command=
                        lambda: [root.destroy(),speak("Showing Wikipedia"),wiki_part(root)]
                        )

        left_root.pack(side=LEFT, fill=BOTH)
        home_button.pack(padx=15, pady=15)
        micro_off_button.pack(padx=15, pady=15)
        app_button.pack(padx=15, pady=15)
        web_button.pack(padx=15, pady=15)
        wiki_button.pack(padx=15, pady=15)


        #*******right block
        right_root = Frame(root, bg="lightblue1", height=340, width=350)
        time_button = Button(right_root, text="Current Time", width=20, height=2, bg="cornflower blue",
                             font=('arial', 12, 'bold'), activebackground="medium aquamarine", activeforeground="white",
                             border=2, command= lambda :time_gui())
        music_button = Button(right_root, text="Play Music", width=20, height=2, bg="cornflower blue",
                             font=('arial', 12, 'bold'), activebackground="medium aquamarine", activeforeground="white",
                             border=2, command= lambda :play_music())
        musicOn_button = Button(right_root, text="MusicOn Website", width=20, height=2, bg="cornflower blue",
                             font=('arial', 12, 'bold'), activebackground="medium aquamarine", activeforeground="white",
                             border=2, command= lambda :musicOn_web())
        right_root.pack(side=LEFT, fill=BOTH, padx=50, pady=30, expand=1)
        time_button.pack(pady=32)
        music_button.pack(pady=32)
        musicOn_button.pack(pady=32)







root = Tk()
obj = GUI_system(root)
mainloop()
