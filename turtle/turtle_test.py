#################################################################################################
#  pip install PythonTurtle
#  https://docs.python.org/3/library/turtle.html#introduction
#
#################################################################################################

from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(100)
    print(abs(pos()))
    if abs(pos()) < 1:
        break
end_fill()
done()