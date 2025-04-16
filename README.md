# 🛒 Python Project: Smart Shopping Cart with Tax Calculation

This is a beginner-friendly Python program that simulates a simple shopping cart.  
It demonstrates the use of:

- `filter()` to separate items based on price
- `map()` to apply 18% tax to items costing ₹500 or more
- `reduce()` to calculate the total bill

---

## 🚀 How It Works

### 📥 Step 1: Input Cart Items

The program takes space-separated prices as input:

```python
cart = []
input_cart = input("Enter the prices of items you have added to the cart (separated by spaces): ")
prices = [float(price) for price in input_cart.split()]
cart.extend(prices)

    print("Your cart contains:", cart)

```
## Sample Ouput
Enter the prices of items you have added to the cart (separated by spaces): 200 350 400 555 650
Your cart contains: [200.0, 350.0, 400.0, 555.0, 650.0]
Your total bill with 18% tax on items above 500 is 2571.9 Rs/-
