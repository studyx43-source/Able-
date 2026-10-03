def product_available(stock: int, quantity: int) -> bool:
    return quantity > 0 and stock >= quantity
