class Flight_Booking:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def info(self):
        print(f"Passenger name: {self.name}")
        print(f"Passenger surname: {self.surname}")

class Passenger(Flight_Booking):
    def __init__(self, name, surname, seat):
        super().__init__(name, surname)
        self.seat = seat

        if seat >= 10:
            print("Seat reserved:", seat)
            print("Available seats")
        else:
            print("Seats are not available")

class Ticket(Flight_Booking):
    def __init__(self, name, surname, passport, visa, id_card, flight):
        super().__init__(name, surname)
        self.passport = 10
        self.visa = 20
        self.id_card = 30
        self.flight = 40

        if flight == 20:
            print("Flight is available")

        passport_input = int(input("Enter 10 if you have a passport: "))
        visa_input = int(input("Enter 20 if you have a visa: "))
        id_card_input = int(input("Enter 30 if you have an ID card: "))

        self.check_in(passport_input, visa_input, id_card_input)

    def check_in(self, passport_input, visa_input, id_card_input):
        if passport_input == self.passport:
            print("Passport available")
        if visa_input == self.visa:
            print("Visa available")
        if id_card_input == self.id_card:
            print("ID card available")

class Boarding(Flight_Booking):
    def __init__(self, name, surname ,requirement_checkin):
        super().__init__(name, surname)
        self.requirement_checkin = requirement_checkin

    def board(self):
        if self.requirement_checkin == 10:
          print("Passenger fulfill all the specifications")

passenger = Passenger("John", "Doe", 12)
ticket = Ticket("Jane", "Smith", 10, 20, 30, 20)
boarding_pass = Boarding("Alice", "Johnson",10)

passenger.info()
ticket.info()
boarding_pass.board()

            
             
      
    