"""
                                ।। श्री ।।
                           ।। श्री गणेशाय नम: ।। 
                       
                This is code of Telegram Bot — Picaboo.
                Created by "Niranjan Pratibha Nagnath Bhol."
                Made in 💛 with ........ .
                                                            """

from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import time

with open('Token.txt', 'r') as Token:
    TOKEN = Token.read()

updater = Updater(TOKEN,
        use_context=True)

# Start

def start(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text(
		"Hi there, I am Picaboo..!! 👻")
    time.sleep(1)
    update.message.reply_text(
		"I can help you with,\n\n✿ Textbooks\n✿ Notes\n✿ Assignments\n✿ Lab Manuals\n    ..... and many more..!!")
    time.sleep(1)
    update.message.reply_text(
		"Please, Select the Subject. 📚")
    time.sleep(1)
    update.message.reply_text(
    "Click on to 👉 /Select_a_Subject to Dive In ...")

def selecting_subject(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Select a Subject :-\n\n ➜  /Physics - For Physics\n ➜  /Chemistry - For Chemistry\n ➜  /BEE - For BEE\n ➜  /BXE - For BXE\n ➜  /PPS - For PPS\n ➜  /Mechanics - For Mechanics\n ➜  /MathsI - For Maths-I\n ➜  /SME - For SME\n ➜  /More")

# Subjects

def physics(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("➜ /Physics_Textbook\n➜ /Physics_Notes\n➜ /Physics_Assignments\n➜ /Physics_LabManual")

def chemistry(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("➜ /Chemistry_Textbook\n➜ /Chemistry_Notes\n➜ /Chemistry_Assignments\n➜ /Chemistry_LabManual")

def bee(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("➜ /BEE_Textbook\n➜ /BEE_Notes\n➜ /BEE_Assignments\n➜ /BEE_LabManual")

def bxe(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("➜ /BXE_Textbook\n➜ /BXE_Notes\n➜ /BXE_Assignments\n➜ /BXE_LabManual")

def pps(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("➜ /PPS_Textbook\n➜ /PPS_Notes\n➜ /PPS_Assignments\n➜ /PPS_LabManual")

def mechanics(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("➜ /Mechanics_Textbook\n➜ /Mechanics_Notes\n➜ /Mechanics_Assignments\n➜ /Mechanics_LabManual")

def maths_I(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("➜ /MathsI_Textbook\n➜ /MathsI_Notes\n➜ /MathsI_Assignments\n➜ /MathsI_LabManual")

def sme(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("➜ /SME_Textbook\n➜ /SME_Notes\n➜ /SME_Assignments\n➜ /SME_LabManual")

def more(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("➜ /Timetable\n➜ /I_have_a_Suggestion")

# Content
# Physics ------------------------------------------------------------------------------------------------------------

def physics_textbook(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Wait a second... 🤏\nI am sending Physics Textbook... 📤")
    time.sleep(0.5)
    update.message.reply_document('https://t.me/DPU_DIT_Bot/3')

# Physics Notes ------------------------------------------------------------------------------------------------------------

def physics_notes(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Select a Chapter :-\n\n➜  /Physics_nU1 - Physics U-1 notes\n➜  /Physics_nU2 - Physics U-2 notes\n➜  /Physics_nU3 - Physics U-3 notes\n➜  /Physics_nU4 - Physics U-4 notes\n➜  /Physics_nU5 - Physics U-5 notes\n➜  /Physics_nU6 - Physics U-6 notes\n")

def physics_nU1(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_document('')
def physics_nU2(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")
def physics_nU3(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")
def physics_nU4(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")
def physics_nU5(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")
def physics_nU6(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")

# Physics Assignments ------------------------------------------------------------------------------------------------------------

def physics_assignments(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Select a Chapter :-\n\n➜  /Physics_aU1 - Physics U-1 asgmt\n➜  /Physics_aU2 - Physics U-2 asgmt\n➜  /Physics_aU3 - Physics U-3 asgmt\n➜  /Physics_aU4 - Physics U-4 asgmt\n➜  /Physics_aU5 - Physics U-5 asgmt\n➜  /Physics_aU6 - Physics U-6 asgmt\n")

def physics_aU1(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_document('')
def physics_aU2(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")
def physics_aU3(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")
def physics_aU4(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")
def physics_aU5(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")
def physics_aU6(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")

# Physics Lab Manual ------------------------------------------------------------------------------------------------------------

def physics_labManual(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Select an Experiment :-\n\n➜  /Physics_e1 - Physics Expt-1\n➜  /Physics_e2 - Physics Expt-2\n➜  /Physics_e3 - Physics Expt-3\n➜  /Physics_e4 - Physics Expt-4\n➜  /Physics_e5 - Physics Expt-5\n➜  /Physics_e6 - Physics Expt-6\n")

def physics_e1(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_document('')
def physics_e2(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Experiment sikhane to de. 😅")
def physics_e3(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Experiment sikhane to de. 😅")
def physics_e4(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Experiment sikhane to de. 😅")
def physics_e5(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Experiment sikhane to de. 😅")
def physics_e6(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Experiment sikhane to de. 😅")

# Chemistry ------------------------------------------------------------------------------------------------------------

def chemistry_textbook(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Wait a second... 🤏\nI am sending Chemistry Textbook... 📤")
    time.sleep(0.5)
    update.message.reply_document('https://t.me/DPU_DIT_Bot/4')

# Chemistry Notes ------------------------------------------------------------------------------------------------------------

def chemistry_notes(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Select a Chapter :-\n\n➜  /Chemistry_nU1 - Chemistry U-1 notes\n➜  /Chemistry_nU2 - Chemistry U-2 notes\n➜  /Chemistry_nU3 - Chemistry U-3 notes\n➜  /Chemistry_nU4 - Chemistry U-4 notes\n➜  /Chemistry_nU5 - Chemistry U-5 notes\n➜  /Chemistry_nU6 - Chemistry U-6 notes\n")

def chemistry_nU1(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_document('')
def chemistry_nU2(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")
def chemistry_nU3(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")
def chemistry_nU4(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")
def chemistry_nU5(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")
def chemistry_nU6(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")

# Chemistry Assignments ------------------------------------------------------------------------------------------------------------

def chemistry_assignments(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Select a Chapter :-\n\n➜  /Chemistry_aU1 - Chemistry U-1 asgmt\n➜  /Chemistry_aU2 - Chemistry U-2 asgmt\n➜  /Chemistry_aU3 - Chemistry U-3 asgmt\n➜  /Chemistry_aU4 - Chemistry U-4 asgmt\n➜  /Chemistry_aU5 - Chemistry U-5 asgmt\n➜  /Chemistry_aU6 - Chemistry U-6 asgmt\n")

def chemistry_aU1(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_document('')
def chemistry_aU2(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")
def chemistry_aU3(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")
def chemistry_aU4(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")
def chemistry_aU5(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")
def chemistry_aU6(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")

# Chemistry Lab Manual ------------------------------------------------------------------------------------------------------------

def chemistry_labManual(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Select an Experiment :-\n\n➜  /Chemistry_e1 - Chemistry Expt-1\n➜  /Chemistry_e2 - Chemistry Expt-2\n➜  /Chemistry_e3 - Chemistry Expt-3\n➜  /Chemistry_e4 - Chemistry Expt-4\n➜  /Chemistry_e5 - Chemistry Expt-5\n➜  /Chemistry_e6 - Chemistry Expt-6\n")

def chemistry_e1(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_document('')
def chemistry_e2(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Experiment sikhane to de. 😅")
def chemistry_e3(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Experiment sikhane to de. 😅")
def chemistry_e4(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Experiment sikhane to de. 😅")
def chemistry_e5(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Experiment sikhane to de. 😅")
def chemistry_e6(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Experiment sikhane to de. 😅")

# BEE ------------------------------------------------------------------------------------------------------------

def bee_textbook(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Wait a second... 🤏\nI am sending BEE Textbook... 📤")
    time.sleep(0.5)
    update.message.reply_document('https://t.me/DPU_DIT_Bot/5')

# BEE Notes ------------------------------------------------------------------------------------------------------------

def bee_notes(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Select a Chapter :-\n\n➜  /BEE_nU1 - BEE U-1 notes\n➜  /BEE_nU2 - BEE U-2 notes\n➜  /BEE_nU3 - BEE U-3 notes\n➜  /BEE_nU4 - BEE U-4 notes\n➜  /BEE_nU5 - BEE U-5 notes\n➜  /BEE_nU6 - BEE U-6 notes\n")

def bee_nU1(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_document('')
def bee_nU2(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")
def bee_nU3(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")
def bee_nU4(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")
def bee_nU5(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")
def bee_nU6(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")

# BEE Assignments ------------------------------------------------------------------------------------------------------------

def bee_assignments(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Select a Chapter :-\n\n➜  /BEE_aU1 - BEE U-1 asgmt\n➜  /BEE_aU2 - BEE U-2 asgmt\n➜  /BEE_aU3 - BEE U-3 asgmt\n➜  /BEE_aU4 - BEE U-4 asgmt\n➜  /BEE_aU5 - BEE U-5 asgmt\n➜  /BEE_aU6 - BEE U-6 asgmt\n")

def bee_aU1(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_document('')
def bee_aU2(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")
def bee_aU3(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")
def bee_aU4(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")
def bee_aU5(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")
def bee_aU6(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")

# BEE Lab Manual ------------------------------------------------------------------------------------------------------------

def bee_labManual(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Select an Experiment :-\n\n➜  /BEE_e1 - BEE Expt-1\n➜  /BEE_e2 - BEE Expt-2\n➜  /BEE_e3 - BEE Expt-3\n➜  /BEE_e4 - BEE Expt-4\n➜  /BEE_e5 - BEE Expt-5\n➜  /BEE_e6 - BEE Expt-6\n")

def bee_e1(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_document('')
def bee_e2(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Experiment sikhane to de. 😅")
def bee_e3(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Experiment sikhane to de. 😅")
def bee_e4(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Experiment sikhane to de. 😅")
def bee_e5(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Experiment sikhane to de. 😅")
def bee_e6(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Experiment sikhane to de. 😅")

# BXE ------------------------------------------------------------------------------------------------------------

def bxe_textbook(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Wait a second... 🤏\nI am sending BXE Textbook... 📤")
    time.sleep(0.5)
    update.message.reply_document('https://t.me/DPU_DIT_Bot/6')

# BXE Notes ------------------------------------------------------------------------------------------------------------

def bxe_notes(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Select a Chapter :-\n\n➜  /BXE_nU1 - BXE U-1 notes\n➜  /BXE_nU2 - BXE U-2 notes\n➜  /BXE_nU3 - BXE U-3 notes\n➜  /BXE_nU4 - BXE U-4 notes\n➜  /BXE_nU5 - BXE U-5 notes\n➜  /BXE_nU6 - BXE U-6 notes\n")

def bxe_nU1(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_document('')
def bxe_nU2(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")
def bxe_nU3(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")
def bxe_nU4(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")
def bxe_nU5(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")
def bxe_nU6(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")

# BXE Assignments ------------------------------------------------------------------------------------------------------------

def bxe_assignments(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Select a Chapter :-\n\n➜  /BXE_aU1 - BXE U-1 asgmt\n➜  /BXE_aU2 - BXE U-2 asgmt\n➜  /BXE_aU3 - BXE U-3 asgmt\n➜  /BXE_aU4 - BXE U-4 asgmt\n➜  /BXE_aU5 - BXE U-5 asgmt\n➜  /BXE_aU6 - BXE U-6 asgmt\n")

def bxe_aU1(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_document('')
def bxe_aU2(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")
def bxe_aU3(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")
def bxe_aU4(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")
def bxe_aU5(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")
def bxe_aU6(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")

# BXE Lab Manual ------------------------------------------------------------------------------------------------------------

def bxe_labManual(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Select an Experiment :-\n\n➜  /BXE_e1 - BXE Expt-1\n➜  /BXE_e2 - BXE Expt-2\n➜  /BXE_e3 - BXE Expt-3\n➜  /BXE_e4 - BXE Expt-4\n➜  /BXE_e5 - BXE Expt-5\n➜  /BXE_e6 - BXE Expt-6\n")

def bxe_e1(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_document('')
def bxe_e2(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Experiment sikhane to de. 😅")
def bxe_e3(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Experiment sikhane to de. 😅")
def bxe_e4(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Experiment sikhane to de. 😅")
def bxe_e5(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Experiment sikhane to de. 😅")
def bxe_e6(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Experiment sikhane to de. 😅")

# PPS ------------------------------------------------------------------------------------------------------------

def pps_textbook(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Wait a second... 🤏\nI am sending PPS Textbook... 📤")
    time.sleep(0.5)
    update.message.reply_document('')

# PPS Notes ------------------------------------------------------------------------------------------------------------

def pps_notes(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Select a Chapter :-\n\n➜  /PPS_nU1 - PPS U-1 notes\n➜  /PPS_nU2 - PPS U-2 notes\n➜  /PPS_nU3 - PPS U-3 notes\n➜  /PPS_nU4 - PPS U-4 notes\n➜  /PPS_nU5 - PPS U-5 notes\n➜  /PPS_nU6 - PPS U-6 notes\n")

def pps_nU1(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_document('')
def pps_nU2(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")
def pps_nU3(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")
def pps_nU4(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")
def pps_nU5(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")
def pps_nU6(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")

# PPS Assignments ------------------------------------------------------------------------------------------------------------

def pps_assignments(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Select a Chapter :-\n\n➜  /PPS_aU1 - PPS U-1 asgmt\n➜  /PPS_aU2 - PPS U-2 asgmt\n➜  /PPS_aU3 - PPS U-3 asgmt\n➜  /PPS_aU4 - PPS U-4 asgmt\n➜  /PPS_aU5 - PPS U-5 asgmt\n➜  /PPS_aU6 - PPS U-6 asgmt\n")

def pps_aU1(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_document('')
def pps_aU2(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")
def pps_aU3(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")
def pps_aU4(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")
def pps_aU5(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")
def pps_aU6(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")

# PPS Lab Manual ------------------------------------------------------------------------------------------------------------

def pps_labManual(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Select an Experiment :-\n\n➜  /PPS_e1 - PPS Expt-1\n➜  /PPS_e2 - PPS Expt-2\n➜  /PPS_e3 - PPS Expt-3\n➜  /PPS_e4 - PPS Expt-4\n➜  /PPS_e5 - PPS Expt-5\n➜  /PPS_e6 - PPS Expt-6\n")

def pps_e1(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_document('')
def pps_e2(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Experiment sikhane to de. 😅")
def pps_e3(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Experiment sikhane to de. 😅")
def pps_e4(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Experiment sikhane to de. 😅")
def pps_e5(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Experiment sikhane to de. 😅")
def pps_e6(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Experiment sikhane to de. 😅")

# Mechanics ------------------------------------------------------------------------------------------------------------

def mechanics_textbook(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Wait a second... 🤏\nI am sending Mechanics Textbook... 📤")
    time.sleep(0.5)
    update.message.reply_document('')

# Mechanics Notes ------------------------------------------------------------------------------------------------------------

def mechanics_notes(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Select a Chapter :-\n\n➜  /Mechanics_nU1 - Mechanics U-1 notes\n➜  /Mechanics_nU2 - Mechanics U-2 notes\n➜  /Mechanics_nU3 - Mechanics U-3 notes\n➜  /Mechanics_nU4 - Mechanics U-4 notes\n➜  /Mechanics_nU5 - Mechanics U-5 notes\n➜  /Mechanics_nU6 - Mechanics U-6 notes\n")

def mechanics_nU1(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_document('')
def mechanics_nU2(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")
def mechanics_nU3(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")
def mechanics_nU4(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")
def mechanics_nU5(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")
def mechanics_nU6(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")

# Mechanics Assignments ------------------------------------------------------------------------------------------------------------

def mechanics_assignments(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Select a Chapter :-\n\n➜  /Mechanics_aU1 - Mechanics U-1 asgmt\n➜  /Mechanics_aU2 - Mechanics U-2 asgmt\n➜  /Mechanics_aU3 - Mechanics U-3 asgmt\n➜  /Mechanics_aU4 - Mechanics U-4 asgmt\n➜  /Mechanics_aU5 - Mechanics U-5 asgmt\n➜  /Mechanics_aU6 - Mechanics U-6 asgmt\n")

def mechanics_aU1(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_document('')
def mechanics_aU2(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")
def mechanics_aU3(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")
def mechanics_aU4(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")
def mechanics_aU5(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")
def mechanics_aU6(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Unit Padhane to de. 😅")

# Mechanics Lab Manual ------------------------------------------------------------------------------------------------------------

def mechanics_labManual(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Select an Experiment :-\n\n➜  /Mechanics_e1 - Mechanics Expt-1\n➜  /Mechanics_e2 - Mechanics Expt-2\n➜  /Mechanics_e3 - Mechanics Expt-3\n➜  /Mechanics_e4 - Mechanics Expt-4\n➜  /Mechanics_e5 - Mechanics Expt-5\n➜  /Mechanics_e6 - Mechanics Expt-6\n")

def mechanics_e1(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_document('')
def mechanics_e2(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Experiment sikhane to de. 😅")
def mechanics_e3(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Experiment sikhane to de. 😅")
def mechanics_e4(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Experiment sikhane to de. 😅")
def mechanics_e5(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Experiment sikhane to de. 😅")
def mechanics_e6(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Pehle Experiment sikhane to de. 😅")

# Maths-I

def mathsI_textbook(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Wait a second... 🤏\nI am sending Maths-I Textbook... 📤")
    time.sleep(0.5)
    update.message.reply_document('')

def mathsI_notes(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Select a Chapter :-\n\n➜  /M1_nU1 - M1 Unit 1 notes\n➜  /M1_nU2 - M1 Unit 2 notes\n➜  /M1_nU3 - M1 Unit 3 notes\n➜  /M1_nU4 - M1 Unit 4 notes\n➜  /M1_nU5 - M1 Unit 5 notes\n➜  /M1_nU6 - M1 Unit 6 notes\n")
    time.sleep(0.5)

def mathsI_nU1(update: Update, context: CallbackContext):
    update.message.reply_document('')
def mathsI_nU2(update: Update, context: CallbackContext):
    update.message.reply_document('')
def mathsI_nU3(update: Update, context: CallbackContext):
    update.message.reply_document('')
def mathsI_nU4(update: Update, context: CallbackContext):
    update.message.reply_document('')
def mathsI_nU5(update: Update, context: CallbackContext):
    update.message.reply_document('')
def mathsI_nU6(update: Update, context: CallbackContext):
    update.message.reply_document('')

def mathsI_assignments(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Select a Chapter :-\n\n➜  /M1_aU1 - M1 U-1 assignment\n➜  /M1_aU2 - M1 U-2 assignment\n➜  /M1_aU3 - M1 U-3 assignment\n➜  /M1_aU4 - M1 U-4 assignment\n➜  /M1_aU5 - M1 U-5 assignment\n➜  /M1_aU6 - M1 U-6 assignment\n")
    time.sleep(0.5)

def mathsI_aU1(update: Update, context: CallbackContext):
    update.message.reply_document('')
def mathsI_aU2(update: Update, context: CallbackContext):
    update.message.reply_document('')
def mathsI_aU3(update: Update, context: CallbackContext):
    update.message.reply_document('')
def mathsI_aU4(update: Update, context: CallbackContext):
    update.message.reply_document('')
def mathsI_aU5(update: Update, context: CallbackContext):
    update.message.reply_document('')
def mathsI_aU6(update: Update, context: CallbackContext):
    update.message.reply_document('')

def mathsI_labManual(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Dude, does maths have lab manual..? 😂")

# SME

def sme_textbook(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Wait a second... 🤏\nI am sending SME Textbook... 📤")
    time.sleep(0.5)
    update.message.reply_document('')

def sme_notes(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Select a Chapter :-\n\n➜  /SME_nU1 - SME Unit 1 notes\n➜  /SME_nU2 - SME Unit 2 notes\n➜  /SME_nU3 - SME Unit 3 notes\n➜  /SME_nU4 - SME Unit 4 notes\n➜  /SME_nU5 - SME Unit 5 notes\n➜  /SME_nU6 - SME Unit 6 notes\n")
    time.sleep(0.5)

def sme_nU1(update: Update, context: CallbackContext):
    update.message.reply_document('')
def sme_nU2(update: Update, context: CallbackContext):
    update.message.reply_document('')
def sme_nU3(update: Update, context: CallbackContext):
    update.message.reply_document('')
def sme_nU4(update: Update, context: CallbackContext):
    update.message.reply_document('')
def sme_nU5(update: Update, context: CallbackContext):
    update.message.reply_document('')
def sme_nU6(update: Update, context: CallbackContext):
    update.message.reply_document('')

def sme_assignments(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Select a Chapter :-\n\n➜  /SME_aU1 - SME U-1 assignment\n➜  /SME_aU2 - SME U-2 assignment\n➜  /SME_aU3 - SME U-3 assignment\n➜  /SME_aU4 - SME U-4 assignment\n➜  /SME_aU5 - SME U-5 assignment\n➜  /SME_aU6 - SME U-6 assignment\n")
    time.sleep(0.5)

def sme_aU1(update: Update, context: CallbackContext):
    update.message.reply_document('')
def sme_aU2(update: Update, context: CallbackContext):
    update.message.reply_document('')
def sme_aU3(update: Update, context: CallbackContext):
    update.message.reply_document('')
def sme_aU4(update: Update, context: CallbackContext):
    update.message.reply_document('')
def sme_aU5(update: Update, context: CallbackContext):
    update.message.reply_document('')
def sme_aU6(update: Update, context: CallbackContext):
    update.message.reply_document('')

def sme_labManual(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Select an Experiment :-\n\n➜  /SME_e1 - SME Experiment 1\n➜  /SME_e2 - SME Experiment 2\n➜  /SME_e3 - SME Experiment 3\n➜  /SME_e4 - SME Experiment 4\n➜  /SME_e5 - SME Experiment 5\n➜  /SME_e6 - SME Experiment 6\n")
    time.sleep(0.5)

def sme_e1(update: Update, context: CallbackContext):
    update.message.reply_document('')
def sme_e2(update: Update, context: CallbackContext):
    update.message.reply_document('')
def sme_e3(update: Update, context: CallbackContext):
    update.message.reply_document('')
def sme_e4(update: Update, context: CallbackContext):
    update.message.reply_document('')
def sme_e5(update: Update, context: CallbackContext):
    update.message.reply_document('')
def sme_e6(update: Update, context: CallbackContext):
    update.message.reply_document('')

# More

def timetable(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text("Wait a second... 🤏\nI am sending Timetable... 📤")
    time.sleep(0.5)
    update.message.reply_document('')

def whatsapp_me(update: Update, context: CallbackContext):
    time.sleep(1)
    update.message.reply_text(
        "https://bit.ly/3RgXdkZ")

def unknown_text(update: Update, context: CallbackContext):
    time.sleep(0.5)
    update.message.reply_text(
        "I am still learning,\ngive me a valid input dear... 😊")

# #####

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('Select_a_Subject', selecting_subject))

# Subjects

updater.dispatcher.add_handler(CommandHandler('Physics', physics))
updater.dispatcher.add_handler(CommandHandler('Chemistry', chemistry))
updater.dispatcher.add_handler(CommandHandler('BEE', bee))
updater.dispatcher.add_handler(CommandHandler('BXE', bxe))
updater.dispatcher.add_handler(CommandHandler('PPS', pps))
updater.dispatcher.add_handler(CommandHandler('Mechanics', mechanics))
updater.dispatcher.add_handler(CommandHandler('MathsI', maths_I))
updater.dispatcher.add_handler(CommandHandler('SME', sme))
updater.dispatcher.add_handler(CommandHandler('More', more))

# Physics Content

updater.dispatcher.add_handler(CommandHandler('Physics_Textbook', physics_textbook))
updater.dispatcher.add_handler(CommandHandler('Physics_Notes', physics_notes))
updater.dispatcher.add_handler(CommandHandler('Physics_assignments', physics_assignments))
updater.dispatcher.add_handler(CommandHandler('Physics_LabManual', physics_labManual))
updater.dispatcher.add_handler(CommandHandler('Physics_nU1', physics_nU1))
updater.dispatcher.add_handler(CommandHandler('Physics_nU2', physics_nU2))
updater.dispatcher.add_handler(CommandHandler('Physics_nU3', physics_nU3))
updater.dispatcher.add_handler(CommandHandler('Physics_nU4', physics_nU4))
updater.dispatcher.add_handler(CommandHandler('Physics_nU5', physics_nU5))
updater.dispatcher.add_handler(CommandHandler('Physics_nU6', physics_nU6))
updater.dispatcher.add_handler(CommandHandler('Physics_aU1', physics_aU1))
updater.dispatcher.add_handler(CommandHandler('Physics_aU2', physics_aU2))
updater.dispatcher.add_handler(CommandHandler('Physics_aU3', physics_aU3))
updater.dispatcher.add_handler(CommandHandler('Physics_aU4', physics_aU4))
updater.dispatcher.add_handler(CommandHandler('Physics_aU5', physics_aU5))
updater.dispatcher.add_handler(CommandHandler('Physics_aU6', physics_aU6))
updater.dispatcher.add_handler(CommandHandler('Physics_e1', physics_e1))
updater.dispatcher.add_handler(CommandHandler('Physics_e2', physics_e2))
updater.dispatcher.add_handler(CommandHandler('Physics_e3', physics_e3))
updater.dispatcher.add_handler(CommandHandler('Physics_e4', physics_e4))
updater.dispatcher.add_handler(CommandHandler('Physics_e5', physics_e5))
updater.dispatcher.add_handler(CommandHandler('Physics_e6', physics_e6))

# Chemistry Content

updater.dispatcher.add_handler(CommandHandler('Chemistry_Textbook', chemistry_textbook))
updater.dispatcher.add_handler(CommandHandler('Chemistry_Notes', chemistry_notes))
updater.dispatcher.add_handler(CommandHandler('Chemistry_assignments', chemistry_assignments))
updater.dispatcher.add_handler(CommandHandler('Chemistry_LabManual', chemistry_labManual))
updater.dispatcher.add_handler(CommandHandler('Chemistry_nU1', chemistry_nU1))
updater.dispatcher.add_handler(CommandHandler('Chemistry_nU2', chemistry_nU2))
updater.dispatcher.add_handler(CommandHandler('Chemistry_nU3', chemistry_nU3))
updater.dispatcher.add_handler(CommandHandler('Chemistry_nU4', chemistry_nU4))
updater.dispatcher.add_handler(CommandHandler('Chemistry_nU5', chemistry_nU5))
updater.dispatcher.add_handler(CommandHandler('Chemistry_nU6', chemistry_nU6))
updater.dispatcher.add_handler(CommandHandler('Chemistry_aU1', chemistry_aU1))
updater.dispatcher.add_handler(CommandHandler('Chemistry_aU2', chemistry_aU2))
updater.dispatcher.add_handler(CommandHandler('Chemistry_aU3', chemistry_aU3))
updater.dispatcher.add_handler(CommandHandler('Chemistry_aU4', chemistry_aU4))
updater.dispatcher.add_handler(CommandHandler('Chemistry_aU5', chemistry_aU5))
updater.dispatcher.add_handler(CommandHandler('Chemistry_aU6', chemistry_aU6))
updater.dispatcher.add_handler(CommandHandler('Chemistry_e1', chemistry_e1))
updater.dispatcher.add_handler(CommandHandler('Chemistry_e2', chemistry_e2))
updater.dispatcher.add_handler(CommandHandler('Chemistry_e3', chemistry_e3))
updater.dispatcher.add_handler(CommandHandler('Chemistry_e4', chemistry_e4))
updater.dispatcher.add_handler(CommandHandler('Chemistry_e5', chemistry_e5))
updater.dispatcher.add_handler(CommandHandler('Chemistry_e6', chemistry_e6))

# BEE Content

updater.dispatcher.add_handler(CommandHandler('BEE_Textbook', bee_textbook))
updater.dispatcher.add_handler(CommandHandler('BEE_Notes', bee_notes))
updater.dispatcher.add_handler(CommandHandler('BEE_assignments', bee_assignments))
updater.dispatcher.add_handler(CommandHandler('BEE_LabManual', bee_labManual))
updater.dispatcher.add_handler(CommandHandler('BEE_nU1', bee_nU1))
updater.dispatcher.add_handler(CommandHandler('BEE_nU2', bee_nU2))
updater.dispatcher.add_handler(CommandHandler('BEE_nU3', bee_nU3))
updater.dispatcher.add_handler(CommandHandler('BEE_nU4', bee_nU4))
updater.dispatcher.add_handler(CommandHandler('BEE_nU5', bee_nU5))
updater.dispatcher.add_handler(CommandHandler('BEE_nU6', bee_nU6))
updater.dispatcher.add_handler(CommandHandler('BEE_aU1', bee_aU1))
updater.dispatcher.add_handler(CommandHandler('BEE_aU2', bee_aU2))
updater.dispatcher.add_handler(CommandHandler('BEE_aU3', bee_aU3))
updater.dispatcher.add_handler(CommandHandler('BEE_aU4', bee_aU4))
updater.dispatcher.add_handler(CommandHandler('BEE_aU5', bee_aU5))
updater.dispatcher.add_handler(CommandHandler('BEE_aU6', bee_aU6))
updater.dispatcher.add_handler(CommandHandler('BEE_e1', bee_e1))
updater.dispatcher.add_handler(CommandHandler('BEE_e2', bee_e2))
updater.dispatcher.add_handler(CommandHandler('BEE_e3', bee_e3))
updater.dispatcher.add_handler(CommandHandler('BEE_e4', bee_e4))
updater.dispatcher.add_handler(CommandHandler('BEE_e5', bee_e5))
updater.dispatcher.add_handler(CommandHandler('BEE_e6', bee_e6))

# BXE Content

updater.dispatcher.add_handler(CommandHandler('BXE_Textbook', bxe_textbook))
updater.dispatcher.add_handler(CommandHandler('BXE_Notes', bxe_notes))
updater.dispatcher.add_handler(CommandHandler('BXE_assignments', bxe_assignments))
updater.dispatcher.add_handler(CommandHandler('BXE_LabManual', bxe_labManual))
updater.dispatcher.add_handler(CommandHandler('BXE_nU1', bxe_nU1))
updater.dispatcher.add_handler(CommandHandler('BXE_nU2', bxe_nU2))
updater.dispatcher.add_handler(CommandHandler('BXE_nU3', bxe_nU3))
updater.dispatcher.add_handler(CommandHandler('BXE_nU4', bxe_nU4))
updater.dispatcher.add_handler(CommandHandler('BXE_nU5', bxe_nU5))
updater.dispatcher.add_handler(CommandHandler('BXE_nU6', bxe_nU6))
updater.dispatcher.add_handler(CommandHandler('BXE_aU1', bxe_aU1))
updater.dispatcher.add_handler(CommandHandler('BXE_aU2', bxe_aU2))
updater.dispatcher.add_handler(CommandHandler('BXE_aU3', bxe_aU3))
updater.dispatcher.add_handler(CommandHandler('BXE_aU4', bxe_aU4))
updater.dispatcher.add_handler(CommandHandler('BXE_aU5', bxe_aU5))
updater.dispatcher.add_handler(CommandHandler('BXE_aU6', bxe_aU6))
updater.dispatcher.add_handler(CommandHandler('BXE_e1', bxe_e1))
updater.dispatcher.add_handler(CommandHandler('BXE_e2', bxe_e2))
updater.dispatcher.add_handler(CommandHandler('BXE_e3', bxe_e3))
updater.dispatcher.add_handler(CommandHandler('BXE_e4', bxe_e4))
updater.dispatcher.add_handler(CommandHandler('BXE_e5', bxe_e5))
updater.dispatcher.add_handler(CommandHandler('BXE_e6', bxe_e6))

# PPS Content

updater.dispatcher.add_handler(CommandHandler('PPS_Textbook', pps_textbook))
updater.dispatcher.add_handler(CommandHandler('PPS_Notes', pps_notes))
updater.dispatcher.add_handler(CommandHandler('PPS_assignments', pps_assignments))
updater.dispatcher.add_handler(CommandHandler('PPS_LabManual', pps_labManual))
updater.dispatcher.add_handler(CommandHandler('PPS_nU1', pps_nU1))
updater.dispatcher.add_handler(CommandHandler('PPS_nU2', pps_nU2))
updater.dispatcher.add_handler(CommandHandler('PPS_nU3', pps_nU3))
updater.dispatcher.add_handler(CommandHandler('PPS_nU4', pps_nU4))
updater.dispatcher.add_handler(CommandHandler('PPS_nU5', pps_nU5))
updater.dispatcher.add_handler(CommandHandler('PPS_nU6', pps_nU6))
updater.dispatcher.add_handler(CommandHandler('PPS_aU1', pps_aU1))
updater.dispatcher.add_handler(CommandHandler('PPS_aU2', pps_aU2))
updater.dispatcher.add_handler(CommandHandler('PPS_aU3', pps_aU3))
updater.dispatcher.add_handler(CommandHandler('PPS_aU4', pps_aU4))
updater.dispatcher.add_handler(CommandHandler('PPS_aU5', pps_aU5))
updater.dispatcher.add_handler(CommandHandler('PPS_aU6', pps_aU6))
updater.dispatcher.add_handler(CommandHandler('PPS_e1', pps_e1))
updater.dispatcher.add_handler(CommandHandler('PPS_e2', pps_e2))
updater.dispatcher.add_handler(CommandHandler('PPS_e3', pps_e3))
updater.dispatcher.add_handler(CommandHandler('PPS_e4', pps_e4))
updater.dispatcher.add_handler(CommandHandler('PPS_e5', pps_e5))
updater.dispatcher.add_handler(CommandHandler('PPS_e6', pps_e6))

# Mechanics Content

updater.dispatcher.add_handler(CommandHandler('Mechanics_Textbook', mechanics_textbook))
updater.dispatcher.add_handler(CommandHandler('Mechanics_Notes', mechanics_notes))
updater.dispatcher.add_handler(CommandHandler('Mechanics_assignments', mechanics_assignments))
updater.dispatcher.add_handler(CommandHandler('Mechanics_LabManual', mechanics_labManual))
updater.dispatcher.add_handler(CommandHandler('Mechanics_nU1', mechanics_nU1))
updater.dispatcher.add_handler(CommandHandler('Mechanics_nU2', mechanics_nU2))
updater.dispatcher.add_handler(CommandHandler('Mechanics_nU3', mechanics_nU3))
updater.dispatcher.add_handler(CommandHandler('Mechanics_nU4', mechanics_nU4))
updater.dispatcher.add_handler(CommandHandler('Mechanics_nU5', mechanics_nU5))
updater.dispatcher.add_handler(CommandHandler('Mechanics_nU6', mechanics_nU6))
updater.dispatcher.add_handler(CommandHandler('Mechanics_aU1', mechanics_aU1))
updater.dispatcher.add_handler(CommandHandler('Mechanics_aU2', mechanics_aU2))
updater.dispatcher.add_handler(CommandHandler('Mechanics_aU3', mechanics_aU3))
updater.dispatcher.add_handler(CommandHandler('Mechanics_aU4', mechanics_aU4))
updater.dispatcher.add_handler(CommandHandler('Mechanics_aU5', mechanics_aU5))
updater.dispatcher.add_handler(CommandHandler('Mechanics_aU6', mechanics_aU6))
updater.dispatcher.add_handler(CommandHandler('Mechanics_e1', mechanics_e1))
updater.dispatcher.add_handler(CommandHandler('Mechanics_e2', mechanics_e2))
updater.dispatcher.add_handler(CommandHandler('Mechanics_e3', mechanics_e3))
updater.dispatcher.add_handler(CommandHandler('Mechanics_e4', mechanics_e4))
updater.dispatcher.add_handler(CommandHandler('Mechanics_e5', mechanics_e5))
updater.dispatcher.add_handler(CommandHandler('Mechanics_e6', mechanics_e6))

# Maths-I Content

updater.dispatcher.add_handler(CommandHandler('MathsI_Textbook', mathsI_textbook))
updater.dispatcher.add_handler(CommandHandler('MathsI_Notes', mathsI_notes))
updater.dispatcher.add_handler(CommandHandler('MathsI_assignments', mathsI_assignments))
updater.dispatcher.add_handler(CommandHandler('MathsI_LabManual', mathsI_labManual))
updater.dispatcher.add_handler(CommandHandler('MathsI_nU1', mathsI_nU1))
updater.dispatcher.add_handler(CommandHandler('MathsI_nU2', mathsI_nU2))
updater.dispatcher.add_handler(CommandHandler('MathsI_nU3', mathsI_nU3))
updater.dispatcher.add_handler(CommandHandler('MathsI_nU4', mathsI_nU4))
updater.dispatcher.add_handler(CommandHandler('MathsI_nU5', mathsI_nU5))
updater.dispatcher.add_handler(CommandHandler('MathsI_nU6', mathsI_nU6))
updater.dispatcher.add_handler(CommandHandler('MathsI_aU1', mathsI_aU1))
updater.dispatcher.add_handler(CommandHandler('MathsI_aU2', mathsI_aU2))
updater.dispatcher.add_handler(CommandHandler('MathsI_aU3', mathsI_aU3))
updater.dispatcher.add_handler(CommandHandler('MathsI_aU4', mathsI_aU4))
updater.dispatcher.add_handler(CommandHandler('MathsI_aU5', mathsI_aU5))
updater.dispatcher.add_handler(CommandHandler('MathsI_aU6', mathsI_aU6))

# SME Content

updater.dispatcher.add_handler(CommandHandler('SME_Textbook', sme_textbook))
updater.dispatcher.add_handler(CommandHandler('SME_Notes', sme_notes))
updater.dispatcher.add_handler(CommandHandler('SME_assignments', sme_assignments))
updater.dispatcher.add_handler(CommandHandler('SME_LabManual', sme_labManual))
updater.dispatcher.add_handler(CommandHandler('SME_nU1', sme_nU1))
updater.dispatcher.add_handler(CommandHandler('SME_nU2', sme_nU2))
updater.dispatcher.add_handler(CommandHandler('SME_nU3', sme_nU3))
updater.dispatcher.add_handler(CommandHandler('SME_nU4', sme_nU4))
updater.dispatcher.add_handler(CommandHandler('SME_nU5', sme_nU5))
updater.dispatcher.add_handler(CommandHandler('SME_nU6', sme_nU6))
updater.dispatcher.add_handler(CommandHandler('SME_aU1', sme_aU1))
updater.dispatcher.add_handler(CommandHandler('SME_aU2', sme_aU2))
updater.dispatcher.add_handler(CommandHandler('SME_aU3', sme_aU3))
updater.dispatcher.add_handler(CommandHandler('SME_aU4', sme_aU4))
updater.dispatcher.add_handler(CommandHandler('SME_aU5', sme_aU5))
updater.dispatcher.add_handler(CommandHandler('SME_aU6', sme_aU6))
updater.dispatcher.add_handler(CommandHandler('SME_e1', sme_e1))
updater.dispatcher.add_handler(CommandHandler('SME_e2', sme_e2))
updater.dispatcher.add_handler(CommandHandler('SME_e3', sme_e3))
updater.dispatcher.add_handler(CommandHandler('SME_e4', sme_e4))
updater.dispatcher.add_handler(CommandHandler('SME_e5', sme_e5))
updater.dispatcher.add_handler(CommandHandler('SME_e6', sme_e6))

# More Content

updater.dispatcher.add_handler(CommandHandler('Timetable', timetable))
updater.dispatcher.add_handler(CommandHandler('I_have_a_Suggestion', whatsapp_me))

# Filters out unknown commands & messages.

updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

# updater.start_polling

updater.start_polling()

# A Special Thanks to Maansi & Sanket.