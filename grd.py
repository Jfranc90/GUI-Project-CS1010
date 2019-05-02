import sys, pygame, tkinter


pygame.init()

def minorDiagO(list):
    minorWin = False
    a = 2
    y = 0
    xList = []
    for x in range(len(list)):
        if(x == a):
            xList.insert(y,list[x])
            y += 1
            a += 2
    #if(len(list) > 3):
     #   list.pop(3)
        
    yo  = xList.count("O")
    if(yo == 3):
        minorWin = True
    return minorWin

def minorDiagX(list):
    minorWin = False
    a = 2
    y = 0
    xList = []
    for x in range(len(list)):
        if(x == a):
            xList.insert(y,list[x])
            y += 1
            a += 2
            
    #if(len(list) > 4):
     #   list.pop(3)
        
    yo  = xList.count("X")
    print("YO X",yo)
    print("X LIST",xList)
    if(yo == 3):
        minorWin = True
    return minorWin
    
def majorDiagO(list):
    majorWin = False
    a = 0
    y = 0
    xList = []
    for x in range(len(list)):
        if(x == a):
            xList.insert(y,list[a])
            y += 1
            a += 4
    yo  = xList.count("O")
    print("YO O", yo)
    print("OLIST",xList)
    if(yo == 3):
        majorWin = True
    return majorWin

def majorDiagX(list):
    majorWin = False
    a = 0
    y = 0
    xList = []
    for x in range(len(list)):
        if(x == a):
            xList.insert(y,list[a])
            y += 1
            a += 4
    yo  = xList.count("X")
    if(yo == 3):
        majorWin = True
    return majorWin
    
def checkCol1(list):
    colWin = False
    a = 0
    y = 0
    count = 1
    xList = []
    for x in range(len(list)):
        xList.insert(y,list[a])
        y += 1
        a += 3
        if((x + 1) % 3 == 0):
            yo = xList.count("X")
            if(yo == 3):
                colWin = True
            y = 0
            xList = []
            a = 0
            a += count
            count += 1

    return colWin

def checkCol2(list):
    colWin = False
    a = 0
    y = 0
    count = 1
    xList = []
    for x in range(len(list)):
        xList.insert(y,list[a])
        y += 1
        a += 3
        if((x + 1) % 3 == 0):
            yo = xList.count("O")
            if(yo == 3):
                colWin = True
            y = 0
            xList = []
            a = 0
            a += count
            count += 1

    return colWin

def checkRow2(list):
    winner = False
    rowWin = False
    xList = []
    y = 0
    for x in range(len(list)):
        xList.insert(y,list[x])
        y += 1
        if((x + 1) % 3 == 0):
            yo = xList.count("O")
            if(yo == 3):
                rowWin = True
            y = 0
            xList = []
    return rowWin

def checkRow1(list):
    winner = False
    rowWin = False
    xList = []
    y = 0
    for x in range(len(list)):
        xList.insert(y,list[x])
        y += 1
        if((x + 1) % 3 == 0):
            yo = xList.count("X")
            if(yo == 3):
                rowWin = True
            y = 0
            xList = []
    return rowWin
        
def printList(list):
    three = []
    y = 0
    for x in range(len(list)):
        three.insert(y,list[x])
        y += 1
        if((x + 1)  % 3 == 0):
            print(three)
            y = 0
            three = []

        
def createTable():
    width = 600
    height = 600
    screen = pygame.display.set_mode((width,height))
    white = (255,255,255)
    black = (0,0,0)
    blue = (66,134,244)
    screen.fill(black)
    pygame.display.update()

    rectWidth = (width / 3) - 1
    rectHeight = (height / 3) - 1
    xRect = 0
    yRect = 0

    rect1 = pygame.draw.rect(screen,white,[0,0,rectWidth,rectHeight])
    rect2 = pygame.draw.rect(screen,white,[200, 0,rectWidth,rectHeight])
    rect3 = pygame.draw.rect(screen,white,[400,0,rectWidth,rectHeight])
    rect4 = pygame.draw.rect(screen,white,[0,200,rectWidth,rectHeight])
    rect5 = pygame.draw.rect(screen,white,[200,200,rectWidth,rectHeight])
    rect6 = pygame.draw.rect(screen,white,[400,200,rectWidth,rectHeight])
    rect7 = pygame.draw.rect(screen,white,[0,400,rectWidth,rectHeight])
    rect8 = pygame.draw.rect(screen,white,[200,400,rectWidth,rectHeight])
    rect9 = pygame.draw.rect(screen,white,[400,400,rectWidth,rectHeight])

    cross = pygame.image.load("images/cross.png")
    circle = pygame.image.load("images/circle.png")
    cross = pygame.transform.scale(cross,(100,100))
    circle = pygame.transform.scale(circle,(100,100))
    pygame.display.update()
    
    containerList = ["-","-","-","-","-","-","-","-","-"]
    counter = 0
    end1 = False
    end2 = False
    
    while(counter != 9):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                counter += 9
                pygame.quit()
                sys.exit()
            if counter % 2 == 0:
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if rect1.collidepoint(pos) and containerList[0] == "-":
                        containerList[0] = "X"
                        screen.blit(cross,(50,50))
                        printList(containerList)
                        counter += 1
                    elif rect2.collidepoint(pos) and containerList[1] == "-":
                        containerList[1] = "X"
                        screen.blit(cross,(250,50))
                        printList(containerList)
                        counter += 1
                    elif rect3.collidepoint(pos) and containerList[2] == "-":
                        containerList[2] = "X"
                        screen.blit(cross,(450,50))
                        printList(containerList)
                        counter += 1
                    elif rect4.collidepoint(pos) and containerList[3] == "-":
                        containerList[3] = "X"
                        screen.blit(cross,(50,250))
                        printList(containerList)
                        counter += 1
                    elif rect5.collidepoint(pos) and containerList[4] == "-":
                        containerList[4] = "X"
                        screen.blit(cross,(250,250))
                        printList(containerList)
                        counter += 1
                    elif rect6.collidepoint(pos) and containerList[5] == "-":
                        containerList[5] = "X"
                        screen.blit(cross,(450,250))
                        printList(containerList)
                        counter += 1
                    elif rect7.collidepoint(pos) and containerList[6] == "-":
                        containerList[6] = "X"
                        screen.blit(cross,(50,450))
                        printList(containerList)
                        counter += 1
                    elif rect8.collidepoint(pos) and containerList[7] == "-":
                        containerList[7] = "X"
                        screen.blit(cross,(250,450))
                        printList(containerList)
                        counter += 1
                    elif rect9.collidepoint(pos) and containerList[8] == "-":
                        containerList[8] = "X"
                        screen.blit(cross,(450,450))
                        printList(containerList)
                        counter += 1
                    pygame.display.update()
                    row = checkRow1(containerList)
                    col = checkCol1(containerList)
                    major = majorDiagX(containerList)
                    minor = minorDiagX(containerList)
                    if(row is True or col is True or major is True or minor is True):
                        end1 = True
            if(end1 is True):
                break
            if counter % 2 == 1:
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if rect1.collidepoint(pos) and containerList[0] == "-":
                        containerList[0] = "O"
                        screen.blit(circle,(50,50))
                        printList(containerList)
                        counter += 1
                    elif rect2.collidepoint(pos) and containerList[1] == "-":
                        containerList[1] = "O"
                        screen.blit(circle,(250,50))
                        printList(containerList)
                        counter += 1
                    elif rect3.collidepoint(pos) and containerList[2] == "-":
                        containerList[2] = "O"
                        screen.blit(circle,(450,50))
                        printList(containerList)
                        counter += 1
                    elif rect4.collidepoint(pos) and containerList[3] == "-":
                        containerList[3] = "O"
                        screen.blit(circle,(50,250))
                        printList(containerList)
                        counter += 1
                    elif rect5.collidepoint(pos) and containerList[4] == "-":
                        containerList[4] = "O"
                        screen.blit(circle,(250,250))
                        printList(containerList)
                        counter += 1
                    elif rect6.collidepoint(pos) and containerList[5] == "-":
                        containerList[5] = "O"
                        screen.blit(circle,(450,250))
                        printList(containerList)
                        counter += 1
                    elif rect7.collidepoint(pos) and containerList[6] == "-":
                        containerList[6] = "O"
                        screen.blit(circle,(50,450))
                        printList(containerList)
                        counter += 1
                    elif rect8.collidepoint(pos) and containerList[7] == "-":
                        containerList[7] = "O"
                        screen.blit(circle,(250,450))
                        printList(containerList)
                        counter += 1
                    elif rect9.collidepoint(pos) and containerList[8] == "-":
                        containerList[8] = "O"
                        screen.blit(circle,(450,450))
                        printList(containerList)
                        counter += 1
                    pygame.display.update()
                    row = checkRow2(containerList)
                    col = checkCol2(containerList)
                    major = majorDiagO(containerList)
                    minor = minorDiagO(containerList)
                    if(row is True or col is True or major is True or minor is True):
                        end2 = True
                    if(end2 is True):
                        break
        if(end2 is True or end1 is True):
            pygame.quit()
            break
         
    if(end1):
        win1 = tkinter.Tk()
        win1.geometry("300x300")
        win1.title("WINNER!")
        label_1 = tkinter.Label(win1, text = "Player 1 Wins!", command = None)
        label_1.pack()
        win1.mainloop()
        
    elif(end2):
        win2 = tkinter.Tk()
        win2.geometry("300x300")
        win2.title("WINNER!")
        label_1 = tkinter.Label(win2, text = "Player 2 Wins!", command = None)
        label_1.pack()
        win2.mainloop()
    else:
        tie = tkinter.Tk()
        tie.geometry("300x300")
        tie.title("NO WINNER!")
        label_1 = tkinter.Label(tie, text = "NO WINNERS!", command = None)
        label_1.pack()
        tie.mainloop()
   
    sys.exit()
    
def introTable(): 
    intro = tkinter.Tk()
    intro.geometry('300x300')
    intro.configure(bg = "black")
    intro.title("TIC_TAC_TOE")
    button_1 = tkinter.Button(intro, text = "Start Game", command = createTable)
    button_1.pack()
    intro.mainloop()

introTable()
   
