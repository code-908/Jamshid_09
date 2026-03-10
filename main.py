import random
qatnasiwshilar = [1,2,3,]
insanlar = ['dawlet','rasul','sultan','jamshid']
shartler = ['20 marte otirip turiw','\n15 ret andjumaniya','bryus 10 marte']
random.shuffle(insanlar)
insan = random.choice(insanlar)
shart = random.choice(shartler)
adamsani = random.choice(qatnasiwshilar)
print(f"bugingi oyinda {adamsani}")
print('oyin baslandi.. ')
print(f"bugingi sabaqta \"{insan.upper()}-bizlerdin shartti orinlaydi")
print(f"shartimiz {shart}")