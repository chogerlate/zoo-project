class Zoo:
    def get_ticket_price(self, age):
        # Handle invalid age (negative numbers)
        if age < 0:
            return 0
        # Child ticket (0-12 years)
        elif 0 <= age <= 12:
            return 50
        # Teen ticket (13-20 years)
        elif 13 <= age <= 20:
            return 100
        # Adult ticket (21-60 years)
        elif 21 <= age <= 60:
            return 150
        # Senior ticket (61+ years)
        else:
            return 100