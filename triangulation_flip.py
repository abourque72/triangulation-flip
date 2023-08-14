import tkinter as tk
import math

class RegularPolygonApp:
    def __init__(self, root, sides, size):
        self.root = root
        self.canvas = tk.Canvas(root, width=size, height=size)
        self.canvas.pack()
        
        self.sides = sides
        self.size = size
        self.radius = size // 2
        self.center = (size // 2, size // 2)
        
        self.points = self.calculate_polygon_points()
        self.triangles = self.calculate_initial_triangles()
        self.diagonals = self.calculate_initial_diagonals()
        self.draw_polygon()
        
        self.canvas.bind('<Button-1>', self.on_click)
        
    def calculate_polygon_points(self):
        points = []
        for i in range(self.sides):
            angle = 2 * math.pi * i / self.sides
            x = self.center[0] + self.radius * math.cos(angle)
            y = self.center[1] + self.radius * math.sin(angle)
            points.append([x, y])
        return points
    
    def calculate_initial_triangles(self):
        triangles = []
        for i in range(1, self.sides - 1):
            triangles.append([self.points[0], self.points[i], self.points[i+1]])
        return triangles
        
    def calculate_initial_diagonals(self):
        diagonals = []
        for i in range(2, self.sides-1):
            d = self.canvas.create_line(self.points[0], self.points[i], fill='blue', width=2)
            diagonals.append(d)
        return diagonals
    
    def draw_polygon(self):
        self.canvas.create_polygon(self.points, outline='black', fill='', width=2)
            
    def on_diagonal_click(self, d):
        c = self.canvas.coords(d)
        p1 = [c[0],c[1]]
        p2 = [c[2],c[3]]
        p3_1, p3_2 = 0,0
        t_1, t_2 = 0,0
        first = False
        for t in self.triangles:
            if p1 in t and p2 in t and not first:
                t_1 = t
                for e in t:
                    if e != p1 and e != p2:
                        p3_1 = e
                first = True
            elif p1 in t and p2 in t and first:
                t_2 = t
                for e in t:
                    if e != p1 and e != p2:
                        p3_2 = e
        
        self.diagonals.remove(d)
        self.triangles.remove(t_1)
        self.triangles.remove(t_2)
        self.canvas.delete(d)
        
        f = self.canvas.create_line(p3_1, p3_2, fill='blue', width=2)
        self.diagonals.append(f)
        self.triangles.append([p1,p3_1,p3_2])
        self.triangles.append([p2,p3_1,p3_2])
            
    def is_point_on_line(self, px, py, x1, y1, x2, y2):
        d1 = math.sqrt((px - x1)**2 + (py - y1)**2)
        d2 = math.sqrt((px - x2)**2 + (py - y2)**2)
        line_length = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        buffer = 0.5  # A small buffer to allow for easier clicking
        
        return math.isclose(d1 + d2, line_length, abs_tol=buffer)
        
    def on_click(self, event):
        for d in self.diagonals:
            c = self.canvas.coords(d)
            if self.is_point_on_line(event.x, event.y, c[0], c[1], c[2], c[3]):
                self.on_diagonal_click(d)
                return
            

if __name__ == "__main__":
    cfg_sides = 9
    cfg_size = 400
    cfg = 'flip_config.txt'
    try:
        with open(cfg, 'r') as file:
            for line in file:
                line_split = line.split('=')
                if line_split[0] == 'sides':
                    cfg_sides = int(line_split[1])
                elif line_split[0] == 'size':
                    cfg_size = int(line_split[1])
    except FileNotFoundError:
        print("Config file not found. Please create a flip_config.txt file and format as per the instructions on GitHub.")
    except Exception as e:
        print("An error occurred: ", e)
    
    root = tk.Tk()
    app = RegularPolygonApp(root, sides=cfg_sides, size=cfg_size)
    root.mainloop()
