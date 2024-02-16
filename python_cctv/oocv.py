import cv2

image = cv2.imread('C:\Users\user\Desktop\obrazek.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BAYER_BGGR2GRAY)

license_plate_cascade = cv2.CascadeClassifier('sciezka/do/kaskady/tablice.xml')
car_cascade = cv2.CascadeClassifier('sciezka/do/kaskady/samochody.xml')
people_cascade = cv2.CascadeClassifier('sciezka/do/kaskady/ludzi.xml')


license_plates = license_plate_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
cars = car_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
people = people_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))



for (x, y, w, h) in license_plates:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
for (x, y, w, h) in cars:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
for (x, y, w, h) in people:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)



cv2.imshow('Rozpoznanie obrazu', image)
cv2.waitKey(0)
cv2.destroyAllWindows()




#Te linie kodu wykorzystują wczytane kaskady Haara do detekcji tablic rejestracyjnych, samochodów i ludzi na obrazie w odcieniach szarości.
#Metoda detectMultiScale() służy do wykrywania obiektów na obrazie. Parametry takie jak scaleFactor, minNeighbors i minSize kontrolują precyzję detekcji.