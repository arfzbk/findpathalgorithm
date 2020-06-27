import sys


#Labirentimizi girdi alıyoruz ve yazmak üzere çıktı dosyasını açıyoruz
labirent_girdisi=open(sys.argv[1])
labirent_ciktisi=open(sys.argv[2],'w')
#Labirentimizi yazdıracağımız liste
labirent=[]
#Labirentimiz en son yol_ekle fonksiyonundan çıktı dosyamıza yazdırılacaktır
def yol_ekle(string):
    ekle=""
    for i in string:
        if i=="s":
            ekle+="s,"
        elif i=="h":
            ekle+="h,"
        elif i=="f":
            ekle+="f,"
        elif i=="0":
             ekle+="0,"
        elif i=="1":
            ekle+="1,"
    labirent_ciktisi.write(ekle+"\n")
    print(str(ekle))
    
def listeye_labirent_ekle(string):
    if string=="":
        return
    labirent.append(list(string.strip("\n")))
    listeye_labirent_ekle(labirent_girdisi.readline())
#Labirent listesi eklenir,burada ilk satırı fonksiyonumuza gönderdim ve fonksiyonun içinde recursiveleyerek boş bir stringe yakınsadım.
listeye_labirent_ekle(labirent_girdisi.readline())
#Başlangıç,bitiş,ve güçlendirme noktasının koordinat değişkenlerini ve labirentimizin genişliği ile yüksekliğini oluşturucak değişkenleri tanımladım.
baslangicX=0
baslangicY=0
bitisX=0
bitisY=0
guc_artirmaX=0
guc_artirmaY=0
#Labirentimizin yüksekliğini ve enini burada atadım.
width=len(labirent)
height=len(labirent[0])
#Burada buradan_gecti adlı bir liste tanımlayarak labirentte gezdiğimiz yerleri true,false olarak belirlememiz gerekli.
buradan_gecti=[]
#Burada en son doğru yolu çıktı vericek listemizi tanımladım
dogru_yol=[]
#Burada bir for döngüsü ile labirenti gezdik ve başlangıç,bitiş,güçlendirme noktalarını belirledik ve değişkenlere atadık.
for i in range(len(labirent)):
    #buradan_gecti listemizin girilen labirentin boyutuna göre her elemanına False ekleyecek gecici bir liste tanımladım.
    gecici_liste1=[]
    #cıktımızı vericek olan dogru_yol listemizi labirentin boyutuna göre her elemanına ilk olarak "0" ekledim
    gecici_liste2=[]
    for j in range(len(labirent[0])):
        if labirent[i][j]=="s":
            baslangicX=i
            baslangicY=j
        elif labirent[i][j]=="h":
            guc_artirmaX=i
            guc_artirmaY=j
        elif labirent[i][j]=="f":
            bitisX=i
            bitisY=j
        gecici_liste1.append(False)
        gecici_liste2.append("0")
    buradan_gecti.append(gecici_liste1)
    dogru_yol.append(gecici_liste2)
    #Listeleri ekledikten sonra içini boşalttım
    del gecici_liste1
    del gecici_liste2


#Verilen başlangıç ve bitiş koordinatlarına göre labirentimizi çözen algoritma fonksiyonu        
def yolu_coz(x,y,bitisX,bitisY):
    #Verilen koordinatlara ulaştığımızda return olarak "1" değerini döndürücek
    if x==bitisX and y==bitisY:
        dogru_yol[x][y]="1"
        return "1"
    #Eğer duvara geldiyse veya buradan geçtiyse "0" değerini döndürücek
    if labirent[x][y]=="w" or buradan_gecti[x][y] : 
        return "0"
    #Buradan daha önce gecmediyse şimdi olan konumu True yapacak
    buradan_gecti[x][y]=True
    if x!=0:
        #X konumu duvara gelmediyse bir önceki x konumu sorgulatıyoruz ve aynı şekilde özyinelemeli olarak gidiyor.
        if yolu_coz(x-1,y,bitisX,bitisY)=="1":
            dogru_yol[x][y]="1"
            return "1"
    if x!=width-1:
        if yolu_coz(x+1,y,bitisX,bitisY)=="1":
            dogru_yol[x][y]="1"
            return "1"
    if y!=0:
        #Y konumu duvara gelmediği surece özyinelemeli olarak y konumunu sorgulatıyoruz
        if yolu_coz(x,y-1,bitisX,bitisY)=="1":
            dogru_yol[x][y]="1"
            return "1"
    if y!=height-1:
        if yolu_coz(x,y+1,bitisX,bitisY)=="1":
            dogru_yol[x][y]="1"
            return "1"
    return "0"
#Burada ilk olarak H güçlendirme noktasını bulmaya çalışıyoruz
yolu_coz(baslangicX,baslangicY,guc_artirmaX,guc_artirmaY)
#Yolumuzu çizdikten sonra buradan_gecti listemizi tekrardan her elemanını False yapıyoruz çünkü geçilen yerlerden tekrar geçmek zorunda olabiliriz.
buradan_gecti=[]
for i in range(len(labirent)):
    gecici_liste=[]
    for j in range(len(labirent[0])):
        gecici_liste.append(False)
    buradan_gecti.append(gecici_liste)
    del gecici_liste
#Buradan ise bitiş noktasını buluyoruz
yolu_coz(guc_artirmaX,guc_artirmaY,bitisX,bitisY)

dogru_yol[guc_artirmaX][guc_artirmaY]="h"
dogru_yol[baslangicX][baslangicY]="s"
dogru_yol[bitisX][bitisY]="f"
#Doğru yolun teker teker çıktıya yazdırılması
for i in dogru_yol:
    yol_ekle(i)
#Dosyanın kapanması
labirent_ciktisi.close()
labirent_girdisi.close()


