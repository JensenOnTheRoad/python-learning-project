import ddddocr


class VerifyCodeParser:
    image_path = ''

    def __init__(self, path):
        self.image_path = path

    def parser(self):
        ocr = ddddocr.DdddOcr()
        with open(self.image_path, 'rb') as f:
            img_bytes = f.read()
        res = ocr.classification(img_bytes)
        return res


if __name__ == '__main__':
    image_path = './code.png'
    parser = VerifyCodeParser(image_path)
    print(parser.parser())
