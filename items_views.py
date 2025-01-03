from typing import Annotated

from fastapi import APIRouter, Path

router = APIRouter(prefix="/items", tags=["items"])


@router.get("/")
def list_items():
    return [
        'items1',
        'items2',
    ]


@router.get("/latest/")
def get_latest_items():
    return {"item": {'id': '0', 'name': 'latest'}}


@router.get("/{item_id}/")
def get_item_by_id(item_id: Annotated[int, Path(ge=1, lt=10000000)]):
    """
    accepts ID from 1 to 10000000
    from typing import Annotated
    from fastapi import FastAPI, Path
    """
    return {
        'item': {
            'id': item_id,
        }
    }
