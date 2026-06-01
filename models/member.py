class Member():
    """Represents a library member."""
    
    def __init__(self, full_name):
        self.member_id = None
        self.full_name = full_name
    
    def describe(self):
        """Returns a formatted description of the member."""
        return(
            f"ID: {self.member_id}\n"
            f"Full Name: {self.full_name.title()}"
        )
    
