from datetime import datetime
import requests
import cv2

current_time = datetime.now().strftime("%H%M%S")
test_url = "bbc.com"
request_url = f"http://localhost:5000?url={test_url}&dateTime={current_time}"
blob_url = ""

def qrGenerator():
    try:
        print(request_url)
        r=requests.get(url=request_url)
        data = r.json()
        blob_url = data["qrurl"]
        print(blob_url)
        return blob_url
    except:
        print("GET request unsuccessful")
        

def qrComparison(url):
    try: 
        #Download Image
        filename = url.split('/')[-1]
        r = requests.get(url).content
        with open(filename, 'wb') as handler:
            handler.write(r)
    except:
        print('Image Download Unsuccessful')

    try:
        img=cv2.imread(filename)
        detector=cv2.QRCodeDetector()
        val,b,c=detector.detectAndDecode(img)
        print(val)
        if val == test_url:
            return "Test URL and QR Code generated are the same, Yippey!!"
        else:
            return "Test URL and QR Code generated are not the same"
    except:
        print("There was an error with image comparison, kindly check")

if __name__ == "__main__":
    qrComparison(url=request_url)




