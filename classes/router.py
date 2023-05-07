class Router:
    """Router class that holds most information that real routers would hold to help the simulation run."""

    def __init__(self, ID, IP_Address, MAC_Address, Routing_Protocol, failure_probability):
        """Initialize the router with its IP address, MAC address, and routing protocol."""
        self.ID = ID # for the sake of having a simple ID for each router instead of printing the IP address
        self.IP_Address = IP_Address
        self.MAC_Address = MAC_Address
        self.Routing_Protocol = Routing_Protocol
        self.failure_probability = failure_probability
        self.routing_table = {}
        self.neighbors = []
        # self.ARP_cache = {}
        self.routing_table[IP_Address] = [0, IP_Address]

    def add_neighbor(self, neighbor):
        """Add a neighbor to the router."""
        self.neighbors.append(neighbor)
    
    def get_neighbors(self):
        """Return the neighbors of the router."""
        return self.neighbors
    
    def get_IP_Address(self):
        """Return the IP address of the router."""
        return self.IP_Address

    def get_MAC_Address(self):
        """Return the MAC address of the router."""
        return self.MAC_Address

    def get_Routing_Protocol(self):
        """Return the routing protocol of the router."""
        return self.Routing_Protocol
    
    def get_routing_table(self):
        """Return the routing table of the router."""
        return self.routing_table

    def update_routing_table(self, destination, cost, next_hop):
        """Update the routing table of the router."""
        self.routing_table[destination] = [cost, next_hop]

    def get_failure_probability(self):
        """Return the failure probability of the router."""
        return self.failure_probability
    
    def get_ID(self):
        """Return the ID of the router."""
        return self.ID