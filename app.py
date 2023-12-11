from PIL import Image
import os
FolderDesmadre = "/Users/rachelrivera/downloads/midesmadre/"
FolderImages = "/Users/rachelrivera/downloads/imagenes/"

if __name__ == "__main__":
    for filename in os.listdir(FolderDesmadre):
        fn, ext= os.path.splitext