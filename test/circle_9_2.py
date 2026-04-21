import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ======================== Геометрические функции ========================
def line_intersection(p1, p2, p3, p4):
    x1, y1 = p1; x2, y2 = p2; x3, y3 = p3; x4, y4 = p4
    denom = (x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4)
    if abs(denom) < 1e-10:
        return None
    t = ((x1 - x3)*(y3 - y4) - (y1 - y3)*(x3 - x4)) / denom
    x = x1 + t*(x2 - x1)
    y = y1 + t*(y2 - y1)
    return np.array([x, y])

def foot_of_perpendicular(point, line_start, line_end):
    p = np.array(point)
    a = np.array(line_start)
    b = np.array(line_end)
    ab = b - a
    t = np.dot(p - a, ab) / np.dot(ab, ab)
    return a + t * ab

def orthocenter(A, B, C):
    foot_A = foot_of_perpendicular(A, B, C)
    foot_B = foot_of_perpendicular(B, A, C)
    return line_intersection(A, foot_A, B, foot_B)

def nine_point_circle(A, B, C):
    mid_AB = (A + B) / 2
    mid_AC = (A + C) / 2
    perp_AB = np.array([-(B[1]-A[1]), B[0]-A[0]])
    perp_AC = np.array([-(C[1]-A[1]), C[0]-A[0]])
    O_circ = line_intersection(mid_AB, mid_AB + perp_AB, mid_AC, mid_AC + perp_AC)
    R_circ = np.linalg.norm(O_circ - A)
    H = orthocenter(A, B, C)
    N = (O_circ + H) / 2
    R = R_circ / 2
    return N, R

# ======================== Данные треугольника ========================
A = np.array([0.0, 0.0])
B = np.array([6.0, 0.0])
C = np.array([2.0, 5.0])

mid_AB = (A + B) / 2
mid_BC = (B + C) / 2
mid_CA = (C + A) / 2

foot_A = foot_of_perpendicular(A, B, C)
foot_B = foot_of_perpendicular(B, A, C)
foot_C = foot_of_perpendicular(C, A, B)

H = orthocenter(A, B, C)
mid_AH = (A + H) / 2
mid_BH = (B + H) / 2
mid_CH = (C + H) / 2

nine_points = [mid_AB, mid_BC, mid_CA, foot_A, foot_B, foot_C, mid_AH, mid_BH, mid_CH]
N, R = nine_point_circle(A, B, C)

# ======================== Настройка графика ========================
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_aspect('equal')
ax.grid(True, linestyle='--', alpha=0.6)

all_points = np.vstack([A, B, C, H] + nine_points)
x_min, x_max = all_points[:, 0].min(), all_points[:, 0].max()
y_min, y_max = all_points[:, 1].min(), all_points[:, 1].max()
dx, dy = (x_max - x_min)*0.2, (y_max - y_min)*0.2
ax.set_xlim(x_min - dx, x_max + dx)
ax.set_ylim(y_min - dy, y_max + dy)

# Создаём объекты один раз (без label, чтобы не плодить легенду)
triangle_line, = ax.plot([], [], 'b-', lw=2)
mid_scat = ax.scatter([], [], c='green', s=80, zorder=5)
foot_scat = ax.scatter([], [], c='orange', s=80, zorder=5)
euler_scat = ax.scatter([], [], c='purple', s=80, zorder=5)
circle_line, = ax.plot([], [], 'r--', lw=2)

# Создаём легенду вручную, явно указав нужные элементы и подписи
legend_elements = [
    plt.Line2D([0], [0], color='b', lw=2, label='Треугольник'),
    plt.scatter([0], [0], c='green', s=80, label='Середины сторон'),
    plt.scatter([0], [0], c='orange', s=80, label='Основания высот'),
    plt.scatter([0], [0], c='purple', s=80, label='Середины отрезков (ортоцентр → вершины)'),
    plt.Line2D([0], [0], color='r', linestyle='--', lw=2, label='Окружность девяти точек')
]
ax.legend(handles=legend_elements, loc='upper right')

# ======================== Анимация ========================
def init():
    triangle_line.set_data([], [])
    mid_scat.set_offsets(np.empty((0, 2)))
    foot_scat.set_offsets(np.empty((0, 2)))
    euler_scat.set_offsets(np.empty((0, 2)))
    circle_line.set_data([], [])
    ax.set_title("Шаг 1: Треугольник")
    return triangle_line, mid_scat, foot_scat, euler_scat, circle_line

def update(frame):
    # Треугольник (всегда)
    triangle_line.set_data([A[0], B[0], C[0], A[0]], [A[1], B[1], C[1], A[1]])
    
    # Кадр 1: середины сторон
    if frame >= 1:
        mid_scat.set_offsets([mid_AB, mid_BC, mid_CA])
    else:
        mid_scat.set_offsets(np.empty((0, 2)))
    
    # Кадр 2: основания высот
    if frame >= 2:
        foot_scat.set_offsets([foot_A, foot_B, foot_C])
    else:
        foot_scat.set_offsets(np.empty((0, 2)))
    
    # Кадр 3: середины отрезков от ортоцентра
    if frame >= 3:
        euler_scat.set_offsets([mid_AH, mid_BH, mid_CH])
    else:
        euler_scat.set_offsets(np.empty((0, 2)))
    
    # Кадр 4: окружность
    if frame == 4:
        theta = np.linspace(0, 2*np.pi, 100)
        x_circ = N[0] + R * np.cos(theta)
        y_circ = N[1] + R * np.sin(theta)
        circle_line.set_data(x_circ, y_circ)
    else:
        circle_line.set_data([], [])
    
    titles = [
        "Шаг 1: Треугольник",
        "Шаг 2: Середины сторон",
        "Шаг 3: Основания высот",
        "Шаг 4: Точки Эйлера (середины от ортоцентра)",
        "Шаг 5: Окружность девяти точек"
    ]
    ax.set_title(titles[frame])
    
    return triangle_line, mid_scat, foot_scat, euler_scat, circle_line

ani = FuncAnimation(fig, update, frames=5, init_func=init,
                    interval=1500, blit=False, repeat=False)

plt.show()
# ani.save('nine_point_circle.gif', writer='pillow', fps=1)  # при желании