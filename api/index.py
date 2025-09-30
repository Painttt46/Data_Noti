from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Any, Dict

app = FastAPI()

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
        print("✅ ได้รับข้อมูลจาก Power Automate:")
        print(f"   - อีเมลผู้ตอบ: {payload.responder_email}")
        print(f"   - เวลาที่ส่ง: {payload.submission_time}")
        
        print("   - ข้อมูลในฟอร์ม:")
        for question, answer in payload.form_data.items():
            print(f"     - {question}: {answer}")

        return {
            "status": "success", 
            "message": "Data received successfully."
        }
    
    except Exception as e:
        print(f"❌ เกิดข้อผิดพลาด: {e}")
        raise HTTPException(status_code=500, detail=str(e))

handler = app
