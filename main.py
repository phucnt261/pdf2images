from fastapi import FastAPI, UploadFile
from pdf2image import convert_from_bytes
import base64, io

app = FastAPI()

@app.post("/pdf-to-images")
async def pdf_to_images(file: UploadFile):
    pdf_bytes = await file.read()
    pages = convert_from_bytes(pdf_bytes, dpi=200)  # dpi=200 cho chất lượng OK
    images_base64 = []
    for page in pages:
        buffer = io.BytesIO()
        page.save(buffer, format="PNG")
        img_str = base64.b64encode(buffer.getvalue()).decode("utf-8")
        images_base64.append(img_str)
    return {"images": images_base64}
