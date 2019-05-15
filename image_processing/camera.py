import cv2


class Camera:
    def __init__(self, width, height):
        self.window_size = (width, height)

        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.camera = cv2.VideoCapture(0)

    def image(self):
        ret, img = self.camera.read()
        img = cv2.resize(img, self.window_size)
        img = cv2.flip(img, 1)
        return img

    def show(self, img):
        cv2.imshow("cam", img)
        cv2.waitKey(10)

    def kill(self):
        cv2.destroyAllWindows()

    def write_message(self, img, text):
        cv2.putText(img, text, (10, 25), self.font, 1, (255, 255, 255), 1, cv2.LINE_AA)

    def draw_rect(self, img, contour):
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    def draw_circle(self, img, position, thickness):
        cv2.circle(img, position, 10, (0, 0, 255), thickness)
