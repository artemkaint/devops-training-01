from fastapi import APIRouter, Depends, Response

from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

health_error = {
    '5XX': {
        "description": "Сервис недоступен",
    }
}

@router.get(
    "/health/",
    status_code=200,
    summary='Проверка работоспособности сервиса',
    response_description='Сервис активен',
    responses=health_error,
)
@router.head(
    "/health/",
    status_code=204,
    summary='Проверка работоспособности сервиса',
    response_description='Сервис активен',
    responses=health_error,
)
async def health_check():
    return Response(status_code=200)
