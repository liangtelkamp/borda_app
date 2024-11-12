
<div style="text-align: center;">
    <img src="images/Slide2.png" alt="Alt text" title="a title" width="500" />
</div>

<div style="text-align: center;">
  <h1>Codekwaliteit bij NextHuman 🚀</h1>
</div>

We willen ervoor zorgen dat onze code niet alleen werkt, maar ook gemakkelijk te lezen en onderhouden is. Daarom hebben we deze gids opgesteld om een paar belangrijke principes van codekwaliteit te delen. 

   * [Basis concepten 'Goede code'](#basis-concepten-goede-code)
        * [Modularity](#modularity)
        * [Cohesion](#cohesion)
        * [Separation of concerns](#separation-of-concerns)
        * [Information hiding and abstraction](#information-hiding-and-abstraction)
        * [Coupling](#coupling)
        * [One Rule to Rule Them All](#one-rule-to-rule-them-all)
- [Principles of Maintainable Code](#principles-of-maintainable-code)
   * [Write short units of code](#write-short-units-of-code)
   * [Write simple units of code (KISS)](#write-simple-units-of-code-kiss)
   * [Write code once (DRY)](#write-code-once-dry)
   * [Keep unit interfaces small](#keep-unit-interfaces-small)
   * [Separate concerns - Cohesion and Coupling](#separate-concerns-cohesion-and-coupling)
      + [Tightly coupled, Low cohseion](#tightly-coupled-low-cohseion)
      + [Better cohesion](#better-cohesion)
      + [Tightly coupled (bad example)](#tightly-coupled-bad-example)
   * [Couple architecture components loosely](#couple-architecture-components-loosely)
   * [Keep architecture components balanced](#keep-architecture-components-balanced)
   * [Keep your codebase small & YAGNI](#keep-your-codebase-small-yagni)
   * [Automate development pipeline and test](#automate-development-pipeline-and-test)
   * [Write clean ](#write-clean)

# Basis concepten 'Goede code'
## Modularity
Dit is de mate waarin een systeem is opgedeeld in afzonderlijke modules of componenten. Goede modulaire ontwerpen zijn gemakkelijker te begrijpen, te onderhouden en te testen. Modules moeten duidelijk gedefinieerde verantwoordelijkheden hebben en goed samenwerken om het systeem als geheel te laten werken.

## Cohesion
Dit is de mate waarin de elementen binnen een module bij elkaar horen. Hoge cohesie betekent dat de elementen nauw verwant zijn en samenwerken om een gemeenschappelijk doel te bereiken. Lage cohesie betekent dat de elementen minder gerelateerd zijn en verschillende taken zelfstandig uitvoeren.

## Separation of concerns
SoC keeps systems modular and maintainable by separating different concerns into distinct sections. Each section is responsible for a specific aspect of the system, such as user interface, data storage, or business logic. This separation makes it easier to understand, test, and modify individual components without affecting others.

## Information hiding and abstraction
Information hiding restricts access to certain parts of a module, making them private or protected. Abstraction focuses on exposing only essential details while hiding unnecessary complexity. These principles help in reducing complexity, improving security, and promoting reusability.

## Coupling
Dit is de mate van afhankelijkheid tussen modules. Losse koppeling betekent dat modules onafhankelijk van elkaar werken en veranderingen in de ene module weinig invloed hebben op andere modules. Strakke koppeling betekent dat modules sterk van elkaar afhankelijk zijn, waardoor veranderingen in de ene module grote impact kunnen hebben op andere modules.
## One Rule to Rule Them All
Easy to change (ETC) is the one rule that encompasses all other rules. If your code is easy to change, it is likely to be maintainable, testable, and scalable. Design your systems with change in mind, and you'll be on the right path to writing high-quality code.

# Principles of Maintainable Code
## Write short units of code
Writing short units of code is a good practice to keep the codebase clean and maintainable. It is easier to understand and test small units of code. It is also easier to reuse small units of code in other parts of the codebase. According to Farley, functions should be no longer than 20-30 lines of code.

<details>
  <summary>Example</summary>


```python
def process_order(order):
    # Step 1: Validate the order
    if not order['item'] or order['quantity'] <= 0 or not order['customer']:
        return "Invalid order"
    
    # Step 2: Calculate the total price
    price_per_item = 20
    total_price = order['quantity'] * price_per_item
    
    # Step 3: Apply discount
    if order['quantity'] >= 10:
        total_price *= 0.9  # 10% discount

    # Step 4: Save order to database (dummy function)
    print(f"Saving order for {order['customer']} with total {total_price}")

    return f"Order processed for {order['customer']}, total price: {total_price}"

# Calling the function
order = {'item': 'book', 'quantity': 15, 'customer': 'John Doe'}
print(process_order(order))

```
```python
def validate_order(order):
    if not order['item'] or order['quantity'] <= 0 or not order['customer']:
        return False
    return True

def calculate_price(quantity, price_per_item=20):
    return quantity * price_per_item

def apply_discount(total_price, quantity, discount_threshold=10, discount_rate=0.1):
    if quantity >= discount_threshold:
        return total_price * (1 - discount_rate)
    return total_price

def save_order(order, total_price):
    print(f"Saving order for {order['customer']} with total {total_price}")

def process_order(order):
    if not validate_order(order):
        return "Invalid order"
    
    total_price = calculate_price(order['quantity'])
    total_price = apply_discount(total_price, order['quantity'])
    
    save_order(order, total_price)
    
    return f"Order processed for {order['customer']}, total price: {total_price}"

# Calling the function
order = {'item': 'book', 'quantity': 15, 'customer': 'John Doe'}
print(process_order(order))

```

- Single Responsibility: Each function now has a clear purpose (validation, price calculation, discount application, etc.).
- Reusability: The calculate_price and apply_discount functions can be reused elsewhere.
- Testability: Each function is small and easier to test individually.
- Readability: The code is more readable and maintainable, making it easier to understand the process.
</details>

## Write simple units of code (KISS)
Refers to the principle of keeping code simple and straightforward. It is easier to understand, debug, and maintain simple code. Complex solutions should be avoided unless absolutely necessary.

<details>
  <summary>Example</summary>

```python
def sum_of_numbers(numbers):
    result = 0
    for i in range(0, len(numbers)):
        result = result + numbers[i]
    return result

numbers = [1, 2, 3, 4, 5]
print(sum_of_numbers(numbers))
```
```python
def sum_of_numbers(numbers):
    return sum(numbers)

numbers = [1, 2, 3, 4, 5]
print(sum_of_numbers(numbers))
```
- Simplicity: The code is now much shorter and uses Python's built-in sum() function, which is designed to handle this operation efficiently.
- Readability: The logic is clearer at a glance — it directly states the intention of summing the list.
- Less Error-Prone: By avoiding manual indexing and iteration, there's less chance for mistakes.
</details>


## Write code once (DRY)
Duplication in code is a common source of bugs and maintenance headaches. The DRY principle (Don't Repeat Yourself) encourages developers to avoid repeating code by abstracting common functionality into reusable components.

<details>
  <summary>Example</summary>

```python
def square_area(side):
    return side * side

def rectangle_area(length, width):
    return length * width

# Calling both functions
print(square_area(4))   # Output: 16
print(rectangle_area(5, 3))  # Output: 15
```
```python
def calculate_area(length, width=None):
    """Calculates area of a rectangle or square if width is not provided."""
    if width is None:
        width = length  # It's a square
    return length * width

# Calling the single function
print(calculate_area(4))        # Output: 16 (Square)
print(calculate_area(5, 3))     # Output: 15 (Rectangle)
```
</details>

## Keep unit interfaces small
Reducing the number of parameters in a function's interface makes it easier to understand and use. It also helps in keeping the function focused on a single task.

<details>
  <summary>Example</summary>

```python
def create_user_profile(name, age, email, address, phone_number, occupation):
    return {
        "name": name,
        "age": age,
        "email": email,
        "address": address,
        "phone_number": phone_number,
        "occupation": occupation
    }

# Calling the function
profile = create_user_profile("Alice", 30, "alice@example.com", "123 Main St", "555-1234", "Engineer")
print(profile)
```
```python
def create_user_profile(user_info):
    return {
        "name": user_info["name"],
        "age": user_info["age"],
        "email": user_info["email"],
        "address": user_info["address"],
        "phone_number": user_info["phone_number"],
        "occupation": user_info["occupation"]
    }

# User information as a dictionary
user_info = {
    "name": "Alice",
    "age": 30,
    "email": "alice@example.com",
    "address": "123 Main St",
    "phone_number": "555-1234",
    "occupation": "Engineer"
}

# Calling the function
profile = create_user_profile(user_info)
print(profile)
```
- Smaller Interface: The function now accepts a single parameter (`user_info`), making it easier to test and reuse.
- Clarity: It’s clearer what data is being passed, and related data is grouped logically.
- Flexibility: The function is more flexible because it's easy to add or remove fields from the `user_info` dictionary without modifying the function signature.
</details>

## Separate concerns - Cohesion and Coupling
Cohesion: The degree to which the elements inside a module belong together. High cohesion means the elements are related and work together to achieve a common purpose. Low cohesion means the elements are not closely related and perform different tasks independently.

Coupling: The degree of interdependence between modules. Loose coupling means modules are independent and changes in one module have minimal impact on other modules. Tight coupling means modules are highly dependent on each other, and changes in one module can have a significant impact on other modules.

Difference: Cohesion is about how closely related and focused the responsibilities of a module are. Coupling is about how dependent modules are on each other.

<details>
<summary>Example cohesion</summary>

### Tightly coupled, Low cohseion

```python
class UserAccountManager:
    def __init__(self, username, password, email, profile_info):
        self.username = username
        self.password = password
        self.email = email
        self.profile_info = profile_info

    # Authentication related methods
    def authenticate(self, username, password):
        # Logic for authenticating user
        pass

    # Profile management methods
    def update_profile(self, new_profile_info):
        # Logic for updating profile
        self.profile_info = new_profile_info

    # Email notification methods
    def send_email(self, subject, message):
        # Logic to send email
        pass

    # Other methods related to user accounts
    def reset_password(self, new_password):
        # Logic to reset password
        self.password = new_password

```
To improve cohesion, we can break down the UserAccountManager class into several smaller classes, each with a single responsibility.

### Better cohesion

```python
class AuthenticationService:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def authenticate(self, username, password):
        # Logic for authenticating user
        return username == self.username and password == self.password

class UserProfile:
    def __init__(self, profile_info):
        self.profile_info = profile_info

    def update_profile(self, new_profile_info):
        # Logic for updating profile
        self.profile_info = new_profile_info

class EmailService:
    def __init__(self, email):
        self.email = email

    def send_email(self, subject, message):
        # Logic to send email
        print(f"Sending email to {self.email} with subject: {subject}")

class PasswordService:
    def __init__(self, password):
        self.password = password

    def reset_password(self, new_password):
        # Logic to reset password
        self.password = new_password

```

</details>

<details>
<summary>Example coupling </summary>

### Tightly coupled (bad example)
```python
class PaymentGateway:
    def process_payment(self, credit_card_number, amount):
        # Logic to process payment
        print(f"Processing payment of ${amount} using credit card {credit_card_number}")

class OrderProcessor:
    def __init__(self):
        # Tight coupling: OrderProcessor is directly tied to PaymentGateway
        self.payment_gateway = PaymentGateway()

    def process_order(self, credit_card_number, amount):
        # Logic to process order
        self.payment_gateway.process_payment(credit_card_number, amount)
        print("Order processed successfully.")

# Usage
order_processor = OrderProcessor()
order_processor.process_order("1234-5678-9101-1121", 100.0)
```

- Dependency Injection: OrderProcessor receives a PaymentProcessor as a parameter, which decouples it from any specific payment implementation.
- Loose Coupling: We can now replace PaymentGateway with a different implementation without changing the OrderProcessor logic, making the system more flexible and easier to test or extend.

```python
from abc import ABC, abstractmethod

# Interface (abstract base class) for PaymentProcessor
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, credit_card_number, amount):
        pass

# PaymentGateway implements the PaymentProcessor interface
class PaymentGateway(PaymentProcessor):
    def process_payment(self, credit_card_number, amount):
        # Logic to process payment
        print(f"Processing payment of ${amount} using credit card {credit_card_number}")

# OrderProcessor is loosely coupled with the payment processor through dependency injection
class OrderProcessor:
    def __init__(self, payment_processor: PaymentProcessor):
        self.payment_processor = payment_processor  # Dependency injection

    def process_order(self, credit_card_number, amount):
        # Logic to process order
        self.payment_processor.process_payment(credit_card_number, amount)
        print("Order processed successfully.")

# Usage
payment_gateway = PaymentGateway()
order_processor = OrderProcessor(payment_gateway)
order_processor.process_order("1234-5678-9101-1121", 100.0)
```

</details>

## Couple architecture components loosely

## Keep architecture components balanced

## Keep your codebase small & YAGNI

## Automate development pipeline and test

## Write clean 
Clean code avoids confusion by removing unnecessary comments and dead code. A cleaner codebase is easier for team members to work with, leading to better collaboration and efficiency. Writing clean code allows developers to focus on solving current problems rather than navigating through irrelevant artifacts.

<details>
<summary>Example</summary>

```python
def calculate_total(prices):
    # TODO: Handle discounts in the future
    total = 0
    for price in prices:
        total += price
    return total

def process_order(order):
    # This function is no longer needed
    pass

# Example usage
order_prices = [10.99, 5.49, 3.75]
total_price = calculate_total(order_prices)
print(f"Total price: ${total_price:.2f}")
```

```python
def calculate_total(prices):
    """Calculate the total price from a list of prices."""
    total = sum(prices)
    return total

# Example usage
order_prices = [10.99, 5.49, 3.75]
total_price = calculate_total(order_prices)
print(f"Total price: ${total_price:.2f}")
```

</details>