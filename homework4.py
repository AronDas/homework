class Vehicle:

    def __init__(self, name, capacity):
        """Initialize vehicle with name and seating capacity."""
        self.name = name
        self.capacity = capacity

    def fare(self):
        """Calculate standard fare based on capacity (Base rate: $100 per seat)."""
        return self.capacity * 100


class Bus(Vehicle):

    def fare(self):
        """Calculate bus fare with an extra 10% maintenance charge."""
        # Get the standard fare from the parent class
        base_fare = super().fare()
        # Add the 10% maintenance fee
        total_fare = base_fare + (base_fare * 0.10)
        return total_fare

school_bus = Bus("School Bus", 50)

# Display the results
print(f"Vehicle Name: {school_bus.name}")
print(f"Seating Capacity: {school_bus.capacity}")
print(f"Total Bus Fare: ${school_bus.fare():.2f}")
