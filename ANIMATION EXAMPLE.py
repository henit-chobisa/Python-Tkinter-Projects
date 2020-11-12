import tkinter
import time
 
# width of the animation window
animation_window_width=800
# height of the animation window
animation_window_height=600
# initial x position of the ball
animation_ball_start_xpos = 50
# initial y position of the ball
animation_ball_start_ypos = 50
# radius of the ball
animation_ball_radius = 30
# the pixel movement of ball for each iteration
animation_ball_min_movement = 5
# delay between successive frames in seconds
animation_refresh_seconds = 0.001
 
# The main window of the animation
def create_animation_window():
  window = tkinter.Tk()
  window.title("Tkinter Animation Demo")
  # Uses python 3.6+ string interpolation
  window.geometry(f'{animation_window_width}x{animation_window_height}')
  return window
 
# Create a canvas for animation and add it to main window
def create_animation_canvas(window):
  canvas = tkinter.Canvas(window)
  canvas.configure(bg="black")
  canvas.pack(fill="both", expand=True)
  return canvas
 
# Create and animate ball in an infinite loop
def animate_ball(window, canvas,xinc,yinc):
  ball = canvas.create_oval(animation_ball_start_xpos-animation_ball_radius,
            animation_ball_start_ypos-animation_ball_radius,
            animation_ball_start_xpos+animation_ball_radius,
            animation_ball_start_ypos+animation_ball_radius,
            fill="red", outline="green", width=4)
  while True:
    canvas.move(ball,xinc,yinc)
    window.update()
    time.sleep(animation_refresh_seconds)
    ball_pos = canvas.coords(ball)
    # unpack array to variables
    xl,yl,xr,yr = ball_pos
    if xl < abs(xinc) or xr > animation_window_width-abs(xinc):
      xinc = -xinc
    if yl < abs(yinc) or yr > animation_window_height-abs(yinc):
      yinc = -yinc
 
# The actual execution starts here
animation_window = create_animation_window()
animation_canvas = create_animation_canvas(animation_window)
animate_ball(animation_window,animation_canvas, animation_ball_min_movement, animation_ball_min_movement)
