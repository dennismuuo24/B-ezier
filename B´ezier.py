import tkinter as tk

def draw_bezier_curve(canvas, P1, P2, P3, P4, tolerance):
    # midpoints
    M1 = ((P1[0] + P2[0]) / 2, (P1[1] + P2[1]) / 2)
    M2 = ((P2[0] + P3[0]) / 2, (P2[1] + P3[1]) / 2)
    M3 = ((P3[0] + P4[0]) / 2, (P3[1] + P4[1]) / 2)
    # midpoints of midpoints
    M12 = ((M1[0] + M2[0]) / 2, (M1[1] + M2[1]) / 2)
    M23 = ((M2[0] + M3[0]) / 2, (M2[1] + M3[1]) / 2)
    # final midpoint
    M = ((M12[0] + M23[0]) / 2, (M12[1] + M23[1]) / 2)

    # Termination condition
    if abs(P1[0] - P4[0]) < tolerance and abs(P1[1] - P4[1]) < tolerance:
        canvas.create_line(P1, P4, fill="black")
        return

    # Recursive call
    draw_bezier_curve(canvas, P1, M1, M12, M, tolerance)
    draw_bezier_curve(canvas, M, M23, M3, P4, tolerance)

def update_curve(canvas, P1_scale, P2_scale, P3_scale, P4_scale, tolerance_scale):
    canvas.delete("curve")
    P1 = (P1_scale.get(), 300)
    P2 = (P2_scale.get(), 100)
    P3 = (P3_scale.get(), 100)
    P4 = (P4_scale.get(), 300)
    draw_bezier_curve(canvas, P1, P2, P3, P4, tolerance_scale.get())

def main():
    root = tk.Tk()
    root.title("Adjustable Bezier Curve")

    # button to adjust the curve
    adjust_button = tk.Button(root, text="Adjust Curve", command=lambda: update_curve(canvas, P1_scale, P2_scale, P3_scale, P4_scale, tolerance_scale))
    adjust_button.pack()

    canvas = tk.Canvas(root, width=600, height=400)
    canvas.pack()

    # initial control points
    P1 = (100, 300)
    P2 = (200, 100)
    P3 = (400, 100)
    P4 = (500, 300)

    #  sliders for adjusting control points
    P1_scale = tk.Scale(root, from_=0, to=600, orient=tk.HORIZONTAL, label="P1 x-coordinate")
    P1_scale.set(P1[0])
    P1_scale.pack()

    P2_scale = tk.Scale(root, from_=0, to=600, orient=tk.HORIZONTAL, label="P2 x-coordinate")
    P2_scale.set(P2[0])
    P2_scale.pack()

    P3_scale = tk.Scale(root, from_=0, to=600, orient=tk.HORIZONTAL, label="P3 x-coordinate")
    P3_scale.set(P3[0])
    P3_scale.pack()

    P4_scale = tk.Scale(root, from_=0, to=600, orient=tk.HORIZONTAL, label="P4 x-coordinate")
    P4_scale.set(P4[0])
    P4_scale.pack()

    # slider for adjusting tolerance
    tolerance_scale = tk.Scale(root, from_=0.1, to=10, resolution=0.1, orient=tk.HORIZONTAL, label="Tolerance")
    tolerance_scale.set(1)
    tolerance_scale.pack()

    # Draw initial Bezier curve
    draw_bezier_curve(canvas, P1, P2, P3, P4, 1)

    root.mainloop()

if __name__ == "__main__":
    main()
