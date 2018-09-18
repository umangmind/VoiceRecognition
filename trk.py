#rendering the HTML page which has the button
from flask import Flask, render_template, Response, request, redirect, url_for
import VerifyFile
from VerifyFile import verify_file
import win32api


app = Flask(__name__)   

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/voiceVerify', methods=['GET'])
def hello_world():
 #voice = r'.\EagleDoor-Voice-Authentication\my_voice_ubm.wav'
 voice = r'my_voice_ubm.wav'
 print("hello uma")
 VerificationResult = VerifyFile.verify_file('3df4068322a9479b99f59be512059ab0',voice,'54228031-e7b3-4172-bba4-4f13fcc9d34e')
 if VerificationResult == "Accept":
  return render_template('loginSuccess.html')
 else:
  win32api.MessageBox(0, 'Please Provide Correct Credentials!', 'Login Failed', 0x00001000) 
  return render_template('index.html')
 
 
 
#background process happening without any refreshing
#@app.route('/background_process_test')
#def background_process_test():
 #   print "Hello"
  #  return "nothing"""
  
if __name__ == '__main__':
	app.run(debug=True)