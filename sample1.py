'''

from imageai.Prediction import ImagePrediction
import os
execution_path = os.getcwd()


prediction = ImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath(os.path.join(execution_path, "resnet50_weights_tf_dim_ordering_tf_kernels.h5"))
prediction.loadModel()


predictions, probabilities = prediction.predictImage(os.path.join(execution_path, "image.jpg"), result_count=2)
for eachPrediction, eachProbability in zip(predictions, probabilities):
	print(eachPrediction , " : " , eachProbability)
'''

from imageai.Detection import ObjectDetection
from PIL import Image
import os


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
		v = ((temp[2] - temp[0]) * (temp[3] - temp[1]))
		if v > largest[0]:
			largest[1] = eachObject

	if largest[1]:
		if largest[1]["percentage_probability"] > 80:
			say = ("There is a " + eachObject["name"] + " ahead")
		elif largest[1]["percentage_probability"] > 45:
			say = ("I think there is a " + eachObject["name"] + " ahead")
		else:
			say = ("There might be a " + eachObject["name"] + "ahead")
		os.system("say " + say)
	else:
		os.system("say can not detect anything ahead")

recog("sample1.jpg")



	





#name, percentage_probablility, box_points


"""
	if doOverlap((eachObject['box_points'][0], eachObject['box_points'][1]),(eachObject['box_points'][2], eachObject['box_points'][3]),(centerbox[0], centerbox[1]),(centerbox[2], centerbox[3])):
		print(eachObject["name"] , " : " , eachObject["percentage_probability"] )
"""




