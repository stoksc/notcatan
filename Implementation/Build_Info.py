"""
This is the Build_Info class. It contains information that was transmitted from the Client_Control to the Host_Control.
"""


class Build_Info:

    def __init__(self, row, column, edge, vertex, dev_card):
        """
        The Build_Info initializes with all values populated with some value when created.

        Args:
            row? (Int): An Integer value representing which row the corresponding Tile will be located in Board.
            column? (Int): An Integer value representing which column the corresponding Tile will be located in Board.
            edge? (String): A String value representing which Edge in the Tile's edge_array the Road is to be built on.
            vertex? (String): A String value representing which Vertex in the Tile's vertex_array the Settlement or City
            is to be built on.
            dev_card? (Boolean): A Boolean value representing whether or not a Development_Card needs to be generated.

        Returns:
            None
        """
        self.dev_card = dev_card
        if self.dev_card is True:
            self.build_type = "Development Card"
        elif edge is not None:
            self.build_type = "Road"
            self.row = row
            self.column = column
            self.edge = edge
        elif vertex is not None:
            self.row = row
            self.column = column
            self.build_type = "Settlement/City"
            self.vertex = vertex

    def get_dev_card(self):
        return self.dev_card

    def get_build_type(self):
        return self.build_type

    def get_edge(self):
        return self.edge

    def get_vertex(self):
        return self.vertex

    def get_row(self):
        return self.row

    def get_column(self):
        return self.column
