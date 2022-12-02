print("====== Program Manipulasi String ======")
print("pilihan menu")
print("1.Hitung Kata")
print ("2.Ubah Kata")

pilihan =input("pilihan anda :")

kata = input("Masukkan sebuah kalimat/kata: ")

def Hitung_Kata():
    a= input (" Masukkan kata yang ingin dihitung :")
    a1= kata.count(a)
    print("Terdapat sebanyak", a1,"kata",a, "di dalam kalimat")

def Ubah_Kata():
    b= input(" Masukkan kata yang ingin di ubah : ")
    c= input("Masukkan kata pengganti :")
    d=kata.replace(b,c)
    print ("String berhasil diubah menjadi :", d)

if pilihan =="1" :
    Hitung_Kata()
elif pilihan =="2":
    Ubah_Kata()
else: 
    print("Pilihan yang anda input tidak terdaftar di dalam pilihan ")
    
    


