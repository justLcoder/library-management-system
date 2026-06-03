from models.book import Book
from models.member import Member 
from models.loan import Loan 
from models.library import Library 

member1 = Member("Shahzod Tursinboyev")
member1.member_id = 1

data = member1.to_dict()

member2 = Member.from_dict(data)

print(member1.describe())
print()
print(member2.describe())