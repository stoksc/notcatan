##### David says:

In Inventory.py

>   Think about placing the resources in an array with references to the index as dictionary e.g.:
    self.resources_arr = [self.b, self.l, self.w, self.g, self.o]
    This way we can make a dictionary referring to the object that needs to be built and when passed
    to the add_object method subtract from the array of resources based on the dictionary reference passed
    to the method e.g.:

    def add_object(self, self.resources_arr, object_to_add):
        if object_to_add == ROAD:
            if has_road(self):
                self.resources_arr[self.b] = self.resources_arr[self.b -1]
                self.resources_arr[self.l] = self.resources_arr[self.l -1]
                self.roads.append(road)
        if object_to_add == SETTLEMENT:
            if has_settlement(self):
                self.resources_arr[self.b] = self.resources_arr[self.b -1]
                self.resources_arr[self.l] = self.resources_arr[self.l -1]
                self.resources_arr[self.w] = self.resources_arr[self.w -1]
                self.resources_arr[self.g] = self.resources_arr[self.g -1]
                self.settlesments.append(settlement)
        if object_to_add == CITY:
            if has_city(self):
                self.resources_arr[self.g] = self.resources_arr[self.g -2]
                self.resources_arr[self.o] = self.resources_arr[self.o -3]
        if object_to_add == DEV_CARD:
            if has_dev_card(self):
                self.resources_arr[arr.w] = self.resources_arr[self.w -1]
                self.resources_arr[arr.g] = self.resources_arr[self.g -1]
                self.resources_arr[arr.o] = self.resources_arr[self.o -1]
                self.dev_cards.append(dev_card)
___

##### We said:

In Board.py


> Either pure gold or pure garbage. Not sure yet.
        Need to figure out how to set edge's tiles and vertex's tile, but this needs to sit
        for a day for me to think about my first statement.
        Instead of creating the edge first, instead grab the pointers together in an array as
        a batch, then iterate through array to initialize the pointers as a group to a single edge.
        e.g. if edge @ index in tile.edge_arr is nil, grab edge pointer at index of tile.edge_arr
        and place in temp_edge_arr
        Then grab the other corresponding edges of corresponding tiles in tile.tile_arr and use logic
        to iterate through temp_edge_arr and link to newly constructed edge.
        I didn't wanna modify the code yet seeing as I've yet to practice more with Python, and I'd
        like you to walk me through the logic of this code when you get a chance before making any
        modifications and possibly derping it up.
        

"""quotes""" are for docstrings, not comments. Don't comment huge blocks of code and leave it there, it'll all start to get way too messy way too fast. I set a bad example with what I did with the docstring in board.

##### To mark something as needing to be done, do this:
> \# TODO: this needs to be done

e.g. in place_road, in player.

##### Instead of adding a bunch of verbose stuff, just put:

> \# TODO: discuss ideas in XXXXXX.md commit doc.

I also made a slack and a kanban for us. 
