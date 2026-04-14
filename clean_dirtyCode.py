"""
Module to handle invoice processing following SOLID principles.
"""

def calculate_discounted_total(amount: float, has_discount: bool) -> float:
    """Calculates the amount after applying potential discounts."""
    discount_rate = 0.90 if has_discount else 1.0
    return amount * discount_rate

def apply_tax(amount: float, tax_rate: float = 0.15) -> float:
    """Applies tax to a given amount."""
    return amount * (1 + tax_rate)

def save_invoice_to_file(customer_name: str, total_amount: float, filename: str = "data.txt"):
    """Handles the persistence of invoice data to a text file."""
    try:
        with open(filename, "w") as file:
            file.write(f"User: {customer_name} Total: {total_amount:.2f}")
    except IOError as e:
        print(f"Error saving file: {e}")

def process_invoice(customer_name: str, base_amount: float, has_discount: bool):
    """
    Orchestrates the invoice process: calculation, logging, and saving.
    Following SRP (Single Responsibility Principle).
    """
    # 1. Calculation Logic
    discounted_total = calculate_discounted_total(base_amount, has_discount)
    final_total = apply_tax(discounted_total)
    
    # 2. Console Output
    print(f"Processing invoice for: {customer_name}")
    print(f"Final Amount: {final_total:.2f}")
    
    # 3. Data Persistence
    save_invoice_to_file(customer_name, final_total)
    
    return final_total

if __name__ == "__main__":
    # Example execution with clear variable names
    invoice_total = process_invoice("Juan Perez", 100.0, True)
    