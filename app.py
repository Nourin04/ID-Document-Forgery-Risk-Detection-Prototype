from fastapi import FastAPI, UploadFile, File
import shutil
import os

from image_utils import check_blur, check_resolution, detect_edges
from fraud_detector import analyze_with_gemini
from report_generator import generate_report

from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request

app = FastAPI()
templates = Jinja2Templates(directory="templates")

UPLOAD_FOLDER = "uploads"

# Create uploads folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
@app.get("/")
def home():
    return {"message": "ID Fraud Detection API is running"}


@app.post("/upload-id")
async def upload_id(file: UploadFile = File(...)):

    # Validate file type
    if file.content_type not in ["image/jpeg", "image/png"]:
        return {"error": "Invalid file type. Please upload JPG or PNG."}

    # Save uploaded file
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Run image quality checks
    blur, blur_score = check_blur(file_path)
    resolution = check_resolution(file_path)
    edges = detect_edges(file_path)

    # Run AI analysis safely
    try:
        ai_analysis = analyze_with_gemini(file_path)
    except Exception as e:
        ai_analysis = f"AI analysis unavailable: {str(e)}"

    # Generate structured fraud report
    report = generate_report(blur, resolution, edges)

    # Return response
    return {
        "filename": file.filename,
        "blur_detected": blur,
        "blur_score": blur_score,
        "resolution": resolution,
        "edge_score": int(edges),
        "ai_analysis": ai_analysis,
        "fraud_report": report,
        "fraud_confidence": min(report["risk_score"] / 100, 1.0)
    }