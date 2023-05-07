from classes.router import Router

class Network:
    def __init__(self):
        self.routers = []
        self.links = []
        self.weights = []
        self.link_reliability = []
        
    def add_link(self, router1, router2, link_reliability, bandwidth, delay, weight):
        r1 = router1.get_ID()
        r2 = router2.get_ID()

        # If the IP address of router is not in the list of ip addresses, add it
        if r1 not in self.routers:
            self.routers.append(r1)
        if r2 not in self.routers:
            self.routers.append(r2)
        
        # Add the link to the list of links if it doesn't exist yet
        if [r1, r2] not in self.links and [r2, r1] not in self.links:
            self.links.append([r1, r2])

            # Calculate the weight of the link and add to list of weights
            self.weights.append(bandwidth*weight + delay*weight + (1-link_reliability)*weight)
            
            # Add the link reliability to the list of link reliabilities
            self.link_reliability.append(link_reliability)

    def get_routers(self):
        return self.routers
    
    def get_weight(self, router1, router2):
        # Get the index of the link
        index = self.links.index([router1, router2])
        
        # Return the weight of the link
        return self.weights[index]
    
