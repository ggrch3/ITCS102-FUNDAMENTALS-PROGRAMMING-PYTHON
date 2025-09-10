print("Welcome to the Manga Reader Recommender!")
print("You must first answer some questions to know the exact Manga to recommend")

genre = input("What genre would you like (action, romance, ecchi): ").lower()
duration = input("How long (short, medium, long): ").lower()
decade = input("In what decade (90s, 2000s, 2010s, 2020s): ").lower()

import time

time.sleep(1)
print("Here are the recommendations that we got for you\n", end="", flush=True)



if genre == "action" and duration == "short" and decade == "90s":
	time.sleep(1)
	print("\nBasara, Battle Angel Alita, Crows, Gunsmith cats, The legend of Mother Sarah, Wangan Midnight.")
elif genre == "action" and duration == "medium" and decade == "90s":
	time.sleep(1)
	print("RG Veda, The Heroic Legend of  Arislan, Sailor moon, The Vision of Escaflowne, Tenchi Muyo, Runouni Kenshin")
elif genre == "action" and duration == "long" and decade == "90s":
	time.sleep
	print("One Piece, Berserk, Dragon Ball, SLam Dunk.")

elif genre == "action" and duration == "short" and decade == "2000s":
	time.sleep
	print("Gantz, Ryuko's ring")
elif genre == "action" and duration == "medium" and decade == "2000s":
	time.sleep
	print("Full Metal Alchemist, 20th century Boys, Gray man omnibus")
elif genre == "action" and duration == "long" and decade == "2000s":
	time.sleep
	print("Naruto, Death note, Attack on Titan, TOkyo Ghoul, Seven Deadly Sins.")

elif genre == "action" and duration == "short" and decade == "2010s":
	time.sleep(1)
	print("Akame ga Kill!, Btoom, Hikari-Man")

elif genre == "action" and duration == "medium" and decade == "2010s":
	time.sleep(1)
	print("Blue Exorcist, Akame ga Kill, Seraph of the End, Deadman Wonderland")

elif genre == "action" and duration == "long" and decade == "2010s":
	time.sleep(1)
	print("Eminence in Shadow, One Punch Man, Attack on Titan, My Hero Academia, Black Clover, Fairy Tail")

elif genre == "action" and duration == "short" and decade == "2020s":
	time.sleep(1)
	print("the Valiant must fall, The Tale of the Outcast, Shikizakamura")

elif genre == "action" and duration == "medium" and decade == "2020s":
	time.sleep(1)
	print("Tokyo Duel, Ninja vs. Gokudo, Gachiakuta, Lili-Men")

elif genre == "action" and duration == "long" and decade == "2020s":
	time.sleep(1)
	print("Jujutsu Kaisen, Demon SLayer, Tokyo Revengers")

# ----------------- Romance -----------------


if genre == "romance" and duration == "short" and decade == "90s":
	time.sleep(1)
	print("Ao Haru Ride, Kakafukaka, I fell in love after school(Hokago, Koi Shita)")

elif genre == "romance" and duration == "medium" and decade == "90s":
	time.sleep(1)
	print("Kare First love, A perfect day for love letters, Parl Pink")

elif genre == "romance" and duration == "long" and decade == "90s":
	time.sleep(1)
	print("Video Girl Ai, Boys Over Flowers")

elif genre == "romance" and duration == "short" and decade == "2000s":
	time.sleep(1)
	print("Aishiteruze baby, Fruit Basket another.")

elif genre == "romance" and duration == "medium" and decade == "2000s":
	time.sleep(1)
	print("Lovely★Complex, Absolute Boyfriend, Peach Girl: Sae's Story")

elif genre == "romance" and duration == "long" and decade == "2000s":
	time.sleep(1)
	print("Fruit Basket, Boys Be..., Skip Beat!")

elif genre == "romance" and duration == "short" and decade == "2010s":
	time.sleep(1)
	print("Orange, Wolf Girl & Black Prince, My Little Monster, Say 'I love You'. ")

elif genre == "romance" and duration == "medium" and decade == "2010s":
	time.sleep(1)
	print("Horimiya, Ao Haru Ride, Strobe Edge, Tonari no Kaibutsu-kun")

elif genre == "romance" and duration == "long" and decade == "2010s":
	time.sleep(1)
	print("Namaikizari")

elif genre == "romance" and duration == "short" and decade == "2020s":
	time.sleep(1)
	print("And Yet, You  Are So Sweet,  Assorted Entanglements")

elif genre == "romance" and duration == "medium" and decade == "2020s":
	time.sleep(1)
	print("A condition called Love, Anyway I'm Falling in love with you")

elif genre == "romance" and duration == "long" and decade == "2020s":
	time.sleep(1)
	print("A condition called love, Love is war")


#--------------- ECCHI -------------

if genre == "ecchi" and duration == "short" and decade == "90s":
	time.sleep(1)
	print("Golden Boy, DNA²")

elif genre == "ecchi" and duration == "medium" and decade == "90s":
	time.sleep(1)
	print("Video GIrl AI, Onegai Teacher")

elif genre == "ecchi" and duration == "long" and decade == "90s":
	time.sleep(1)
	print("Aa! Megami-Sama, Tenchi Muyo!")

elif genre == "ecchi" and duration == "short" and decade == "2000s":
	time.sleep(1)
	print("Girl's Bravo, DearS, Najica Blitz Tactics")

elif genre == "ecchi" and duration == "medium" and decade == "2000s":
	time.sleep(1)
	print("Ichigo, To LOVE-Ru, AI Kora")

elif genre == "ecchi" and duration == "long" and decade == "2000s":
	time.sleep(1)
	print("Mahou Sensei Negima, School Rumble, Rosario = Vampire")

elif genre == "ecchi" and duration == "short" and decade == "2010s":
	time.sleep(1)
	print("Maken-Ki! Kai, HenNeko, Sundome!! Milky Way")

elif genre == "ecchi" and duration == "medium" and decade == "2010s":
	time.sleep(1)
	print("Highschool of the Dead, Prison Sxhool, to LOVE-Ru Darkness, Nozoki Ana")

elif genre == "ecchi" and duration == "long" and decade == "2010s":
	time.sleep(1)
	print("Food Wars!, TRinity Seven")

elif genre == "ecchi" and duration == "short" and decade == "2020s":
	time.sleep(1)
	print("New Normal, Ayakashi Triangle")

elif genre == "ecchi" and duration == "medium" and decade == "2020s":
	time.sleep(1)
	print("To LOVE-RU Darkness")

elif genre == "ecchi" and duration == "long" and decade == "2020s":
	time.sleep(1)
	print("Ayakashi Triangle, Redo of Healer")

#---------------------Fall---------------------

else:
	print("Sorry.. couldn't find any recommendation for you.")

