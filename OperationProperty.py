import wx

from Kernel import Module
from icons import *

_ = wx.GetTranslation


class OperationProperty(wx.Frame, Module):
    def __init__(self, *args, **kwds):
        # begin wxGlade: OperationProperty.__init__
        kwds["style"] = kwds.get("style",
                                 0) | wx.DEFAULT_FRAME_STYLE | wx.FRAME_FLOAT_ON_PARENT | wx.FRAME_TOOL_WINDOW | wx.TAB_TRAVERSAL
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((414, 593))

        # Menu Bar
        self.RasterProperty_menubar = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        item = wxglade_tmp_menu.Append(wx.ID_ANY, _("Clear"), _("Delete all the layers"))
        self.Bind(wx.EVT_MENU, self.on_menu_clear, id=item.GetId())
        item = wxglade_tmp_menu.Append(wx.ID_ANY, _("Other/Blue/Red"), _("Set layers to the default"))
        self.Bind(wx.EVT_MENU, self.on_menu_default0, id=item.GetId())
        item = wxglade_tmp_menu.Append(wx.ID_ANY, _("Basic"), _("Set layers to basic form"))
        self.Bind(wx.EVT_MENU, self.on_menu_default1, id=item.GetId())
        wxglade_tmp_menu.AppendSeparator()
        item = wxglade_tmp_menu.Append(wx.ID_ANY, _("Save"), _("Save the current layer set"))
        self.Bind(wx.EVT_MENU, self.on_menu_save, id=item.GetId())
        item = wxglade_tmp_menu.Append(wx.ID_ANY, _("Load"), _("Load existing layer sets"))
        self.Bind(wx.EVT_MENU, self.on_menu_load, id=item.GetId())
        item = wxglade_tmp_menu.Append(wx.ID_ANY, _("Import"), _("Import existing layers"))
        self.Bind(wx.EVT_MENU, self.on_menu_import, id=item.GetId())
        self.RasterProperty_menubar.Append(wxglade_tmp_menu, _("Layers"))
        self.SetMenuBar(self.RasterProperty_menubar)
        # Menu Bar end
        self.main_panel = wx.Panel(self, wx.ID_ANY)
        self.button_add_layer = wx.BitmapButton(self.main_panel, wx.ID_ANY, icons8_plus_50.GetBitmap())
        self.listbox_layer = wx.ListBox(self.main_panel, wx.ID_ANY, choices=[], style=wx.LB_ALWAYS_SB | wx.LB_SINGLE)
        self.button_remove_layer = wx.BitmapButton(self.main_panel, wx.ID_ANY, icons8_delete_50.GetBitmap())
        self.button_layer_color = wx.Button(self.main_panel, wx.ID_ANY, "")
        self.combo_type = wx.ComboBox(self.main_panel, wx.ID_ANY, choices=[_("Engrave"), _("Cut"), _("Raster"), _("Image")],
                                      style=wx.CB_DROPDOWN)
        self.checkbox_output = wx.CheckBox(self.main_panel, wx.ID_ANY, _("Output"))
        self.text_speed = wx.TextCtrl(self.main_panel, wx.ID_ANY, "20.0")
        self.text_power = wx.TextCtrl(self.main_panel, wx.ID_ANY, "1000.0")
        self.text_raster_step = wx.TextCtrl(self.main_panel, wx.ID_ANY, "1")
        self.text_overscan = wx.TextCtrl(self.main_panel, wx.ID_ANY, "20")
        self.combo_raster_direction = wx.ComboBox(self.main_panel, wx.ID_ANY,
                                                  choices=[_("Top To Bottom"), _("Bottom To Top"), _("Right To Left"),
                                                           _("Left To Right"), _("Crosshatch")], style=wx.CB_DROPDOWN)
        self.radio_directional_raster = wx.RadioBox(self.main_panel, wx.ID_ANY, _("Directional Raster"),
                                                    choices=[_("Bidirectional"), _("Unidirectional")], majorDimension=2,
                                                    style=wx.RA_SPECIFY_ROWS)
        self.radio_start_preference = wx.RadioBox(self.main_panel, wx.ID_ANY, _("Raster Start Preference"),
                                                  choices=[" ", " ", " ", " ", " ", " ", " ", " ", " "], majorDimension=3,
                                                  style=wx.RA_SPECIFY_ROWS)
        self.checkbox_advanced = wx.CheckBox(self.main_panel, wx.ID_ANY, _("Advanced"))
        self.checkbox_custom_d_ratio = wx.CheckBox(self.main_panel, wx.ID_ANY, _("Custom D-Ratio"))
        self.text_custom_d_ratio = wx.TextCtrl(self.main_panel, wx.ID_ANY, "0.261")
        self.checkbox_custom_accel = wx.CheckBox(self.main_panel, wx.ID_ANY, _("Acceleration"))
        self.slider_accel = wx.Slider(self.main_panel, wx.ID_ANY, 1, 1, 4, style=wx.SL_AUTOTICKS | wx.SL_LABELS)
        self.check_dot_enable = wx.CheckBox(self.main_panel, wx.ID_ANY, _("Dot Length (mils)"))
        self.text_dot_length = wx.TextCtrl(self.main_panel, wx.ID_ANY, "1")
        self.check_group_pulse = wx.CheckBox(self.main_panel, wx.ID_ANY, _("Group Pulses"))
        self.check_passes = wx.CheckBox(self.main_panel, wx.ID_ANY, _("Passes"))
        self.text_passes = wx.TextCtrl(self.main_panel, wx.ID_ANY, "1")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.on_button_add, self.button_add_layer)
        self.Bind(wx.EVT_LISTBOX, self.on_list_layer_click, self.listbox_layer)
        self.Bind(wx.EVT_LISTBOX_DCLICK, self.on_list_layer_dclick, self.listbox_layer)
        self.Bind(wx.EVT_BUTTON, self.on_button_remove, self.button_remove_layer)
        self.Bind(wx.EVT_BUTTON, self.on_button_layer, self.button_layer_color)
        self.Bind(wx.EVT_COMBOBOX, self.on_combo_operation, self.combo_type)
        self.Bind(wx.EVT_CHECKBOX, self.on_check_output, self.checkbox_output)
        self.Bind(wx.EVT_TEXT, self.on_text_speed, self.text_speed)
        self.Bind(wx.EVT_TEXT_ENTER, self.on_text_speed, self.text_speed)
        self.Bind(wx.EVT_TEXT, self.on_text_power, self.text_power)
        self.Bind(wx.EVT_TEXT_ENTER, self.on_text_power, self.text_power)
        self.Bind(wx.EVT_TEXT, self.on_text_raster_step, self.text_raster_step)
        self.Bind(wx.EVT_TEXT_ENTER, self.on_text_raster_step, self.text_raster_step)
        self.Bind(wx.EVT_TEXT, self.on_text_overscan, self.text_overscan)
        self.Bind(wx.EVT_TEXT_ENTER, self.on_text_overscan, self.text_overscan)
        self.Bind(wx.EVT_COMBOBOX, self.on_combo_raster_direction, self.combo_raster_direction)
        self.Bind(wx.EVT_RADIOBOX, self.on_radio_directional, self.radio_directional_raster)
        self.Bind(wx.EVT_RADIOBOX, self.on_radio_raster_preference, self.radio_start_preference)
        self.Bind(wx.EVT_CHECKBOX, self.on_check_advanced, self.checkbox_advanced)
        self.Bind(wx.EVT_CHECKBOX, self.on_check_dratio, self.checkbox_custom_d_ratio)
        self.Bind(wx.EVT_TEXT, self.on_text_dratio, self.text_custom_d_ratio)
        self.Bind(wx.EVT_TEXT_ENTER, self.on_text_dratio, self.text_custom_d_ratio)
        self.Bind(wx.EVT_CHECKBOX, self.on_check_acceleration, self.checkbox_custom_accel)
        self.Bind(wx.EVT_COMMAND_SCROLL, self.on_slider_accel, self.slider_accel)
        self.Bind(wx.EVT_CHECKBOX, self.on_check_dot_length, self.check_dot_enable)
        self.Bind(wx.EVT_TEXT, self.on_text_dot_length, self.text_dot_length)
        self.Bind(wx.EVT_TEXT_ENTER, self.on_text_dot_length, self.text_dot_length)
        self.Bind(wx.EVT_CHECKBOX, self.on_check_group_pulses, self.check_group_pulse)

        self.Bind(wx.EVT_CLOSE, self.on_close, self)
        self.combo_type.SetFocus()

    def on_close(self, event):
        self.device.close('window', self.name)
        event.Skip()  # Call destroy as regular.

    def initialize(self, channel=None):
        self.device.close('window', self.name)
        self.Show()

    def shutdown(self, channel=None):
        try:
            self.Close()
        except RuntimeError:
            pass

    def __set_properties(self):
        # begin wxGlade: OperationProperty.__set_properties
        self.SetTitle(_("Operation Properties"))
        self.button_add_layer.SetSize(self.button_add_layer.GetBestSize())
        self.listbox_layer.SetMinSize((40, -1))
        self.button_remove_layer.SetSize(self.button_remove_layer.GetBestSize())
        self.button_layer_color.SetBackgroundColour(wx.Colour(0, 0, 0))
        self.button_layer_color.SetToolTip(_("Change/View color of this layer"))
        self.combo_type.SetToolTip(_("Default Operation Mode Type"))
        self.combo_type.SetSelection(0)
        self.checkbox_output.SetToolTip(_("Output This Layer"))
        self.checkbox_output.SetValue(1)
        self.text_speed.SetToolTip(_("Speed at which to perform the action in mm/s."))
        self.text_power.SetToolTip(_("1000 always on. 500 it's half power (fire every other step). This is software PPI control."))
        self.text_raster_step.SetToolTip(_("Scan gap / step size, is the distance between scanlines in a raster engrave. Distance here is in 1/1000th of an inch."))
        self.text_overscan.SetToolTip(_("Overscan amount"))
        self.combo_raster_direction.SetToolTip(_("Direction to perform a raster"))
        self.combo_raster_direction.SetSelection(0)
        self.radio_directional_raster.SetToolTip(_("Rastering on forward and backswing or only forward swing?"))
        self.radio_directional_raster.SetSelection(0)
        self.radio_start_preference.SetToolTip(_("Set the preference for where rasters should start. Middle means no preference."))
        self.radio_start_preference.SetSelection(4)
        self.checkbox_advanced.SetToolTip(_("Turn on advanced options?"))
        self.checkbox_custom_d_ratio.SetToolTip(_("Enables the ability to modify the diagonal ratio."))
        self.text_custom_d_ratio.SetToolTip(_("Diagonal ratio is the ratio of additional time needed to perform a diagonal step rather than an orthogonal step. (0.261 default)"))
        self.checkbox_custom_accel.SetToolTip(_("Enables the ability to modify the acceleration factor."))
        self.slider_accel.SetToolTip(_("Acceleration Factor Override"))
        self.check_dot_enable.SetToolTip(_("Enable Dot Length Feature"))
        self.check_dot_enable.SetValue(1)
        self.text_dot_length.SetToolTip(_("PPI minimum on length for making dash patterns"))
        self.check_group_pulse.SetToolTip(_("Attempts to adjust the pulse grouping for data efficiency."))
        self.check_passes.SetToolTip(_("Enable Passes"))
        self.text_passes.SetToolTip(_("Run operation how many times?"))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: OperationProperty.__do_layout
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_main = wx.BoxSizer(wx.HORIZONTAL)
        param_sizer = wx.BoxSizer(wx.VERTICAL)
        passes_sizer = wx.StaticBoxSizer(wx.StaticBox(self.main_panel, wx.ID_ANY, _("Passes")), wx.VERTICAL)
        sizer_22 = wx.BoxSizer(wx.HORIZONTAL)
        advanced_ppi_sizer = wx.StaticBoxSizer(wx.StaticBox(self.main_panel, wx.ID_ANY, _("PPI Advanced")), wx.HORIZONTAL)
        sizer_19 = wx.BoxSizer(wx.VERTICAL)
        sizer_20 = wx.BoxSizer(wx.HORIZONTAL)
        advanced_sizer = wx.StaticBoxSizer(wx.StaticBox(self.main_panel, wx.ID_ANY, _("Speedcode Advanced")), wx.VERTICAL)
        sizer_12 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_11 = wx.BoxSizer(wx.HORIZONTAL)
        raster_sizer = wx.StaticBoxSizer(wx.StaticBox(self.main_panel, wx.ID_ANY, _("Raster")), wx.VERTICAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        speed_power_sizer = wx.BoxSizer(wx.HORIZONTAL)
        power_sizer = wx.StaticBoxSizer(wx.StaticBox(self.main_panel, wx.ID_ANY, _("Power (ppi)")), wx.HORIZONTAL)
        speed_sizer = wx.StaticBoxSizer(wx.StaticBox(self.main_panel, wx.ID_ANY, _("Speed (mm/s)")), wx.HORIZONTAL)
        layer_sizer = wx.StaticBoxSizer(wx.StaticBox(self.main_panel, wx.ID_ANY, _("Layer")), wx.HORIZONTAL)
        layers_sizer = wx.BoxSizer(wx.VERTICAL)
        layers_sizer.Add(self.button_add_layer, 0, 0, 0)
        layers_sizer.Add(self.listbox_layer, 10, wx.EXPAND, 0)
        layers_sizer.Add(self.button_remove_layer, 0, 0, 0)
        sizer_main.Add(layers_sizer, 1, wx.EXPAND, 0)
        layer_sizer.Add(self.button_layer_color, 0, 0, 0)
        layer_sizer.Add(self.combo_type, 1, 0, 0)
        layer_sizer.Add(self.checkbox_output, 1, 0, 0)
        param_sizer.Add(layer_sizer, 0, wx.EXPAND, 0)
        speed_sizer.Add(self.text_speed, 1, 0, 0)
        speed_power_sizer.Add(speed_sizer, 1, wx.EXPAND, 0)
        power_sizer.Add(self.text_power, 1, 0, 0)
        speed_power_sizer.Add(power_sizer, 1, wx.EXPAND, 0)
        param_sizer.Add(speed_power_sizer, 0, wx.EXPAND, 0)
        label_7 = wx.StaticText(self.main_panel, wx.ID_ANY, _("Raster Step (mils)"))
        sizer_3.Add(label_7, 1, 0, 0)
        sizer_3.Add(self.text_raster_step, 1, 0, 0)
        raster_sizer.Add(sizer_3, 0, wx.EXPAND, 0)
        label_6 = wx.StaticText(self.main_panel, wx.ID_ANY, _("Overscan (mils/%)"))
        sizer_6.Add(label_6, 1, 0, 0)
        sizer_6.Add(self.text_overscan, 1, 0, 0)
        raster_sizer.Add(sizer_6, 0, wx.EXPAND, 0)
        label_5 = wx.StaticText(self.main_panel, wx.ID_ANY, _("Raster Direction"))
        sizer_4.Add(label_5, 1, 0, 0)
        sizer_4.Add(self.combo_raster_direction, 1, 0, 0)
        raster_sizer.Add(sizer_4, 0, wx.EXPAND, 0)
        sizer_5.Add(self.radio_directional_raster, 3, wx.EXPAND, 0)
        sizer_5.Add(self.radio_start_preference, 1, 0, 0)
        raster_sizer.Add(sizer_5, 1, wx.EXPAND, 0)
        param_sizer.Add(raster_sizer, 0, wx.EXPAND, 0)
        param_sizer.Add(self.checkbox_advanced, 0, 0, 0)
        sizer_11.Add(self.checkbox_custom_d_ratio, 1, 0, 0)
        sizer_11.Add(self.text_custom_d_ratio, 1, 0, 0)
        advanced_sizer.Add(sizer_11, 0, wx.EXPAND, 0)
        sizer_12.Add(self.checkbox_custom_accel, 1, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_12.Add(self.slider_accel, 1, wx.EXPAND, 0)
        advanced_sizer.Add(sizer_12, 0, wx.EXPAND, 0)
        param_sizer.Add(advanced_sizer, 0, wx.EXPAND, 0)
        sizer_20.Add(self.check_dot_enable, 1, 0, 0)
        sizer_20.Add(self.text_dot_length, 1, 0, 0)
        sizer_19.Add(sizer_20, 1, wx.EXPAND, 0)
        sizer_19.Add(self.check_group_pulse, 0, 0, 0)
        advanced_ppi_sizer.Add(sizer_19, 1, wx.EXPAND, 0)
        param_sizer.Add(advanced_ppi_sizer, 0, wx.EXPAND, 0)
        sizer_22.Add(self.check_passes, 1, 0, 0)
        sizer_22.Add(self.text_passes, 1, 0, 0)
        passes_sizer.Add(sizer_22, 0, wx.EXPAND, 0)
        param_sizer.Add(passes_sizer, 0, wx.EXPAND, 0)
        sizer_main.Add(param_sizer, 1, wx.EXPAND, 0)
        self.main_panel.SetSizer(sizer_main)
        sizer_1.Add(self.main_panel, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        self.Centre()
        # end wxGlade

    def on_menu_clear(self, event):  # wxGlade: OperationProperty.<event_handler>
        print("Event handler 'on_menu_clear' not implemented!")
        event.Skip()

    def on_menu_default0(self, event):  # wxGlade: OperationProperty.<event_handler>
        print("Event handler 'on_menu_default0' not implemented!")
        event.Skip()

    def on_menu_default1(self, event):  # wxGlade: OperationProperty.<event_handler>
        print("Event handler 'on_menu_default1' not implemented!")
        event.Skip()

    def on_menu_save(self, event):  # wxGlade: OperationProperty.<event_handler>
        print("Event handler 'on_menu_save' not implemented!")
        event.Skip()

    def on_menu_load(self, event):  # wxGlade: OperationProperty.<event_handler>
        print("Event handler 'on_menu_load' not implemented!")
        event.Skip()

    def on_menu_import(self, event):  # wxGlade: OperationProperty.<event_handler>
        print("Event handler 'on_menu_import' not implemented!")
        event.Skip()

    def on_button_add(self, event):  # wxGlade: OperationProperty.<event_handler>
        print("Event handler 'on_button_add' not implemented!")
        event.Skip()

    def on_list_layer_click(self, event):  # wxGlade: OperationProperty.<event_handler>
        print("Event handler 'on_list_layer_click' not implemented!")
        event.Skip()

    def on_list_layer_dclick(self, event):  # wxGlade: OperationProperty.<event_handler>
        print("Event handler 'on_list_layer_dclick' not implemented!")
        event.Skip()

    def on_button_remove(self, event):  # wxGlade: OperationProperty.<event_handler>
        print("Event handler 'on_button_remove' not implemented!")
        event.Skip()

    def on_button_layer(self, event):  # wxGlade: OperationProperty.<event_handler>
        print("Event handler 'on_button_layer' not implemented!")
        event.Skip()

    def on_combo_operation(self, event):  # wxGlade: OperationProperty.<event_handler>
        print("Event handler 'on_combo_operation' not implemented!")
        event.Skip()

    def on_check_output(self, event):  # wxGlade: OperationProperty.<event_handler>
        print("Event handler 'on_check_output' not implemented!")
        event.Skip()

    def on_text_speed(self, event):  # wxGlade: OperationProperty.<event_handler>
        print("Event handler 'on_text_speed' not implemented!")
        event.Skip()

    def on_text_power(self, event):  # wxGlade: OperationProperty.<event_handler>
        print("Event handler 'on_text_power' not implemented!")
        event.Skip()

    def on_text_raster_step(self, event):  # wxGlade: OperationProperty.<event_handler>
        print("Event handler 'on_text_raster_step' not implemented!")
        event.Skip()

    def on_text_overscan(self, event):  # wxGlade: OperationProperty.<event_handler>
        print("Event handler 'on_text_overscan' not implemented!")
        event.Skip()

    def on_combo_raster_direction(self, event):  # wxGlade: OperationProperty.<event_handler>
        print("Event handler 'on_combo_raster_direction' not implemented!")
        event.Skip()

    def on_radio_directional(self, event):  # wxGlade: OperationProperty.<event_handler>
        print("Event handler 'on_radio_directional' not implemented!")
        event.Skip()

    def on_radio_raster_preference(self, event):  # wxGlade: OperationProperty.<event_handler>
        print("Event handler 'on_radio_raster_preference' not implemented!")
        event.Skip()

    def on_check_advanced(self, event):  # wxGlade: OperationProperty.<event_handler>
        print("Event handler 'on_check_advanced' not implemented!")
        event.Skip()

    def on_check_dratio(self, event):  # wxGlade: OperationProperty.<event_handler>
        print("Event handler 'on_check_dratio' not implemented!")
        event.Skip()

    def on_text_dratio(self, event):  # wxGlade: OperationProperty.<event_handler>
        print("Event handler 'on_text_dratio' not implemented!")
        event.Skip()

    def on_check_acceleration(self, event):  # wxGlade: OperationProperty.<event_handler>
        print("Event handler 'on_check_acceleration' not implemented!")
        event.Skip()

    def on_slider_accel(self, event):  # wxGlade: OperationProperty.<event_handler>
        print("Event handler 'on_slider_accel' not implemented!")
        event.Skip()

    def on_check_dot_length(self, event):  # wxGlade: OperationProperty.<event_handler>
        print("Event handler 'on_check_dot_length' not implemented!")
        event.Skip()

    def on_text_dot_length(self, event):  # wxGlade: OperationProperty.<event_handler>
        print("Event handler 'on_text_dot_length' not implemented!")
        event.Skip()

    def on_check_group_pulses(self, event):  # wxGlade: OperationProperty.<event_handler>
        print("Event handler 'on_check_group_pulses' not implemented!")
        event.Skip()

    def on_key_press(self, event):
        keycode = event.GetKeyCode()
        if keycode == wx.WXK_ESCAPE:
            self.Close()
        if keycode == wx.WXK_TAB:
            self.on_tab_traversal()
        event.Skip()

    def on_tab_traversal(self):
        """ Tab Traversal is part of wx.Panel, so It's added here programatically, rather than add one."""
        focus = self.FindFocus()
        if focus is self:
            self.text_speed.SetFocus()
            self.text_speed.SelectAll()
        elif focus is self.text_speed:
            self.text_power.SetFocus()
            self.text_power.SelectAll()
        elif focus is self.text_power:
            self.text_raster_step.SetFocus()
            self.text_power.SelectAll()