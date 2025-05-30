# Library Membership

Here, our task is to create a class for Library Membership which follows the following properties:
- Create a Member class with attributes member_name and member_id.
- Create a PremiumMember subclass that inherits from Member and includes methods for set_membership_period and set_discount.
- Use method chaining to initialize a PremiumMember instance and set details like membership period and discount.


## 1. Member Class
We can create a member class in two ways:
- staticly declared class attributes
- dynamically declared class attributes

Staticly, i.e. the attributes `member_name` and `member_id`are hardcoded (already typed into the code block) as follows:

```python
class Member:    
    member_name = 'ABC'
    member_id = 10
```
Here in this example we don't add any \_\_init__ method, we don't need to pass any values, since it is already hardcoded

Dynamically is basically that the user can values for `member_name` and `member_id`

```python
class Member:
    def __init__(self, member_name, member_id):
        self.member_name = member_name
        self.member_id = member_id
```
