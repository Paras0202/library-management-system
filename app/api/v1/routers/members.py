from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.config.database import get_db
from app.schemas.v1.requests.member import MemberCreate, MemberUpdate
from app.schemas.v1.responses.member import MemberResponse
from app.services.member_service import MemberService

router = APIRouter(prefix="/members", tags=["Members"])

@router.get("/", response_model=List[MemberResponse])
async def get_members(db: AsyncSession = Depends(get_db)):
    return await MemberService.get_members(db)

@router.get("/{member_id}", response_model=MemberResponse)
async def get_member(member_id: int, db: AsyncSession = Depends(get_db)):
    return await MemberService.get_member(member_id, db)

@router.post("/", response_model=MemberResponse, status_code=201)
async def create_member(member: MemberCreate, db: AsyncSession = Depends(get_db)):
    return await MemberService.create_member(member, db)

@router.put("/{member_id}", response_model=MemberResponse)
async def update_member(member_id: int, member: MemberUpdate, db: AsyncSession = Depends(get_db)):
    return await MemberService.update_member(member_id, member, db)

@router.delete("/{member_id}")
async def delete_member(member_id: int, db: AsyncSession = Depends(get_db)):
    return await MemberService.delete_member(member_id, db)
