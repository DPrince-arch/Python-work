from datetime import datetime
from typing import Optional, Literal
from pydantic import BaseModel, Field


class TodoBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=255, description="Title of the task")
    description: Optional[str] = Field(None, description="Optional details about the task")
    completed: bool = Field(False, description="Completion status")
    priority: Literal["low", "medium", "high"] = Field("medium", description="Task priority level")


class TodoCreate(TodoBase):
    pass


class TodoUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = None
    completed: Optional[bool] = None
    priority: Optional[Literal["low", "medium", "high"]] = None


class TodoResponse(TodoBase):
    id: int
    created_at: datetime
    completed_at: Optional[datetime] = None

    model_config = {"from_attributes": True}