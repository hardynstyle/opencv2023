# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 06:53:03 2022

@author: hardyn
"""
# import sys
from kivymd.toast import toast
from kivy.lang import Builder
from kivymd.uix.toolbar import MDToolbar
from kivy.utils import get_color_from_hex
from kivymd.app import MDApp

from kivymd.uix.bottomsheet import MDGridBottomSheet
KV = '''
#:import get_color_from_hex kivy.utils.get_color_from_hex

#:set text_color get_color_from_hex("#090909")
#:set focus_color get_color_from_hex("#85c4be")
#:set ripple_color get_color_from_hex("#c5bdd2")
#:set bg_color get_color_from_hex("#faffff")
#:set selected_color get_color_from_hex("#0c6c4d")


<DrawerClickableItem@MDNavigationDrawerItem>
    focus_color: focus_color
    unfocus_color: bg_color
    text_color: text_color
    icon_color: text_color
    ripple_color: ripple_color
    selected_color: selected_color
    _no_ripple_effect: True


<DrawerLabelItem@MDNavigationDrawerItem>
    bg_color: bg_color
    text_color: text_color
    icon_color: text_color
    _no_ripple_effect: True


MDScreen:

    id:das
    MDBottomNavigation:
        panel_color: get_color_from_hex("#eeeaea")
        selected_color_background: get_color_from_hex("#97ecf8")
        text_color_active: 0, 0, 0, 1

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Mail'
            icon: 'gmail'
            badge_icon: "numeric-10"

            MDLabel:
                text: 'Mail'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Discord'
            icon: 'discord'
            badge_icon: "numeric-5"

            MDLabel:
                text: 'Discord'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'LinkedIN'
            icon: 'linkedin'

            MDLabel:
                text: 'LinkedIN'
                halign: 'center'        
    MDFloatingActionButtonSpeedDial:
        # x: root.width - self.width - dp(100)
        # y: dp(120)
  
            
        
        data: app.data
       
       
        # hint_animation: True
        # bg_hint_color: app.theme_cls.primary_light
        bg_color_root_button:(0,0,0,1)
        bg_color_stack_button:(0,0,0,1)
        bg_hint_color:(0,0,0,1)   
        color_icon_root_button:(0,1,0,1)
        color_icon_stack_button:(0,1,0,1)         
 
            
    MDBoxLayout:
            
        id: box
        orientation: "vertical"
        spacing: "12dp"
        pos_hint: {"top": 1}
        adaptive_height: True            
    MDNavigationLayout:



            
                
                # MDToolbar:
                #     title: "Barra de Navegador:"
                #     elevation: 10
                #     pos_hint: {"top": 1}
                #     md_bg_color: focus_color
                #     specific_text_color: text_color
                #     left_action_items:
                #         [  [ 'menu', lambda x:   nav_drawer.set_state("open")  if nav_drawer.state == "close" else                             nav_drawer.set_state("close")                             ]                             ]

        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0) if self.anchor == "left" else (16, 0, 0, 16)
            md_bg_color: bg_color

            MDNavigationDrawerMenu:

                MDNavigationDrawerHeader:
                    title: "ESTRUC-FEM"
                    text: "ray.huanca.16.@unsch.edu.pe"
                    source: "logo/metal.png"
                    spacing: "10dp"
                    padding: "12dp", 0, 0, "80dp"

                MDNavigationDrawerLabel:
                    text: "Mail"

                DrawerClickableItem:
                    icon: "gmail"
                    right_text: "+99"
                    text_right_color: text_color
                    text: "Inbox"

                DrawerClickableItem:
                    icon: "send"
                    text: "Outbox"

                MDNavigationDrawerDivider:

                MDNavigationDrawerLabel:
                    text: "bases"

                DrawerClickableItem:
                    icon: "information"
                    text: "info"
                DrawerClickableItem:
                    icon: "tooltip-plus"
                    text: "extensiones"
                    on_press: app.adds_menu_inferior()
                DrawerClickableItem:
                    icon: "exit-to-app"
                    text: "exit"
                    # on_press: quit()
                   
                    

'''


class TestNavigationDrawer(MDApp):
    data = {
        'Python': 'language-python',
        'PHP': 'language-php',
        'C++': 'language-cpp',
    }
    def build(self):
        self.theme_cls.primary_palette = "Indigo"
        return Builder.load_string(KV)
    def on_start(self):    
    
        type_height="medium",
        self.root.ids.box.add_widget(
            MDToolbar(
                
                
                md_bg_color=get_color_from_hex("#2d2734"),
                # left_action_items=[["arrow-left", lambda x: x]],
              
                left_action_items=[  [ 'menu', lambda x:   self.root.ids.nav_drawer.set_state("open")]] ,

                right_action_items=[
                   
                    ["magnify", lambda x: x],
                    ["dots-vertical", lambda x: x],
                ],
                title="Starling" 
            )
        )
        # TestNavigationDrawer.adds_menu_inferior(self)
    def callback_for_menu_items(self, *args):
        toast(args[0])        
    def adds_menu_inferior(self):
        print("entro a la funcion")
        bottom_sheet_menu = MDGridBottomSheet()
        data = {
            "Facebook": "facebook",
            "YouTube": "youtube",
            "Twitter": "twitter",
            "Da Cloud": "cloud-upload",
            "Camera": "camera",
        }
        for item in data.items():
            bottom_sheet_menu.add_item(
                item[0],
                lambda x, y=item[0]: self.callback_for_menu_items(y),
                icon_src=item[1],
            )
        bottom_sheet_menu.open()            
TestNavigationDrawer().run()
