import pandas as pd
from matplotlib import pyplot as plt
from autocorrect import Speller
spell = Speller(lang="en")

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)

data = pd.read_csv("menu.csv")
categories = data['Category'].unique()

print("McWelcome")
print("Menu Categories:")
for ctg in categories:
    print(f"- {ctg}")

selected_ctg = spell(input("\nPlease type in the category: ")).title()
selected_ctg = selected_ctg.replace("And", "&")

while selected_ctg not in categories:
    print("Unfortunately, that is not a valid category, please check your spelling and try again.")
    selected_ctg = spell(input("\nPlease type in the category: ")).title()
    selected_ctg = selected_ctg.replace("And", "&")

filtered_items = data[data['Category'] == selected_ctg]

print(f"\nItems in '{selected_ctg}' category:")

columns = list(filtered_items.columns)
print("\nYou can select from the following information to display:")
for col in columns:
    print(f"- {col}")

info_to_display = spell(input("\nPlease type in the specific information you want to know (e.g., Calories, Fat, etc.): ")).title()


while info_to_display not in columns:
    print("Unfortunately, that is not a valid option, please check your spelling and try again.")
    info_to_display = spell(input("\nPlease type in the specific information you want to know: ")).title()

print(f"\nShowing {info_to_display} for items in '{selected_ctg}' category:")
print(filtered_items[['Item', info_to_display]])

plt.figure(figsize=(10, 6))
plt.bar(filtered_items['Item'], filtered_items[info_to_display], color='orange')
plt.title(f"{info_to_display} of Items in {selected_ctg}")
plt.xlabel("Items")
plt.ylabel(info_to_display)
plt.xticks(rotation=90, fontsize=4)
plt.tight_layout()
plt.show()
print("Never Gonna Give You Up")