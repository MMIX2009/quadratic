import streamlit as st
import sympy as sp

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No real solutions"
    else:
        root1 = (-b + sp.sqrt(discriminant)) / (2 * a)
        root2 = (-b - sp.sqrt(discriminant)) / (2 * a)
        return root1, root2

st.title("Quadratic Equation Solver")

st.latex(r"ax^2 + bx + c = 0")

a = st.number_input("Enter coefficient a:", value=1.0)
b = st.number_input("Enter coefficient b:", value=0.0)
c = st.number_input("Enter coefficient c:", value=0.0)

if st.button("Solve"):
    if a == 0:
        st.error("Coefficient 'a' cannot be zero for a quadratic equation.")
    else:
        solution = solve_quadratic(a, b, c)
        if isinstance(solution, str):
            st.write(solution)
        else:
            st.latex(fr"x = \frac{{-{b} \pm \sqrt{{{b**2 - 4*a*c}}}}}{{2*a}}")
            st.write(f"Roots: {solution[0]}, {solution[1]}")
