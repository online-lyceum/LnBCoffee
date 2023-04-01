import logging

from fastapi import APIRouter, Depends
from api_template.services import example

import schemas


logger = logging.getLogger(__name__)
router = APIRouter(
    prefix='/api',
    tags=["Hello"],
)


@router.get('')
async def get_hello_msg():
    return 'Hello from FastAPI and Lawrence'


@router.get(
    '',
    response_model=schemas.lessons.LessonList
)
async def get_examples(
        subgroup_id: Optional[int] = None,
        service: example = Depends(example)
):
    return await service.get_list(
        subgroup_id=subgroup_id
    )
