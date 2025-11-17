from spivrobitnyk import Spivrobitnyk
from menedzher import Menedzher

if __name__ == "__main__":
    # об'єкти
    s1 = Spivrobitnyk("Cергій", 10000, 28, 10)
    s2 = Spivrobitnyk("Анна", 90000, 30, 5)
    m1 = Menedzher("Геннадій", 6000, 30, 5, 15)
    m2 = Menedzher("Павло", 23000, 29, 10, 20)

    spivrobitnyky = [s1, s2, m1, m2]

    for sp in spivrobitnyky:
        print(f"Співробітник: {sp.get_imya()}")
        print(f"  Зарплата: {sp.rozrahuvaty_zarplatu():.2f} грн")
        print(f"  Бонус: {sp.rozrahuvaty_bonus():.2f} грн")
        if isinstance(sp, Menedzher):
            print(" ", sp.zvit())
        print("-" * 40)
