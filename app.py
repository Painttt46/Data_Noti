from fastapi import FastAPI, HTTPException ,Request 
from pydantic import BaseModel, Field
from typing import Any, Dict
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # อนุญาตการเชื่อมต่อจากทุกโดเมน
    allow_credentials=True,
    allow_methods=["*"], # อนุญาตทุก HTTP Method
    allow_headers=["*"], # อนุญาตทุก HTTP Header
)

class PowerAutomatePayload(BaseModel):
    responder_email: str = Field(..., example="user@example.com")
    submission_time: str = Field(..., example="2025-09-30T10:30:00Z")
    form_data: Dict[str, Any]


@app.get("/")
async def read_root():
    return {"status": "ok", "message": "API is online!"}

@app.post("/api")
async def receive_power_automate_data(payload: PowerAutomatePayload):
    
    try:
        print("✅ have Data")
        print(f"   - respond email: {payload.responder_email}")
        print(f"   - submit time: {payload.submission_time}")
        
        print("   - forms data:")
        for question, answer in payload.form_data.items():
            print(f"     - {question}: {answer}")

        return {
            "status": "success", 
            "message": "Data received successfully."
        }
    
    except Exception as e:
        print(f"❌ error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/Notify")
async def notify(request: Request):
   #รอ DATA BAS
