from breezypythongui import EasyFrame


class LabelDemo(EasyFrame):
    """
    Displays a greeting in a window.
    """

    def __init__(self):
        """
        Set up the window and the label.
        """
        EasyFrame.__init__(self)
        self.addLabel(text="Hello world!", row=1, colum=1)

    def main(self) -> None:
        """
        Instantiates and pops up the window.
        :return: None
        """
        LabelDemo().mainloop()
