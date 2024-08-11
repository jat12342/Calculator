from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.toolbar import MDTopAppBar

Kv='''

float:
    man:man
    
    ScreenManager:
        id:man
        home:home
        
        Screen:
            id:home
            name:'home'
            
                
            MDTopAppBar:
                title:'HAR HAR MAHADEV'
                left_action_items:[['menu',lambda x: n1.set_state("open")]]
                pos_hint:{'top':1}

            MDLabel:
                id:l1
                text:'HAR HAR MAHADEV'       
                font_style:'H4'   
                bold:True
                font_size:'20sp'
                pos_hint:{'center_x':0.7,'center_y':0.7}
                
                
                                                                      
                                                
                
            MDNavigationDrawer:
                id:n1
                MDBoxLayout:
                    orientation:'vertical'
                    MDLabel:
                        id:l2
                        text:'RAM-RAM'
                        font_style:'H4'
                        bold:True
                        size_hint:0.3,0.3
                        font_size:'10sp'
                    MDLabel:
                        id:l3
                        text:'UNDER DEVELOPMENT'
                        font_style:'H4'
                        font_size:'10sp'
                        bold:True
                        size_hint:0.3,0.3                                                                    
                
                

            
                 
     













'''






class float(FloatLayout):
    pass


class Demo(MDApp):
    def build(self):
        b=Builder.load_string(Kv)
        return b
        
                
                        
Demo().run()                                       
      
    






