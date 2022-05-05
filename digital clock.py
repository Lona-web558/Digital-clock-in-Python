//====================================================================================================
//The Free Edition of C++ to Python Converter limits conversion output to 100 lines per file.

//To purchase the Premium Edition, visit our website:
//https://www.tangiblesoftwaresolutions.com/order/order-cplus-to-python.html
//====================================================================================================

import math

class Digital_Clock:

    def _initialize_instance_fields(self):
        #instance fields found by C++ to Python Converter:
        self._X = 0
        self._Y = 0
        self._SIZE = 0
        self._COLOR = 0
        self._HEIGHT = 0
        self._WIDTH = 0
        self._VER = None
        self._HOR = None
        self.style = 0

#C++ TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to multiple constructors:
#ORIGINAL LINE: Digital_Clock()
    def __init__(self):
        self._initialize_instance_fields()

        self.style = 1
        self._SIZE = 1
        self._HEIGHT = 1
        self._WIDTH = 12
        self._COLOR = 15
        self.bar_make()

#C++ TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to multiple constructors:
#ORIGINAL LINE: Digital_Clock(int s, int c, int st)
    def __init__(self, s, c, st):
        self._initialize_instance_fields()

        self.style = st
        self._SIZE = s
        self._COLOR = c
        self._HEIGHT = 1
        self._WIDTH = 6
        self.bar_make()

    def bar_make(self):
        x = None
        y = None
        w = None
        h = None
        area = None
        x = 10
#C++ TO PYTHON CONVERTER TODO TASK: C++ to Python Converter cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        y = getmaxy()/2
        w = self._WIDTH *self._SIZE
        h = self._HEIGHT *self._SIZE
        setfillstyle(self.style,self._COLOR)
        bar(x+h,y,x+w-h,y+h)
        setcolor(self._COLOR)
        line(x,y+math.trunc(h / float(2)),x+h,y)
        line(x,y+math.trunc(h / float(2)),x+h,y+h)
        floodfill(x+math.trunc(h / float(2)),y+math.trunc(h / float(2)),self._COLOR)
        setcolor(self._COLOR)
        line(x+w-h,y,x+w+-h+h,y+math.trunc(h / float(2)))
        line(x+w-h,y+h,x+w-h+h,y+math.trunc(h / float(2)))
        floodfill(x+w-h+math.trunc(h / float(2)),y+math.trunc(h / float(2)),self._COLOR)
        area = imagesize(x,y,x+w,y+h)
#C++ TO PYTHON CONVERTER TODO TASK: The memory management function 'malloc' has no equivalent in Python:
        self._HOR = malloc(area)
        getimage(x,y,x+w,y+h,self._HOR)
        putimage(x,y,self._HOR,XOR_PUT)
#C++ TO PYTHON CONVERTER TODO TASK: C++ to Python Converter cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        x = getmaxx()/2
        y = 10
        h = self._SIZE *self._WIDTH
        w = self._HEIGHT *self._SIZE
        bar(x,y+w,x+w,y+h-w)
        setcolor(self._COLOR)
        line(x,y+w,x+math.trunc(w / float(2)),y)
        line(x+w,y+w,x+math.trunc(w / float(2)),y)
        floodfill(x+math.trunc(w / float(2)),y+math.trunc(w / float(2)),self._COLOR)
        setcolor(self._COLOR)
        line(x,y+h-w,x+math.trunc(w / float(2)),y+h)
        line(x+w,y+h-w,x+math.trunc(w / float(2)),y+h)
        floodfill(x+math.trunc(w / float(2)),y+h-math.trunc(w / float(2)),self._COLOR)
        area = imagesize(x,y,x+w,y+h)
#C++ TO PYTHON CONVERTER TODO TASK: The memory management function 'malloc' has no equivalent in Python:
        self._VER = malloc(area)
        getimage(x,y,x+w,y+h,self._VER)
        putimage(x,y,self._VER,XOR_PUT)

    def PutDig(self, x, y, n):
        num = None
        gap = None
        qu = None
        rem = None
        gap = (self._SIZE *self._HEIGHT)
        num = n
        if num == 62:
            self.DrawDig(x, y, 62)
        if num == 63:
            self.DrawDig(x, y, 63)
        if num>=0 and num<10:
            self.DrawDig(x, y, 0)
            self.DrawDig(x+self._WIDTH *self._SIZE+self._HEIGHT *self._SIZE+gap, y, n)
        if num>=10 and num<61:
            qu = math.trunc(num / float(10))
            rem = math.fmod(num, 10)
            self.DrawDig(x, y, qu)
            self.DrawDig(x+self._WIDTH *self._SIZE+self._HEIGHT *self._SIZE+gap, y, rem)

    def DrawDig(self, x, y, n):
        H = [[1, 0, 1], [0, 0, 0], [1, 1, 1], [1, 1, 1], [0, 1, 0], [1, 1, 1], [1, 1, 1], [1, 0, 0], [1, 1, 1], [1, 1, 1]]
        ph = [[1, 1, 0], [1, 1, 0]]
        pv = [[1, 1, 1, 0], [1, 1, 1, 1]]
        V = [[1, 1, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0], [0, 1, 0, 1], [1, 1, 0, 1], [1, 0, 0, 1], [1, 0, 1, 1], [0, 1, 0, 1], [1, 1, 1, 1], [1, 1, 0, 1]]
        HX = [x, x, x]
        HY = [y, y+self._WIDTH *self._SIZE, y+2 *self._WIDTH *self._SIZE]
        VX = [x-math.trunc((self._HEIGHT *self._SIZE) / float(2)), x+self._WIDTH *self._SIZE-math.trunc((self._HEIGHT *self._SIZE) / float(2)), x-math.trunc((self._HEIGHT *self._SIZE) / float(2)), x+self._WIDTH *self._SIZE-math.trunc((self._HEIGHT *self._SIZE) / float(2))]
        VY = [y+math.trunc((self._HEIGHT *self._SIZE) / float(2)), y+math.trunc((self._HEIGHT *self._SIZE) / float(2)), y+self._WIDTH *self._SIZE+math.trunc((self._HEIGHT *self._SIZE) / float(2)), y+self._WIDTH *self._SIZE+math.trunc((self._HEIGHT *self._SIZE) / float(2))]
        i = None
        setfillstyle(1,getpixel(x-1,y-1))
        bar(x-math.trunc((self._SIZE *self._HEIGHT) / float(2)),y,x+self._WIDTH *self._SIZE+math.trunc((self._SIZE *self._HEIGHT) / float(2)),y+2 *self._SIZE *self._WIDTH+self._HEIGHT *self._SIZE)

//====================================================================================================
//End of the allowed output for the Free Edition of C++ to Python Converter.

//To purchase the Premium Edition, visit our website:
//https://www.tangiblesoftwaresolutions.com/order/order-cplus-to-python.html
//====================================================================================================
