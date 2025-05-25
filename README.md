
# ☕ Coffee Shop Challenge

Welcome to the **Coffee Shop Challenge**, a Python-based OOP (Object-Oriented Programming) mini-project. The goal is to model a simple coffee shop system involving customers, coffee types, and their respective orders while practicing core OOP principles like encapsulation, associations, and data validation.

---

## 📋 Requirements

### 1. Models & Initializers

#### 🧍 Customer
```python
__init__(self, name)
```
- Accepts a name (must be a `str` with **1–15 characters**).
- `name` property:
  - Getter returns the customer's name.
  - Setter enforces string type and length constraints.

#### ☕ Coffee
```python
__init__(self, name)
```
- Accepts a name (must be a `str` with **at least 3 characters**).
- `name` property:
  - Getter returns the coffee’s name.
  - **Immutable** once set during initialization.

#### 🧾 Order
```python
__init__(self, customer, coffee, price)
```
- Accepts:
  - A `Customer` instance.
  - A `Coffee` instance.
  - A `price` (`float` between **1.0 and 10.0**).
- `price` property:
  - Getter returns the order price.
  - **Immutable** and validated on initialization.

---

### 2. Object Relationships

- `Order.customer` → Returns the associated `Customer` (with type-checking).
- `Order.coffee` → Returns the associated `Coffee` (with type-checking).
- `Customer.orders()` → Returns all `Order` instances for that customer.
- `Customer.coffees()` → Returns a unique list of `Coffee` instances they’ve ordered.
- `Coffee.orders()` → Returns all `Order` instances for that coffee.
- `Coffee.customers()` → Returns a unique list of `Customer` instances who’ve ordered that coffee.

---

### 3. Aggregates & Associations

- `Customer.create_order(coffee, price)`  
  - Instantiates a new `Order`, linking the `Customer` and the given `Coffee`.

- `Coffee.num_orders()`  
  - Returns the total number of orders for this coffee (**0 if none**).

- `Coffee.average_price()`  
  - Returns the average price across all orders for this coffee (**0 if none**).

---

### 4. 🔥 Bonus Feature (Optional)

- `Customer.most_aficionado(coffee)` *(classmethod)*  
  - Returns the `Customer` who has spent the **most** on the given `Coffee`.  
  - Returns `None` if no orders exist.

---

## ✅ Learning Objectives

- Master **object-oriented programming** patterns.
- Implement **data encapsulation** and **validation**.
- Practice working with **object associations** and **aggregated behaviors**.

---

## 🛠️ Getting Started

1. Clone the repository.
2. Implement the `Customer`, `Coffee`, and `Order` classes.
3. Write test scripts to validate behavior and relationships.
4. Explore optional features for advanced OOP practice.

---

## 📎 License

This project is for educational purposes and is open-source under the MIT License.
