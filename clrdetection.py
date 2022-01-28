import cv2
import pandas as pd

#Please Double Click On Image To Get Color :
#If You Download the Image it will be in Your Download Location
#Error Handling
try :
    img = cv2.imread('C://Users//Lenovo//Downloads//orange.jpg')
#if using same Folder : img = cv2.imread('orange.jpg')
    clicked = False
    r = g = b = x_pos = y_pos = 0

    #Columns in CSV File
    try:
        index = ["color", "color_name", "hex", "R", "G", "B"]
        csv = pd.read_csv('C://Users//Lenovo//AppData//Local//Programs//Python//Python39//opencv//colors.csv', names=index, header=None)
        #if using same Folder : csv = pd.read_csv('colors.csv')
        def color_name(R, G, B):
            minimum = 10000
            for i in range(len(csv)):
                d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
                if d <= minimum:
                    minimum = d
                    cname = csv.loc[i, "color_name"]
            return cname

        def function(event, x, y, flags, param):
            if event == cv2.EVENT_LBUTTONDBLCLK:
                global b, g, r, x_pos, y_pos, clicked
                clicked = True
                x_pos = x
                y_pos = y
                b, g, r = img[y, x]
                b = int(b)
                g = int(g)
                r = int(r)


        cv2.namedWindow('image')
        cv2.setMouseCallback('image', function)
        cv2.putText(img,'Use ESc TO Get Rid Of Screen',(20, 20), 2, 0.6, cv2.LINE_AA)
        var = True
        while var:
            cv2.imshow("image", img)
            if clicked:

                # cv2.rectangle(image, start point, endpoint, color, thickness)-1 fills entire rectangle
                cv2.rectangle(img, (20, 20), (750, 60), (b, g, r), -1)

                # Creating text string to display( Color name and RGB values )
                text = color_name(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)

                # cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
                cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

                #For Light Color Text Will Be Dark
                if r + g + b >= 600:
                    cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)    
            # ESC TO Kill Window
            if cv2.waitKey(20) & 0xFF == 27:
                break
        cv2.destroyAllWindows()
    except FileNotFoundError as err :
        print("Error : ",'File Not Found')
except FileNotFoundError as err :
    print("File Not Found")
except Exception as err :
    print("Customize Error : ",err)