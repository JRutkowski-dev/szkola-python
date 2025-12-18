def powitanie(imie):
	return f"witaj {imie} w systemie Linux!"

print (powitanie("uczniu"))

def rysuj_choinke(n):
	print(f"\n--- WESOŁYCH ŚWIĄT (Z Windowsa) ---")
	for i in range(n):
		print(' ' * (n - i - 1) + '*' * (2 * i + 1))
	print(' ' * (n - 1) + '|')
	
if __name__ == "__main__":
	rysuj_choinke(10)
	