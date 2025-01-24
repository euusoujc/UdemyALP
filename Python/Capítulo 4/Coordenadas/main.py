def defina_o_quadrante():

    coordenada_escolhida = input('Escolha as coordenadas de x e y(x,y): ')
    x, y = map(float, coordenada_escolhida.split(','))
    if x > 0 and y > 0:
        print('Coordenadas do primeiro quadrante')
    elif x < 0 and y > 0:
        print('Coordenadas do segundo quadrante')
    elif x < 0 and y < 0:
        print('Coordenadas do terceiro quadrante')
    elif x > 0 and y < 0:
        print('Coordenadas do quarto quadrante')
    else:
        print("Ponto localizado no eixo de origem")


defina_o_quadrante()
