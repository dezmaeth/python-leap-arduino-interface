import Leap, sys

class Listener(Leap.Listener):

    def on_init(self, controller):
        print "Prendido!"

    def on_connect(self, controller):
        print "Connectado!!"

    def on_disconnect(self, controller):
        print "Desconectado"

    def on_exit(self, controller):
        print "Cerrado"

    def on_frame(self, controller):
        print "cuadro"
        frame = controller.frame()
        print "Frame id: %d, timestamp: %d, manos: %d, dedos: %d, herramientas: %d" % (
        frame.id, frame.timestamp, len(frame.hands), len(frame.fingers), len(frame.tools))


def main():

    listener = Listener()
    controller = Leap.Controller()

    controller.add_listener(listener)

    print "Presiona enter para cerrar..."
    sys.stdin.readline()
    controller.remove_listener(listener)
    
if __name__ == "__main__":
    main()