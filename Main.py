#importing libraries
from tkinter import ttk
from tkinter.messagebox import showinfo
import cv2
from tkinter import *
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\ocrtesseract.exe'

#Create an instance of tkinter frame or window
root =Tk()
root.title("IDENTIFYING DRIVERS LOCALITY AND TRANSALATING\nROAD SIGN BOARDS TO THEIR LOCAL LANGUAGE")
#Set the geometry of tkinter frame
root.geometry('700x500')
title= Label(root,text="IDENTIFYING DRIVERS LOCALITY AND \nTRANSALATING ROAD SIGN BOARDS TO THEIR LOCAL LANGUAGE",font=('arial',14,'bold'),fg='#fff6da',bg='#ed1250')
title.pack()
temp=Label(root,text=" ")
temp.pack()

#ip_camera feature
def capture():
    # url containing ip address generated 
    # by DroidCam app for accessing camera
    url = 'http://192.168.0.141:4747/video'
          
    try:
        #initializing the camera
        cap = cv2.VideoCapture(url)
        while(True):
            ret, frame = cap.read()
            
            #showing frame by frame in a window
            if frame is not None:
                cv2.imshow('Mobile Camera', frame)
            q = cv2.waitKey(1)
            if q == ord("q"):
                break
            #enter key value is 13
            if q== 13:
                #when enter key is pressed,
                #the frame is saved
                cv2.imwrite('C:/Users/vinod_000/VScodeProjects/Mini_Project/captured_img.jpg',frame)
                #and calling action method
                action()
                break
        cv2.destroyWindow('Mobile Camera')
    except Exception as e:
        print(e)
        showinfo(title='Connection Error',message='Connection to tcp://192.168.0.108:4747 failed: Error number -138 occurred')
        exit()
#creating a button for calling the capture method
cam_button=ttk.Button(root,text="LAUNCH CAMERA",command=capture)
cam_button.pack()

def compare():
    #comparing identified state and displaying the information
    if(final_text.__contains__("MH")):
        state.configure(text="MAHARASTRA")
        trnslated_txt.configure(text="पुढे जड वाहतूक",font=("arial",30))

    if(final_text.__contains__("TS")):
        state.configure(text="TELANGANA")
        trnslated_txt.configure(text="వేగం పులకరిస్తుంది \nకానీ చంపుతుంది",font=("arial",25))
    
    if(final_text.__contains__("AP")):
        state.configure(text="ANDHRA PRADESH")
        trnslated_txt.configure(text="వేగం పులకరిస్తుంది \nకానీ చంపుతుంది",font=("arial",25))

    if(final_text.__contains__("TN")):
        state.configure(text="TAMIL NADU")
        trnslated_txt.configure(text="வேகம் சிலிர்க்கிறது \nஆனால் கொல்லும்",font=("arial",25))
    if(final_text.__contains__("MP")):
        state.configure(text="MADHYA PRADESH")
        trnslated_txt.configure(text="गति रोमांचित करती है \nलेकिन मारती है",font=("arial",25))
    if(final_text.__contains__("RJ")):
        state.configure(text="RAJASTHAN")
        trnslated_txt.configure(text="गति रोमांचित करती है \nलेकिन मारती है",font=("arial",25))
    if(final_text.__contains__("KA")):
        state.configure(text="KARNATAKA")
        trnslated_txt.configure(text="ವೇಗ ರೋಮಾಂಚನಗೊಳ್ಳುತ್ತದೆ \nಆದರೆ ಕೊಲ್ಲುತ್ತದೆ",font=("arial",25))
    if(final_text.__contains__("KL")):
        state.configure(text="KERALA")
        trnslated_txt.configure(text="വേഗത \nരോമാഞ്ചമുണ്ടാക്കുന്നു, \nപക്ഷേ കൊല്ലുന്നു",font=("arial",25))
    if(final_text.__contains__("DL")):
        state.configure(text="DELHI")
        trnslated_txt.configure(text="गति रोमांचित करती है \nलेकिन मारती है",font=("arial black",25))



#Extracting text using pytesseract
final_text=" "
def action():
    
    #img =cv2.imread('C:/Users/vinod_000/VScodeProjects/Mini_Project/captured_img.jpg')
    img=cv2.imread('C:/Users/vinod_000/VScodeProjects/Mini_Project/dl.jpeg')
    def ocr_core(img):
        global final_text
        final_text= pytesseract.image_to_string(img)
        final_text=str(final_text)
        final_text=final_text.strip("")
        print(final_text)
        return final_text
        
    #image pre-processing
    def get_grayscale(image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    def remove_noise (image):
        return cv2.medianBlur (image, 5)

    def thresholding (image):
        return cv2.threshold (image, 8, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    img=get_grayscale (img)
    
    #img=thresholding (img)
    #img=remove_noise(img)
    cv2.imshow("pre_view",img)
    extracted_text=ocr_core(img)
   
    extracted_text=str(extracted_text)
    extracted_text=extracted_text.strip("")
    extracted.configure(text=extracted_text)
    compare()

mylabel2=Label(root,text="Extracted License Number",font=("ariel",15,"bold"))
mylabel2.pack()
extracted=Label(root,text=" ")
extracted.pack()

drvr_locality=Label(root,text="Drivers belongs to:",font=("arial",14,"bold"))
drvr_locality.pack()

state=Label(root,text=" ",font=('arial',12,'bold'),fg='#ed1250')
state.pack()

board=Label(root,text="DIGITAL BOARD",font=("arial",14,"bold"))
board.pack()

trnslated_txt=Label(root,text=" ",font=("arial black",15,"bold"),bg="black",fg="red",width=25,height=10,relief=RAISED)
trnslated_txt.pack()

root.mainloop()