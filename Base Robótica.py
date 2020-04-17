# ______________________ OPENCV ___________________________
# https://docs.opencv.org/master/d3/df2/tutorial_py_basic_ops.html

# _______________________________ BÁSICO __________________________________
# Lendo o arquivo
arquivo = cv2.imread("nome_arquivo.jpg")

# Quantidade de pixels na horizontal e vertical
# Retorna rows (linhas), columns (colunas), channels (canais)
arquivo.shape()

# Acessar os valores de um pixel e modificando
arquivo[px1, px2]
arquivo[px1, px2] = [R, G, B]

# Transformando os canais
arquivo_gray = cv2.cvtColor(arquivo, cv2.COLOR_RGB2GRAY)

# Mostrando imagens
# 1: plt
plt.imshow(arquivo, cmap="tipo de canal", vmin=0, vmax=255)
# 2: cv2
cv2.imshow()


# Criando imagens vazias

# 1: Fazendo a cópia de uma imagem e zerando
imagem[:] = 0

# 2: Criando uma nova
imagem = np.zeros((512, 1024), dtype=np.uint8)

# Iteração 
# Para cada linha 
for i in range(imagem_.shape[0]):
    # Para cada coluna
    for j in range(imagem.shape[1]):
        # Para cada pixel
        saida[i][j] = imagem[i][j]

# Equalização de Histogramas
imagem_eq = cv2.equalizeHist(imagem)

# Limiarização: transforma tons de cinza em binária
imagem_eq = cv2.equalizeHist(imagem)
plt.imshow(limiarizada, cmap="Greys_r")

# Detecção de bordas
min_contrast = 100
max_contrast = 200
# Usando canny
linhas = cv2.Canny(small, min_contrast, max_contrast )

# ColorPicker
colorpicker = widgets.ColorPicker(
    concise=False,
    description='Escolha uma cor',
    value='#ff0e00',
    disabled=False
)

# Detecção de cores
hsv1, hsv2 = aux.ranges(colorpicker.value)
mask = cv2.inRange(img_hsv, hsv1, hsv2)
# Segmentado fecha buracos
segmentado_cor = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,np.ones((10, 10)))
selecao = cv2.bitwise_and(img_rgb, img_rgb, mask=segmentado_cor)
# Melhorando imagem
mascara_blur = cv2.blur(mascara_2, (3,3))

# Contornos usando a detecção de cores acima
# Usar o segmetado
contornos, arvore = cv2.findContours(, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contornos_img = img_rgb.copy()
cv2.drawContours(contornos_img, contornos, -1, [0, 0, 255], 3)

# Contornos de novo
cv2.drawContours(contornos_img, contornos, -1, [255, 0, 0], 5);

# Centro de massa
def center_of_contour(contorno):
    """ Retorna uma tupla (cx, cy) que desenha o centro do contorno"""
    M = cv2.moments(contorno)
    # Usando a expressão do centróide definida em: https://en.wikipedia.org/wiki/Image_moment
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    return (int(cX), int(cY))
    
def crosshair(img, point, size, color):
    """ Desenha um crosshair centrado no point.
        point deve ser uma tupla (x,y)
        color é uma tupla R,G,B uint8
    """
    x,y = point
    cv2.line(img,(x - size,y),(x + size,y),color,5)
    cv2.line(img,(x,y - size),(x, y + size),color,5)
    


# Detecção de maior objeto
maior = None
maior_area = 0
for c in contornos:
    area = cv2.contourArea(c)
    if area > maior_area:
        maior_area = area
        maior = c


# TRANSFORMADA DE HOUGH
# Usar Canny
lines = cv2.HoughLinesP(hough_img, 10, math.pi/180.0, 100, np.array([]), 45, 5)
# Ligando linhas 
for i in range(a):
    # Faz uma linha ligando o ponto inicial ao ponto final, com a cor vermelha (BGR)
    cv2.line(hough_img_rgb, (lines[i][0][0], lines[i][0][1]), (lines[i][0][2], lines[i][0][3]), (0, 0, 255), 5, cv2.LINE_AA)

# Hough Circles
bordas = auto_canny(mask)
circles=cv2.HoughCircles(image=bordas,method=cv2.HOUGH_GRADIENT,dp=1.5,minDist=40,param1=200,param2=100,minRadius=5,maxRadius=200)
bordas_rgb = cv2.cvtColor(bordas, cv2.COLOR_GRAY2RGB)
output = bordas_rgb

if circles is not None:        
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        # draw the outer circle
        cv2.circle(output,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv2.circle(output,(i[0],i[1]),2,(0,0,255),3)



# Ponto de Fuga
for x in range(0, len(lines)):    
        for rho, theta in lines[x]:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            x1 = int(x0 + 1000*(-b))
            y1 = int(y0 + 1000*(a))
            x2 = int(x0 - 1000*(-b))
            y2 = int(y0 - 1000*(a))
            m = (y2 - y1)/(x2 - x1)
            
            h = y1 - m*x1

            lista_h.append(h)
            lista_m.append(m)

            if m>0.3 and m<2:
                cv2.line(frame,(x1,y1), (x2,y2), (50,0,255),2) 
            elif m<-0.3 and m>-2:
                cv2.line(frame,(x1,y1), (x2,y2), (50,0,255),2) 

    if len(lista_m) > 1 and lista_m[0] != lista_m[1]:
        x_i = (lista_h[1] - lista_h[0])/(lista_m[0] - lista_m[1])
        y_i = lista_m[0] * x_i + lista_h[0]
        x_i = int(x_i)
        y_i = int(y_i)
    
    if lista_m[0] - lista_m[1] > 0.5:
        cv2.circle(frame, (x_i, y_i), 1, (0,255,0), 5)

____ ROS _____

