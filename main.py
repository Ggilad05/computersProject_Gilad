import matplotlib.pyplot as plt
import numpy as np

def fit_linear(filename):
    X = []
    DX = []
    Y = []
    DY = []
    my_file = open(filename, "r")
    data = my_file.readline()
    my_file.close()
    data = data.lower()
    xy_multilist = []
    clean_xy_multilist = []
    sorted_xy_multilist = []
    if "x" and "dx" and "y" and "dy" in data: ### אם המידע מגיע בצורה של עמודות ###
        my_file = open(file_input, "r")
        for line in my_file:
            xy_multilist.append(line.split(' '))
        indx = xy_multilist.index(['\n'])
        result = check_xymultilist(xy_multilist[:indx]) ### check if all Data lists with the samelength ###
        if not (result):
            print(" Input file error: Data lists are not the samelength.")
        elif not (check_if_less_zero(xy_multilist[:indx])): ### check if all uncertainties positive##
            print("Input file error: Not" + " " + 'all' + " " + "uncertainties are positive.")
        else:
            Xlable, Ylable = Find_bars_names(xy_multilist[indx + 1:])
            for box in xy_multilist[:indx]:
                box_2 = []
                for item in box:
                    stripped_item = item.strip("\n")
                    box_2.append(stripped_item)
                clean_xy_multilist.append(box_2)
            first_row = clean_xy_multilist[0]
            for i in range(0, len(first_row)):
                box_2 = []
                box_2.append(first_row[i])
                for o in clean_xy_multilist[1:]:
                    box_2.append(o[i])
                sorted_xy_multilist.append(box_2)
            for i in sorted_xy_multilist:
                i[0] = i[0].lower()
                if i[0] == "x":
                    for item in i[1:]:
                        X.append(float(item))
                if i[0] == "y":
                    for item in i[1:]:
                        Y.append(float(item))
                if i[0] == "dx":
                    for item in i[1:]:
                        DX.append(float(item))
                if i[0] == "dy":
                    for item in i[1:]:
                        DY.append(float(item))
            a = fun_a(X, Y, DY)
            da = fun_da(X, DY)
            b = fun_b(Y, a, X, DY)
            db = fun_db(X, DY)
            chi_2 = fun_chi_2(Y, a, b, X, DY)
            chi_2red = fun_chi_2red(chi_2, X)
            print("a=" + "" + str(a) + "" + "+-" + str(da))
            print("b=" + "" + str(b) + "" + "+-" + str(db))
            print("chi2=" + "" + str(chi_2))
            print("chi2_reduced=" + "" + str(chi_2red))

            x = np.array(X)
            my_y = np.array(Y)
            formula = a * x + b
            xerr = np.array(DX)
            yerr = np.array(DY)

            y = formula
            plt.errorbar(x, my_y, yerr=yerr, xerr=xerr, fmt='none', ecolor='b')
            plt.plot(x, y, "r")
            plt.xlabel(xlabel=Xlable)
            plt.ylabel(ylabel=Ylable)
            plt.show()
            plt.savefig("linear_fit.svg")
            my_file.close()

    else: ### אם המידע מגיע בצורה של שורות ###
        my_file = open(filename, "r")
        for line in my_file:
            xy_multilist.append(line.split(' '))
        indx = xy_multilist.index(['\n'])
        result = check_xymultilist_2(xy_multilist[:indx])  ### check if all Data lists with the samelength ###
        if not (result):
            print(" Input file error: Data lists are not the samelength.")
        else:

            Xlable, Ylable = Find_bars_names(xy_multilist[indx + 1:])
            for box in xy_multilist[:indx]:
                box_2 = []
                for item in box:
                    stripped_item = item.strip("\n")
                    box_2.append(stripped_item)
                clean_xy_multilist.append(box_2)
            if not (check_if_less_zero_2(clean_xy_multilist)):  ### check if all uncertainties positive##
                print("Input file error: Not" + " " + 'all' + " " + "uncertainties are positive.")
            else:
                for i in clean_xy_multilist:
                    i[0] = i[0].lower()
                    if i[0] == "x":
                        for item in i[1:]:
                            X.append(float(item))
                    if i[0] == "y":
                        for item in i[1:]:
                            Y.append(float(item))
                    if i[0] == "dx":
                        for item in i[1:]:
                            DX.append(float(item))
                    if i[0] == "dy":
                        for item in i[1:]:
                            DY.append(float(item))
                a = fun_a(X, Y, DY)
                da = fun_da(X, DY)
                b = fun_b(Y, a, X, DY)
                db = fun_db(X, DY)
                chi_2 = fun_chi_2(Y, a, b, X, DY)
                chi_2red = fun_chi_2red(chi_2, X)
                print("a=" + "" + str(a) + "" + "+-" + str(da))
                print("b=" + "" + str(b) + "" + "+-" + str(db))
                print("chi2=" + "" + str(chi_2))
                print("chi2_reduced=" + "" + str(chi_2red))

                x = np.array(X)
                my_y = np.array(Y)
                formula = a * x + b
                xerr = np.array(DX)
                yerr = np.array(DY)

                y = formula
                plt.errorbar(x, my_y, yerr=yerr, xerr=xerr, fmt='none', ecolor='b')
                plt.plot(x, y, "r")
                plt.xlabel(xlabel=Xlable)
                plt.ylabel(ylabel=Ylable)
                plt.show()
                plt.savefig("linear_fit.svg")
                my_file.close()


def Find_bars_names(Multilist):#פונקציה שמוצאת את שמות הצירים#
    x_lable = ""
    y_lable= ""
    Clean_xy_multilist=[]

    for box in Multilist:
        box_2 = []
        for item in box:
            stripped_item = item.strip("\n")
            box_2.append(stripped_item)
        Clean_xy_multilist.append(box_2)

    for i in Clean_xy_multilist:
        if i[0]=="x":
            for item in i[2:]:
                x_lable=x_lable+str(item)
        if i[0]=="y":
            for item in i[2:]:
                y_lable=y_lable+str(item)
    return x_lable,y_lable


def fun_chi_2red(chi,x):#פונקציה שמחשבת את ערך החי בריבוע רדיוס
    N=0
    for i in range(0,len(x)):
        N=N+1
    return chi/(N-2)


def fun_chi_2(y,a,b,x,dy):#פונקציה שמחשבת את ערך החי בריבוע
    Chi=0
    for i in range(0,len(x)):
        Chi=Chi+((y[i]-(a*x[i]+b))/(dy[i]))**2
    return Chi

def fun_db(x,dy):# b פונקציה שמחשבת את השגיאה של 
    dy_power_avarage = 0
    s_dy = 0
    N = 0
    for i in range(0, len(dy)):
        dy_power_avarage = dy_power_avarage + ((dy[i] ** 2) / dy[i] ** 2)
        s_dy = s_dy + (1 / (dy[i] ** 2))
        N = N + 1
    dy_power_avarage = dy_power_avarage / (s_dy)
    x_avarage = 0
    power_x_avarage = 0
    for i in range(0, len(x)):
        x_avarage = x_avarage + (x[i] / (dy[i] ** 2))
        power_x_avarage = power_x_avarage + (x[i] ** 2 / (dy[i] ** 2))
    x_avarage = x_avarage / (s_dy)
    power_x_avarage = power_x_avarage / (s_dy)

    return np.sqrt((dy_power_avarage)*(power_x_avarage) / (N * (power_x_avarage - (x_avarage ** 2))))

def fun_b(y,a,x,dy):# b פונקציה שמחשבת את 
    s_dy = 0
    y_avarage=0
    for i in range(0,len(y)):
        y_avarage=y_avarage+(y[i]/(dy[i]**2))
        s_dy = s_dy + (1 / (dy[i] ** 2))
    y_avarage=y_avarage/(s_dy)
    x_avarage = 0
    for i in range(0, len(x)):
        x_avarage = x_avarage + (x[i] / (dy[i] ** 2))
    x_avarage = x_avarage / (s_dy)

    return y_avarage-a*x_avarage


def fun_da(x,dy):# da פונקציה שמחשבת את 
    dy_power_avarage=0
    s_dy = 0
    N=0
    for i in range(0,len(dy)):
        dy_power_avarage=dy_power_avarage+((dy[i] ** 2)/dy[i] ** 2)
        s_dy=s_dy+(1/(dy[i]**2))
        N=N+1
    dy_power_avarage = dy_power_avarage / (s_dy)
    x_avarage = 0
    power_x_avarage = 0
    for i in range(0, len(x)):
        x_avarage = x_avarage + (x[i] / (dy[i] ** 2))
        power_x_avarage = power_x_avarage + (x[i] ** 2 / (dy[i] ** 2))
    x_avarage = x_avarage / (s_dy)
    power_x_avarage = power_x_avarage /(s_dy)

    return np.sqrt((dy_power_avarage/(N*(power_x_avarage-(x_avarage**2)))))

def fun_a(x,y,dy):# a פונקציה שמחשבת את 
    xy_avarage=0
    s_dy=0
    for i in range(0,len(x)):
        xy_avarage=xy_avarage+(x[i]*y[i])/(dy[i]**2)
        s_dy=s_dy+(1/(dy[i]**2))
    xy_avarage=xy_avarage/(s_dy)
    x_avarage=0
    power_x_avarage = 0
    for i in range(0,len(x)):
        x_avarage=x_avarage+(x[i]/(dy[i]**2))
        power_x_avarage = power_x_avarage+(x[i]**2/(dy[i]**2))
    x_avarage=x_avarage/(s_dy)
    power_x_avarage=power_x_avarage/(s_dy)
    y_avarage=0
    for i in range(0,len(y)):
        y_avarage=y_avarage+(y[i]/(dy[i]**2))
    y_avarage=y_avarage/(s_dy)

    return ((xy_avarage-(x_avarage*y_avarage))/(power_x_avarage-(x_avarage**2)))


def check_if_less_zero_2(multilist):#פונקציה שבודקת אם קיים אי ודאות שלילי למקרה שהמידע מגיע בשורות
    for i in multilist:
        i[0] = i[0].lower()
        if i[0] == "dx":
            for item in i[1:]:
                if float(item)<0:
                    return False
        if i[0] == "dy":
            for item in i[1:]:
                if float(item)<0:
                    return False
    return True


def check_if_less_zero(multilist):# פונקציה שבודקת אם קיים אי ודאות שלילי למקרה שהמידע מגיע בעמודות
    clean_xy_multilist = []
    sorted_xy_multilist=[]
    for box in multilist:
        box_2 = []
        for item in box:
            stripped_item = item.strip("\n")
            box_2.append(stripped_item)
        clean_xy_multilist.append(box_2)
    first_row = clean_xy_multilist[0]
    for i in range(0, len(first_row)):
        box_2 = []
        box_2.append(first_row[i])
        for o in clean_xy_multilist[1:]:
            box_2.append(o[i])
        sorted_xy_multilist.append(box_2)
    for i in sorted_xy_multilist:
        i[0] = i[0].lower()
        if i[0] == "dx":
            for item in i[1:]:
                if float(item)<0:
                    return False
        if i[0] == "dy":
            for item in i[1:]:
                if float(item)<0:
                    return False
    return True


def check_xymultilist(xylist):# פונקציה שבודקת אם לא חסרים נתונים למקרה שהמידע מגיע בעמודות
    for line in xylist:
        if len(line) < 4:
            return False
    return True

def check_xymultilist_2(xylist):# פונקציה שבודקת אם לא חסרים נתונים למקרה שהמידע מגיע בשורות
    first_row=len(xylist[1])
    for line in xylist:
        if len(line) != first_row:
            return False
    return True

#main
file_input=str(input("Enter file name:"))
fit_linear(file_input)
