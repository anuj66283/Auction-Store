from store.models import Category, SubCategory

categories = [
    Category(name="Electronics"),
    Category(name="Clothing"),
    Category(name="Books")
]

for category in categories:
    category.save()

subcategories = [
    SubCategory(category=categories[0], name="Mobile Phones"),
    SubCategory(category=categories[0], name="Laptops"),
    SubCategory(category=categories[0], name="Televisions"),
    
    SubCategory(category=categories[1], name="Men's Clothing"),
    SubCategory(category=categories[1], name="Women's Clothing"),
    SubCategory(category=categories[1], name="Kids' Clothing"),
    
    SubCategory(category=categories[2], name="Fiction"),
    SubCategory(category=categories[2], name="Non-fiction"),
    SubCategory(category=categories[2], name="Children's Books")
]

for subcategory in subcategories:
    subcategory.save()