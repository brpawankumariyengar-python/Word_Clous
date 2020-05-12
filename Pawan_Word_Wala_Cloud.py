#we import the most important module wordcloud to create a word cloud
from wordcloud import WordCloud as Shabdh_Megh

#we also import STOPWORDS from wordcloud module. These are words used in general Usage and are thus eliminated before we create a word Cloud
from wordcloud import STOPWORDS as Anavanchit_Shabdh

from PIL import Image

#Here we import pyplot to use a figure as a cloud
import matplotlib.pyplot as Chitra_Pradarshan

#We import numpy  to create an array of images
import numpy as Ganit_Ki_Kachori

#We import wikipedia module so that we can quickly do a wikipedia serarch for any input provided by the user 
import wikipedia

import random
#We import the random module so that we can access random numbers to decide which mask image to choose from

Random_Nirnaya = random.choice([1,2,3,4,5,6,7]) # Here we generate a random number from 1 to 7 as we have 7 images

RangHeen_Chitra = None

if (Random_Nirnaya == 1): 
		RangHeen_Chitra = Ganit_Ki_Kachori.array(Image.open("01_India_Mask.png"))
		print("The Map of Great Nation of India has been randomly chosen for you")
if (Random_Nirnaya == 2): 
		RangHeen_Chitra = Ganit_Ki_Kachori.array(Image.open("02_Girl_Mask.png"))
		print("Picture of a girl has been randomly chosen for you")
if (Random_Nirnaya == 3): 
		RangHeen_Chitra = Ganit_Ki_Kachori.array(Image.open("03_WorldMap_Mask.jpg"))
		print("The picture of World Map has been randomly chosen for you")
if (Random_Nirnaya == 4): 
		RangHeen_Chitra = Ganit_Ki_Kachori.array(Image.open("04_Butterfly_Mask.jpg"))
		print("A Picture of an amazing butterfly has been randomly chosen for you")
if (Random_Nirnaya == 5): 
		RangHeen_Chitra = Ganit_Ki_Kachori.array(Image.open("05_Bat_Mask.png"))
		print("A Picture of a scary bat has been randomly chosen for you")
if (Random_Nirnaya == 6): 
		RangHeen_Chitra = Ganit_Ki_Kachori.array(Image.open("06_Boy_Mask.png"))
		print("A Picture of a boy has been randomly chosen for you")
if (Random_Nirnaya == 7): 
		RangHeen_Chitra = Ganit_Ki_Kachori.array(Image.open("07_Flower_Mask.png"))
		print("A Picture of a a beautiful flowre has been randomly chosen for you")
		
print('\n'+'\n')

#Here we take up an put from user using input() method
User_Ka_Jawab = input("please provide a topic to build the world cloud on:"+'\n'+'\n')

#we search Wikipedia for the input provided by the user and select the most popular (the one on the top) option
Sheershak = wikipedia.search(User_Ka_Jawab)
Sheershak = Sheershak[0]
print('\n')
print("We shall now generate a word cloud based upon your input:  " + str(User_Ka_Jawab))
print('\n')

print(Sheershak)

#We pull up the wikipedia page as per the inputs provided by the user
Prushtha = wikipedia.page(Sheershak)

#Now we extract the contents of the page 
Soochana = Prushtha.content

#We create a set of Stop words here so that these can be supplied as an inputs to generate a word cloud
anavanchit_shabdh = set(Anavanchit_Shabdh)

#Here we generate the word cloud based upon the image we have selected and we have set the limit to 100 words
shabdh_megh = Shabdh_Megh(background_color="white", max_words=100, mask=RangHeen_Chitra,stopwords=anavanchit_shabdh, contour_color='red')

#Finally we generate the Word Cloud 
shabdh_megh.generate(Soochana) # Here the text is filled into the word cloud

#We generate an instance of word cloud we created and display via matplotlib (generally used to show graphs)
Chitra_Pradarshan.imshow(shabdh_megh,interpolation = 'bilinear')
Chitra_Pradarshan.axis("off") # By this we ensure that Axis Bars are not displated
Chitra_Pradarshan.show()

#we savee the created file onto a picture file	
shabdh_megh.to_file("Temp_Picture.png")
