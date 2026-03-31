from fastapi import APIRouter

from user import router as user_router
from items import router as items_router
from ledger import router as ledger_router
from reports import router as reports_router

router = APIRouter()

router.include_router(user_router)
router.include_router(items_router)
router.include_router(ledger_router)
router.include_router(reports_router)