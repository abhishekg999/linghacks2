# import speech_recognition as sr


# r = sr.Recognizer()
# aaryan = sr.AudioFile('/Users/adivate2021/Downloads/aaryan.wav')
# with aaryan as source:
# 	audio = r.record(source)
# print(r.recognize_google(audio))

import speech_recognition as sr
import os
import time

from imageai.Detection import ObjectDetection
from PIL import Image
import cv2


#1612.8, 1209.6, 2419.2, 1814.4
def doOverlap(l1, r1, l2, r2):
	if (l1[0] > r2[0] or l2[0] > r1[0]):
		print(l1, r2, l2, r1)
		print(str(l1[0]) + " > " + str(r2[0]))
		print(str(l2[0]) + " > " + str(r1[0]))
		return False

	if (l1[1] < r2[1] or l2[1] < r1[1]):
		print(l1, r2, l2, r1)
		print(str(l1[1]) + " < " + str(r2[1]))
		print(str(l2[1]) + " < " + str(r1[1]))
		return False
  
	return True


execution_path = os.getcwd()
detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
detector.loadModel()


def recog(image):
	global detections
	im = Image.open(image)
	width, height = im.size

	detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , image), output_image_path=os.path.join(execution_path , "imagenew.jpg"))

	centerbox = (((width/2)-(width/10)), ((height/2)-(height/10)), ((width/2)+(width/10)), ((height/2)+(height/10)))
	print (centerbox)

	largest = [0, "none"]
	for eachObject in detections:
		#print(eachObject["name"] , " : " , eachObject["percentage_probability"] )
		print(eachObject["name"] , " : " , eachObject["percentage_probability"] )
		print("\n")
		print("sfkasfsjfkafsfjdsfakfdjkbfskj")
		temp = eachObject["box_points"]

		if doOverlap((eachObject['box_points'][0], eachObject['box_points'][1]),(eachObject['box_points'][2], eachObject['box_points'][3]),(centerbox[0], centerbox[1]),(centerbox[2], centerbox[3])):
			print(eachObject["name"] , " : " , eachObject["percentage_probability"] )

		v = ((temp[2] - temp[0]) * (temp[3] - temp[1]))
		if v > largest[0]:
			largest[1] = eachObject

	if largest[1]["percentage_probability"] > 80:
		say = ("There is a " + eachObject["name"] + " ahead")
	elif largest[1]["percentage_probability"] > 45:
		say = ("I think there is a " + eachObject["name"] + " ahead")
	else:
		say = ("There might be a " + eachObject["name"] + "ahead")
	os.system("say " + say)

def secondRecognitionProgram():

	r = sr.Recognizer()
	mic = sr.Microphone()

	say = "Do you want more info?"
	os.system("say " + say)
	with mic as source:
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source, phrase_time_limit = 0.69)
	response = {
		"success": True,
		"error": None,
		"transcription": None
	}

	try:
		response["transcription"] = r.recognize_google(audio)
	except sr.RequestError:
		response["success"] = False
		response["error"] = "API unavailable"
	except sr.UnknownValueError:
		response["error"] = "Unable to recognize speech"
	print(response)
	transcription = response["transcription"]
	nt = []

	working = False
	if transcription == "yes" or "yeah":
		for x in range(len(detections)):
			if detections[x]["name"] not in nt:
				nt.append(detections[x]["name"])
				
		working = True
		if len(nt) == 1:
			say = "I only see a " + nt[0] 
			os.system("say " + say)
		elif len(nt) == 2:
			say = "I see a " + nt[0] + " and a " + nt[1]
			os.system("say " + say)
		else: 
			say = "I see a"
			for x in range(len(nt)-1):
				say += " , " + nt[x] 
			say += " , and a " + nt[len(nt) -1]
			print (say)
			os.system("say " + say)

	elif transcription == "no":
		working = True
	else:
		secondRecognitionProgram()


	#################
def RecognitionProgram():
	r = sr.Recognizer()
	mic = sr.Microphone()
	with mic as source:
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source, phrase_time_limit = 0.69)
	response = {
		"success": True,
		"error": None,
		"transcription": None
	}
	try:
		response["transcription"] = r.recognize_google(audio)
	except sr.RequestError:
		response["success"] = False
		response["error"] = "API unavailable"
	except sr.UnknownValueError:
		response["error"] = "Unable to recognize speech"
	print(response)
	transcription = response["transcription"]
	if transcription == "site" or transcription == "sight" or transcription == "see" or transcription == "vision":
		camera = cv2.VideoCapture(0)
		say = "Opening vision, scanning your enviornment."
		os.system("say " + say)
		time.sleep(0.1)  # If you don't wait, the image will be dark
		return_value, image = camera.read()
		cv2.imwrite('opencv.png', image)
		del(camera)
		recog("opencv.png")

		secondRecognitionProgram()
		RecognitionProgram()	
	else:
		RecognitionProgram()		
RecognitionProgram()

