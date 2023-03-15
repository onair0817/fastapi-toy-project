from fastapi import FastAPI, Query
from typing import Optional, List


app = FastAPI()


# @app.get("/many_items/")
# async def read_many_items(
#     # q: Optional[str] = Query("fixedquery", min_length=3, max_length=50)
#     q: Optional[List[str]] = Query(
#         "okay",
#     )
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


#


@app.get("/many_items/")
async def read_many_item_list(
    # q: Optional[str] = Query("fixedquery", min_length=3, max_length=50)
    q: Optional[List[str]] = Query(["foo", "bar"], deprecated=True),
):
    # results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    query_items = {"q": q}
    return query_items
