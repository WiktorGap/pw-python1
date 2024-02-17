#OpenCV (Open Source Computer Vision Library) to biblioteka do przetwarzania obrazów i analizy wizyjne

import cv2

#Wczytywanie obrazu z pliku

image = cv2.imread('obraz.jpg')

#Wyświetl obraz

cv2.imshow('Obraz', image)   #wyswietli obraz w oknie
cv2.waitKey(0)  #oczekuje na naciscie dowolnego klawisza
cv2.destroyAllWindows()   # zamyka okna


#Konwersja do odcieni szarośći

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Funkcja cv2.cvtColor() służy do konwersji kolorów. 
#W tym przypadku, konwertujemy obraz na odcienie szarości

blurred_image = cv2.GaussianBlur(image, (5,5, 0))

#Funkcja cv2.GaussianBlur() wykonuje rozmycie Gaussowskie na obrazie. W przykładzie, (5, 5) to rozmiar jądra filtra, a 0 to odchylenie standardowe.

#Detekcja krawędzi (Canny):

edges = cv2.Canny(gray_image, 50 , 150)
#Funkcja cv2.Canny() wykonuje detekcję krawędzi na obrazie w odcieniach szarości. 
#Parametry 50 i 150 to progi gradientu, które pomagają w określeniu mocnych i słabych krawędzi.


#Detekcja konturów

countours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#Funkcja cv2.findContours() znajduje kontury w obrazie. Zwraca listę konturów i hierarchię konturów. 
#Parametry cv2.RETR_EXTERNAL i cv2.CHAIN_APPROX_SIMPLE określają rodzaj hierarchii i sposób aproksymacji konturów.


#Rysowanie konturów

cv2.drawContours(image,countours, -1 , (0,255,0), 2)

#Funkcja cv2.drawContours() rysuje kontury na obrazie. 
#Parametr -1 oznacza rysowanie wszystkich konturów, a (0, 255, 0) to kolor konturów w formacie BGR.


#zmiana rozmairu obrazu

resized_image = cv2.resize(image, (width, height))

#Ta funkcja zmienia rozmiar obrazu na podstawie podanych szerokości (width) i wysokości (height). 
#Wartości te określają nowe wymiary obrazu.




#Rotacja Obrazu:

M = cv2.getRotationMatrix2D((width/2, height/2), angle, scale)
rotated_image = cv2.warpAffine(image, M, (width, height))


#Ta sekwencja operacji tworzy macierz rotacji M i stosuje ją do obrazu za pomocą funkcji cv2.warpAffine(). 
#Parametry angle i scale kontrolują kąt rotacji i skalowanie obrazu


#Progowanie (Binaryzacja)

ret, binary_image = cv2.threshold(gray_image, threshold_value, max_value, cv2.THRESH_BINARY)

#Binaryzacja przekształca obraz w obraz binarny, 
#gdzie piksele powyżej pewnego progu (threshold_value) przyjmują maksymalną wartość (max_value), a poniżej - minimalną (0


# Segmentacja kolorów:

lower_bound = np.array([H_low, S_low, V_low])
upper_bound = np.array([H_high, S_high, V_high])
color_mask = cv2.inRange(image_hsv, lower_bound, upper_bound)


#W przypadku segmentacji kolorów, przekształcamy obraz do przestrzeni barw HSV,
# a następnie tworzymy maskę koloru, w której tylko piksele o wartościach barw zawartych w danym zakresie są zachowywane.


#Detekcja obiektów

#Detekcja kształtów:
contours, hierarchy = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for contour in contours:
    # ... wykonaj operacje na konturze ...

#Funkcja cv2.findContours() znajduje kontury w obrazie binarnym. 
#W przypadku detekcji kształtów możemy iterować przez znalezione kontury i podejmować działania w zależności od kształtu



#Detekcja twarzy:
    
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.3, minNeighbors=5)
#Ta sekwencja kodu wykorzystuje klasyfikator kaskadowy Haara do detekcji twarzy w obrazie.
# Parametry scaleFactor i minNeighbors kontrolują precyzję detekcji.


#Obsługa strumienia wideo z kamery:

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    cv2.imshow("Video", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()







#Zapis strumienia wideo:
out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 30, (width, height))
while True:
    ret, frame = cap.read()
    out.write(frame)
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
out.release()




