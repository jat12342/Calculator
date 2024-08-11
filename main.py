from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder
from kivymd.toast.kivytoast.kivytoast import toast

kv='''
Manager:
    Fir:
    Sec:
                
<Fir>:
    name:'Home'          
 
    MDTextFieldRect:
        id:e1       
        pos_hint:{'center_x':0.5,'center_y':0.9} 
        font_size:'20sp'           
        size_hint:0.95,0.2    
        multiline:True
        disabled:True
                 
    MDRectangleFlatButton:  
        id:b1
        text_color:1,0,0,1
        text:"1"
        pos_hint:{'center_x':0.1,'center_y':0.7500}
        size_hint:0.01,0.01
        font_size:'10sp'
        on_press:
            e1.text+=self.text

    MDRectangleFlatButton:  
        id:b2
        text_color:1,0,0,1
        text:"2"
        pos_hint:{'center_x':0.3,'center_y':0.7500}
        size_hint:0.01,0.01
        font_size:'10sp'
        on_press:
            e1.text+=self.text

    MDRectangleFlatButton:  
        id:b3
        text_color:1,0,0,1
        text:"3"
        pos_hint:{'center_x':0.5,'center_y':0.7500}
        size_hint:0.01,0.01
        font_size:'10sp'
        on_press:
            e1.text+=self.text

    MDRectangleFlatButton:  
        id:b4
        text_color:1,0,0,1
        text:"4"
        pos_hint:{'center_x':0.7,'center_y':0.7500}
        size_hint:0.01,0.01
        font_size:'10sp'
        on_press:
            e1.text+=self.text
            
    MDRectangleFlatButton:  
        id:b+
        text_color:1,0,0,1
        text:"+"
        pos_hint:{'center_x':0.9,'center_y':0.7400}
        size_hint:0.01,0.10
        font_size:'10sp'
        on_press:
            e1.text+=self.text

    MDRectangleFlatButton:  
        id:b5
        text_color:1,0,0,1
        text:"5"
        pos_hint:{'center_x':0.1,'center_y':0.68}
        size_hint:0.01,0.01
        font_size:'10sp'
        on_press:
            e1.text+=self.text

    MDRectangleFlatButton:  
        id:b6
        text_color:1,0,0,1
        text:"6"
        pos_hint:{'center_x':0.3,'center_y':0.68}
        size_hint:0.01,0.01
        font_size:'10sp'
        on_press:
            e1.text+=self.text
            
    MDRectangleFlatButton:  
        id:b7
        text_color:1,0,0,1
        text:"7"
        pos_hint:{'center_x':0.5,'center_y':0.68}
        size_hint:0.01,0.01
        font_size:'10sp'
        on_press:
            e1.text+=self.text

    MDRectangleFlatButton:  
        id:b8
        text_color:1,0,0,1
        text:"8"
        pos_hint:{'center_x':0.7,'center_y':0.68}
        size_hint:0.01,0.01
        font_size:'10sp'
        on_press:
            e1.text+=self.text

    MDRectangleFlatButton:  
        id:b*
        text_color:1,0,0,1
        text:"*"
        pos_hint:{'center_x':0.9,'center_y':0.63}
        size_hint:0.01,0.1
        font_size:'10sp'
        on_press:
            e1.text+=self.text
            
    MDRectangleFlatButton:  
        id:b9
        text_color:1,0,0,1
        text:"9"
        pos_hint:{'center_x':0.1,'center_y':0.61}
        size_hint:0.01,0.01
        font_size:'10sp'
        on_press:
            e1.text+=self.text
           

    MDRectangleFlatButton:  
        id:b0
        text_color:1,0,0,1
        text:"0"
        pos_hint:{'center_x':0.3,'center_y':0.61}
        size_hint:0.01,0.01
        font_size:'10sp'
        on_press:
            e1.text+=self.text

    MDRectangleFlatButton:  
        id:b.
        text_color:1,0,0,1
        text:"."
        pos_hint:{'center_x':0.5,'center_y':0.61}
        size_hint:0.01,0.01
        font_size:'10sp'
        on_press:
            e1.text+=self.text

    MDRectangleFlatButton:  
        id:bc
        text_color:1,0,0,1
        text:"C"
        pos_hint:{'center_x':0.7,'center_y':0.61}
        size_hint:0.01,0.01
        font_size:'10sp'
        on_press:
            e1.text=""

    MDRectangleFlatButton:  
        id:b/
        text_color:1,0,0,1
        text:"/"
        pos_hint:{'center_x':0.9,'center_y':0.52}
        size_hint:0.01,0.1
        font_size:'10sp'
        on_press:
            e1.text+=self.text

    MDRectangleFlatButton:  
        id:b-
        text_color:1,0,0,1
        text:"-"
        pos_hint:{'center_x':0.7,'center_y':0.52}
        size_hint:0.01,0.1
        font_size:'10sp'
        on_press:
            e1.text+=self.text
            
    MDRectangleFlatButton:  
        id:b=
        text_color:1,0,0,1
        text:"="
        pos_hint:{'center_x':0.3,'center_y':0.52}
        size_hint:0.6,0.1
        font_size:'10sp'
        on_press:
            app.solve()
       
                
                                                
  
    MDRectangleFlatButton:    
        text:'×'           
        size_hint:1,0.1
        pos_hint:{'center_x':0.5,'center_y':0.4}
        on_press:
            app.bk()
            
    MDFloatingActionButton:
        icon:'arrow-right'             
        on_press:
            app.root.current='sec'       
            app.root.transition.direction="left"
            

                     
            


        
<Sec>:
    name:'sec'
    MDLabel:
        text:'RAM-RAM'
        font_style:'H2'
        bold:True
        pos_hint:{'center_x':0.6,'center_y':0.8}
        
        
        
        
        
        
        
    MDLabel:
        id:ll1
        text:"UNDER DEVELOPMENT"       
        halign:'center'
        font_style:'H1'
        bold:True
        font_size:'20sp'
        text_color:1,0,0,1
   
    MDFloatingActionButton:
        id:bb1
        icon:'arrow-left'
        text:"back"        
        on_press:
            app.root.current="Home"
            app.root.transition.direction="right"
             
                






'''

class Fir(Screen):
    pass
    
    
class Sec(Screen):
    pass
    
    
class Manager(ScreenManager):
    pass


class Demo(MDApp):
    def build(self):
        self.u=Builder.load_string(kv)
        return self.u
        
    def solve(self):
        a=self.u.get_screen('Home').ids.e1.text
        try:
            b=str(eval(a))
            self.u.get_screen('Home').ids.e1.text=b
        except:
            toast("ERROR")
            self.u.get_screen('Home').ids.e1.text=""
            
    def bk(self):
        self.u.get_screen('Home').ids.e1.do_backspace(from_undo=False,mode='bkspc')
               
        
        
        

Demo().run()




