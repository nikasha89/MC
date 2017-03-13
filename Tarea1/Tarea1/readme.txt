a.Inside NoiseRutine Folder is:

    1. noisyImf Folder that contains images with differents types of noises.
    2. addNoise.py file --> python code that add noise at images
    3. An example image.

b.Inside Processing Operation Folder is:

    1. Contrast Enhancement
    2. Intensity Transformation
    3. Smoothing Filter
    4. ToGrayScale

#Brief Explanation:
- En cada carpeta a y b, están los ejercicios de tratamiento de imágenes.

    -En a) se localizan las rutinas relativas a añadir ruido a las imágenes. De forma que, dentro de addNoise.py:

            Tipos de Ruidos posibles a añadir:

            'gauss'     Gaussian-distributed additive noise.
            'poisson'   Poisson-distributed noise generated from the data.
            's&p'       Replaces random pixels with 0 or 1.
            'speckle'   Multiplicative noise using out = image + n*image,where
                        n is uniform noise with specified mean & variance.

        En la variable siguiente escribiremos el tipo de ruido que queramos aplicar:
            noise_typ = 'speckle'
        Y en la variable siguiente, estableceremos el path de la imagen a la que queramos añadir el ruido:
            imgPath = 'trex.jpg'

        De forma que, al ejecutar el script, nos resultará la imagen con el nombre del tipo de ruido que le hayamos
        aplicado dentro de la carpeta noisyImg.


    -En b) se localizan los ejercicios relativos al tratamiento con imágenes:

        1. Contrast Enhancement
        2. Intensity Transformation
        3. Smoothing Filter
        4. ToGrayScale
