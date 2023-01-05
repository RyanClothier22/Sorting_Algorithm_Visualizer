from tkinter import *
import random
import time

class Board:
    def __init__(self, rect_nums, canvas, c_w, c_h):
        self.rect_nums = rect_nums
        self.r_w = c_w / rect_nums
        self.r_h = c_h / rect_nums
        self.c_w = c_w
        self.c_h = c_h
        self.canvas = canvas
        self.deck = []
        self.time_delay = 0.05
        self.rect_color = 'red'
        self.build()

    def build(self):
        for i in range(self.rect_nums):
            self.deck.append(self.canvas.create_rectangle(self.r_w* i, self.c_h-self.r_w*(i+1),self.r_w*(i+1), self.c_h, fill=self.rect_color))
    def remove_all(self):
        for i in self.deck:
            self.canvas.delete(i)

    def update_all(self):
        self.r_w = self.c_w / self.rect_nums
        self.r_h = self.c_h / self.rect_nums
        self.deck = []

    def shuffle(self):
        #shuffle the deck
        shuffled_deck = random.sample(self.deck, len(self.deck))
        shuff_h = [self.canvas.coords(i)[1] for i in shuffled_deck]
        for i in range(len(self.deck)):
            new_coords = self.canvas.coords(self.deck[i])
            new_coords[1] = shuff_h[i]
            self.canvas.coords(self.deck[i], new_coords)
        #print("------")


    def sort(self, input):
        if input == "Insertion":
            self.insertion()
        elif input == "Selection":
            self.selection()
        elif input == "Bubble":
            self.bubble()
        else:
            return None

    def insertion(self):
        #Organize he heights of the rectangles into a list
        heights = [self.c_h - self.canvas.coords(i)[1] for i in self.deck]

        # Sort the height list
        for i in range(len(heights)):
            min_index = i
            for j in range(i+1, len(heights)):
                if heights[j] < heights[min_index]:
                    min_index = j

            # swap the min and i heights
            (heights[min_index], heights[i]) = (heights[i], heights[min_index])

            #save coords of big rect
            norm_1 = self.canvas.coords(self.deck[i])
            #print(f"wrong rect: {norm_1}, index: {min_index}")

            #save coords of small rect
            norm_2 = self.canvas.coords(self.deck[min_index])
            #print(f"right rect: {norm_2} index: {i}")

            # Make new coords for rects

            # Coords 1
            coords_a = [norm_1[0], norm_2[1], norm_1[2], norm_1[3]]
            coords_b = [norm_2[0], norm_1[1], norm_2[2], norm_2[3]]

            self.canvas.coords(self.deck[i], coords_a)
            self.canvas.coords(self.deck[min_index], coords_b)
            self.canvas.update()
            time.sleep(self.time_delay)

    def selection(self):
        heights = [self.c_h - self.canvas.coords(i)[1] for i in self.deck]
        n = len(heights)
        for i in range(n):
            min_index = i

            for j in range(i + 1, n):
                # select the minimum element in every iteration
                if heights[j] < heights[min_index]:
                    min_index = j
            # swapping the elements to sort the array
            (heights[i], heights[min_index]) = (heights[min_index], heights[i])

            norm_1 = self.canvas.coords(self.deck[i])
            norm_2 = self.canvas.coords(self.deck[min_index])
            coords_a = [norm_1[0], norm_2[1], norm_1[2], norm_1[3]]
            coords_b = [norm_2[0], norm_1[1], norm_2[2], norm_2[3]]

            self.canvas.coords(self.deck[i], coords_a)
            self.canvas.coords(self.deck[min_index], coords_b)
            self.canvas.update()
            time.sleep(self.time_delay)

    def bubble(self):
        heights = [self.c_h - self.canvas.coords(i)[1] for i in self.deck]
        n = len(heights)

        swapped = False
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if heights[j] > heights[j + 1]:
                    swapped = True

                    heights[j], heights[j + 1] = heights[j + 1], heights[j]

                    norm_1 = self.canvas.coords(self.deck[j])
                    norm_2 = self.canvas.coords(self.deck[j+1])
                    coords_a = [norm_1[0], norm_2[1], norm_1[2], norm_1[3]]
                    coords_b = [norm_2[0], norm_1[1], norm_2[2], norm_2[3]]

                    self.canvas.coords(self.deck[j], coords_a)
                    self.canvas.coords(self.deck[j+1], coords_b)
                    self.canvas.update()
                    time.sleep(self.time_delay)
            if not swapped:
                return