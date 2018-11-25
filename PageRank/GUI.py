import wx
import sys
import wx


class MyPanel(wx.Panel):
    def __init__(self, parent,*args, **kwds):
        self.parent = parent
        wx.Panel.__init__(self, parent, *args, **kwds)

        ## parameters
        self.page_scroller_result = dict()
        
        self.dummy_panel = wx.Panel(self, wx.ID_ANY)

        ## input search results.
        self.search_input_txtctrl = wx.TextCtrl(self, wx.ID_ANY, "")

        ## button for executing the search results
        self.search_btn = wx.Button(self, wx.ID_ANY, "search")
        self.search_btn.Bind(wx.EVT_BUTTON, self.run_search)

        ## incremental button for the page viewing
        self.page_scroller = wx.SpinCtrl(self, -1, "", (30, 50))
        self.page_scroller.SetRange(1,100)
        self.page_scroller.SetValue(1)
        self.Bind(wx.EVT_SPINCTRL, self.OnSpin, self.page_scroller)
        self.Bind(wx.EVT_TEXT, self.OnText, self.page_scroller)

        ## Display of search results
        self.results_txtctrl = wx.TextCtrl(self, wx.ID_ANY, "",
                                           style = wx.TE_MULTILINE| wx.TE_RICH2|wx.TE_WORDWRAP)

        ## for notes taking .
        self.notes_txtctrl = wx.TextCtrl(self, wx.ID_ANY, "",
                                           style = wx.TE_MULTILINE| wx.TE_RICH2|wx.TE_WORDWRAP)

        self.__do_layout()


    def __do_layout(self):

        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        mid_portion_sizer =  wx.BoxSizer(wx.HORIZONTAL)
        
        sizer_2.Add(self.search_input_txtctrl, 5, wx.ALL | wx.EXPAND, 7)
        sizer_2.Add(self.search_btn, 0, wx.ALL | wx.EXPAND, 7)

        mid_portion_sizer.Add(self.page_scroller,1, wx.ALL | wx.EXPAND, 7)
        mid_portion_sizer.Add((-1,-1),4, wx.ALL | wx.EXPAND, 7)
        
        sizer_1.Add(sizer_2, 1, wx.ALL | wx.EXPAND, 3)
        sizer_1.Add(mid_portion_sizer, 1, wx.EXPAND, 0)
        sizer_1.Add(self.results_txtctrl, 10, wx.ALL | wx.EXPAND, 10)
        sizer_1.Add(self.notes_txtctrl, 5, wx.ALL | wx.EXPAND, 10)
        
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)

    def OnSpin(self, evt):
        """Page Scroller function: on scroll. Scroll to correct page"""
        target_output = self.page_scroller_result[self.page_scroller.GetValue()]
        self.results_txtctrl.SetValue(target_output) 

    def OnText(self, evt):
        """Page Scroller function: on enter text. text to correct page"""
        target_output = self.page_scroller_result[self.page_scroller.GetValue()]
        self.results_txtctrl.SetValue(target_output)

    def trigger_scroller_event(self):
        """Manually trigger the event for the self.page_scroller to display the first set of result"""
        evt = wx.PyCommandEvent(wx.EVT_TEXT.typeId,self.page_scroller.GetId())
        self.GetEventHandler().ProcessEvent(evt) 

    def run_search(self, evt):
        """Run the google search """
        search_input = self.search_input_txtctrl.GetValue()
        self.execute_google_search(str(search_input))
        self.set_result_to_dict_for_page_scroller()
        self.clear_result_screen()
        self.trigger_scroller_event()



class MyApp(wx.App):
    def __init__(self):
        wx.App.__init__(self,redirect =False)
        self.frame= MyFrame(None,wx.ID_ANY, "Google Search")
        self.SetTopWindow(self.frame)    
        self.frame.Show()
        
def run():
    try:
        app = MyApp()
        app.MainLoop()
    except  IndexError:
        del app#make sure to include this


if __name__ == '__main__':

    run()