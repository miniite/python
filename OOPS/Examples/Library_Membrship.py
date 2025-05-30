# 1. Library Membership System:

# Create a Member class with attributes member_name and member_id.
# Create a PremiumMember subclass that inherits from Member and includes methods for set_membership_period and set_discount.
# Use method chaining to initialize a PremiumMember instance and set details like membership period and discount.

class Member:
    def __init__(self, member_name, member_id):
        self.member_name = member_name
        self.member_id = member_id

class PremiumMember(Member):
    def __init__(self, member_name, member_id):
        super().__init__(member_name, member_id)
        self.membership_period = None
        self.discount = None

    def set_membership_period(self, period):
        self.membership_period = period
        return self 

    def set_discount(self, discount):
        self.discount = discount
        return self 


premium_member = PremiumMember("Alice Smith", "PM001")
    
premium_member.set_membership_period("12 months")
premium_member.set_discount(15)


print(f"Name: {premium_member.member_name}")
print(f"ID: {premium_member.member_id}")
print(f"Period: {premium_member.membership_period}")
print(f"Discount: {premium_member.discount}%")
