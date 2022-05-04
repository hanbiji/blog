from PIL import Image
import glob

def convertToPDF(folder, PDFname, deleteLast=False):
    '''
    converts all images in a folder to a PDF. 
    '''
    imageList = []
    for filename in glob.glob(folder + f'/*'):
        image=Image.open(filename)
        image.load()
        background = Image.new("RGB", image.size, (255, 255, 255))
        background.paste(image, mask=image.split()[3]) # 3 is the alpha channel
        # background.convert('RGB') # convert to RGB
        imageList.append(background)

    imageList[0].save(f'./' + PDFname + '.pdf',save_all=True, append_images=imageList[1:]) # take the first image and add everything else

if __name__ == "__main__":
    folder = r"./png/"
    pdfFile = r"pdf-name"
    convertToPDF(folder, pdfFile)
