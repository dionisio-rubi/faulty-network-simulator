class Network:
    def __init__(self):
        self.routers = []
        self.IP_Addresses = {} # IPaddresses[node] = IP address
        self.links = []
        self.weights = []
        
    def add_link(self, router1, router2, bandwidth, delay):
        # If the IP address of router is not in the list of ip addresses, add it
        if router1 not in list(self.IP_Addresses.values()):
            self.IP_Addresses[len(self.IP_Addresses)] = router1
        if router2 not in list(self.IP_Addresses.values()):
            self.IP_Addresses[len(self.IP_Addresses)] = router2

        node1 = list(self.IP_Addresses.keys())[list(self.IP_Addresses.values()).index(router1)]
    
        node2 = list(self.IP_Addresses.keys())[list(self.IP_Addresses.values()).index(router2)]
        
        # Add the link to the list of links if it doesn't exist yet
        if [node1, node2] not in self.links and [node2, node1] not in self.links:
            self.links.append([node1, node2])

            # Calculate the weight of the link and add to list of weights
            self.weights.append(bandwidth * delay)

    def get_routers(self):
        return self.routers
    
