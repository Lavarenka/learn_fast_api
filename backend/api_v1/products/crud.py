from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Product
from .chemas import ProductCreate, ProductUpdate, ProductUpdatePartial


async def get_products(session: AsyncSession) -> list[Product]:
    """
    we get product objects

    """
    stmt = select(Product).order_by(Product.id)  # request all product
    result: Result = await session.execute(stmt)
    products = result.scalars().all()
    return list(products)


async def get_product(session: AsyncSession, product_id: int) -> Product | None:
    """
    we get product object by id

    """
    return await session.get(Product, product_id)


async def create_product(session: AsyncSession, product_in: ProductCreate) -> Product:
    """
    create product object

    """
    product = Product(**product_in.model_dump())
    session.add(product)  # add session
    await session.commit()  # save product in db
    # await session.refresh(product)  # save field update database
    return product


async def update_product(
        session: AsyncSession,
        product: Product,
        product_update: ProductUpdate | ProductUpdatePartial,
        partial: bool = False,
) -> Product:
    for name, value in product_update.model_dump(exclude_unset=partial).items():
        setattr(product, name, value)
    await session.commit()
    return product


# async def update_product_partial(
#         session: AsyncSession,
#         product: Product,
#         product_update: ProductUpdatePartial
# ):
#     for name, value in product_update.model_dump(exclude_unset=True).items():
#         setattr(product, name, value)
#     await session.commit()
#     return product


async def delete_product(
        session: AsyncSession,
        product: Product,
) -> None:
    await session.delete(product)
    await session.commit()
