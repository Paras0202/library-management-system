from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException

from app.models.domain.member import Member
from app.schemas.v1.requests.member import MemberCreate, MemberUpdate

class MemberService:
    @staticmethod
    async def get_members(db: AsyncSession):
        result = await db.execute(select(Member))
        return result.scalars().all()

    @staticmethod
    async def get_member(member_id: int, db: AsyncSession):
        result = await db.execute(select(Member).where(Member.id == member_id))
        member = result.scalar_one_or_none()
        if not member:
            raise HTTPException(status_code=404, detail="Member not found")
        return member

    @staticmethod
    async def create_member(member_data: MemberCreate, db: AsyncSession):
        member = Member(**member_data.dict())
        db.add(member)
        await db.commit()
        await db.refresh(member)
        return member

    @staticmethod
    async def update_member(member_id: int, update_data: MemberUpdate, db: AsyncSession):
        member = await MemberService.get_member(member_id, db)
        for field, value in update_data.dict(exclude_unset=True).items():
            setattr(member, field, value)
        await db.commit()
        await db.refresh(member)
        return member

    @staticmethod
    async def delete_member(member_id: int, db: AsyncSession):
        member = await MemberService.get_member(member_id, db)
        await db.delete(member)
        await db.commit()
        return {"message": "Member deleted successfully"}
