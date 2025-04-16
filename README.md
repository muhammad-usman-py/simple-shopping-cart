# 🛒 Python Project: Smart Shopping Cart with Tax Calculation  
> **A simple, beginner-friendly Python project that shows the real-life use of `filter()`, `map()`, and `reduce()`!**

---

## 📌 Description

This Python program simulates a smart shopping cart that:

- ✅ Filters items above or below ₹500  
- 💸 Calculates **18% GST** on items priced ₹500 or more  
- ➕ Adds up your **total bill**, including tax

Perfect for beginners who want to learn Python with real-world examples! 🙌

---

## 🧠 Concepts Covered

- `filter()` – to filter items by price  
- `map()` – to apply tax to selected items  
- `reduce()` – to calculate total bill  
- User Input, List Manipulation, and Basic Functions

---

## 🚀 How It Works

### 📥 Step 1: Enter Your Cart Items

```python
cart = []
input_cart = input("Enter the prices of items you have added to the cart (separated by spaces): ")
prices = [float(price) for price in input_cart.split()]
cart.extend(prices)

print("Your cart contains:", cart)
```

---

### ⚙️ Step 2: Program Does the Work

- Separates items `>= ₹500` and `< ₹500`  
- Calculates **18% tax** on eligible items  
- Sums up everything and gives your final bill!

---

## 📊 Sample Output

```
Enter the prices of items you have added to the cart (separated by spaces): 200 350 400 555 650
Your cart contains: [200.0, 350.0, 400.0, 555.0, 650.0]
Your total bill with 18% tax on items above 500 is 2571.9 Rs/-
```

---

## 📁 File Structure

```
├── shopping_cart.py       # 🧾 Main Python script
├── README.md              # 📘 Project Documentation
└── thumbnail.png          # 📸 Thumbnail for GitHub / Social Media
```

---

## 📸 Thumbnail Preview

> *(Attach the thumbnail here or drag it in GitHub README)*  
`![Smart Cart Thumbnail](thumbnail.png)`

---

## 📣 Author

**Muhammad Usman**  
💻 Class 12 Student | Future AI Engineer  
📍 Follow my learning journey on [https://www.instagram.com/muhmmad.usman.tech/](#) | [https://www.linkedin.com/in/muhammad-usman-py/](#)
