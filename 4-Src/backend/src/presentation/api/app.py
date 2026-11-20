from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from src.domain.shared.exceptions import BusinessException

app = FastAPI()

@app.exception_handler(BusinessException)
async def business_exception_handler(request: Request, exc: BusinessException):
    return JSONResponse(
        status_code=exc.http_status,
        content={
            "statusCode": exc.http_status,
            "status": "error",
            "message": exc.message,
            "errorCode": exc.error_code,
            "data": None
        }
    )

# بقیه کدهای مربوط به lifespan و include_router ...