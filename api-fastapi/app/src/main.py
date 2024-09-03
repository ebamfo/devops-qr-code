from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import qrcode
import os

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://qrcode.ebamforesume.cloud", "https://qrcode.ebamforesume.cloud",
                   "http://www.qrcode.ebamforesume.cloud", "https://www.qrcode.ebamforesume.cloud"],
    allow_credentials=True,
    allow_methods=["GET"],  # Allows GET methods
    allow_headers=["*"],  # Allows all headers
)



@app.get("/")
def read_item(url, dateTime):
    if not url and not dateTime:
        raise HTTPException(status_code=400, detail="url and dateTime query parameters are required")

    try:
        # Create a QR code instance
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=8,
            border=2
        )
        qr.add_data(url)
        qr.make(fit=True)

        # Create the QR code image
        img = qr.make_image(fill_color="black", back_color="white")

        # Define the file path
        qr_code_name = f"{dateTime}.png"
        
        img.save(qr_code_name)
        
        qrcode_blob_url = upload_blob_file(qrcode_blob_name=qr_code_name)

        return {"qrurl": qrcode_blob_url}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while generating the QR code: {str(e)}")


def upload_blob_file(qrcode_blob_name, container_name: str = 'qrcodes') -> str:
    try:
        connect_str = os.environ.get('AZURESTORAGECONNECTIONSTRINGQR')
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)

        # Get the container client
        container_client = blob_service_client.get_container_client(container_name)

        if not container_client.exists():
             container_client.create_container(public_access='blob')

        # Upload to container
        blob_client = container_client.get_blob_client(qrcode_blob_name)

        with open(file=os.path.join('./', qrcode_blob_name), mode="rb") as data:
            blob_client.upload_blob(data=data, overwrite=True)

        # Construct the blob URL
        blob_url = f"https://qrcode80335.blob.core.windows.net/{container_name}/{qrcode_blob_name}"

        #Delete QR Code Image from local storage after it has been uploaded to Cloud Storage
        os.remove(qrcode_blob_name)

        return blob_url

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while uploading the QR code: {str(e)}")

    
