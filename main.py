from converter import convert
from grid import Square

grid = convert('./data/game.sdk')
print('Before:')
grid.show_grid()
print('-------------------------')
grid.solve()
print('After:')
grid.show_grid()

validity = grid.get_validity_report()
print(f"Valid? {validity['valid']}")
if not validity['valid']:
    print(f"Invalid parts: {validity['invalid_parts']}")
