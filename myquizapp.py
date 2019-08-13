from tkinter import Tk, Frame, Label, Button
from time import sleep

class Question:
	def __init__(self, question, answer, correct):
	 self.question = question
	 self.answer = answer
	 self.correct = correct
	def check(self, letter, view):

		if(letter == self.correct):
			global right
			label = Label(view, text = "Right!")
			right += 1
		else:
			label = Label(view, text = "Wrong, learn the way to answer this.")
		label.pack()
		view.after(1000, lambda *args: self.decodeView(view))

	def GUIconstruct(self, window):
		view = Frame(window)
		Label(view, text = self.question).pack()
		Button(view, text = self.answer[0], command = lambda *args: self.check("A", view)).pack()
		Button(view, text = self.answer[1], command = lambda *args: self.check("B", view)).pack()
		Button(view, text = self.answer[2], command = lambda *args: self.check("C", view)).pack()
		Button(view, text = self.answer[3], command = lambda *args: self.check("D", view)).pack()
		#Button(view, text = self.answer[4], command = lambda *args: self.check("E", view)).pack()
		return view

	def decodeView(self, view):
		view.pack_forget()
		askQuestion()

def askQuestion():
	global questions, window, index, button, right, allquestions
	if(len(questions) == index + 1):
		Label(window, text="Thank you for answering the questions. " + str(right) + " of " + str(number_of_questions) + " questions answered right").pack()
		return
	button.pack_forget()
	index += 1
	questions[index].GUIconstruct(window).pack()

questions = []
file = open("Chapter 28 Biology.txt", "r")
line = file.readline()
while(line != ""):
    questionString = line
    answers = []
    for i in range (4):
        answers.append(file.readline())

    correct = file.readline()
    correct = correct[:-1]
    questions.append(Question(questionString, answers, correct))
    line = file.readline()
file.close()
index = -1
right = 0
number_of_questions = len(questions)

window = Tk()
button = Button(window, text="Start", command=askQuestion)
button.pack()
window.mainloop()


