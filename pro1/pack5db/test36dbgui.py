
import wx
import wx.xrc
import MySQLdb
import sys
import ast


with open('mariadb.txt', mode='r') as f:
    aa = f.read()
    config = ast.literal_eval(aa)
    

class MyGogek ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"고객자료 보기", pos = wx.DefaultPosition, size = wx.Size( 474,320 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        #self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"사번 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        bSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )
        
        self.txtNo = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.txtNo, 0, wx.ALL, 5 )
        
        self.m_staticText2 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"직원명 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        bSizer2.Add( self.m_staticText2, 0, wx.ALL, 5 )
        
        self.txtName = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.txtName, 0, wx.ALL, 5 )
        
        self.btnLogin = wx.Button( self.m_panel1, wx.ID_ANY, u"로그인", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.btnLogin, 0, wx.ALL, 5 )
        
        
        self.m_panel1.SetSizer( bSizer2 )
        self.m_panel1.Layout()
        bSizer2.Fit( self.m_panel1 )
        bSizer1.Add( self.m_panel1, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.staMsg = wx.StaticText( self.m_panel2, wx.ID_ANY, u"고객목록", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staMsg.Wrap( -1 )
        bSizer3.Add( self.staMsg, 0, wx.ALL, 5 )
        
        
        self.m_panel2.SetSizer( bSizer3 )
        self.m_panel2.Layout()
        bSizer3.Fit( self.m_panel2 )
        bSizer1.Add( self.m_panel2, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.lstGogek = wx.ListCtrl( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
        bSizer4.Add( self.lstGogek, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        self.m_panel3.SetSizer( bSizer4 )
        self.m_panel3.Layout()
        bSizer4.Fit( self.m_panel3 )
        bSizer1.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.staCount = wx.StaticText( self.m_panel4, wx.ID_ANY, u"인원수", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staCount.Wrap( -1 )
        bSizer5.Add( self.staCount, 0, wx.ALL, 5 )
        
        
        self.m_panel4.SetSizer( bSizer5 )
        self.m_panel4.Layout()
        bSizer5.Fit( self.m_panel4 )
        bSizer1.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # lstGogek 객체에 제목
        self.lstGogek.InsertColumn(0, '고객번호', width=100)
        self.lstGogek.InsertColumn(1, '고객명', width=150)
        self.lstGogek.InsertColumn(2, '고객전화', width=200)
                
        # Connect Events
        self.btnLogin.Bind( wx.EVT_BUTTON, self.OnLogin )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def OnLogin( self, event ):
        if self.txtNo.GetValue() == '':
            wx.MessageBox('사번 입력', '알림', wx.OK)
            self.txtNo.SetFocus()
            return
        
        if self.txtName.GetValue() == '':
            wx.MessageBox('직원명 입력', '알림', wx.OK)
            self.txtName.SetFocus()
            return
        
        self.LoginCheck()
        
    def LoginCheck(self):
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            
            no = self.txtNo.GetValue()
            name = self.txtName.GetValue()
            #print(no, name)
            
            sql = """
                select count(*) from jikwon
                where jikwon_no='{0}' and jikwon_name='{1}'
            """.format(no, name)
            #print(sql)
            cursor.execute(sql)
            count = cursor.fetchone()[0]    # 데이터 하나
            #print(count)
            
            if count == 0:
                wx.MessageBox('로그인 실패', '알림', wx.OK)
                return 
            else:
                self.staMsg.SetLabelText(no + '번 직원의 관리고객 목록')
                self.DisplayData(no)    # 직원자료 출력 메소드 호출
                
            
        except Exception as e:
            print('LoginCheck err : ', e)
        finally:
            cursor.close()
            conn.close()
        
        
    def DisplayData(self, no):
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            
            sql = """
                select gogek_no, gogek_name, gogek_tel
                from gogek
                where gogek_damsano={}
            """.format(no)
            #print(sql)
            
            cursor.execute(sql)
            datas = cursor.fetchall()
            
            self.lstGogek.DeleteAllItems()  # ListCtrl 초기화
            
            for d in datas:
                i = self.lstGogek.InsertItem(1000, 0)   # ListCtrl 최대 행 수를 적어줌
                self.lstGogek.SetItem(i, 0, str(d[0]))
                self.lstGogek.SetItem(i, 1, d[1])
                self.lstGogek.SetItem(i, 2, d[2])
                
            self.staCount.SetLabelText('인원수 :' + str(len(datas)))
            
            
        except Exception as e:
            print('DisplayData err : ', e)
        finally:
            cursor.close()
            conn.close()
    
if __name__ == '__main__':
    app = wx.App()
    MyGogek(None).Show()
    app.MainLoop()    
