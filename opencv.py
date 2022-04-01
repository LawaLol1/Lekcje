import cv2
import imutils

#Źródło obrazu
cap = cv2.VideoCapture(0)

#Pozycja punktu X kwadratu
x = 400
z = 100

#Główna pętla programu
while True:

    #Zczytywanie obrazu z kamery i przekazywanie do frame
    ret, frame = cap.read()
    
    #Skalowanie klatki do 800 pikseli
    frame = imutils.resize(frame, width=800) 

    #Rysowanie kwadratu
    cv2.rectangle(frame, (z, 100), (x, 400), (255, 255, 255, 255), 10)

    #Sprawdzanie czy x jest większe niż 1200
    if x>1200:
        x = 0

    #Sprawdzanie czy z jest większe od 800
    if z>800:
        z = 0
    
    #Inkrementacja x i z ( dodawanie o jeden )
    x = x + 1
    z = z + 1

    #Tworzenie okna i wyświetlanie klatek
    cv2.imshow("Capturing", frame) 

    #Sprawdzanie czy klawisz 'q' jest wciśnięty
    if cv2.waitKey(1) & 0xFF == ord('q'):
        #Przerywanie głównej pętli programu
        break

#Zwolnienie źródła obrazu i pamięci ram
cap.release()

#Zniszczenie okienek programu
cv2.destroyAllWindows()