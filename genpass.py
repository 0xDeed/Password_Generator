import random
import sys 

def encrypt_function(size):

#Lista de los Caracteres --------------------------------------------------------------------------------------------------
	chars = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","z"]
	chars_M = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Z"]
	esp_chars = ["@","|","#","$","%","&","/","(",")","=","?","¿","¡","!","*","[","]","{","}",";",":","_","-","ñ","Ñ"]
	num = ["1","2","3","4","5","6","7","8","9"]
#-------------------------------------------------------------------------------------------------------------------------- 
	
	if size < 4:
		print("Password length must contain more than 4 characters")
		exit()
	n = 0 
	while n < size:
	#-----------------------
		f = chars
		s = chars_M
		t = esp_chars
		w = num 
		lista = [f,s,t,w]
	#-----------------------
		r = random.choice(lista)
		resultados = []
		resultados.append((random.choice(r)))
		
		for i in resultados:
			print(i,end="") 
		n=n+1
		
if __name__ == "__main__":
	
	try:
		numero = sys.argv[1]
	except:
		print("Example: python genpass.py <password length>")
		exit()
		
	encrypt_function(int(numero))
 


