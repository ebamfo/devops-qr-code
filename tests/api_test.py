from datetime import datetime
import requests
import cv2

current_time = datetime.now().strftime("%H%M%S")
test_url = "bbc.com"
request_url = f"http://localhost:5000?url={test_url}&dateTime={current_time}"
blob_url = ""

def qrGenerator():
    try:
        print(f"Making GET request to: {request_url}")
        r = requests.get(url=request_url)
        data = r.json()
        blob_url = data["qrurl"]
        print(f"QR Code URL: {blob_url}")
        return blob_url
    except Exception as e:
        print(f"GET request unsuccessful: {e}")
        return None

def qrComparison(url):
    try: 
        # Download Image
        filename = url.split('/')[-1]
        r = requests.get(url).content
        with open(filename, 'wb') as handler:
            handler.write(r)
        print(f"Image downloaded as: {filename}")
    except Exception as e:
        print(f"Image download unsuccessful: {e}")
        return

    try:
        # QR Code detection and decoding
        img = cv2.imread(filename)
        detector = cv2.QRCodeDetector()
        val, _, _ = detector.detectAndDecode(img)
        print(f"Decoded QR code value: {val}")
        if val == test_url:
            return "Test URL and QR Code generated are the same, Yippey!!"
        else:
            return "Test URL and QR Code generated are not the same"
    except Exception as e:
        print(f"There was an error with image comparison: {e}")

if __name__ == "__main__":
    blob_url = qrGenerator()
    if blob_url:
        result = qrComparison(url=blob_url)
        if result:
            print(result)
