from geometry import circle, rectangle

def main():
    r = 3
    l = 4
    w = 2

    print(f"Cerc (r={r}): aria = {circle.area(r):.4f}, circumferinta = {circle.circumference(r):.4f}")
    print(f"Dreptunghi (l={l}, w={w}): aria = {rectangle.area(l, w):.4f}, perimetru = {rectangle.perimeter(l, w):.4f}")

if __name__ == "__main__":
    main()
