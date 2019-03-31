Vision

A tool to give sight using machine learning, speech recognition, and object recognition



Requirements:
like a bunch of other libraries
- tensorflow
- h5py
- cv2
- speech_recognition
- pillow
- imageai

install portaudio through homebrew(mac) or apt(linux) or somewhere else windows
- before installing speech_recognition

Also need .h5 file
using resnet50_coco_best_v2.0.1.h5
(can also use other models, but some stuff would have to be changed)

sample1 is with a image if there isn't anything too interesting near you

else, micwithmore.py is the full thing
when run, say "vision" to open
It will take a picture from whatever camera it detects and use the pretrained Resnet object detection machine learning model.

it gives the output in speech based on the percentage accuracy probablility

further interaction includes asking for all objects nearby
