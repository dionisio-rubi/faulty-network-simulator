# import all the classes needed
from classes.network import Network
from classes.router import Router

def main():
    # Create a network
    network = Network()

    # Create routers
    a = Router("124.124.124.124", "AA:AA:AA:AA:AA:AA", "RIP", 0.9)
    b = Router("255.255.255.255", "BB:BB:BB:BB:BB:BB", "RIP", 0.2)
    c = Router("123.123.123.123", "CC:CC:CC:CC:CC:CC", "RIP", 0.5)
    d = Router("122.122.122.122", "DD:DD:DD:DD:DD:DD", "RIP", 0.7)
    e = Router("111.111.111.111", "EE:EE:EE:EE:EE:EE", "RIP", 0.3)
    f = Router("222.222.222.222", "FF:FF:FF:FF:FF:FF", "RIP", 0.1)

    # Add routers to network

    # Menu, loop until user exits
    print("Welcome to the Network Simulator!")
    print("This Simulator is created by Rubi Dionisio and Alex Mozqueda")
    while True:
        print("\nPlease select an option from the menu below:\n")
        print("1. Print routers in network")
        print("2. Run Simulation")
        print("3. Exit")

        # Get user input
        user_input = input("\nEnter your choice: ")

        # Do actions based on user input
        if user_input == "1":
            print("\nThe routers in the network are:")
            print(network.get_routers())
        elif user_input == "2":
            print("\nRunning simulation...")
            # Run simulation
            
        elif user_input == "3":
            print("Exiting...")
            break


if __name__ == "__main__":
    main()