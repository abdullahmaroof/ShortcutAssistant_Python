from tkinter import *
import time
from PIL import ImageTk, Image
from Backend import *


def time_gui():
    root = Toplevel()
    root.geometry("400x300")
    root.title('Shortcut Menu Assistant')
    root.iconbitmap(r'logo.ico')
    root.configure(bg='ghost white')
    heading_label = Label(root, text="Current Time & Day", font=("arial",16,"bold"), width=20, bg="dodger blue")
    #clock
    def c_time():
        hour = time.strftime("%I")
        minute = time.strftime("%M")
        second = time.strftime("%S")
        tell_ap = time.strftime("%p")
        day = time.strftime("%A")
        t_zone = time.strftime("%Z")
        month = time.strftime("%B")
        date = time.strftime("%d")
        time_Label.config(text=hour + ":" + minute + ":" + second +" "+tell_ap)
        time_Label.after(1000, c_time)
        day_zone.config(text=t_zone + "\n" + day + "\n"+ date +"  " + month)
    time_Label = Label(root, text="", font=("Helvetica",24), fg="medium aquamarine", bg="black", width=12, height=2)
    day_zone = Label(root, text="", font=("#555555", 12), bg="ghost white", fg="#555555")
    exit_button = Button(root, text="Back", width=12, height=2, bg="cornflower blue",
                         font=('arial', 12, 'bold'), activebackground="medium aquamarine",
                         activeforeground="white", border=2, command= lambda :root.destroy())
    heading_label.pack(pady=20)
    time_Label.pack(pady=5)
    day_zone.pack(pady=10)
    c_time()
    cur_time()
    exit_button.pack(pady=10)


def MS_app(root):
    root = Tk()
    root.geometry("600x400")
    root.title('Shortcut Menu Assistant')
    root.iconbitmap(r'logo.ico')
    root.configure(bg='ghost white')
    # **********left block********
    left_root = Frame(root, bg="ghost white", height=400, width=150)
    # button for chrome websites chr_button
    home_button = Button(left_root, text="Home", width=15, height=2, bg="cornflower blue",
                         font=('arial', 11, 'bold'), activebackground="medium aquamarine",
                         activeforeground="white", border=2, command=
                         lambda: [root.destroy(),home_gui(root)])
    micro_off_button = Button(left_root, text="MS Office", width=15, height=2, bg="cornflower blue",
                              font=('arial', 11, 'bold'), activebackground="medium aquamarine",
                              activeforeground="white", border=2
                              )
    app_button = Button(left_root, text="Applications", width=15, height=2, bg="cornflower blue",
                        font=('arial', 11, 'bold'), activebackground="medium aquamarine", activeforeground="white",
                        border=2, command=
                        lambda: [root.destroy(),speak("Showing Laptop Applications"),app_gui(root)])
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

    right_root = Frame(root, bg="lightblue1", height=340, width=350)
    right_root.pack(side=LEFT, fill=BOTH, padx=50, pady=30, expand=1)
    MS_heading_label = Label(right_root, text="MS OFFICE", font=("arial", 16, "bold"), width=15, bg="dodger blue")
    MS_heading_label.pack(pady=10)
    #part1
    part1_frame = Frame(right_root, height=80, bg="red")
    part1_frame.pack(side=TOP, fill=BOTH, pady=5)
    left_part1 = Frame(part1_frame, bg="lightblue1", height=80)
    right_part1 = Frame(part1_frame, bg="lightblue1", height=80)
    left_part1.pack(side=LEFT, fill=BOTH, expand=1)
    right_part1.pack(side=LEFT, fill=BOTH, expand=1)
    excel_btn =  Button(left_part1, text="MS EXCEL", width=12, height=2, bg="cornflower blue",
                             font=('arial', 11, 'bold'), activebackground="medium aquamarine", activeforeground="white",
                             border=2 , command= lambda :excel())
    excel_btn.pack(pady=10)
    word_btn = Button(right_part1, text="MS WORD", width=12, height=2, bg="cornflower blue",
                             font=('arial', 11, 'bold'), activebackground="medium aquamarine", activeforeground="white",
                             border=2, command=lambda: word())
    word_btn.pack(pady=10)



    #PART2
    part2_frame = Frame(right_root, height=80, bg="red")
    part2_frame.pack(side=TOP, fill=BOTH, pady=5)
    left_part2 = Frame(part2_frame, bg="lightblue1", height=80)
    right_part2 = Frame(part2_frame, bg="lightblue1", height=80)
    left_part2.pack(side=LEFT, fill=BOTH, expand=1)
    right_part2.pack(side=LEFT, fill=BOTH, expand=1)
    ppt_btn = Button(left_part2, text="MS PowerPoint", width=12, height=2, bg="cornflower blue",
                             font=('arial', 11, 'bold'), activebackground="medium aquamarine", activeforeground="white",
                             border=2, command=lambda: ppt())
    ppt_btn.pack(pady=10)
    acc_btn = Button(right_part2, text="MS ACEESS", width=12, height=2, bg="cornflower blue",
                             font=('arial', 11, 'bold'), activebackground="medium aquamarine", activeforeground="white",
                             border=2, command=lambda: access())
    acc_btn.pack(pady=10)


    #PART3
    part3_frame = Frame(right_root, height=80, bg="red")
    left_part3 = Frame(part3_frame, bg="lightblue1", height=80)
    right_part3 = Frame(part3_frame, bg="lightblue1", height=80)
    pub_btn = Button(left_part3, text="MS Publisher", width=12, height=2, bg="cornflower blue",
                             font=('arial', 11, 'bold'), activebackground="medium aquamarine", activeforeground="white",
                             border=2, command=lambda: publisher())
    one_btn = Button(right_part3, text="MS OneNote", width=12, height=2, bg="cornflower blue",
                             font=('arial', 11, 'bold'), activebackground="medium aquamarine", activeforeground="white",
                             border=2, command=lambda: onenote())
    part3_frame.pack(side=TOP, fill=BOTH, pady=5)
    left_part3.pack(side=LEFT, fill=BOTH, expand=1)
    right_part3.pack(side=LEFT, fill=BOTH, expand=1)
    pub_btn.pack(pady=10)
    one_btn.pack(pady=10)

    exit_button = Button(right_root, text="Back", width=12, height=2, bg="cornflower blue",
                         font=('arial', 12, 'bold'), activebackground="medium aquamarine",
                         activeforeground="white", border=2, command=lambda: [root.destroy(),home_gui(root)])
    exit_button.pack(pady=10)

def home_gui(root):
    root = Tk()
    root.geometry("600x400")
    root.title('Shortcut Menu Assistant')
    root.iconbitmap(r'logo.ico')
    root.configure(bg='ghost white')
    # **********left block********
    left_root = Frame(root, bg="ghost white", height=400, width=150)
    # button for chrome websites chr_button
    home_button = Button(left_root, text="Home", width=15, height=2, bg="cornflower blue",
                         font=('arial', 11, 'bold'), activebackground="medium aquamarine",
                         activeforeground="white", border=2)
    micro_off_button = Button(left_root, text="MS Office", width=15, height=2, bg="cornflower blue",
                              font=('arial', 11, 'bold'), activebackground="medium aquamarine",
                              activeforeground="white", border=2, command=
                              lambda: [root.destroy(),speak("Showing MS Office Applications"),MS_app(root)]
                              )
    app_button = Button(left_root, text="Applications", width=15, height=2, bg="cornflower blue",
                        font=('arial', 11, 'bold'), activebackground="medium aquamarine", activeforeground="white",
                        border=2, command=
                        lambda: [root.destroy(),speak("Showing Laptop Applications"),app_gui(root)])
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

    # *******right block
    right_root = Frame(root, bg="lightblue1", height=340, width=350)
    time_button = Button(right_root, text="Current Time", width=20, height=2, bg="cornflower blue",
                         font=('arial', 12, 'bold'), activebackground="medium aquamarine", activeforeground="white",
                         border=2, command=lambda: time_gui())
    music_button = Button(right_root, text="Play Music", width=20, height=2, bg="cornflower blue",
                          font=('arial', 12, 'bold'), activebackground="medium aquamarine", activeforeground="white",
                          border=2, command=lambda: play_music())
    musicOn_button = Button(right_root, text="MusicOn Website", width=20, height=2, bg="cornflower blue",
                            font=('arial', 12, 'bold'), activebackground="medium aquamarine", activeforeground="white",
                            border=2, command=lambda: musicOn_web())
    right_root.pack(side=LEFT, fill=BOTH, padx=50, pady=30, expand=1)
    time_button.pack(pady=32)
    music_button.pack(pady=32)
    musicOn_button.pack(pady=32)


def app_gui(root):
    root = Tk()
    root.geometry("600x400")
    root.title('Shortcut Menu Assistant')
    root.iconbitmap(r'logo.ico')
    root.configure(bg='ghost white')
    # **********left block********
    left_root = Frame(root, bg="ghost white", height=400, width=150)
    # button for chrome websites chr_button
    home_button = Button(left_root, text="Home", width=15, height=2, bg="cornflower blue",
                         font=('arial', 11, 'bold'), activebackground="medium aquamarine",
                         activeforeground="white", border=2, command=
                         lambda: [root.destroy(), home_gui(root)])
    micro_off_button = Button(left_root, text="MS Office", width=15, height=2, bg="cornflower blue",
                              font=('arial', 11, 'bold'), activebackground="medium aquamarine",
                              activeforeground="white", border=2, command=
                        lambda: [root.destroy(),speak("Showing MS Office Applications"),MS_app(root)]
                              )
    app_button = Button(left_root, text="Applications", width=15, height=2, bg="cornflower blue",
                        font=('arial', 11, 'bold'), activebackground="medium aquamarine", activeforeground="white",
                        border=2)
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

    right_root = Frame(root, bg="lightblue1", height=340, width=350)
    right_root.pack(side=LEFT, fill=BOTH, padx=50, pady=30, expand=1)
    MS_heading_label = Label(right_root, text="Laptop Application", font=("arial", 16, "bold"), width=15, bg="dodger blue")
    MS_heading_label.pack(pady=10)
    # part1
    part1_frame = Frame(right_root, height=80, bg="red")
    part1_frame.pack(side=TOP, fill=BOTH, pady=5)
    left_part1 = Frame(part1_frame, bg="lightblue1", height=80)
    right_part1 = Frame(part1_frame, bg="lightblue1", height=80)
    left_part1.pack(side=LEFT, fill=BOTH, expand=1)
    right_part1.pack(side=LEFT, fill=BOTH, expand=1)
    whatsapp_btn = Button(left_part1, text="Whatsapp", width=12, height=2, bg="cornflower blue",
                       font=('arial', 11, 'bold'), activebackground="medium aquamarine", activeforeground="white",
                       border=2, command=lambda: WA_app())
    whatsapp_btn.pack(pady=10)
    zoom_btn = Button(right_part1, text="ZOOM", width=12, height=2, bg="cornflower blue",
                      font=('arial', 11, 'bold'), activebackground="medium aquamarine", activeforeground="white",
                      border=2, command=lambda: Zoom_app())
    zoom_btn.pack(pady=10)

    # PART2
    part2_frame = Frame(right_root, height=80, bg="red")
    part2_frame.pack(side=TOP, fill=BOTH, pady=5)
    left_part2 = Frame(part2_frame, bg="lightblue1", height=80)
    right_part2 = Frame(part2_frame, bg="lightblue1", height=80)
    left_part2.pack(side=LEFT, fill=BOTH, expand=1)
    right_part2.pack(side=LEFT, fill=BOTH, expand=1)
    dev_btn = Button(left_part2, text="Dev C++", width=12, height=2, bg="cornflower blue",
                     font=('arial', 11, 'bold'), activebackground="medium aquamarine", activeforeground="white",
                     border=2, command=lambda: dev_app())
    dev_btn.pack(pady=10)
    team_btn = Button(right_part2, text="TeamViewer", width=12, height=2, bg="cornflower blue",
                     font=('arial', 11, 'bold'), activebackground="medium aquamarine", activeforeground="white",
                     border=2, command=lambda: team_app())
    team_btn.pack(pady=10)

    # PART3
    part3_frame = Frame(right_root, height=80, bg="red")
    left_part3 = Frame(part3_frame, bg="lightblue1", height=80)
    right_part3 = Frame(part3_frame, bg="lightblue1", height=80)
    filmora_btn = Button(left_part3, text="Filmora", width=12, height=2, bg="cornflower blue",
                     font=('arial', 11, 'bold'), activebackground="medium aquamarine", activeforeground="white",
                     border=2, command=lambda: filmora_app())
    skype_btn = Button(right_part3, text="Skype", width=12, height=2, bg="cornflower blue",
                     font=('arial', 11, 'bold'), activebackground="medium aquamarine", activeforeground="white",
                     border=2, command=lambda: skype_app())
    part3_frame.pack(side=TOP, fill=BOTH, pady=5)
    left_part3.pack(side=LEFT, fill=BOTH, expand=1)
    right_part3.pack(side=LEFT, fill=BOTH, expand=1)
    filmora_btn.pack(pady=10)
    skype_btn.pack(pady=10)

    exit_button = Button(right_root, text="Back", width=12, height=2, bg="cornflower blue",
                         font=('arial', 12, 'bold'), activebackground="medium aquamarine",
                         activeforeground="white", border=2, command=lambda: [root.destroy(), home_gui(root)])
    exit_button.pack(pady=10)



def web_gui(root):
    root = Tk()
    root.geometry("600x400")
    root.title('Shortcut Menu Assistant')
    root.iconbitmap(r'logo.ico')
    root.configure(bg='ghost white')
    # **********left block********
    left_root = Frame(root, bg="ghost white", height=400, width=150)
    # button for chrome websites chr_button
    home_button = Button(left_root, text="Home", width=15, height=2, bg="cornflower blue",
                         font=('arial', 11, 'bold'), activebackground="medium aquamarine",
                         activeforeground="white", border=2, command=
                         lambda: [root.destroy(), home_gui(root)])
    micro_off_button = Button(left_root, text="MS Office", width=15, height=2, bg="cornflower blue",
                              font=('arial', 11, 'bold'), activebackground="medium aquamarine",
                              activeforeground="white", border=2, command=
                        lambda: [root.destroy(),speak("Showing MS Office Applications"),MS_app(root)]
                              )
    app_button = Button(left_root, text="Applications", width=15, height=2, bg="cornflower blue",
                        font=('arial', 11, 'bold'), activebackground="medium aquamarine", activeforeground="white",
                        border=2, command=
                                  lambda : [root.destroy(),speak("Showing Laptop Applications"),app_gui(root)]
                        )
    web_button = Button(left_root, text="Websites", width=15, height=2, bg="cornflower blue",
                        font=('arial', 11, 'bold'), activebackground="medium aquamarine", activeforeground="white",
                        border=2)
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

    right_root = Frame(root, bg="lightblue1", height=340, width=350)
    right_root.pack(side=LEFT, fill=BOTH, padx=50, pady=30, expand=1)
    MS_heading_label = Label(right_root, text="Websites", font=("arial", 16, "bold"), width=15, bg="dodger blue")
    MS_heading_label.pack(pady=10)
    # part1
    part1_frame = Frame(right_root, height=80, bg="red")
    part1_frame.pack(side=TOP, fill=BOTH, pady=5)
    left_part1 = Frame(part1_frame, bg="lightblue1", height=80)
    right_part1 = Frame(part1_frame, bg="lightblue1", height=80)
    left_part1.pack(side=LEFT, fill=BOTH, expand=1)
    right_part1.pack(side=LEFT, fill=BOTH, expand=1)
    google_btn = Button(left_part1, text="Google", width=12, height=2, bg="cornflower blue",
                       font=('arial', 11, 'bold'), activebackground="medium aquamarine", activeforeground="white",
                       border=2, command=lambda: google())
    google_btn.pack(pady=10)
    youtube_btn = Button(right_part1, text="YouTube", width=12, height=2, bg="cornflower blue",
                      font=('arial', 11, 'bold'), activebackground="medium aquamarine", activeforeground="white",
                      border=2, command=lambda: YT())
    youtube_btn.pack(pady=10)

    # PART2
    part2_frame = Frame(right_root, height=80, bg="red")
    part2_frame.pack(side=TOP, fill=BOTH, pady=5)
    left_part2 = Frame(part2_frame, bg="lightblue1", height=80)
    right_part2 = Frame(part2_frame, bg="lightblue1", height=80)
    left_part2.pack(side=LEFT, fill=BOTH, expand=1)
    right_part2.pack(side=LEFT, fill=BOTH, expand=1)
    fb_btn = Button(left_part2, text="FaceBook", width=12, height=2, bg="cornflower blue",
                     font=('arial', 11, 'bold'), activebackground="medium aquamarine", activeforeground="white",
                     border=2, command=lambda: fb())
    fb_btn.pack(pady=10)
    git_btn = Button(right_part2, text="Git Hub", width=12, height=2, bg="cornflower blue",
                     font=('arial', 11, 'bold'), activebackground="medium aquamarine", activeforeground="white",
                     border=2, command=lambda: github_web())
    git_btn.pack(pady=10)

    # PART3
    part3_frame = Frame(right_root, height=80, bg="red")
    left_part3 = Frame(part3_frame, bg="lightblue1", height=80)
    right_part3 = Frame(part3_frame, bg="lightblue1", height=80)
    gaana_btn = Button(left_part3, text="Gaana", width=12, height=2, bg="cornflower blue",
                     font=('arial', 11, 'bold'), activebackground="medium aquamarine", activeforeground="white",
                     border=2, command=lambda: Gaana_web())
    zoom_btn = Button(right_part3, text="ZOOM", width=12, height=2, bg="cornflower blue",
                     font=('arial', 11, 'bold'), activebackground="medium aquamarine", activeforeground="white",
                     border=2, command=lambda: zoom_web())
    part3_frame.pack(side=TOP, fill=BOTH, pady=5)
    left_part3.pack(side=LEFT, fill=BOTH, expand=1)
    right_part3.pack(side=LEFT, fill=BOTH, expand=1)
    gaana_btn.pack(pady=10)
    zoom_btn.pack(pady=10)

    exit_button = Button(right_root, text="Back", width=12, height=2, bg="cornflower blue",
                         font=('arial', 12, 'bold'), activebackground="medium aquamarine",
                         activeforeground="white", border=2, command=lambda: [root.destroy(), home_gui(root)])
    exit_button.pack(pady=10)

def wiki_part(root):
    root = Tk()
    root.geometry("600x400")
    root.title('Shortcut Menu Assistant')
    root.iconbitmap(r'logo.ico')
    root.configure(bg='ghost white')
    # **********left block********
    left_root = Frame(root, bg="ghost white", height=400, width=150)
    # button for chrome websites chr_button
    home_button = Button(left_root, text="Home", width=15, height=2, bg="cornflower blue",
                         font=('arial', 11, 'bold'), activebackground="medium aquamarine",
                         activeforeground="white", border=2, command=
                         lambda: [root.destroy(), home_gui(root)])
    micro_off_button = Button(left_root, text="MS Office", width=15, height=2, bg="cornflower blue",
                              font=('arial', 11, 'bold'), activebackground="medium aquamarine",
                              activeforeground="white", border=2, command=
                              lambda: [root.destroy(), speak("Showing MS Office Applications"), MS_app(root)]
                              )
    app_button = Button(left_root, text="Applications", width=15, height=2, bg="cornflower blue",
                        font=('arial', 11, 'bold'), activebackground="medium aquamarine", activeforeground="white",
                        border=2, command=
                        lambda: [root.destroy(), speak("Showing Laptop Applications"), app_gui(root)]
                        )
    web_button = Button(left_root, text="Websites", width=15, height=2, bg="cornflower blue",
                        font=('arial', 11, 'bold'), activebackground="medium aquamarine", activeforeground="white",
                        border=2, command=
                        lambda: [root.destroy(),speak("Showing Websites"),web_gui(root)]
                        )
    wiki_button = Button(left_root, text="Wikipedia Search", width=15, height=2, bg="cornflower blue",
                         font=('arial', 11, 'bold'), activebackground="medium aquamarine",
                         activeforeground="white", border=2)

    left_root.pack(side=LEFT, fill=BOTH)
    home_button.pack(padx=15, pady=15)
    micro_off_button.pack(padx=15, pady=15)
    app_button.pack(padx=15, pady=15)
    web_button.pack(padx=15, pady=15)
    wiki_button.pack(padx=15, pady=15)

    right_root = Frame(root, bg="lightblue1", height=340, width=350)
    right_root.pack(side=LEFT, fill=BOTH, padx=50, pady=30, expand=1)
    wiki_heading_label = Label(right_root, text="Wikipedia", font=("arial", 16, "bold"), width=15, bg="dodger blue")
    wiki_heading_label.pack(pady=10)
    search_frame = Frame(right_root, height=40, bg="lightblue1")
    search_frame.pack(pady=10, fill=BOTH)
    text_box_search = Entry(search_frame, width=30)
    text_box_search.pack(side=LEFT, padx=8 ,pady=10)
    search_button = Button(search_frame, text="Search", width=12, height=1, bg="cornflower blue",
                         font=('arial', 10), activebackground="medium aquamarine",
                         activeforeground="white", border=2, command= lambda : weki(text_box_search.get()))
    search_button.pack(side= LEFT, padx=10,pady=10)
    result.set()

    result_frame = Label(right_root,text=weki(text_box_search.get), font=('arial', 10), height=9, bg="white")
    result_frame.pack(pady=10, padx=10, fill=BOTH)
    exit_button = Button(right_root, text="Back", width=12, height=2, bg="cornflower blue",
                         font=('arial', 12, 'bold'), activebackground="medium aquamarine",
                         activeforeground="white", border=2, command=lambda: [root.destroy(), home_gui(root)])
    exit_button.pack(pady=10)