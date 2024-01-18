class Ticket:
    def __init__(self, destination, price):
        self.destination = destination
        self.price = price


class MetroTicketingSystem:
    def __init__(self):
        self.tickets = []

    def add_ticket(self, ticket):
        self.tickets.append(ticket)

    def display_available_tickets(self):
        print("Available Tickets:")
        for i, ticket in enumerate(self.tickets, start=1):
            print(f"{i}. Destination: {ticket.destination}, Price: {ticket.price}")

    def buy_ticket(self, choice):
        try:
            choice = int(choice)
            if 1 <= choice <= len(self.tickets):
                selected_ticket = self.tickets[choice - 1]
                print(f"You have bought a ticket to {selected_ticket.destination} for {selected_ticket.price}.")
            else:
                print("Invalid choice. Please select a valid ticket.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    metro_system = MetroTicketingSystem()

    # Adding some sample tickets
    ticket1 = Ticket("Station A", 5.00)
    ticket2 = Ticket("Station B", 7.50)
    ticket3 = Ticket("Station C", 10.00)

    metro_system.add_ticket(ticket1)
    metro_system.add_ticket(ticket2)
    metro_system.add_ticket(ticket3)

    while True:
        print("\nWelcome to the Metro Ticketing System")
        print("1. Display Available Tickets")
        print("2. Buy a Ticket")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            metro_system.display_available_tickets()
        elif choice == "2":
            metro_system.display_available_tickets()
            ticket_choice = input("Enter the number of the ticket you want to buy: ")
            metro_system.buy_ticket(ticket_choice)
        elif choice == "3":
            print("Thank you for using the Metro Ticketing System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
