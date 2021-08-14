                                            #importing libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv

import tkinter as tk
from tkinter import messagebox
from tkinter import *

                                            #importing csv file

df_ = pd.read_csv ('admission_predict.csv')

                             #analyzing and retrieving required data (dropping columns)

df=df_.drop(['research', 'serial_no'],axis=1)
df = df.sort_values('gre_score')
df.set_index('gre_score')
df = df.reset_index(level=0, drop=True)
print(df.head())
print(df.info())

#value_counts and display

df_grecount = df['gre_score'].value_counts()
df_toeflcount = df['toefl_score'].value_counts()
df_sopcount = df['sop'].value_counts()
df_cgpacount = df['cgpa'].value_counts()
df_chancecount = df['chance_of_admit'].value_counts()
df_urcount = df['university_rating'].value_counts()

print(df_grecount)
print(df_sopcount)
print(df_toeflcount)
print(df_cgpacount)
print(df_chancecount)
print(df_urcount)

                                            #mean, max, min values

#gre
gre_min = df['gre_score'].min()
print(gre_min)
gre_max = df['gre_score'].max()
print(gre_max)
gre_mean = df['gre_score'].mean()
print(gre_mean)

#toefl
toefl_min = df['toefl_score'].min()
print(toefl_min)
toefl_max = df['toefl_score'].max()
print(toefl_max)
toefl_mean = df['toefl_score'].mean()
print(toefl_mean)

#cgpa
cgpa_min = df['cgpa'].min()
print(cgpa_min)
cgpa_max = df['cgpa'].max()
print(cgpa_max)
cgpa_mean = df['cgpa'].mean()
print(cgpa_mean)

#chance_of_admit
coa_min = df['chance_of_admit'].min()
print(coa_min)
coa_max = df['chance_of_admit'].max()
print(coa_max)
coa_mean = df['chance_of_admit'].mean()
print(coa_mean)

#ur
ur_min = df['university_rating'].min()
print(ur_min)
ur_max = df['university_rating'].max()
print(ur_max)
ur_mean = df['university_rating'].mean()
print(ur_mean)

#sop
sop_min = df['sop'].min()
print(sop_min)
sop_max = df['sop'].max()
print(sop_max)
sop_mean = df['sop'].mean()
print(sop_mean)

                                                    #graphs and values

df_gre = df.gre_score.head(400)
df_toefl = df['toefl_score']
df_cgpa = df.cgpa[1:30]
df_chance = df['chance_of_admit']
df_ur = df['university_rating']
df_sop = df['sop']

sns.countplot(x = df_gre, data=df)
#plt.show()
sns.countplot(x = df_toefl, data=df)
#plt.show()
sns.countplot(x = df_chance, data=df)
#plt.show()
sns.countplot(x = df_cgpa, data=df)
#plt.show()
sns.countplot(x = df_sop, data=df)
#plt.show()
#sns.countplot(x = df_ur, data=df)
#plt.show()

df.hist(figsize=(12,8))
#plt.show()

def hist():
    corr = df.corr()
    sns.heatmap(corr, vmax=0.9,vmin=0,annot=True,cmap="YlGnBu")
    plt.show()

                                                    #tkinter code

main_window = Tk()
main_window.geometry("1000x500")
main_window.title("Welcome")
def window():
    main_w = Toplevel(main_window)
    main_w.geometry('1000x600')
    main_w.title(" Admission Predictor")
    def compose_result():
        # type conversion
        val1 = float(e1.get())
        val2 = float(e2.get())
        val3 = float(e3.get())
        val4 = float(e4.get())
        val5 = float(e5.get())
                                         # building formula
        gre = val1 / 340
        toefl = val2 / 120
        cgpa = val3 / 10
        sop = val4 / 5
        ur = val5 / 5

                                        # prediction formula

        admission_success = (0.3 * gre) + (0.3 * toefl) + (0.3 * cgpa) + (0.05 * sop) + (0.05 * ur)
        print(admission_success)

        # cases

        if admission_success >= 0.9:
            messagebox.showinfo("Title", "You can apply for\n 1.ECE\n 2.Mechanical\n3.Civil\n4.Electrical\n 5.CSE\n 6.IT\n 7.AE")
        if 0.8 < admission_success < 0.9:
            messagebox.showinfo("Title", "You can apply for\n 1.ECE\n 2.Mechanical\n3.Civil\n4.Electrical ")
        if 0.7 < admission_success < 0.8:
            messagebox.showinfo("Title", "You can apply for\n 1.Mechanical\n2.Civil")
        if admission_success < 0.7:
            messagebox.showinfo("Title", "You are on the waiting list")

    label_1 = Label(main_w,text = "XYZ Institute Institue Admission Predictor", font = ('Times New Roman', 40))
    label_1.grid(columnspan=20, ipady=70)

    w1 = Label(main_w, text="Enter your GRE Score out of 340:", font=('Courier', 15))
    w1.grid(sticky=E, columnspan=5, row=23, column=0)
    e1 = Entry(main_w)
    e1.grid(row=23, column=6)
    w2 = Label(main_w, text="Enter your TOEFL Score out of 120:", font=('Courier', 15))
    w2.grid(sticky=E, columnspan=5)
    e2 = Entry(main_w)
    e2.grid(row=24, column=6)
    w3 = Label(main_w, text="Enter your CGPA out of 10:", font=('Courier', 15))
    w3.grid(sticky=E, columnspan=5)
    e3 = Entry(main_w)
    e3.grid(row=25, column=6)
    w4 = Label(main_w, text="Enter your SOP out of 5:", font=('Courier', 15))
    w4.grid(sticky=E, columnspan=5)
    e4 = Entry(main_w)
    e4.grid(row=26, column=6)
    w5 = Label(main_w, text="Enter your University Rating out of 5:", font = ('Courier', 15))
    w5.grid(sticky=E, columnspan=5)
    e5 = Entry(main_w)
    e5.grid(row=27, column=6)

    b1 = Button(main_w, text="Submit",  command = compose_result, activeforeground = 'grey')
    b1.grid(row=30, column=6, sticky=W)
    b2 = Button(main_w, text="Back", command=quit)
    b2.grid(row=30, column=6, sticky=E)


label1 = Label(main_window, text="XYZ Institute Admission Prediction Portal", font=('Times New Roman', 40))
label1.pack()
message = Message(main_window, text="Institution Predictor is a tool for predicting whether or not the students who "
                                    "applied for the admission at our college are capable for joining the institution, "
                                    "if yes then what stream they will get the admission.", font = ("Courier", 15), bd = 1)
message.pack()
button = Button(main_window, text="Open the \n Predictor portal", command=window, font = 10)
button.pack()
button1 = Button(main_window, text="Statistics of candidates", command = hist , font = 10)
button1.pack()
main_window.mainloop()
