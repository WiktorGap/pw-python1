import cv2
import time
import win32gui , win32con



def minimazieWindow():
    window = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(window,win32con.SW_MINIMIZE)
    #importuje moduły win32gui i win32con, które są częścią pywin32 i dostarczają funkcji i stałych związanych z programowaniem interfejsu użytkownika na platformie Windows.
    #Używa funkcji GetForegroundWindow z modułu win32gui, aby uzyskać uchwyt (handle) aktualnie aktywnego okna. Uchwyt okna to unikalny identyfikator przypisany do danego okna przez system Windows
    #Używa funkcji ShowWindow z modułu win32gui, aby zmienić stan widoczności okna. Parametr win32con.SW_MINIMIZE oznacza, że okno zostanie zminimalizowane.
    




def cctv():
    video = cv2.VideoCapture(0)
    # Jest używane do przechwytywania strumienia wideo z dostępnej kamery. 
    #W tym przypadku argument 0 oznacza, że zostanie użyta domyślna kamera, która jest zazwyczaj wbudowana w laptopa lub podłączona poprzez USB.
    video.set(3,640)
    video.set(4,480)
    #video.set(3, 640) ustawia szerokość obrazu na 640 pikseli.
    #video.set(4, 480) ustawia wysokość obrazu na 480 pikseli.
    width =  video.get(3)
    height = video.get(4)
    print(f"Video format is set to {width} x {height}  pixels")
    print("Help-- \n1.Press esc key to exit. \n2.Press m to Minimalize")
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    #out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
    #out to obiekt cv2.VideoWriter, który będzie zapisywał wideo w formacie XVID z prędkością klatek 20.0 klatek na sekundę i rozdzielczością 640x480 pikseli do pliku o nazwie 'output.avi'.
    #służy do ustalenia formatu kodeka do zapisu wideo za pomocą OpenCV.
    date_time = time.strftime("recording %H-%M-%d  -%m -%y")
    #date_time = time.strftime("recording %H-%M-%d -%m -%y"): Tworzy łańcuch znaków reprezentujący bieżącą datę i czas w formacie "recording godzina-minuta-dzień -miesiąc -rok". To jest uzyskiwane za pomocą funkcji time.strftime z modułu time. 
    #Na przykład, taki łańcuch znaków może wyglądać tak: "recording 12-30-01 -01 -22
    output = cv2.VideoWriter('footages/'+date_time+'.mp4', fourcc, 20.0, (640, 480))
    #output = cv2.VideoWriter('foorages/'+date_time+'.mp4' , fourcc, 20.0, (640, 480))
    # Powyższy kod tworzy obiekt VideoWriter do zapisywania wideo o nazwie zbudowanej na podstawie bieżącej daty i czasu w katalogu 'foorages/' i używa kodeka 'mp4v' (możesz dostosować to do swoich potrzeb) z prędkością 20.0 klatek na sekundę i rozdzielczością 640x480 pikseli.
    while video.isOpened():
        #while video.isOpened():: To jest pętla while, która będzie działać, dopóki kamera (obiekt video) jest otwarta. 
        #Pętla będzie kontynuować przetwarzanie klatek, dopóki strumień wideo jest dostępn
        check , frame = video.read()
        #W każdej iteracji pętli, ta linia kodu odczytuje klatkę z kamery przy użyciu metody read(). 
        #Zmienna check oznacza wartość logiczną, czy operacja odczytu przebiegła pomyślnie (True) czy nie (False). Zmienna frame zawiera samą klatkę.
        if check == True:
            frame = cv2.flip(frame,1)
            # Ta linia kodu odwraca klatkę w poziomie przy użyciu funkcji cv2.flip. 
            #Parametr 1 oznacza odwrócenie w poziomie, co może być przydatne, jeśli chcesz uzyskać lustrzane odbicie obrazu.
            t = time.ctime()
            cv2.rectangle(frame,(5,5,100,20), (255,255,255), cv2.FILLED)
            cv2.putText(frame,"Camera 1", (20,20), cv2.FONT_HERSHEY_DUPLEX, 0.5,(5,5,5),1)
            #cv2.putText(frame,(420,460), cv2.FONT_HERSHEY_DUPLEX, 0.5 ,(5,5,5),1)
            #t = time.ctime(): Tworzy łańcuch znaków reprezentujący bieżący czas w formie czytelnej dla człowieka, za pomocą funkcji time.ctime() z modułu time.

            #cv2.rectangle(frame, (5,5,100,20), (255,255,255), cv2.FILLED): Rysuje prostokąt na klatce.
            # Pierwszy parametr to obraz, na którym zostanie narysowany prostokąt (frame). 
            #Drugi parametr to punkt początkowy prostokąta (5, 5), a trzeci parametr to punkt końcowy (100, 20).
            # Ostatni parametr (255, 255, 255) to kolor prostokąta (biały), a cv2.FILLED oznacza, że prostokąt ma być wypełniony.
            # cv2.putText(frame, "Camera 1", (20,20), cv2.FONT_HERSHEY_DUPLEX, 0.5, (5,5,5), 1): Dodaje tekst do klatki.
            # Pierwszy parametr to obraz (frame), drugi parametr to tekst ("Camera 1"), trzeci parametr to pozycja startowa tekstu (20, 20), 
            #czwarty parametr to czcionka (cv2.FONT_HERSHEY_DUPLEX), piąty parametr to rozmiar czcionki (0.5), 
            #szósty parametr to kolor tekstu (czarny), a siódmy parametr to grubość tekstu (1).
            cv2.imshow('CCTV camera', frame)
            output.write(frame)
            if cv2.waitKey(1) == 27:
                print("Video foorage saved in current directory")
                break


            #if cv2.waitKey(1) == 27:: Sprawdza, czy został naciśnięty klawisz. cv2.waitKey(1) zwraca kod klawisza naciśniętego w czasie trwania 1 milisekundy. 
            #W tym przypadku, 27 odpowiada klawiszowi Esc. 
            #Jeśli Esc zostanie naciśnięty, pętla zostanie przerwana, a program zakończy działani
            elif cv2.waitKey(1) == ord('m'):
                minimazieWindow()

            #elif cv2.waitKey(1) == ord('m'):: Sprawdza, czy został naciśnięty klawisz 'm'. ord('m') zwraca wartość liczbową reprezentującą kod znaku 'm'. 
            #Jeśli 'm' zostanie naciśnięte, wywoływana jest funkcja minimazieWindow(
        else:
            print("can't open camera, chceck configuration")
            break
        video.release()
        #video.release(): Zwolnienie zasobów kamery. Funkcja release() na obiekcie VideoCapture z modułu OpenCV zwalnia zasoby związane z przechwytywaniem wideo. 
        #W tym przypadku, oczekuje się, że video to obiekt VideoCapture, który został wcześniej otwarty do przechwytywania strumienia wideo z kamery.
        output.release()
        #output.release(): Zwolnienie zasobów zapisywania wideo. Funkcja release() na obiekcie VideoWriter z modułu OpenCV zwalnia zasoby związane z zapisywaniem wideo. 
        #W tym przypadku, oczekuje się, że output to obiekt VideoWriter, który został wcześniej utworzony do zapisywania klatek wideo.
        cv2.destroyAllWindows()
        #cv2.destroyAllWindows(): Zamykanie wszystkich okien. Funkcja ta zamyka wszystkie otwarte okna utworzone przez OpenCV. 
        #W kontekście tego kodu, może to dotyczyć okna, w którym wyświetlane jest strumienie wideo.
    print("*"*80+"\n"+" "*30+"Welcome to cctv software\n"+"*"*80)
    ask = int(input("DO you want to open the cctv?\n1. yes\n2. no\n>>>"))
    if ask ==1:
        cctv()
    elif ask ==2:
        print("bye bye!")
        exit




            



    
    
