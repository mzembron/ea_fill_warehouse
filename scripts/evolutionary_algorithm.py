import pandas as pd
import numpy as np
import random
from warehouse import Warehouse 
import os
FREE_CELL_VALUE = -1

DIRNAME = os.path.dirname(__file__)
FILENAME_BLOCKS = os.path.join(DIRNAME, '../data/blocks.csv')
class EvolutionaryAlgotihm():
    
    def __init__(self):
        self.warehouse = Warehouse(4,7)
        self.warehouse.get_blocks_from_csv(FILENAME_BLOCKS)
    
    def mutation(self):
        if(len(self.warehouse.blocks_in_warehouse) == 0):
            self.warehouse.place_random_block()
        else:
            """ Randomly: place, remove or exchange """
            pass


    def create_crossover_border(self):
        #TO DO po zmianie 
        return random.randint(0, self.warehouse.warehouse_matrix.shape[1])

    def delete_divided_blocks(self, some_warehoue, border, side):
        left_warehouse = some_warehoue[:][:border]
        right_warehouse = some_warehoue[:][border:]

        uniq_left = np.unique(left_warehouse[left_warehouse!=FREE_CELL_VALUE])
        uniq_right = np.unique(right_warehouse[right_warehouse!=FREE_CELL_VALUE])

        if (side == "left"):
            for u_r in uniq_right:
                if u_r in uniq_left:
                    left_warehouse.remove_block(u_r)
                    uniq_left = uniq_left[uniq_left!=u_r]
            return left_warehouse, uniq_left

        else:
            for u_l in uniq_left:
                if u_l in uniq_right:
                    right_warehouse.remove_block(u_l)
                    uniq_right = uniq_right[uniq_right!=u_l]
            return right_warehouse, uniq_right

    def crossover(self):

        #TO DO po zmianie 
        first_warehouse = Warehouse(4,7).warehouse_matrix
        second_warehouse = Warehouse(4,7).warehouse_matrix


        border = self.create_crossover_border()
        left_warehouse, uniq_left = self.delete_divided_blocks(first_warehouse, border, 'left')
        right_warehouse, uniq_right = self.delete_divided_blocks(second_warehouse, border, 'right')

        for u_l in uniq_left:
            if u_l in uniq_right:
                if(random.choice([True, False])):
                    right_warehouse.remove_block(u_l)
                    uniq_right = uniq_right[uniq_right!=u_l]
                else:
                    left_warehouse.remove_block(u_l)
                    uniq_left = uniq_left[uniq_left!=u_l]
        
        #TO DO po zmianie 
        warehouse_to_return = np.full(self.warehouse.warehouse_matrix.shape, FREE_CELL_VALUE,dtype=int)
        warehouse_to_return[:][:border] =  left_warehouse
        warehouse_to_return[:][border:] = right_warehouse
        return warehouse_to_return



