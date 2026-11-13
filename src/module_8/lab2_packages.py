class Package:
    def __init__(self, number, sender, recipient, weight):
        self.number = number
        self.sender = sender
        self.recipient = recipient
        self.weight = weight
        
    @property
    def number(self):
        return self._number
 
    @number.setter
    def number(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Not a number")
        if value <= 0:
            raise ValueError("Not a positive number")
        self._number = value
    
    @property
    def weight(self):
        return self._weight
    
    @weight.setter
    def weight(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Not a number")
        if value < 0:
            raise ValueError("Not a positive number")
        self._weight = value
            
def main():
    try:
        packages = [
            Package(number=1, sender="Alice", recipient="Bob", weight=10),
            Package(number=2, sender="Bob", recipient="Charlie", weight=5)
        ]
        for package in packages:
            print(f"{package.number}: {package.sender} to {package.recipient}, {package.weight}kg")
        
    except (ValueError, TypeError) as error:
        print(f"Error creating package: {error}")
            

if __name__ == "__main__":
    main()

