import strawberry
from datetime import datetime
from crud.user_transaction import get_user_transaction, user_transaction
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from sqlalchemy.orm import Session
from schemas.user_transaction import TransactionInput

@strawberry.type
class Transaction:
    id: int
    user_id: int
    amount: float
    date: str

    @staticmethod
    async def create_transaction_instance(session: AsyncSession, id: int) -> List["Transaction"]:
        result = await get_user_transaction(session=session, id=id)
        data = []
        for transaction in result:
            user_transaction = Transaction(
                id=transaction.id,
                user_id=transaction.user_id,
                amount=transaction.amount,
                date=transaction.date,
            )
            data.append(user_transaction)
        return data

    @staticmethod
    def create_user_transaction(session: Session, transaction_input: TransactionInput) -> "Transaction":
        result = user_transaction(session=session, transaction=transaction_input)
        transaction = Transaction(
            id=result.id,
            user_id=result.user_id,
            amount=result.amount,
            date=result.date,
        )
        return transaction