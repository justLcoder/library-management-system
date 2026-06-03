class Member:
    """Represents a library member."""
    
    def __init__(self, full_name):
        self.member_id = None
        self.full_name = full_name

    # Serializer and deserializer:
    def to_dict(self):
        return {
            'member_id': self.member_id,
            'full_name': self.full_name
        }
    
    @classmethod
    def from_dict(cls, data):
        member = cls(data['full_name'])
        member.member_id = data['member_id']
        return member
    
    def describe(self):
        """Returns a formatted description of the member."""
        return(
            f"ID: {self.member_id}\n"
            f"Full Name: {self.full_name.title()}"
        )
    
    def __repr__(self):
        return f"{self.member_id}: {self.full_name}"