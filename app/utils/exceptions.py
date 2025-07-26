from fastapi import HTTPException, status

class BookNotAvailableError(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Book is not available for loan"
        )

class MemberNotFoundError(HTTPException):
    def __init__(self, member_id: int):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Member with ID {member_id} not found"
        )

class LoanAlreadyReturnedError(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="This loan has already been marked as returned"
        )
