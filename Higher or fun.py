# 1. Add country code to phone numbers
op = map(lambda i: "+91" + i,["9876543210","9123456780","9988776655"])
print(list(op))
#output
#['+919876543210', '+919123456780', '+919988776655']

# 2. convert prices from dollars to rupees given product prices [10,25,40,100] in dollars, use map() to convert them to rupees (1 usd = 83 inr)
prices_in_dollars = [10, 25, 40, 100]
usd_to_inr = 83
prices_in_rupees = list(map(lambda x: x * usd_to_inr, prices_in_dollars))
print("Prices in Rupees:", prices_in_rupees)
#output
#Prices in Rupees: [830, 2075, 3320, 8300]

# 3. filter gmail id's from ["deepu08@gmail.com", "abc4@gmail.com", "dhdy@gmail.com"] use filter() to keep only gmail id's
emails = ["deepu08@gmail.com", "abc4@gmail.com", "dhdy@gmail.com"]
gmail_ids = list(filter(lambda email: "@gmail.com" in email, emails))
print("Gmail IDs:", gmail_ids)
#output
#Gmail IDs: ['deepu08@gmail.com', 'abc4@gmail.com', 'dhdy@gmail.com']

# 4. get short product names. from["pen", "notebook", "charger", "bag"], use filter() to return names with length <= 5
products = ["Pen", "Notebook", "Laptop", "Charger", "Bag"]
short_names = list(filter(lambda name: len(name) <= 5, products))
print("Short product names:", short_names)
#output
#Short product names: ['Pen', 'Bag']

# 5. convert names to usernames from["Deepthi", "Arha","Kajal"], use msp() to convert into usernames (lowercase with @gmail.com)
usernames = ["Deepthi", "Arha","Kajal"]
usernames = list(map(lambda name: name.lower() + "@gmail.com", usernames))
print("usernames:", usernames)
#output
#usernames: ['deepthi@gmail.com', 'arha@gmail.com', 'kajal@gmail.com']

# 6. filter expired products. given product expiry years[2022, 2023, 2025, 2026], use filter() to keep only expired ones (assume current year = 2025)
expiry_years = [2022, 2023, 2024, 2025]
current_year = 2025
expired = list(filter(lambda year: year < current_year, expiry_years))
print("expired products:", expired)
#output
#expired products: [2022, 2023, 2024]

# 7. mask credit card numbers from ["123456789098765", "546372827392825"], use map() to mask thm as "*2825"
credit_cards = ["123456789098765", "546372827392825"]
masked_cards = list(map(lambda card: "*" * (len(card) - 4) + card[-4:], credit_cards))
print("Masked cards:", masked_cards)
#output
#Masked cards: ['8765', '**2825']

# 8. filter high salary employees from [25000, 45000, 60000, 15000, 80000], use filter() to return employees with salary >= 40000
salaries = [25000, 45000, 60000, 15000, 80000]
high_salaries = list(filter(lambda sal: sal >= 40000, salaries))
print("High salary employees:", high_salaries)
#output
#High salary employees: [45000, 60000, 80000]

# 9. Format procudct labels from ["apple", "mango", "orange"], use mp() to format them as --> "product:Apple"
products = ["apple", "mango", "orange"]
labels = list(map(lambda p: "product:" + p.capitalize(), products))
print("Formatted labels:", labels)
#output
#Formatted labels: ['product:Apple', 'product:Mango', 'product:Orange']

# 10. Students passed from student marks [35, 80, 55, 20, 90], use filter() to return students who scored >= 40
marks = [35, 80, 55, 20, 90]
passed = list(filter(lambda m: m >= 40, marks))
print("Passed students:", passed)
#output
Passed students: [80, 55, 90]

higher or fun