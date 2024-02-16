import cv2
import time
import datetime

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_deafult.xml")
body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody_deafult.xml")
detection = True
detection_stopped_time = None
timer_started = False
SECONDS_TO_

frame_size = (int(cap.get(3), int(cap.get(4))))
fourcc = cv2.VideoWriter_forucc(*"mp4v")
out = cv2.VideoWriter("video.mp4", fourcc, 20 , frame_size)




#cv2.CascadeClassifier: Jest to klasa w OpenCV, która umożliwia używanie klasyfikatorów kaskadowych, w tym klasyfikatorów Haar'a, do detekcji obiektów.
#cv2.data.haarcascades: Jest to ścieżka do katalogu zawierającego pliki klasyfikatorów Haar'a dostarczone przez OpenCV. cv2.data to moduł w OpenCV, który zawiera różne ścieżki do danych, takie jak modele, kaskady itp
#"haarcascade_frontalfa_deafult.xml": To jest nazwa pliku klasyfikatora Haar'a, który będzie używany do detekcji twarzy. W tym przypadku używany jest plik o nazwie "haarcascade_frontalfa_deafult.xml".



while True:
    _, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BAYER_BG2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3,5)
    bodies = face_cascade.detectMultiScale(gray, 1.3,5)

    if len(faces) + len(bodies) >0:
        detection = True

    out.write(frame)




    #cv2.COLOR_BAYER_BG2GRAY: To jest stała reprezentująca przekształcenie kolorów z przestrzeni Bayer BG na odcienie szarości (grayscale). 
    #W tym przypadku, przestrzeń kolorów źródłowa to Bayer BG, a docelowa to odcienie szarości.
    #Po wykonaniu tej operacji, gray zawiera obraz w odcieniach szarości, co jest często wymagane do efektywnego przetwarzania obrazu, takiego jak detekcja twarz
    #face_cascade.detectMultiScale: Jest to metoda obiektu CascadeClassifier, która służy do detekcji obiektów na obrazie.
    #gray: To jest obraz w odcieniach szarości, na którym chcemy przeprowadzić detekcję obiektów (w tym przypadku, twarzy).
    #1.3: Jest to skala detekcji, która kontroluje, jak bardzo obiekt musi różnić się od otoczenia, aby został uznany za obiekt. Wyższe wartości oznaczają, że obiekt może być mniejszy.
    #5: To jest minimalna liczba sąsiadujących prostokątów, aby uznać detekcję za poprawną. Wartość ta pomaga eliminować fałszywe pozytywy.

    #for (x,y,width,height) in faces:
        #cv2.rectangle(frame, (x,y), (x + width) , (y + height), (255,0,0),3)
        #cv2.rectangle: Jest to funkcja w OpenCV używana do rysowania prostokątów.
        #frame: To jest obraz, na którym chcemy narysować prostokąt.
        #(x, y): To są współrzędne lewego górnego rogu prostokąta.
        #(x + width, y + height): To są współrzędne prawego dolnego rogu prostokąta. Wartości width i height to odpowiednio szerokość i wysokość prostokąta.
        #(255, 0, 0): To jest kolor prostokąta w formacie BGR. W tym przypadku, (255, 0, 0) oznacza niebieski kolor.
        #3: To jest grubość linii prostokąta





    cv2.imshow("Camera", frame)


    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
