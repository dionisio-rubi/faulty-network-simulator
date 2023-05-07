class Network:
    def __init__(self):
        self.routers = []
        self.links = []
        self.weights = []
        self.link_reliability = []
        
    def add_link(self, router1, router2, link_reliability, bandwidth, delay, weight):
        # If the IP address of router is not in the list of ip addresses, add it
        if router1 not in self.routers:
            self.routers.append(router1)
        if router2 not in self.routers:
            self.routers.append(router2)
        
        # Add the link to the list of links if it doesn't exist yet
        if [router1, router2] not in self.links and [router2, router1] not in self.links:
            self.links.append([router1, router2])

            # Calculate the weight of the link and add to list of weights
            self.weights.append(bandwidth*weight + delay*weight + (1-link_reliability)*weight)

    def get_routers(self):
        return self.routers
    
    def get_weight(self, router1, router2):
        # Get the index of the link
        index = self.links.index([router1, router2])
        
        # Return the weight of the link
        return self.weights[index]
    
