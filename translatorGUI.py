from tkinter import *
from tkinter import ttk,messagebox
import tkinter as tk
from googletrans import Translator
from textblob import TextBlob
import text_to_speech as sp
import webbrowser
def main():


	def maintrans():
		def fun(x):
			#Get the input from the user 
			lets=e1.get('1.0', END)
			#translating work starts here
			translator = Translator()
			dt1 = translator.detect(lets)
			translated = translator.translate(lets,src=dt1.lang, dest=x)
			#label
			label=Label(root,text="Translated Word",font=("Helvetica",15,"bold italic"),bg="white",fg="red").place(x=865,y=100)
			#voice output 
			a = TextBlob(translated.text)
			b = a.detect_language()
			#text output
			tex=Text(root,font=("fontawesome",15,"bold italic"),height=15,width=40,borderwidth=10)
			tex.place(x=660,y=140)
			tex.insert(tk.END,translated.text)
			#clear the section
			b4=Button(root,text="Clear",fg="blue",bg="white",command=lambda: tex.delete("1.0",END))
			b4.place(x=920,y=490)
			try:
				sp.speak(translated.text,b)
			except:
				messagebox.showerror("Failed","Voice Input Not Available for This Language")
		def trans(event):
			try:
				if(option.get()==langs[0]):
					fun('en')	

				elif(option.get()==langs[1]):
					fun('ta')

				elif(option.get()==langs[2]):
					fun('af')

				elif(option.get()==langs[3]):
					fun('sq')

				elif(option.get()==langs[4]):
					fun('am')

				elif(option.get()==langs[5]):
					fun('ar')

				elif(option.get()==langs[6]):
					fun('hy')

				elif(option.get()==langs[7]):
					fun('az')

				elif(option.get()==langs[8]):
					fun('eu')

				elif(option.get()==langs[9]):
					fun('be')

				elif(option.get()==langs[10]):
					fun('bn')

				elif(option.get()==langs[11]):
					fun('bs')

				elif(option.get()==langs[12]):
					fun('bg')

				elif(option.get()==langs[13]):
					fun('ca')

				elif(option.get()==langs[14]):
					fun('ceb')

				elif(option.get()==langs[15]):
					fun('ny')

				elif(option.get()==langs[16]):
					fun('zh-cn')

				elif(option.get()==langs[17]):
					fun('zh-tw')

				elif(option.get()==langs[18]):
					fun('co')

				elif(option.get()==langs[19]):
					fun('hr')

				elif(option.get()==langs[20]):
					fun('cs')

				elif(option.get()==langs[21]):
					fun('da')

				elif(option.get()==langs[22]):
					fun('nl')

				elif(option.get()==langs[23]):
					fun('eo')

				elif(option.get()==langs[24]):
					fun('et')

				elif(option.get()==langs[25]):
					fun('tl')

				elif(option.get()==langs[26]):
					fun('fi')

				elif(option.get()==langs[27]):
					fun('fr')

				elif(option.get()==langs[28]):
					fun('fy')

				elif(option.get()==langs[29]):
					fun('gl')

				elif(option.get()==langs[30]):
					fun('ka')

				elif(option.get()==langs[31]):
					fun('de')

				elif(option.get()==langs[32]):
					fun('el')

				elif(option.get()==langs[33]):
					fun('gu')

				elif(option.get()==langs[34]):
					fun('ht')

				elif(option.get()==langs[35]):
					fun('ha')

				elif(option.get()==langs[36]):
					fun('haw')

				elif(option.get()==langs[37]):
					fun('iw')

				elif(option.get()==langs[38]):
					fun('he')

				elif(option.get()==langs[39]):
					fun('hi')

				elif(option.get()==langs[40]):
					fun('hmn')

				elif(option.get()==langs[41]):
					fun('hu')

				elif(option.get()==langs[42]):
					fun('is')

				elif(option.get()==langs[43]):
					fun('ig')

				elif(option.get()==langs[44]):
					fun('id')

				elif(option.get()==langs[45]):
					fun('ga')

				elif(option.get()==langs[46]):
					fun('it')

				elif(option.get()==langs[47]):
					fun('ja')

				elif(option.get()==langs[48]):
					fun('jw')

				elif(option.get()==langs[49]):
					fun('kn')

				elif(option.get()==langs[50]):
					fun('kk')

				elif(option.get()==langs[51]):
					fun('km')

				elif(option.get()==langs[52]):
					fun('ko')

				elif(option.get()==langs[53]):
					fun('ku')

				elif(option.get()==langs[54]):
					fun('ky')

				elif(option.get()==langs[55]):
					fun('lo')

				elif(option.get()==langs[56]):
					fun('la')

				elif(option.get()==langs[57]):
					fun('lv')

				elif(option.get()==langs[58]):
					fun('lt')

				elif(option.get()==langs[59]):
					fun('lb')

				elif(option.get()==langs[60]):
					fun('mk')

				elif(option.get()==langs[61]):
					fun('mg')

				elif(option.get()==langs[62]):
					fun('ms')

				elif(option.get()==langs[63]):
					fun('ml')

				elif(option.get()==langs[64]):
					fun('mt')

				elif(option.get()==langs[65]):
					fun('mi')

				elif(option.get()==langs[66]):
					fun('mr')

				elif(option.get()==langs[67]):
					fun('mn')

				elif(option.get()==langs[68]):
					fun('my')

				elif(option.get()==langs[69]):
					fun('ne')

				elif(option.get()==langs[70]):
					fun('no')

				elif(option.get()==langs[71]):
					fun('or')

				elif(option.get()==langs[72]):
					fun('ps')

				elif(option.get()==langs[73]):
					fun('fa')

				elif(option.get()==langs[74]):
					fun('pl')

				elif(option.get()==langs[75]):
					fun('pt')

				elif(option.get()==langs[76]):
					fun('pa')

				elif(option.get()==langs[77]):
					fun('ro')

				elif(option.get()==langs[78]):
					fun('ru')

				elif(option.get()==langs[79]):
					fun('sm')

				elif(option.get()==langs[80]):
					fun('gd')

				elif(option.get()==langs[81]):
					fun('sr')

				elif(option.get()==langs[82]):
					fun('st')

				elif(option.get()==langs[83]):
					fun('sn')

				elif(option.get()==langs[84]):
					fun('sd')

				elif(option.get()==langs[85]):
					fun('si')

				elif(option.get()==langs[86]):
					fun('sk')

				elif(option.get()==langs[87]):
					fun('sl')

				elif(option.get()==langs[88]):
					fun('so')

				elif(option.get()==langs[89]):
					fun('es')

				elif(option.get()==langs[90]):
					fun('su')

				elif(option.get()==langs[91]):
					fun('sw')

				elif(option.get()==langs[92]):
					fun('sv')

				elif(option.get()==langs[93]):
					fun('tg')

				elif(option.get()==langs[94]):
					fun('te')

				elif(option.get()==langs[95]):
					fun('th')

				elif(option.get()==langs[96]):
					fun('tr')

				elif(option.get()==langs[97]):
					fun('uk')

				elif(option.get()==langs[98]):
					fun('ur')

				elif(option.get()==langs[99]):
					fun('ug')

				elif(option.get()==langs[100]):
					fun('uz')

				elif(option.get()==langs[101]):
					fun('vi')

				elif(option.get()==langs[102]):
					fun('cy')

				elif(option.get()==langs[103]):
					fun('xh')

				elif(option.get()==langs[104]):
					fun('yi')

				elif(option.get()==langs[105]):
					fun('yo')

				elif(option.get()==langs[106]):
					fun('zu')

			except:
				messagebox.showerror("Translation Failed","Unknown Error Occured")
			

		#combobox
		langs=[
				"English", #0
				"Tamil",#1
				"Afrikaans",#2
				"Albanian",#3
				"Amharic",#4
				"Arabic",#5
				"Armenian",#6
				"Azerbaijani",#7
				"Basque",#8
				"Belarusian",#9
				"Bengali",#10
				"Bosnian",#11
				"Bulgarian",#12
				"Catalan",#13
				"Cebuano",#14
				"Chichewa",#15
				"Chinese (Simplified)",#16
				"Chinese (Traditional)",#17
				"Corsican",#18
				"Croatian",#19
				"Czech",#20
				"Danish",#21
				"Dutch",#22
				"Esperanto",#23
				"Estonian",#24
				"Filipino",#25
				"Finnish",#26
				"French",#27
				"Frisian",#28
				"Galician",#29
				"Georgian",#30
				"German",#31
				"Greek",#32
				"Gujarati",#33
				"Haitian Creole",#34
				"Hausa",#35
				"Hawaiian",#36
				"Hebrew(1)",#37
				"Hebrew(2)",#38
				"Hindi",#39
				"Hmong",#40
				"Hungarian",#41
				"Icelandic",#42
				"Igbo",#43
				"Indonesian",#44
				"Irish",#45
				"Italian",#46
				"Japanese",#47
				"Javanese",#48
				"Kannada",#49
				"Kazakh",#50
				"Khmer",#51
				"Korean",#52
				"Kurdish (Kurmanji)",#53
				"Kyrgyz",#54
				"Lao",#55
				"Latin",#56
				"Latvian",#57
				"Lithuanian",#58
				"Luxembourgish",#59
				"Macedonian",#60
				"Malagasy",#61
				"Malay",#62
				"Malayalam",#63
				"Maltese",#64
				"Maori",#65
				"Marathi",#66
				"Mongolian",#67
				"Myanmar (Burmese)",#68
				"Nepali",#69
				"Norwegian",#70
				"Odia",#71
				"Pashto",#72
				"Persian",#73
				"Polish",#74
				"Portuguese",#75
				"Punjabi",#76
				"Romanian",#77
				"Russian",#78
				"Samoan",#79
				"Scots Gaelic",#80
				"Serbian",#81
				"Sesotho",#82
				"Shona",#83
				"Sindhi",#84
				"Sinhala",#85
				"Slovak",#86
				"Slovenian",#87
				"Somali",#88
				"Spanish",#89
				"Sundanese",#90
				"Swahili",#91
				"Swedish",#92
				"Tajik",#93
				"Telugu",#94
				"Thai",#95
				"Turkish",#96
				"Ukrainian",#97
				"Urdu",#98
				"Uyghur",#99
				"Uzbek",#100
				"Vietnamese",#101
				"Welsh",#102
				"Xhosa",#103
				"Yiddish",#104
				"Yoruba",#105
				"Zulu"#106
			]
		option = ttk.Combobox(root,value=langs,state='readonly')
		option.current(0)
		option.bind("<<ComboboxSelected>>",trans)
		option.place(x=255,y=520)
	def contact_me():
		webbrowser.open("https://www.instagram.com/manjunathan_c/")
	root=tk.Tk()
	root.geometry("1300x700")
	root.configure(bg="pink")
	root.title("Translator | Manjunathan C")
	
	#heading
	label1=Label(root,text="Translator",font=("Helvetica",30,"bold italic"),bg="maroon",fg="#FFA781").place(x=555,y=10)
	
	#enter word
	label2=Label(root,text="Enter the word to Translate",font=("Helvetica",15,"bold italic"),bg="white",fg="red").place(x=215,y=100)

	#info
	dev=Label(root,text="DEVELOPED BY:- Manjunathan C")
	dev.place(x=555,y=645)
	#word entry
	e1=Text(root,font=("fontawesome",15,"bold italic"),height=15,width=40,borderwidth=10)
	e1.place(x=60,y=140)

	img=PhotoImage(file='myicon.png')
	root.iconphoto(False,img)
	#button
	b1=Button(root,text="Choose the Language and Translate",fg="blue",bg="white",command=maintrans)
	b1.place(x=215,y=490)

	b2=Button(root,text="Clear",fg="blue",bg="white",command=lambda: e1.delete("1.0",END))
	b2.place(x=155,y=520)
	

	b3=Button(root,text="Exit",fg="blue",bg="white",command=root.quit)
	b3.place(x=475,y=520)
	
	contact=Button(root,text="Contact",command=contact_me)
	contact.place(x=620,y=670)
	#translator=Translator()


	root.mainloop()
main()
