import wx
class CalculatorFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        self.result = wx.TextCtrl(panel, style=wx.TE_RIGHT)
        vbox.Add(self.result, flag=wx.EXPAND | wx.TOP | wx.BOTTOM, border=4)

        gridBox = wx.GridSizer(4, 4, 10, 10)
        buttons = ['7', '8', '9', '/',
                   '4', '5', '6', '*',
                   '1', '2', '3', '-',
                   '0', 'C', '=', '+']

        for label in buttons:
            button = wx.Button(panel, label=label)
            gridBox.Add(button, 1, wx.EXPAND)
            button.Bind(wx.EVT_BUTTON, self.OnButtonClicked)

        vbox.Add(gridBox, proportion=1, flag=wx.EXPAND)
        panel.SetSizer(vbox)

        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.SetTitle("Calculator")
        self.Centre()

    def OnButtonClicked(self, event):
        label = event.GetEventObject().GetLabel()
        current = self.result.GetValue()

        if label == 'C':
            self.result.Clear()
        elif label == '=':
            try:
                result = eval(current)
                self.result.SetValue(str(result))
            except Exception as e:
                self.result.SetValue("Error")
        else:
            self.result.SetValue(current + label)

    def OnClose(self, event):
        self.Destroy()

if __name__ == "__main__":
    app = wx.App(False)
    frame = CalculatorFrame(None, size=(300, 400))
    frame.Show()
    app.MainLoop()

