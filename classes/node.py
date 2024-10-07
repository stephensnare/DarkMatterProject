class Node(object):
    def __init__(self, side_length: float, depth: int = 0):
        self.side_length = side_length
        self.depth = depth


        # Define children nodes with default values as None
        self.tlf: 'Node' = None  # Top-Left-Front child
        self.trf: 'Node' = None  # Top-Right-Front child
        self.tlb: 'Node' = None  # Top-Left-Back child
        self.trb: 'Node' = None  # Top-Right-Back child
        self.blf: 'Node' = None  # Bottom-Left-Front child
        self.brf: 'Node' = None  # Bottom-Right-Front child
        self.blb: 'Node' = None  # Bottom-Left-Back child
        self.brb: 'Node' = None  # Bottom-Right-Back child


        def split():
            print("splitting")

        def calculate_center():
            print("calculating center")







