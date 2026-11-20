from typing import Generic, TypeVar, Optional, List
from pydantic import BaseModel

T = TypeVar("T")

class StandardResponse(BaseModel, Generic[T]):
    statusCode: int
    status: str
    message: str
    errorCode: int = 0
    data: Optional[T] = None

class PaginationData(BaseModel, Generic[T]):
    offset: int
    limit: int
    totalRecord: int
    dataList: List[T]