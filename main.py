from fastapi import FastAPI, HTTPException, Query, Path
from services.products import change_product, get_all_products, add_product, remove_product
from schema.product import Product, ProductUpdate
from uuid import uuid4, UUID
from datetime import datetime,timezone

app = FastAPI()


@app.get("/products")
def list_products(
    name: str = Query(
        default=None,
        min_length=3,
        max_length=50,
        description="Search By Product Name"
    ),

    sort_by_price: bool = Query(
        default= False,
        description= "Sort Products by price.",
    ),

    order: str = Query(
        default= "asc", description="Sort order when sort_by_price=true (asc,desc)"
    )
):
    products = get_all_products()

    if name:
        needle = name.strip().lower()

        products = [
            p for p in products
            if needle in p.get("name", "").lower()
        ]

        if not products:
            raise HTTPException(
                status_code=404,
                detail=f"No product found with this name = {name}."
            )
    if sort_by_price:
        reverse = order =="desc"
        products = sorted(products, key=lambda p: p.get("price", 0), reverse=reverse)

    total = len(products)

    return {
        "total": total,
        "items": products
    }

@app.post("/products", status_code=201)
def create_product(product: Product):
    product_dict = product.model_dump(mode="json")

    product_dict["id"] = str(uuid4())
    product_dict["created_at"] = (
        datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    )

    try:
        add_product(product_dict)
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

    return product_dict


@app.delete("/products/{product_id}")
def delete_product(
    product_id: UUID = Path(..., description="Product ID")
):
    try:
        return remove_product(str(product_id))
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )

@app.put("/products/{product_id}")
def update_product(product_id: UUID = Path(..., description="Product UUID"), payload: ProductUpdate = ...):
    try:
        update_product = change_product(
            str(product_id), payload.model_dump(mode = "json", exclude_unset = True)
        )

        return update_product
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail= str(e)
        )
 
