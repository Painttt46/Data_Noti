# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Any, Dict

# สร้าง Instance ของ FastAPI
app = FastAPI(
    title="Power Automate Webhook API",
    description="API สำหรับรับข้อมูลจาก Power Automate workflow",
    version="1.0.0"
)

# สร้าง Model เพื่อรับข้อมูล JSON ที่ส่งมาจาก Power Automate
class PowerAutomatePayload(BaseModel):
    responder_email: str = Field(..., example="user@example.com")
    submission_time: str = Field(..., example="2025-09-30T10:30:00Z")
    form_data: Dict[str, Any]

# สร้าง API Endpoint
@app.post("/webhook/form-response")
async def receive_power_automate_data(payload: PowerAutomatePayload):
    """
    Endpoint นี้จะรอรับข้อมูล (POST request) จาก Power Automate
    """
    try:
        # แสดงข้อมูลที่ได้รับใน Console (Vercel จะแสดงใน Logs)
        print("✅ ได้รับข้อมูลจาก Power Automate:")
        print(f"   - อีเมลผู้ตอบ: {payload.responder_email}")
        print(f"   - เวลาที่ส่ง: {payload.submission_time}")
        
        print("   - ข้อมูลในฟอร์ม:")
        for question, answer in payload.form_data.items():
            print(f"     - {question}: {answer}")

        # ส่ง Response กลับไปบอก Power Automate ว่ารับข้อมูลสำเร็จแล้ว
        return {
            "status": "success", 
            "message": "Data received successfully."
        }
    
    except Exception as e:
        print(f"❌ เกิดข้อผิดพลาด: {e}")
        raise HTTPException(status_code=500, detail=str(e))