from haishoku.haishoku import Haishoku
# img_path = r'img\2.jpg'
def palette(img_path):
    '''
    读取图片并返回主色调和配色方案，dominant type：元组，palette type：元组列表
    '''
    haishoku = Haishoku.loadHaishoku(img_path)
    dominant=haishoku.getDominant(img_path)
    palette=haishoku.getPalette(img_path)#返回元组列表，第一个元组为占比，第二个为RGB
    # Haishoku.showDominant(img_path)#显示主色调
    # Haishoku.showPalette(img_path)#显示配色方案
    return dominant,palette